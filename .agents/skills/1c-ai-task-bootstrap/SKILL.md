---
name: 1c-ai-task-bootstrap
description: Open an already Coordinator-frozen durable task for Local Main execution. Validate semantic readiness, resolve only execution facts, and establish exact source/version, ownership, targets, verification, and STOP/ASK handles before implementation.
compatibility: Requires the 1c-ai-development core/router files to be available at the documented repository paths.
---

# Task Bootstrap

## Role

**Primary owner: Local Main.** This is the execution-side ingress after Coordinator Main has frozen the semantic Task Contract.

Coordinator-owned semantic fields are consumed and validated here, not silently created or changed.

## Minimal read path

Do not open the full core-owner set by default.

For an ordinary already-ready task, read only:

- `.1c-ai/core/TASK_CONTRACT.md` -> `Required fields`, `Ownership of task state`, `Task granularity`;
- `.1c-ai/core/TOKEN_DIET.md` -> `Local Main execution context`;
- `.1c-ai/core/ORCHESTRATION.md` -> `Role and context boundary`, `Local autonomy and correction loop`.

Conditional reads:

- `.1c-ai/core/GIT_GITHUB_FLOW.md` only for Git-backed branch/delivery operations;
- `.1c-ai/core/STOP_ASK.md` only when a material ambiguity/authority boundary is actually hit;
- `.1c-ai/router/ROUTER.md` only when the next Local skill/profile is not already fixed by the TaskHandle/bootstrap packet.

Use exact headings/sections rather than loading whole owner files when the tool permits section-level retrieval.

## Preflight

Start from an already durable bounded task/task-state handle.

If the only input is raw/noisy/materially unclear human intent, do not absorb task-framing responsibility here. Route to `.agents/skills/1c-ai-task-framing/SKILL.md` through `.1c-ai/core/TASK_INTAKE.md`.

Start from the exact assigned durable task record. For the recommended Git-backed route this is usually an Issue body or exact task comment.

Confirm that Coordinator-frozen semantic fields are present and internally usable: Goal, exact positive scope/owned target, CoordinationScope, OwningCoordinator, material product/architecture/data/safety constraints, any optional exceptional DO_NOT_TOUCH/prohibited boundary, any frozen required mechanism, acceptance meaning, material STOP/ASK boundary, and delivery intent.

Resolve or verify only Local execution facts: authoritative source/version identity, Local Main context, exact write ownership, exact target paths/symbols when bounded discovery is allowed, execution profile, applicability of source handles, directly necessary related technical adjustments, and exact runnable verification target. For Git-backed projects this includes repository, accepted base, target branch and current Git identity. For Gitless work, use only an operational project-supplied durable task/source identity; this package does not create the missing Gitless backend.

If a semantic field is materially missing or current source/runtime contradicts it, return a correction/escalation to Coordinator Main instead of filling it locally.

Verify current source/version identity before writes. For Git-backed projects verify the exact Git state.

## Workflow

1. Compare the frozen task packet with current source/version facts.
2. Resolve bounded technical execution facts obtainable from exact sources without changing task semantics.
3. Confirm Coordinator Main / Local Main / subagent authority from `ORCHESTRATION.md`.
4. Route any material semantic contradiction through `STOP_ASK.md` back to Coordinator Main.
5. If the TaskHandle/bootstrap packet already fixes the next Local skill/profile, continue directly. Otherwise use `.1c-ai/router/ROUTER.md` to resolve only that missing route.
6. Return the executable task boundary and next Local workflow.

## Completion

Complete when Local Main can start from exact handles without reading broad task-history or project history.

Do not implement product changes in this skill.
