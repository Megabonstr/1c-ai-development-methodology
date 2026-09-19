---
name: 1c-ai-bounded-implementation
description: Execute one frozen, bounded change contract under one Local Main. Use when goal, scope, source route, constraints, and acceptance are resolved and the task is ready for implementation.
compatibility: Requires the 1c-ai-development core/router files to be available at the documented repository paths.
---

# Bounded Implementation

## Role

**Primary owner: Local Main.** Use only after task-bootstrap has opened an already frozen durable task for execution.

## Minimal read path

Start from the exact TaskHandle/bootstrap packet. Do not reread broad owners merely because they are linked.

For a normal bounded change:

- `.1c-ai/core/ORCHESTRATION.md` -> `Local autonomy and correction loop`; add `Escalation` only if a material contradiction appears;
- `.1c-ai/core/DELIVERY_DISCIPLINE.md` -> `Minimal sufficient solution`, `Expansion requires evidence`, `Complexity alarm`, `Done means stop`;
- `.1c-ai/core/SOURCE_FIRST.md` -> `Generic source order` + `Bounded expansion` only when a technical source/mechanism UNKNOWN exists;
- `.1c-ai/core/TASK_CONTRACT.md` -> `Ownership of task state` / `Task granularity` only when an execution boundary is unclear;
- `.1c-ai/core/STOP_ASK.md` only when a STOP/ASK condition is triggered;
- `.1c-ai/core/GIT_GITHUB_FLOW.md` only for Git-backed branch/delivery operations.

Use the execution profile already selected by the task/bootstrap. Do not reopen the router when that profile is fixed. In the profile, read only `Select this profile when`, `Required identity`, the relevant mutation section, and the verification section needed by the current gate.

## Preflight

Verify exact source/version identity, Local Main context, exclusive active write ownership, positive owned targets, minimal observable goal, required source handles, material constraints/exceptional prohibitions only when present, allowed generalization, and acceptance gates. For Git-backed projects this includes repository/base/branch/HEAD. For Gitless work, use only an operational project-supplied durable task/source identity and do not invent Git fields or storage mechanics.

Do not start from an unresolved material contract.

## Workflow

1. Restate the smallest observable business result that satisfies the durable task.
2. Inspect only the exact current source needed for the change.
3. Implement the smallest proven mechanism. Include the smallest directly necessary adjacent technical correction when required to achieve the frozen Goal and it does not change product/business semantics or cross architecture/data/safety/acceptance authority. Local Main may delegate an exact trivial isolated delta to a Quick Fixer.
4. Before adding a framework, generic abstraction, broad refactor, universal lookup/conversion, or new test infrastructure, require a concrete current-task reason from `DELIVERY_DISCIPLINE.md`.
5. If scope/effort grows materially beyond the business goal, run the complexity alarm and cut optional work.
6. Preserve unrelated work and project conventions.
7. Local Main re-reads the resulting diff in Reviewer mode.
8. For material/high-risk changes, Local Main performs a Critic pass.
9. Run the required bounded validate/fix/retest/debug loop locally.
10. Correct ordinary technical failures and directly related fix-forward work without returning to Coordinator Main. ASK only when the required adjacent change crosses a material semantic/architecture/data/safety/acceptance boundary.
11. Persist or otherwise identify the exact resulting source/version/artifact identity. For Git-backed projects, prefer the exact commit SHA. For Gitless work, use only the project-supplied source snapshot/fingerprint and durable identity actually available; if none exists, report the durability gap instead of inventing one.
12. Hand off to focused verification without expanding the task.

## Delegated write boundary

A Quick Fixer may write only when Local Main supplied:

- exact file/object/location;
- exact requested delta/mechanism;
- exclusive non-overlapping write scope;
- acceptance/STOP boundary.

Local Main must review and integrate every delegated write.

## Completion

When all required acceptance gates are PASS or explicit NOT_REQUIRED, stop implementation expansion.

Record adjacent debt/generalization/polish as separate Issues rather than holding the business task open.

Return changed targets, mechanism, exact source/version/artifact identity, review/critic result, implementation-time checks, adjacent findings, and the first remaining `UNKNOWN`.

Do not redesign shared semantics or broaden adjacent debt.

Coordinator Main draft code may be rewritten substantially when needed inside frozen semantics/scope/invariants/acceptance.

Ordinary technical correction stays local. Only material contradictions escalate through `ORCHESTRATION.md` and `STOP_ASK.md`.
