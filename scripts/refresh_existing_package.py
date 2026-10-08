#!/usr/bin/env python3
"""Review-first update of an existing, pinned 1C AI methodology package.

This tool edits only the package-owned .1c-ai tree, 1c-ai-* skill trees,
and the MethodologyPackage SHA in PROJECT_AI.md. It never commits, pushes,
merges, edits the project's agent adapters, or touches 1C source/runtime.
First installation and uninstall are deliberately out of scope.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

OWNER = "Megabonstr/1c-ai-development-methodology"
PIN = re.compile(
    rb"(?m)^(MethodologyPackage:[ \t]*"
    rb"Megabonstr/1c-ai-development-methodology[ \t]*@[ \t]*)"
    rb"([0-9a-f]{40})([ \t]*\r?$)"
)
EXACT_SHA = re.compile(r"[0-9a-f]{40}\Z")


class RefreshError(Exception):
    pass


def git(repo: Path, *args: str) -> bytes:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if proc.returncode:
        detail = proc.stderr.decode("utf-8", "replace").strip()
        raise RefreshError(f"git {' '.join(args)} failed: {detail[:350]}")
    return proc.stdout


def root_of(path: Path) -> Path:
    root = path.expanduser().resolve(strict=True)
    resolved = Path(git(root, "rev-parse", "--show-toplevel").decode().strip()).resolve()
    if root != resolved:
        raise RefreshError(f"Expected exact Git worktree root: {root}; got {resolved}")
    return root


def exact_commit(repo: Path, sha: str) -> None:
    if not EXACT_SHA.fullmatch(sha):
        raise RefreshError("Source revision must be one exact lowercase 40-character Git SHA")
    resolved = git(repo, "rev-parse", "--verify", f"{sha}^{{commit}}").decode().strip()
    if resolved != sha:
        raise RefreshError(f"Requested revision does not resolve to the exact commit: {sha}")


def package_path(path: str) -> bool:
    return path.startswith(".1c-ai/") or (
        path.startswith(".agents/skills/1c-ai-")
        and len(PurePosixPath(path).parts) >= 4
    )


def inventory(repo: Path, sha: str) -> dict[str, str]:
    result: dict[str, str] = {}
    records = git(repo, "ls-tree", "-r", "-z", sha, "--", ".1c-ai", ".agents/skills")
    for record in records.split(b"\0"):
        if not record:
            continue
        try:
            header, raw_path = record.split(b"\t", 1)
            mode, kind, _ = header.decode("ascii").split(" ")
            path = raw_path.decode("utf-8")
        except (ValueError, UnicodeError) as exc:
            raise RefreshError(f"Unreadable package Git tree entry: {exc}") from exc
        if not package_path(path):
            continue
        if kind != "blob" or mode not in ("100644", "100755"):
            raise RefreshError(f"Package contains an unsupported entry: {path} ({mode}, {kind})")
        result[path] = mode
    if ".1c-ai/START_HERE.md" not in result:
        raise RefreshError(f"Package at {sha} lacks its canonical .1c-ai/START_HERE.md")
    if not any(p.startswith(".agents/skills/1c-ai-") and p.endswith("/SKILL.md")
               for p in result):
        raise RefreshError(f"Package at {sha} has no canonical 1c-ai-* skills")
    return result


def source_bytes(repo: Path, sha: str, path: str) -> bytes:
    return git(repo, "show", f"{sha}:{path}")


def destination(root: Path, rel: str) -> Path:
    p = PurePosixPath(rel)
    if p.is_absolute() or any(x in ("", ".", "..") for x in p.parts) or not package_path(rel):
        raise RefreshError(f"Unsafe package path: {rel}")
    current = root
    for part in p.parts:
        current = current / part
        if current.is_symlink():
            raise RefreshError(f"Symlink in target package path: {rel}")
    if not current.resolve(strict=False).is_relative_to(root):
        raise RefreshError(f"Package path escapes target worktree: {rel}")
    if current.exists() and not current.is_file():
        raise RefreshError(f"Package path is not a regular file: {rel}")
    return current


def parse_installed_pin(root: Path) -> tuple[str, bytes]:
    path = root / "PROJECT_AI.md"
    if path.is_symlink() or not path.is_file():
        raise RefreshError(
            "PROJECT_AI.md missing or unsafe; first adoption needs separate project approval"
        )
    original = path.read_bytes()
    matches = list(PIN.finditer(original))
    if len(matches) != 1:
        raise RefreshError("PROJECT_AI.md must contain exactly one valid MethodologyPackage SHA")
    return matches[0].group(2).decode("ascii"), original


def checksum(data: bytes | None) -> str | None:
    return hashlib.sha256(data).hexdigest() if data is not None else None


def plan(source: Path, target: Path, new_sha: str) -> tuple[dict, list, bytes]:
    exact_commit(source, new_sha)
    old_sha, project_ai = parse_installed_pin(target)
    exact_commit(source, old_sha)
    before, after = inventory(source, old_sha), inventory(source, new_sha)
    actions: list[tuple[str, str, bytes | None, str | None]] = []
    conflicts: list[dict] = []
    for path in sorted(set(before) | set(after)):
        dest = destination(target, path)
        current = dest.read_bytes() if dest.exists() else None
        old = source_bytes(source, old_sha, path) if path in before else None
        new = source_bytes(source, new_sha, path) if path in after else None
        if current == new:
            continue
        if current != old:
            conflicts.append({
                "path": path, "reason": "target differs from installed pinned package",
                "installed_sha256": checksum(old),
                "current_sha256": checksum(current),
                "new_sha256": checksum(new),
            })
            continue
        action = "ADD" if old is None else ("DELETE" if new is None else "UPDATE")
        actions.append((action, path, new, after.get(path)))
    summary = {
        "old_methodology_sha": old_sha,
        "new_methodology_sha": new_sha,
        "target": str(target),
        "actions": [{"op": a, "path": p, "new_sha256": checksum(data)}
                    for a, p, data, _ in actions],
        "conflicts": conflicts,
        "project_pin_change": old_sha != new_sha,
    }
    return summary, actions, project_ai


def perform(source: Path, target: Path, sha: str, apply: bool) -> int:
    summary, actions, project_ai = plan(source, target, sha)
    summary["mode"] = "APPLY" if apply else "PLAN"
    summary["applied"] = False
    if summary["conflicts"]:
        summary["state"] = "CONFLICT_STOP"
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 2
    if not apply:
        summary["state"] = "PLAN_READY"
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    if git(target, "status", "--porcelain=v1", "--untracked-files=all").strip():
        raise RefreshError("Target worktree is dirty; prepare a clean isolated feature branch")
    branch = git(target, "symbolic-ref", "--quiet", "--short", "HEAD").decode().strip()
    if not branch.startswith("feature/"):
        raise RefreshError(f"Refusing edits outside feature/* branch: {branch}")

    for action, path, data, mode in actions:
        dst = destination(target, path)
        if action == "DELETE":
            dst.unlink()
            continue
        assert data is not None
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
        if mode == "100755":
            dst.chmod(dst.stat().st_mode | 0o111)

    new_pin = PIN.sub(
        lambda match: match.group(1) + sha.encode("ascii") + match.group(3),
        project_ai, count=1,
    )
    if new_pin != project_ai:
        (target / "PROJECT_AI.md").write_bytes(new_pin)

    for action, path, data, _ in actions:
        dest = destination(target, path)
        actual = dest.read_bytes() if dest.exists() else None
        if actual != data:
            raise RefreshError(f"Post-write verification failed for {path}; inspect git diff")
    installed, _ = parse_installed_pin(target)
    if installed != sha:
        raise RefreshError("Post-write MethodologyPackage pin verification failed")
    summary["state"] = "APPLIED_UNCOMMITTED"
    summary["applied"] = True
    summary["target_branch"] = branch
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path, help="local methodology Git clone root")
    parser.add_argument("--target", required=True, type=Path, help="local adopting project Git root")
    parser.add_argument("--source-sha", required=True, help="exact accepted methodology commit SHA")
    parser.add_argument("--apply", action="store_true", help="apply plan on a clean feature branch")
    args = parser.parse_args()
    try:
        source, target = root_of(args.source), root_of(args.target)
        if source == target:
            raise RefreshError("Source and target Git worktrees must be different")
        return perform(source, target, args.source_sha, args.apply)
    except (RefreshError, OSError) as exc:
        print(f"REFRESH_BLOCKED: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
