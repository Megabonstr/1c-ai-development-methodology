# Existing-project methodology refresh (Git-backed, review first)

Status: BOUNDED UPDATE HELPER; not a general installer/uninstaller or a replacement for project-specific agent policy.
Machine entry: ../../PROJECT_REFRESH_AGENT_START.txt in the methodology repository.
Implementation: ../../scripts/refresh_existing_package.py.
Canonical adoption owner for new/unpinned projects: ADOPTION.md.
Owner issue: https://github.com/Megabonstr/1c-ai-development-methodology/issues/2

## Decision before touching the project

This route is for a human-authorized update of an already installed pinned
methodology package, not for product work. Inspect the adopting repository's
current Git, root adapter(s), PROJECT_AI.md, installed package paths, and
project-specific instructions/skills. Classify:

- NONE: existing project policy already covers the needed behavior, or copying
  the generic policy would create conflicting canonical owners; do not mutate.
- SELECTIVE: preserve project-specific policy and explicitly approve the exact
  compatible subset. The updater below does NOT implement selective installs:
  perform only a separately reviewed manual change for this route.
- FULL EXISTING-PACKAGE REFRESH: a complete prior pinned copy is already
  installed and the human-authorized update has no ownership conflict.
  Use the helper's three-way preview and, if clean, apply.

Canonical generic package ownership, copied from one exact accepted SHA:

- .1c-ai/** (the shared core, router, profiles, and their assets);
- .agents/skills/1c-ai-*/** (generic agent skills only).

NEVER treat AGENTS.md, CLAUDE.md, GEMINI.md, .github/copilot-instructions.md,
PROJECT_AI.md other than the single MethodologyPackage pin, CODEX/**,
project knowledge, .agents/skills/edt-mcp-*/**, other agent-specific skills,
1C source, test infobases, IDE settings, customer data or credentials as
package-owned. An existing project adapter may link to .1c-ai/START_HERE.md;
modifying that adapter needs separate project authorization.

Live Git/source/runtime and accepted project architecture outrank methodology
prose. Current EDT-MCP tool guides and live schemas outrank copied examples.
Do not distribute version-specific EDT-MCP tool instructions as a second
canonical generic skill pack.

## Package revision and three-way safety

Obtain an exact 40-character methodology source commit SHA. Do not use
floating main, preprod or a ZIP filename as a claimed installed version.
Use a real full-history local Git clone of the methodology repository.

The helper reads the previous MethodologyPackage SHA from PROJECT_AI.md and
the old/new package file inventories from the local methodology Git history.
For each package-owned path:

- current matches incoming bytes: no change (idempotent);
- current matches the old pinned version: add/update/delete to incoming;
- current differs from BOTH pinned old and incoming: CONFLICT_STOP, no writes.

Changed/deleted paths are SHA-256-addressed in the plan; no private file
contents are printed. Missing old commits, missing/multiple MethodologyPackage
pins, non-Git roots, symlinks in owned paths and incomplete package trees fail
closed. If a package-owned file was locally customized, reconcile its intended
policy explicitly in its true owner; do NOT force-sync or silently merge.

The default command is PLAN only. --apply additionally requires a completely
clean local Git worktree on a feature/* branch. It writes just the managed
paths and the exact package SHA in PROJECT_AI.md, verifies the result, and
stops as APPLIED_UNCOMMITTED. It does NOT commit, push, merge, force-reset,
modify a running EDT workspace, or update any remote checkout.

First adoption/uninstall, a damaged/unpinned prior installation, mixed
package ownership, and true per-file selective adoption remain under
ADOPTION.md and issue #2; do not describe the helper as a general installer.

## Windows PowerShell quick route (local executor)

Prerequisites: Git, Python 3, two actual Git checkouts (methodology source
and adopting project). The agent must choose the project's accepted
integration branch based on its own AGENTS.md and task. For the standard
flow this is preprod; do not assume every project has preprod.

    $Method = "C:\AI\1c-ai-development-methodology"
    $Project = "C:\Projects\My1CProject"

    git -C $Method fetch origin --prune
    $MethodSHA = (git -C $Method rev-parse origin/main).Trim()
    git -C $Method cat-file -t $MethodSHA

    git -C $Project fetch origin --prune
    git -C $Project status --short
    # On a clean checkout and after verifying accepted integration HEAD:
    git -C $Project switch -c feature/methodology-refresh-002 origin/preprod

    python "$Method\scripts\refresh_existing_package.py" --source "$Method" --target "$Project" --source-sha "$MethodSHA"
    # Review JSON PLAN_READY, exact changed paths, old/new SHA and conflicts.
    python "$Method\scripts\refresh_existing_package.py" --source "$Method" --target "$Project" --source-sha "$MethodSHA" --apply

    git -C $Project diff --check
    git -C $Project diff --stat
    git -C $Project status --short

An agent executing the task must verify the local paths actually exist and
use the project's chosen base/branch name; commands above are illustrative,
not proof of a user's filesystem or acceptance. Do not run --apply after
CONFLICT_STOP or while the worktree is dirty. The exact script's Python
JSON output is a machine-readable source/target update evidence handle.

After review, commit the bounded change; push that feature branch and open a
PR to the project's accepted integration branch. Run only applicable
repository documentation/skill checks. Do not expand into EDT/source/runtime
tests merely because the repository is a 1C project.

## Cloud GitHub agent / local state boundary

A GitHub-only agent may compare source blobs at two exact Git SHAs, prepare a
minimal feature-branch PR and validate repo checks, but must not claim that
the user's local worktree is updated. Even a successfully pushed branch is
only REMOTE_SOURCE, not LOCAL_SYNC or EDT_RUNTIME.

After accepted merge, an authorized local executor independently:

1. inspects its own Git status and foreign/unsaved changes;
2. fetches and checks out/pulls the exact accepted commit using the
   project's Git/worktree rules;
3. confirms local HEAD, expected files/hashes, MethodologyPackage pin and
   clean worktree;
4. reports LOCAL_SYNC=VERIFIED or UNKNOWN/BLOCKED, never inferred.

If the project keeps its canonical instructions outside the Git checkout
(e.g. a local-only IDE policy), do not copy or overwrite them as part of
this sync. Report that other surface separately.

## Verification and delivery

Required for this documentation-only update:

- exact accepted source SHA and prior installed SHA;
- conflict-free PLAN_READY evidence, including affected file list and hashes;
- bounded diff showing only package-owned paths and pin;
- local repository status before/after and accepted Git commit/PR;
- unchanged project-specific instructions and non-1c-ai-* skills;
- applicable file/skill validation; skip 1C runtime tests as NOT_REQUIRED;
- exact local sync proof or LOCAL_SYNC=UNKNOWN;
- a short technical report, a short Russian user summary, and a detailed
  Markdown evidence report in the project's durable Issue/PR and, where
  required by the project contract, Google Drive.

STOP / ASK when: project policy owners conflict, a package-owned file differs
from both versions, source revision is unreachable, Git is dirty or shared by
another writer, the target branch is not the accepted integration workflow,
or local write/runtime access is missing. Ask one concrete question only for
a material unresolved choice. Never silently fall back to a destructive copy.
