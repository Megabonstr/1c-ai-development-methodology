#!/usr/bin/env python3
"""Offline contract tests for the pinned existing-package refresh helper."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "refresh_existing_package.py"
ADAPTER = "# Local project adapter -- preserve me\n"
LOCAL_SKILL = "# Project-owned EDT skill -- preserve me\n"


def git(repo: Path, *args: str) -> str:
    p = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True, check=True, encoding="utf-8",
    )
    return p.stdout.strip()


def put(repo: Path, rel: str, text: str) -> None:
    dst = repo / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")


def commit(repo: Path, message: str) -> str:
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", message)
    return git(repo, "rev-parse", "HEAD")


class RefreshExistingPinnedPackageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(prefix="methodology-refresh-")
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name)
        self.source = base / "method"
        self.target = base / "project"
        for repo in (self.source, self.target):
            repo.mkdir()
            git(repo, "init", "-q", "-b", "main")
            git(repo, "config", "user.email", "test@example.invalid")
            git(repo, "config", "user.name", "Methodology Test")

        put(self.source, ".1c-ai/START_HERE.md", "router old\n")
        put(self.source, ".1c-ai/core/ADOPTION.md", "adoption old\n")
        put(self.source, ".agents/skills/1c-ai-primary/SKILL.md", "skill old\n")
        put(self.source, ".agents/skills/1c-ai-retired/SKILL.md", "old retired\n")
        self.old_sha = commit(self.source, "old package")

        for p, value in (
            (".1c-ai/START_HERE.md", "router old\n"),
            (".1c-ai/core/ADOPTION.md", "adoption old\n"),
            (".agents/skills/1c-ai-primary/SKILL.md", "skill old\n"),
            (".agents/skills/1c-ai-retired/SKILL.md", "old retired\n"),
            ("AGENTS.md", ADAPTER),
            (".agents/skills/edt-mcp-project-forms/SKILL.md", LOCAL_SKILL),
            ("CODEX/instructions/START_HERE.md", "project policy\n"),
            ("PROJECT_AI.md",
                "# Project\nMethodologyPackage: "
                f"Megabonstr/1c-ai-development-methodology @ {self.old_sha}\n"
                "Knowledge: client-specific\n"),
        ):
            put(self.target, p, value)
        commit(self.target, "installed pinned package")
        git(self.target, "checkout", "-qb", "feature/refresh")

        put(self.source, ".1c-ai/START_HERE.md", "router new\n")
        put(self.source, ".1c-ai/core/ADOPTION.md", "adoption new\n")
        put(self.source, ".1c-ai/core/NEW.md", "new package owner\n")
        put(self.source, ".agents/skills/1c-ai-primary/SKILL.md", "skill new\n")
        git(self.source, "rm", "-q", ".agents/skills/1c-ai-retired/SKILL.md")
        self.new_sha = commit(self.source, "new package")

    def call(self, *extras: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT),
             "--source", str(self.source), "--target", str(self.target),
             "--source-sha", self.new_sha, *extras],
            text=True, capture_output=True, encoding="utf-8", check=False,
        )

    def test_plan_is_read_only_then_apply_updates_only_shared_files(self) -> None:
        before = git(self.target, "status", "--porcelain")
        planned = self.call()
        self.assertEqual(planned.returncode, 0, planned.stderr)
        data = json.loads(planned.stdout)
        self.assertEqual(data["state"], "PLAN_READY")
        self.assertFalse(data["applied"])
        self.assertEqual(git(self.target, "status", "--porcelain"), before)
        self.assertEqual(
            set(x["op"] for x in data["actions"]), {"UPDATE", "ADD", "DELETE"},
        )
        result = self.call("--apply")
        self.assertEqual(result.returncode, 0, result.stderr)
        applied = json.loads(result.stdout)
        self.assertEqual(applied["state"], "APPLIED_UNCOMMITTED")
        self.assertEqual((self.target / ".1c-ai/START_HERE.md").read_text(), "router new\n")
        self.assertEqual((self.target / ".1c-ai/core/NEW.md").read_text(), "new package owner\n")
        self.assertFalse((self.target / ".agents/skills/1c-ai-retired/SKILL.md").exists())
        self.assertEqual(
            (self.target / ".agents/skills/edt-mcp-project-forms/SKILL.md").read_text(),
            LOCAL_SKILL,
        )
        self.assertEqual((self.target / "AGENTS.md").read_text(), ADAPTER)
        self.assertEqual(
            (self.target / "CODEX/instructions/START_HERE.md").read_text(),
            "project policy\n",
        )
        marker = (self.target / "PROJECT_AI.md").read_text()
        self.assertIn(self.new_sha, marker)
        self.assertIn("Knowledge: client-specific", marker)
        self.assertNotIn(self.old_sha, marker)

    def test_repeat_after_committing_is_noop(self) -> None:
        result = self.call("--apply")
        self.assertEqual(result.returncode, 0, result.stderr)
        commit(self.target, "accepted methodology refresh")
        again = self.call("--apply")
        self.assertEqual(again.returncode, 0, again.stderr)
        self.assertEqual(json.loads(again.stdout)["actions"], [])
        self.assertEqual(git(self.target, "status", "--porcelain"), "")

    def test_local_customization_in_owned_file_stops_before_writing(self) -> None:
        put(self.target, ".1c-ai/START_HERE.md", "project custom router\n")
        commit(self.target, "project-local modification")
        before = (self.target / "PROJECT_AI.md").read_bytes()
        result = self.call("--apply")
        self.assertEqual(result.returncode, 2)
        data = json.loads(result.stdout)
        self.assertEqual(data["state"], "CONFLICT_STOP")
        self.assertTrue(any(x["path"] == ".1c-ai/START_HERE.md" for x in data["conflicts"]))
        self.assertEqual((self.target / "PROJECT_AI.md").read_bytes(), before)
        self.assertEqual((self.target / ".1c-ai/core/ADOPTION.md").read_text(), "adoption old\n")

    def test_dirty_worktree_refuses_apply_but_plan_succeeds(self) -> None:
        put(self.target, "UNTRACKED.tmp", "foreign data\n")
        self.assertEqual(self.call().returncode, 0)
        blocked = self.call("--apply")
        self.assertEqual(blocked.returncode, 3)
        self.assertIn("dirty", blocked.stderr.lower())
        self.assertIn(self.old_sha, (self.target / "PROJECT_AI.md").read_text())

    def test_no_writes_outside_feature_branch(self) -> None:
        git(self.target, "checkout", "-q", "main")
        blocked = self.call("--apply")
        self.assertEqual(blocked.returncode, 3)
        self.assertIn("feature/*", blocked.stderr)

    def test_no_implicit_first_install_or_missing_old_revision(self) -> None:
        (self.target / "PROJECT_AI.md").unlink()
        result = self.call("--apply")
        self.assertEqual(result.returncode, 3)
        self.assertIn("PROJECT_AI.md", result.stderr)

    def test_symlink_in_package_target_fails_closed(self) -> None:
        path = self.target / ".1c-ai/core/ADOPTION.md"
        path.unlink()
        path.symlink_to(self.target / "AGENTS.md")
        result = self.call()
        self.assertEqual(result.returncode, 3)
        self.assertIn("Symlink", result.stderr)
        self.assertEqual((self.target / "AGENTS.md").read_text(), ADAPTER)


if __name__ == "__main__":
    unittest.main()
