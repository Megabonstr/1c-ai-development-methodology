#!/usr/bin/env python3
"""Mechanical repository contract validation."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "AGENT_START.txt",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".github/copilot-instructions.md",
    ".1c-ai/START_HERE.md",
    ".1c-ai/core/ADOPTION.md",
    ".1c-ai/core/DELIVERY_DISCIPLINE.md",
    ".1c-ai/core/EVIDENCE_MODEL.md",
    ".1c-ai/core/GIT_GITHUB_FLOW.md",
    ".1c-ai/core/ORCHESTRATION.md",
    ".1c-ai/core/PROJECT_STRUCTURE.md",
    ".1c-ai/core/SOURCE_FIRST.md",
    ".1c-ai/core/STOP_ASK.md",
    ".1c-ai/core/TASK_INTAKE.md",
    ".1c-ai/core/TASK_CONTRACT.md",
    ".1c-ai/core/TOKEN_DIET.md",
    ".1c-ai/core/VERIFICATION_PROFILES.md",
    ".1c-ai/router/ROUTER.md",
    ".1c-ai/profiles/1c-common/TASK_PREFLIGHT.md",
    ".1c-ai/profiles/1c-edt-mcp/PROFILE.md",
    ".1c-ai/profiles/1c-xml-configurator/PROFILE.md",
    "docs/ru/GIT_GITHUB_FLOW.md",
    "docs/ru/BEGINNER_GUIDE.md",
    "docs/ru/AI_COMMUNICATION.md",
    "docs/ru/EVIDENCE_MODEL.md",
    "docs/ru/VERIFICATION_PROFILES.md",
    "docs/ru/ARCHITECTURE.md",
    "docs/ru/ORCHESTRATION.md",
    "docs/ru/PROJECT_STRUCTURE.md",
    "docs/ru/TOKEN_DIET.md",
    "docs/ru/SOURCE_FIRST.md",
    "docs/ru/DEEP_RESEARCH.md",
    "docs/ru/EDT_MCP.md",
    "docs/ru/XML_CONFIGURATOR.md",
    "docs/ru/SKILLS.md",
    "docs/ru/SOURCES_AND_ADOPTION.md",
    "docs/ru/USEFUL_LINKS.md",
    "docs/ru/DELIVERY_DISCIPLINE.md",
    "docs/ru/ONE_C_TASK_PREFLIGHT.md",
    "docs/ru/TASK_FRAMING.md",
    "docs/architecture/REPOSITORY_MODEL.md",
    "docs/patterns/OPTIONAL_CLOUD_BRIDGE.md",
    "sources/SOURCES.md",
    ".github/ISSUE_TEMPLATE/implementation.yml",
    ".github/ISSUE_TEMPLATE/research.yml",
    ".github/pull_request_template.md",
    ".github/workflows/validate-repository.yml",
    "scripts/validate_repository.py",
]

EXPECTED_SKILLS = [
    "1c-ai-task-bootstrap",
    "1c-ai-task-framing",
    "1c-ai-source-first-research",
    "1c-ai-deep-research",
    "1c-ai-bounded-implementation",
    "1c-ai-focused-review",
    "1c-ai-focused-verification",
    "1c-ai-github-handoff",
    "1c-ai-local-runtime-validation",
    "1c-ai-task-closeout",
]

LEGACY_MACHINE_DIRS = [
    "docs/core",
    "router",
    "profiles",
    "skills",
]

SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CANONICAL_REF_RE = re.compile(
    r"`((?:\.1c-ai/(?:core|router|profiles)/|\.agents/skills/1c-ai-)"
    r"[A-Za-z0-9_./-]+)`"
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:
        fail(errors, f"cannot read {path.relative_to(ROOT)} as UTF-8: {exc}")
        return ""


def parse_simple_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = read_text(path, errors)
    lines = text.splitlines()
    rel = path.relative_to(ROOT)

    if not lines or lines[0].strip() != "---":
        fail(errors, f"{rel}: SKILL.md must start with YAML frontmatter delimiter '---'")
        return {}

    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        fail(errors, f"{rel}: missing closing YAML frontmatter delimiter '---'")
        return {}

    result: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            fail(errors, f"{rel}: unsupported frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key or not value:
            fail(errors, f"{rel}: frontmatter key/value must be non-empty: {line!r}")
            continue
        if key in result:
            fail(errors, f"{rel}: duplicate frontmatter key: {key}")
        result[key] = value
    return result


def validate_required_layout(errors: list[str]) -> None:
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).is_file():
            fail(errors, f"missing required file: {rel}")

    for rel in LEGACY_MACHINE_DIRS:
        if (ROOT / rel).exists():
            fail(errors, f"legacy machine tree must be absent: {rel}")

    claude_skills = ROOT / ".claude" / "skills"
    if claude_skills.exists() and list(claude_skills.glob("1c-ai-*")):
        fail(errors, "project .claude/skills/1c-ai-* mirror is forbidden")



PRIVATE_TEXT_SUFFIXES = {".md", ".txt", ".py", ".yml", ".yaml", ".json"}

# Construct known private markers from fragments so the forbidden exact strings
# do not themselves become tracked-text occurrences in this validator.
PRIVATE_MARKERS = (
    "Doctor" + "NSI",
    "Doctor" + " NSI",
    "Доктор" + " НСИ",
    "Megabonstr/" + "Doctor" + "NSI",
)


def validate_private_markers(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if ".git" in rel.parts or path.suffix.lower() not in PRIVATE_TEXT_SUFFIXES:
            continue
        text = read_text(path, errors)
        for marker in PRIVATE_MARKERS:
            if marker in text:
                fail(errors, f"{rel} contains forbidden private project marker")


def validate_agent_entry(errors: list[str]) -> None:
    path = ROOT / "AGENT_START.txt"
    if not path.is_file():
        return
    text = read_text(path, errors)
    if "DO NOT READ README.md" not in text:
        fail(errors, "AGENT_START.txt must explicitly tell agents not to read README.md")
    if len(text.splitlines()) > 100:
        fail(errors, "AGENT_START.txt exceeds the 100-line compact bootstrap budget")
    for token in (
        ".1c-ai/",
        "main",
        "preprod",
        "feature/<task>",
        "TOKEN DIET",
        "DELIVERY DISCIPLINE",
        "VERIFICATION PROFILE",
        "EVIDENCE CODES",
        ".1c-ai/core/ADOPTION.md",
        "Humans need not name skills",
        "CAPABILITY_BLOCKER",
    ):
        if token not in text:
            fail(errors, f"AGENT_START.txt missing compact contract token: {token}")


def validate_agent_adapters(errors: list[str]) -> None:
    for rel in ("AGENTS.md", "CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md"):
        path = ROOT / rel
        if not path.is_file():
            continue
        text = read_text(path, errors)
        if ".1c-ai/START_HERE.md" not in text:
            fail(errors, f"{rel} must route to .1c-ai/START_HERE.md")
        if len(text.splitlines()) > 15:
            fail(errors, f"{rel} exceeds the 15-line thin-adapter budget")


def validate_human_readme(errors: list[str]) -> None:
    path = ROOT / "README.md"
    if not path.is_file():
        return
    text = read_text(path, errors)
    first_lines = "\n".join(text.splitlines()[:12])
    agent_stop_tokens = ("AI AGENT / MODEL - STOP", "AI AGENT / MODEL \u2014 STOP")
    if not any(token in first_lines for token in agent_stop_tokens) or "AGENT_START.txt" not in first_lines:
        fail(errors, "README.md must warn AI agents at the top and route them to AGENT_START.txt")

    human_targets = (
        "docs/ru/GETTING_STARTED.md",
        "docs/ru/BEGINNER_GUIDE.md",
        "docs/ru/AI_COMMUNICATION.md",
        "docs/ru/GIT_GITHUB_FLOW.md",
        "docs/ru/EVIDENCE_MODEL.md",
        "docs/ru/VERIFICATION_PROFILES.md",
        "docs/ru/ARCHITECTURE.md",
        "docs/ru/ORCHESTRATION.md",
        "docs/ru/PROJECT_STRUCTURE.md",
        "docs/ru/TOKEN_DIET.md",
        "docs/ru/SOURCE_FIRST.md",
        "docs/ru/DEEP_RESEARCH.md",
        "docs/ru/EDT_MCP.md",
        "docs/ru/XML_CONFIGURATOR.md",
        "docs/ru/SKILLS.md",
        "docs/ru/SOURCES_AND_ADOPTION.md",
        "docs/ru/USEFUL_LINKS.md",
        "docs/ru/DELIVERY_DISCIPLINE.md",
        "docs/ru/ONE_C_TASK_PREFLIGHT.md",
    )
    for rel in human_targets:
        if rel not in text:
            fail(errors, f"README.md must link human readers to {rel}")

    quick_start = ROOT / "docs" / "ru" / "GETTING_STARTED.md"
    if quick_start.is_file():
        quick_text = read_text(quick_start, errors)
        for step in range(1, 7):
            if f"## Шаг {step}." not in quick_text:
                fail(errors, f"GETTING_STARTED.md missing quick-start step {step}")

        if quick_text.count("CoordinationScope:") < 2:
            fail(errors, "GETTING_STARTED.md must persist CoordinationScope in both minimal PROJECT_AI examples")
        if quick_text.count("OwningCoordinator:") < 2:
            fail(errors, "GETTING_STARTED.md must persist OwningCoordinator in both minimal PROJECT_AI examples")


def validate_branch_flow(errors: list[str]) -> None:
    for rel in (".1c-ai/core/GIT_GITHUB_FLOW.md", "docs/ru/GIT_GITHUB_FLOW.md"):
        path = ROOT / rel
        if not path.is_file():
            continue
        text = read_text(path, errors)
        for token in ("main", "preprod", "feature"):
            if token not in text:
                fail(errors, f"{rel}: missing branch-flow token {token!r}")

    machine = ROOT / ".1c-ai/core/GIT_GITHUB_FLOW.md"
    if machine.is_file():
        text = read_text(machine, errors)
        for token in ("feature -> preprod", "preprod -> main", "squash merge is allowed", "do NOT squash", "fast-forward preprod"):
            if token not in text:
                fail(errors, f"{machine.relative_to(ROOT)} missing ancestry token: {token!r}")

    workflow = ROOT / ".github/workflows/validate-repository.yml"
    if workflow.is_file() and "- preprod" not in read_text(workflow, errors):
        fail(errors, "validation workflow must run on pushes to preprod")


def validate_verification_profiles(errors: list[str]) -> None:
    profile = ROOT / ".1c-ai/core/VERIFICATION_PROFILES.md"
    if profile.is_file():
        text = read_text(profile, errors)
        for token in ("FAST_CLIENT_SLICE", "STANDARD", "HIGH_RISK", "0-3", "WORKING_NATIVE_RESULT"):
            if token not in text:
                fail(errors, f"{profile.relative_to(ROOT)} missing verification token: {token!r}")

    issue = ROOT / ".github/ISSUE_TEMPLATE/implementation.yml"
    if issue.is_file():
        text = read_text(issue, errors)
        for token in ("CoordinationScope:", "OwningCoordinator:", "id: coordination_owner"):
            if token not in text:
                fail(errors, f"{issue.relative_to(ROOT)} missing durable coordinator ownership token: {token!r}")
        for token in ("VerificationProfile", "Priority:", "TestBudget:", "ParityCadence:"):
            if token not in text:
                fail(errors, f"implementation Issue template missing verification token: {token!r}")

    for rel in (
        ".1c-ai/profiles/1c-edt-mcp/PROFILE.md",
        ".1c-ai/profiles/1c-xml-configurator/PROFILE.md",
    ):
        path = ROOT / rel
        if path.is_file() and ".1c-ai/core/VERIFICATION_PROFILES.md" not in read_text(path, errors):
            fail(errors, f"{rel} must route to .1c-ai/core/VERIFICATION_PROFILES.md")


def validate_1c_target_contract(errors: list[str]) -> None:
    common = ROOT / ".1c-ai/profiles/1c-common/TASK_PREFLIGHT.md"
    if common.is_file():
        text = read_text(common, errors)
        for token in (
            "DO_NOT_TOUCH",
            "MISSING_TARGET_POLICY",
            "FILTER_CONTRACT",
            "DataPath",
            "ExecutionContext",
            "Cardinality",
            "Positive target identity is the primary boundary.",
            "Optional material PRESERVE / DO_NOT_TOUCH",
        ):
            if token not in text:
                fail(errors, f"{common.relative_to(ROOT)} missing target-contract token: {token!r}")

    for rel in (
        ".1c-ai/profiles/1c-edt-mcp/PROFILE.md",
        ".1c-ai/profiles/1c-xml-configurator/PROFILE.md",
    ):
        path = ROOT / rel
        if path.is_file() and ".1c-ai/profiles/1c-common/TASK_PREFLIGHT.md" not in read_text(path, errors):
            fail(errors, f"{rel} must route relevant 1C tasks through common TASK_PREFLIGHT")

    issue = ROOT / ".github/ISSUE_TEMPLATE/implementation.yml"
    if issue.is_file():
        text = read_text(issue, errors)
        for token in (
            "DO_NOT_TOUCH",
            "MissingTargetPolicy",
            "FilterContract",
            "Positive scope / owned target",
            "optional material exception only; omit otherwise",
        ):
            if token not in text:
                fail(errors, f"implementation Issue template missing 1C target-contract token: {token!r}")


def validate_skills(errors: list[str]) -> None:
    root = ROOT / ".agents" / "skills"
    if not root.is_dir():
        fail(errors, "missing .agents/skills directory")
        return

    skill_files = sorted(root.glob("1c-ai-*/SKILL.md"))
    actual = [path.parent.name for path in skill_files]
    if actual != sorted(EXPECTED_SKILLS):
        fail(errors, f"canonical skills mismatch: {actual}")

    human_skills = ROOT / "docs" / "ru" / "SKILLS.md"
    if human_skills.is_file():
        human_text = read_text(human_skills, errors)
        for skill_name in EXPECTED_SKILLS:
            if skill_name not in human_text:
                fail(errors, f"docs/ru/SKILLS.md missing canonical skill identifier: {skill_name!r}")

    seen: set[str] = set()
    for path in skill_files:
        rel = path.relative_to(ROOT)
        text = read_text(path, errors)
        meta = parse_simple_frontmatter(path, errors)
        name = meta.get("name", "")
        description = meta.get("description", "")
        compatibility = meta.get("compatibility")

        if not name:
            fail(errors, f"{rel}: missing required frontmatter field 'name'")
        else:
            if len(name) > 64 or not SKILL_NAME_RE.fullmatch(name):
                fail(errors, f"{rel}: invalid skill name: {name!r}")
            if name != path.parent.name:
                fail(errors, f"{rel}: skill name {name!r} must match directory {path.parent.name!r}")
            if name in seen:
                fail(errors, f"{rel}: duplicate skill name: {name}")
            seen.add(name)

        if not description:
            fail(errors, f"{rel}: missing required frontmatter field 'description'")
        elif len(description) > 1024:
            fail(errors, f"{rel}: description exceeds 1024 characters")
        if compatibility is not None and len(compatibility) > 500:
            fail(errors, f"{rel}: compatibility exceeds 500 characters")
        if len(text.splitlines()) > 500:
            fail(errors, f"{rel}: SKILL.md exceeds the repository 500-line limit")


def validate_role_boundaries(errors: list[str]) -> None:
    role_contracts = {
        "1c-ai-task-framing": "Primary owner: Coordinator Main",
        "1c-ai-task-bootstrap": "Primary owner: Local Main",
        "1c-ai-source-first-research": "Shared / delegable skill with two explicit modes",
        "1c-ai-deep-research": "Primary owner: Coordinator Main",
        "1c-ai-bounded-implementation": "Primary owner: Local Main",
        "1c-ai-focused-review": "Primary owner: Local Main",
        "1c-ai-focused-verification": "Primary owner: Local Main",
        "1c-ai-github-handoff": "Shared / delegable Git-backed transport utility",
        "1c-ai-local-runtime-validation": "Primary owner: Local Main",
        "1c-ai-task-closeout": "Primary owner: Coordinator Main",
    }
    for skill_name, token in role_contracts.items():
        path = ROOT / ".agents" / "skills" / skill_name / "SKILL.md"
        if path.is_file() and token not in read_text(path, errors):
            fail(errors, f"{path.relative_to(ROOT)} missing role ownership token: {token!r}")

    router = ROOT / ".1c-ai" / "router" / "ROUTER.md"
    if router.is_file():
        text = read_text(router, errors)
        for token in (
            "Coordinator Main - pre-execution",
            "Handoff boundary - Local Main ingress",
            "Local Main - execution",
            "Shared transport and specialist delegation",
            "Coordinator Main - post-execution",
            "Local Main receives the executable task, not the process/history that created it.",
        ):
            if token not in text:
                fail(errors, f"{router.relative_to(ROOT)} missing role-routing token: {token!r}")
        if "what Local Main is doing now" in text:
            fail(errors, f"{router.relative_to(ROOT)} must not define every workflow intent as Local Main work")

    token_diet = ROOT / ".1c-ai" / "core" / "TOKEN_DIET.md"
    if token_diet.is_file():
        text = read_text(token_diet, errors)
        for token in (
            "## Coordinator context ownership",
            "## Local Main execution context",
            "DoNotTouch / ProhibitedChanges",
            "optional and sparse",
            "Positive scope is the default boundary.",
            "CAPABILITY_BLOCKER",
            "durable result destination",
        ):
            if token not in text:
                fail(errors, f"{token_diet.relative_to(ROOT)} missing role-context section: {token!r}")

    task_contract = ROOT / ".1c-ai" / "core" / "TASK_CONTRACT.md"
    if task_contract.is_file():
        text = read_text(task_contract, errors)
        for token in (
            "## Ownership of task state",
            "Default boundary is positive",
            "optional sparse material exceptions",
            "directly necessary adjacent technical fix-forward work",
        ):
            if token not in text:
                fail(errors, f"{task_contract.relative_to(ROOT)} missing semantic-vs-execution ownership boundary: {token!r}")

    orchestration = ROOT / ".1c-ai" / "core" / "ORCHESTRATION.md"
    if orchestration.is_file():
        text = read_text(orchestration, errors)
        for token in (
            "## 11. Lifecycle closeout",
            "one authoritative compact closeout",
            ".agents/skills/1c-ai-task-closeout/SKILL.md",
            "small directly necessary adjacent technical changes",
            "CAPABILITY_BLOCKER",
        ):
            if token not in text:
                fail(errors, f"{orchestration.relative_to(ROOT)} missing lifecycle-closeout token: {token!r}")

    evidence = ROOT / ".1c-ai" / "core" / "EVIDENCE_MODEL.md"
    if evidence.is_file() and "## Closeout is not evidence" not in read_text(evidence, errors):
        fail(errors, f"{evidence.relative_to(ROOT)} must keep closeout separate from evidence")

    verification = ROOT / ".1c-ai" / "core" / "VERIFICATION_PROFILES.md"
    if verification.is_file():
        text = read_text(verification, errors)
        for token in (
            "verification returns one final compact result/evidence packet",
            "Do not create two full reports for the same task.",
        ):
            if token not in text:
                fail(errors, f"{verification.relative_to(ROOT)} missing closeout/report boundary token: {token!r}")


def validate_adoption_contract(errors: list[str]) -> None:
    adoption = ROOT / ".1c-ai" / "core" / "ADOPTION.md"
    if adoption.is_file():
        text = read_text(adoption, errors)
        for token in (
            "MANUAL_PINNED_COPY",
            "NONE",
            "SELECTIVE",
            "FULL",
            "does not require an existing TaskHandle",
            "MethodologyPackage: Megabonstr/1c-ai-development-methodology @ <exact 40-char SHA>",
            "MANUAL_STRUCTURE_CHECK",
            "GitlessDurableBackend: NOT_SHIPPED",
            "[#2](https://github.com/Megabonstr/1c-ai-development-methodology/issues/2)",
            "[#1](https://github.com/Megabonstr/1c-ai-development-methodology/issues/1)",
        ):
            if token not in text:
                fail(errors, f"{adoption.relative_to(ROOT)} missing adoption token: {token!r}")

    for rel in ("AGENT_START.txt", ".1c-ai/START_HERE.md", ".1c-ai/router/ROUTER.md"):
        path = ROOT / rel
        if path.is_file():
            text = read_text(path, errors)
            if ".1c-ai/core/ADOPTION.md" not in text:
                fail(errors, f"{rel} must route pre-install evaluation to ADOPTION.md")

    adapters = ("AGENTS.md", "CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md")
    for rel in adapters:
        path = ROOT / rel
        if path.is_file() and "methodology evaluation/adoption may start from a repository URL/ref" not in read_text(path, errors):
            fail(errors, f"{rel} must allow URL-first methodology evaluation/adoption")

    claude = ROOT / "CLAUDE.md"
    if claude.is_file():
        text = read_text(claude, errors)
        if "unrelated project-owned Claude skills may coexist" not in text:
            fail(errors, "CLAUDE.md must preserve unrelated project-owned Claude skills")

    quick = ROOT / "docs" / "ru" / "GETTING_STARTED.md"
    if quick.is_file():
        text = read_text(quick, errors)
        if "MethodologyPackage: Megabonstr/1c-ai-development-methodology @ <exact SHA from step 1>" not in text:
            fail(errors, "GETTING_STARTED.md must record the exact methodology SHA during manual pinned adoption")


def validate_local_context_budget(errors: list[str]) -> None:
    local_skills = (
        "1c-ai-task-bootstrap",
        "1c-ai-bounded-implementation",
        "1c-ai-focused-verification",
        "1c-ai-local-runtime-validation",
    )
    for skill_name in local_skills:
        path = ROOT / ".agents" / "skills" / skill_name / "SKILL.md"
        if not path.is_file():
            continue
        text = read_text(path, errors)
        if "## Minimal read path" not in text:
            fail(errors, f"{path.relative_to(ROOT)} must define a Minimal read path")
        if "## Required core\n\nRead:" in text:
            fail(errors, f"{path.relative_to(ROOT)} must not require unconditional full-core reads")

    for rel in (".1c-ai/profiles/1c-edt-mcp/PROFILE.md", ".1c-ai/profiles/1c-xml-configurator/PROFILE.md"):
        path = ROOT / rel
        if path.is_file() and "## Progressive-disclosure read path" not in read_text(path, errors):
            fail(errors, f"{rel} missing progressive-disclosure profile read path")

    token_diet = ROOT / ".1c-ai" / "core" / "TOKEN_DIET.md"
    if token_diet.is_file() and "### Simple Local fast path" not in read_text(token_diet, errors):
        fail(errors, "TOKEN_DIET.md missing simple Local fast path")


def validate_gitless_status(errors: list[str]) -> None:
    project_structure = ROOT / ".1c-ai" / "core" / "PROJECT_STRUCTURE.md"
    if project_structure.is_file():
        text = read_text(project_structure, errors)
        for token in ("DESIGNED_DEGRADED_COMPATIBILITY", "no operational Gitless durable-state backend", "[#1](https://github.com/Megabonstr/1c-ai-development-methodology/issues/1)"):
            if token not in text:
                fail(errors, f"{project_structure.relative_to(ROOT)} missing Gitless status token: {token!r}")

    machine_paths = (
        ".1c-ai/core/TASK_CONTRACT.md",
        ".1c-ai/core/GIT_GITHUB_FLOW.md",
        ".1c-ai/core/ORCHESTRATION.md",
        ".1c-ai/profiles/1c-edt-mcp/PROFILE.md",
        ".1c-ai/profiles/1c-xml-configurator/PROFILE.md",
        ".agents/skills/1c-ai-task-bootstrap/SKILL.md",
        ".agents/skills/1c-ai-bounded-implementation/SKILL.md",
        ".agents/skills/1c-ai-focused-verification/SKILL.md",
        ".agents/skills/1c-ai-local-runtime-validation/SKILL.md",
        ".agents/skills/1c-ai-deep-research/SKILL.md",
        ".agents/skills/1c-ai-github-handoff/SKILL.md",
        ".agents/skills/1c-ai-task-closeout/SKILL.md",
    )
    forbidden = ("accepted durable-state contract", "accepted Gitless snapshot/fingerprint", "accepted durable-state carrier")
    for rel in machine_paths:
        path = ROOT / rel
        if not path.is_file():
            continue
        text = read_text(path, errors)
        for token in forbidden:
            if token in text:
                fail(errors, f"{rel} overstates shipped Gitless support: {token!r}")

def validate_canonical_links(errors: list[str]) -> None:
    owners = [
        ROOT / ".1c-ai" / "START_HERE.md",
        ROOT / ".1c-ai" / "router" / "ROUTER.md",
        ROOT / "AGENT_START.txt",
        ROOT / "README.md",
        ROOT / "docs" / "architecture" / "REPOSITORY_MODEL.md",
    ]
    owners += sorted((ROOT / ".1c-ai" / "core").glob("*.md"))
    owners += sorted((ROOT / ".1c-ai" / "profiles").glob("**/*.md"))
    owners += sorted((ROOT / ".agents" / "skills").glob("1c-ai-*/SKILL.md"))
    owners += sorted((ROOT / "docs" / "ru").glob("*.md"))

    legacy_patterns = (
        re.compile(r"(?<!\.1c-ai/)docs/START_HERE\.md"),
        re.compile(r"docs/core/"),
        re.compile(r"(?<!\.1c-ai/)router/ROUTER\.md"),
        re.compile(r"(?<!\.1c-ai/)profiles/1c-common/"),
        re.compile(r"(?<!\.1c-ai/)profiles/1c-edt-mcp/"),
        re.compile(r"(?<!\.1c-ai/)profiles/1c-xml-configurator/"),
        re.compile(r"(?<!1c-ai-)skills/task-bootstrap"),
        re.compile(r"(?<!1c-ai-)skills/task-framing"),
        re.compile(r"(?<!1c-ai-)skills/source-first-research"),
        re.compile(r"(?<!1c-ai-)skills/bounded-implementation"),
        re.compile(r"(?<!1c-ai-)skills/focused-review"),
        re.compile(r"(?<!1c-ai-)skills/focused-verification"),
        re.compile(r"(?<!1c-ai-)skills/github-handoff"),
        re.compile(r"(?<!1c-ai-)skills/local-runtime-validation"),
        re.compile(r"(?<!1c-ai-)skills/task-closeout"),
    )

    for path in owners:
        if not path.is_file():
            continue
        text = read_text(path, errors)
        for pattern in legacy_patterns:
            if pattern.search(text):
                fail(errors, f"{path.relative_to(ROOT)} contains stale canonical path matching: {pattern.pattern}")

        for rel in sorted(set(CANONICAL_REF_RE.findall(text))):
            if not (ROOT / rel).is_file():
                fail(errors, f"{path.relative_to(ROOT)} references missing canonical file: {rel}")



def validate_project_structure(errors: list[str]) -> None:
    machine = ROOT / ".1c-ai/core/PROJECT_STRUCTURE.md"
    human = ROOT / "docs/ru/PROJECT_STRUCTURE.md"

    if machine.is_file():
        text = read_text(machine, errors)
        for token in (
            "PROJECT_AI.md",
            ".1c-ai/**",
            ".agents/skills/1c-ai-*/**",
            "reserved `1c-ai-` prefix",
            ".tmp/1c-ai/",
            "GitHub Issue/PR/commit/CI",
            "optional independent third backup",
            "secrets",
            "UNKNOWN",
        ):
            if token not in text:
                fail(errors, f"{machine.relative_to(ROOT)} missing project-structure token: {token!r}")

    if human.is_file():
        text = read_text(human, errors)
        for token in ("PROJECT_AI.md", ".1c-ai", ".agents/skills/1c-ai-", "docs/research/", "Резервное копирование"):
            if token not in text:
                fail(errors, f"{human.relative_to(ROOT)} missing human project-structure token: {token!r}")

    start = ROOT / ".1c-ai/START_HERE.md"
    if start.is_file() and ".1c-ai/core/PROJECT_STRUCTURE.md" not in read_text(start, errors):
        fail(errors, ".1c-ai/START_HERE.md must route to PROJECT_STRUCTURE.md")

    readme = ROOT / "README.md"
    if readme.is_file() and "docs/ru/PROJECT_STRUCTURE.md" not in read_text(readme, errors):
        fail(errors, "README.md must link docs/ru/PROJECT_STRUCTURE.md")

    agent_start = ROOT / "AGENT_START.txt"
    if agent_start.is_file() and "PROJECT_AI.md" not in read_text(agent_start, errors):
        fail(errors, "AGENT_START.txt must route to PROJECT_AI.md when present")



def validate_useful_links(errors: list[str]) -> None:
    path = ROOT / "docs/ru/USEFUL_LINKS.md"
    if not path.is_file():
        return

    text = read_text(path, errors)
    lower = text.lower()

    if "utm_" in lower or "utm_source=" in lower:
        fail(errors, "docs/ru/USEFUL_LINKS.md must not contain UTM/tracking links")

    for token in (
        "https://github.com/DitriXNew/EDT-MCP",
        "https://github.com/Nikolay-Shirokov/cc-1c-skills",
        "https://github.com/bia-technologies/yaxunit",
        "https://github.com/1C-Company/v8-code-style",
        "https://github.com/1c-syntax/bsl-language-server",
        "https://github.com/1c-syntax/ssl_3_1",
        "https://agentskills.io/",
    ):
        if token not in text:
            fail(errors, f"docs/ru/USEFUL_LINKS.md missing key source: {token}")

    if "https://github.com/marmyshev/edt-editing" in text:
        fail(errors, "docs/ru/USEFUL_LINKS.md must not recommend the known mirror as a primary source")

    readme = ROOT / "README.md"
    if readme.is_file() and "docs/ru/USEFUL_LINKS.md" not in read_text(readme, errors):
        fail(errors, "README.md must link docs/ru/USEFUL_LINKS.md")



def validate_coordinator_main(errors: list[str]) -> None:
    current_role_files = [
        ROOT / "AGENT_START.txt",
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / "GEMINI.md",
        ROOT / ".github" / "copilot-instructions.md",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "implementation.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "research.yml",
        ROOT / ".1c-ai" / "START_HERE.md",
        ROOT / ".1c-ai" / "router" / "ROUTER.md",
        ROOT / "docs" / "architecture" / "REPOSITORY_MODEL.md",
        ROOT / "README.md",
    ]
    current_role_files += sorted((ROOT / ".1c-ai" / "core").glob("*.md"))
    current_role_files += sorted((ROOT / ".1c-ai" / "profiles").glob("**/*.md"))
    current_role_files += sorted((ROOT / ".agents" / "skills").glob("1c-ai-*/SKILL.md"))
    current_role_files += sorted((ROOT / "docs" / "ru").glob("*.md"))

    for path in current_role_files:
        if not path.is_file():
            continue
        text = read_text(path, errors)
        if "Cloud Main" in text:
            fail(errors, f"{path.relative_to(ROOT)} contains stale canonical Cloud Main terminology")

    orchestration = ROOT / ".1c-ai" / "core" / "ORCHESTRATION.md"
    if orchestration.is_file():
        text = read_text(orchestration, errors)
        for token in (
            "Coordinator Main",
            "CoordinationScope",
            "OwningCoordinator",
            "Local Main",
            "cloud-hosted Coordinator Main",
            "co-located physical execution",
        ):
            if token not in text:
                fail(errors, f"{orchestration.relative_to(ROOT)} missing coordinator token: {token!r}")

    task_contract = ROOT / ".1c-ai" / "core" / "TASK_CONTRACT.md"
    if task_contract.is_file():
        text = read_text(task_contract, errors)
        for token in ("CoordinationScope", "OwningCoordinator"):
            if token not in text:
                fail(errors, f"{task_contract.relative_to(ROOT)} missing coordinator task-contract token: {token!r}")

    project_structure = ROOT / ".1c-ai" / "core" / "PROJECT_STRUCTURE.md"
    if project_structure.is_file():
        text = read_text(project_structure, errors)
        for token in ("CoordinationScope:", "OwningCoordinator:", "AcceptedCheckpoint:", "PROJECT_AI.md"):
            if token not in text:
                fail(errors, f"{project_structure.relative_to(ROOT)} missing coordinator context token: {token!r}")

    token_diet = ROOT / ".1c-ai" / "core" / "TOKEN_DIET.md"
    if token_diet.is_file():
        text = read_text(token_diet, errors)
        if "does not authorize full-scope preload" not in text:
            fail(errors, "TOKEN_DIET must state that CoordinationScope ownership does not authorize full-scope preload")

    human_orchestration = ROOT / "docs" / "ru" / "ORCHESTRATION.md"
    if human_orchestration.is_file():
        text = read_text(human_orchestration, errors)
        for token in ("Главный координатор", "CoordinationScope", "OwningCoordinator", "пример текущей практической реализации"):
            if token not in text:
                fail(errors, f"{human_orchestration.relative_to(ROOT)} missing human coordinator token: {token!r}")



def validate_transport_neutrality(errors: list[str]) -> None:
    adapters = (
        "AGENTS.md",
        "CLAUDE.md",
        "GEMINI.md",
        ".github/copilot-instructions.md",
    )
    for rel in adapters:
        path = ROOT / rel
        if not path.is_file():
            continue
        text = read_text(path, errors)
        if "durable task/task-state handle" not in text:
            fail(errors, f"{rel} must use a transport-neutral durable task/task-state handle")
        if "GitHub Issue/task" in text:
            fail(errors, f"{rel} must not require a GitHub Issue for the generic entry path")

    generic_contracts = {
        ".agents/skills/1c-ai-task-bootstrap/SKILL.md": (
            "Git-backed",
            "Gitless",
            "source/version identity",
        ),
        ".agents/skills/1c-ai-bounded-implementation/SKILL.md": (
            "Git-backed",
            "Gitless",
            "source/version identity",
        ),
        ".agents/skills/1c-ai-deep-research/SKILL.md": (
            "durable task state",
            "Git-backed",
            "Gitless",
        ),
        ".1c-ai/profiles/1c-edt-mcp/PROFILE.md": (
            "Git-backed",
            "Gitless",
            "source/version identity",
        ),
        ".1c-ai/profiles/1c-xml-configurator/PROFILE.md": (
            "Git-backed",
            "Gitless",
            "source/version identity",
        ),
        ".1c-ai/core/TASK_CONTRACT.md": (
            "Source / version identity",
            "Git-backed",
            "Gitless",
        ),
        ".agents/skills/1c-ai-focused-verification/SKILL.md": (
            "source/version/artifact identity",
            "Git-backed",
            "Gitless",
        ),
        ".agents/skills/1c-ai-local-runtime-validation/SKILL.md": (
            "source/version identity",
            "Git-backed",
            "Gitless",
        ),
    }
    for rel, tokens in generic_contracts.items():
        path = ROOT / rel
        if not path.is_file():
            continue
        text = read_text(path, errors)
        for token in tokens:
            if token not in text:
                fail(errors, f"{rel} missing transport-neutral contract token: {token!r}")

    for rel in (
        ".agents/skills/1c-ai-task-bootstrap/SKILL.md",
        ".agents/skills/1c-ai-bounded-implementation/SKILL.md",
        ".agents/skills/1c-ai-deep-research/SKILL.md",
        ".agents/skills/1c-ai-focused-verification/SKILL.md",
        ".agents/skills/1c-ai-local-runtime-validation/SKILL.md",
    ):
        path = ROOT / rel
        if not path.is_file():
            continue
        text = read_text(path, errors)
        if "GitHub remains canonical" in text:
            fail(errors, f"{rel} must not make GitHub canonical for the generic workflow")

    local_runtime = ROOT / ".agents" / "skills" / "1c-ai-local-runtime-validation" / "SKILL.md"
    if local_runtime.is_file():
        text = read_text(local_runtime, errors)
        if "- `.1c-ai/core/GIT_GITHUB_FLOW.md`\n" in text:
            fail(errors, "local-runtime-validation must load GIT_GITHUB_FLOW only for Git-backed projects")
        if "exact Git commit or artifact" in text or "Do not validate an unspecified moving branch" in text:
            fail(errors, "local-runtime-validation contains stale Git-only verification wording")


def validate_task_framing_route(errors: list[str]) -> None:
    router = ROOT / ".1c-ai" / "router" / "ROUTER.md"
    if router.is_file():
        text = read_text(router, errors)
        for token in (
            ".agents/skills/1c-ai-task-framing/SKILL.md",
            "Skill selection is agent-owned",
            "clarification dialogue",
        ):
            if token not in text:
                fail(errors, f"router missing task-framing/intent-routing token: {token!r}")

    skill = ROOT / ".agents" / "skills" / "1c-ai-task-framing" / "SKILL.md"
    if skill.is_file():
        text = read_text(skill, errors)
        for token in (
            "## Route ownership",
            "## Clarification dialogue mode",
            "The Human Owner does not need to say",
            "Do not invoke framing merely because the user is conversational",
        ):
            if token not in text:
                fail(errors, f"{skill.relative_to(ROOT)} missing clarification token: {token!r}")

    human = ROOT / "docs" / "ru" / "AI_COMMUNICATION.md"
    if human.is_file():
        text = read_text(human, errors)
        for token in (
            "Вам не нужно знать названия навыков",
            "Режим уточнения задачи",
            "Коррекция:",
            "Что написать агенту",
        ):
            if token not in text:
                fail(errors, f"{human.relative_to(ROOT)} missing human communication token: {token!r}")

    for rel in ("README.md", "docs/ru/BEGINNER_GUIDE.md", "docs/ru/TOKEN_DIET.md"):
        path = ROOT / rel
        if path.is_file() and "AI_COMMUNICATION.md" not in read_text(path, errors):
            fail(errors, f"{rel} must link the human AI communication guide")


def validate_deep_research(errors: list[str]) -> None:
    skill = ROOT / ".agents" / "skills" / "1c-ai-deep-research" / "SKILL.md"
    human = ROOT / "docs" / "ru" / "DEEP_RESEARCH.md"
    router = ROOT / ".1c-ai" / "router" / "ROUTER.md"

    if skill.is_file():
        text = read_text(skill, errors)
        for token in (
            "Pass V1",
            "Pass V2",
            "Pass V3",
            "10-15 new unique credible sources",
            "SOURCE_LIMIT",
            "ISSUE_ONLY",
            "REPO_ARTIFACTS",
            "ISSUE_PLUS_EXTERNAL_BACKUP",
            "OwningCoordinator",
            "Do **not** use this skill for",
        ):
            if token not in text:
                fail(errors, f"{skill.relative_to(ROOT)} missing deep-research token: {token!r}")

    if human.is_file():
        text = read_text(human, errors)
        for token in ("V1", "V2", "V3", "10-15", "SOURCE_LIMIT", "Coordinator Main", "OwningCoordinator"):
            if token not in text:
                fail(errors, f"{human.relative_to(ROOT)} missing human deep-research token: {token!r}")

    if router.is_file():
        text = read_text(router, errors)
        if ".agents/skills/1c-ai-deep-research/SKILL.md" not in text:
            fail(errors, "router must reference 1c-ai-deep-research")
        if "Do not route one API/signature/version lookup" not in text:
            fail(errors, "router must keep bounded lookup/implementation defects out of deep research")



def validate_optional_cloud_bridge(errors: list[str]) -> None:
    pattern = ROOT / "docs" / "patterns" / "OPTIONAL_CLOUD_BRIDGE.md"
    human = ROOT / "docs" / "ru" / "ORCHESTRATION.md"

    if pattern.is_file():
        text = read_text(pattern, errors)
        for token in (
            "optional provider-dependent acceleration pattern",
            "TaskRevision:",
            "ResultID:",
            "DecisionRequired:",
            "DecisionID:",
            "ParentResultID:",
            "X-GitHub-Delivery",
            "Never blindly retry a result comment",
            "Manual fallback",
            "UNKNOWN",
        ):
            if token not in text:
                fail(errors, f"{pattern.relative_to(ROOT)} missing bridge token: {token!r}")

        for forbidden in (
            "Issue-comment wake-up is supported",
            "arbitrary existing cloud conversation is supported",
        ):
            if forbidden in text:
                fail(errors, f"{pattern.relative_to(ROOT)} makes an unproven provider claim: {forbidden!r}")

    if human.is_file():
        text = read_text(human, errors)
        if "../patterns/OPTIONAL_CLOUD_BRIDGE.md" not in text:
            fail(errors, "docs/ru/ORCHESTRATION.md must link the optional cloud bridge pattern")


def validate_issue_forms(errors: list[str]) -> None:
    for rel in (".github/ISSUE_TEMPLATE/implementation.yml", ".github/ISSUE_TEMPLATE/research.yml"):
        path = ROOT / rel
        if not path.is_file():
            continue
        text = read_text(path, errors)
        if "\t" in text:
            fail(errors, f"{rel}: tabs are not allowed in Issue Form YAML")
        for key in ("name:", "description:", "body:"):
            if not any(line.startswith(key) for line in text.splitlines()):
                fail(errors, f"{rel}: missing top-level {key}")


def main() -> int:
    errors: list[str] = []

    validate_required_layout(errors)
    validate_private_markers(errors)
    validate_agent_entry(errors)
    validate_agent_adapters(errors)
    validate_human_readme(errors)
    validate_branch_flow(errors)
    validate_verification_profiles(errors)
    validate_1c_target_contract(errors)
    validate_skills(errors)
    validate_role_boundaries(errors)
    validate_adoption_contract(errors)
    validate_local_context_budget(errors)
    validate_gitless_status(errors)
    validate_canonical_links(errors)
    validate_project_structure(errors)
    validate_useful_links(errors)
    validate_coordinator_main(errors)
    validate_transport_neutrality(errors)
    validate_task_framing_route(errors)
    validate_deep_research(errors)
    validate_optional_cloud_bridge(errors)
    validate_issue_forms(errors)

    if errors:
        print("Repository validation FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Repository validation OK: "
        f"{len(EXPECTED_SKILLS)} canonical skills; "
        "installable package layout, human/agent split, and branch flow resolved."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
