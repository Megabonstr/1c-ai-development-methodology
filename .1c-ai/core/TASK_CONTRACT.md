# Task Contract

A task starts from a bounded, durable contract.

Raw/noisy/materially unclear human intent is upstream of this owner and is handled by `.1c-ai/core/TASK_INTAKE.md`. An already valid durable bounded task bypasses framing and comes here directly.

For the recommended Git-backed path, the GitHub Issue body or one exact task comment is the default contract carrier. Gitless semantics are designed/degraded only: this package does not ship the durable-state backend. A Gitless task may use an operational project-supplied durable carrier; otherwise durable task continuity is `UNKNOWN/BLOCKED` and must not be invented.

## Required fields

Resolve the fields that materially apply to the task:

- **Goal** - one concrete result.
- **Source / version identity** - exact source state to start from and deliver against. For Git-backed projects this includes repository/base/branch/commit as applicable. For Gitless work, use only a project-supplied snapshot/fingerprint or explicit `UNVERSIONED_CURRENT_STATE` with truthful weaker provenance; that source label does not create the missing durable-state backend.
- **CoordinationScope** - whole project or exact bounded project/domain area owned by this task. May inherit an already explicit durable project default.
- **OwningCoordinator** - exactly one Coordinator Main authority for this task/scope. May inherit an already explicit durable project default.
- **Writer owner** - one writer for each file/owner/worktree scope.
- **Exact positive scope / owned target** - the business outcome and files/objects/modules/documents the task owns, plus directly necessary related implementation that preserves frozen semantics.
- **Required mechanism** - accepted design or implementation route when already known.
- **Source packet** - exact source/evidence handles needed for material decisions.
- **1C target packet** - when load-bearing 1C form/data targets are involved, exact handle to the resolved target/preflight packet from `.1c-ai/profiles/1c-common/TASK_PREFLIGHT.md`.
- **Material constraints** - only invariants/safety/compatibility boundaries that materially affect this task.
- **Prohibited changes / DO_NOT_TOUCH** - optional sparse material exceptions only when the executor could plausibly cross a concrete high-cost boundary. Do not enumerate unrelated fields/objects merely because they are outside scope.
- **Complexity boundary** - smallest acceptable solution plus any generalization/refactor/test-infrastructure explicitly authorized for this task.
- **Verification profile** - optional `FAST_CLIENT_SLICE | STANDARD | HIGH_RISK`; default `STANDARD`.
- **Priority** - optional `WORKING_NATIVE_RESULT | NORMAL | SAFETY_FIRST`; default `NORMAL`.
- **Test budget / cadence override** - optional explicit reasoned override of the selected verification profile.
- **Parity cadence** - optional project/task-specific full parity requirement when the default cadence is insufficient.
- **Acceptance gates** - focused checks required before delivery.
- **Native/user acceptance** - when behavior cannot be proven by source/static checks alone.
- **STOP / ASK boundary** - material choices that must return to the task owner.
- **Delivery boundary** - PR/merge/artifact/evidence destination.

Do not require fields that do not materially affect the task.

Default boundary is positive: what outcome/target the task owns. Ordinary unrelated behavior is outside scope implicitly. Add one compact preservation rule when useful; enumerate explicit prohibitions only for real material risk.

## Ownership of task state

Coordinator Main freezes or corrects the semantic contract:

- Goal and observable behavior;
- CoordinationScope and OwningCoordinator;
- material product/architecture/data/safety constraints;
- exact positive scope / owned outcome;
- material constraints and any exceptional Prohibited changes / DO_NOT_TOUCH that genuinely require explicit protection;
- a required mechanism when that mechanism is itself a frozen decision;
- acceptance meaning and material STOP/ASK boundary;
- delivery intent.

Local Main receives that frozen semantic contract through task bootstrap. It may resolve or verify execution facts and perform small directly necessary adjacent technical fix-forward work that do not change those semantics, including:

- exact local source/version/worktree/project identity;
- exact paths/symbols/targets when safe bounded discovery is allowed;
- execution profile and writer ownership;
- technical preflight facts and applicability of supplied source handles;
- exact runnable verification target;
- directly related helper/query/form/context corrections required to make the owned result work, when they stay inside the same bounded implementation.

Local Main must not silently fill or rewrite a missing product/architecture/data/safety/acceptance decision. If current source/runtime contradicts a material semantic field, return an explicit correction/escalation to Coordinator Main. Do not escalate merely because the implementation needs a small adjacent technical correction inside the frozen positive scope.

## Task granularity

One Task Contract represents one business outcome, not one technical correction.

Ordinary compile errors, execution-context fixes, exact API/signature corrections, and task-owned runtime/test defects remain internal Local Main iterations unless they cross a material semantic/scope/safety/authority boundary.

## Durable transport

Prefer:

```text
short Issue body
or
one exact task comment
```

Do not require a new executor to read the entire Issue history, old chats, broad project history, or unrelated reports when exact handles are available.

## Correction packet

A correction pass should state only:

```text
Wrong:
Evidence:
RequiredDelta:
AcceptanceDelta:
ContinueBranch:
STOPIf:
```

Do not resend the original task context unless the correction changes it.

## Ownership

One file/owner/worktree scope has one writer.

Parallel work is valid only when ownership is disjoint and shared contracts are frozen before writers diverge.

A reviewer does not become a second writer unless a new explicit write boundary is assigned.
