# Delivery Discipline

Canonical machine-facing owner for scope discipline, simplicity, and completion.

## Purpose

Ship the smallest proven solution that satisfies frozen business semantics, safety constraints, project invariants, and required acceptance.

Do not turn a local business change into a reusable framework without concrete evidence that the framework is required.

## Minimal sufficient solution

Before implementation, identify the smallest observable result that makes the Issue successful.

Prefer:

- current project mechanisms;
- applicable standard/BSP public APIs;
- direct bounded mapping/change;
- smallest coherent file/object scope;
- only the verification required by the Task Contract.

Custom generalization is not a quality goal by itself.

## Expansion requires evidence

Do not add by default:

- generic frameworks or abstraction layers;
- universal conversion/search engines;
- broad refactors;
- unrelated metadata changes;
- speculative defensive wrappers;
- new test infrastructure;
- adjacent cleanup;
- future-proofing for unrequested scenarios.

Expand only when at least one is true:

- the Task Contract explicitly requires it;
- current project/standard mechanism requires it;
- a concrete acceptance gate fails without it;
- a real safety/data-integrity/security requirement requires it;
- a demonstrated current reuse requirement makes the direct solution incorrect or materially duplicative.

"Could be useful later" is not enough.

## Complexity alarm

If implementation effort/scope becomes materially larger than the observable business goal, Local Main performs this check before continuing:

1. What exact user-visible/business result must this Issue deliver?
2. Which current changes directly enable that result?
3. Which work is only generalization, polish, future-proofing, adjacent debt, or infrastructure?
4. Can that work be removed/deferred while preserving correctness and required evidence?
5. Is there a real material blocker, or only self-created complexity?

Default action: cut back to the smallest safe solution.

Do not escalate to Coordinator Main merely because the implementation became technically messy. First remove unnecessary complexity locally.

## Done means stop

When all required acceptance gates are PASS or explicit NOT_REQUIRED:

- stop expanding the implementation;
- do not reopen architecture/research for optional polish;
- do not add "while we are here" refactors;
- record adjacent findings separately;
- create a new Issue when remaining work is worth doing.

A completed business task must not be held open by unrelated debt.

After required acceptance and final accepted/delivered identity are known, lifecycle completion includes one compact Coordinator-owned durable closeout. This is completion bookkeeping, not implementation expansion.

Keep trivial closeout trivial. Do not hold an accepted task open for prose polish, a duplicate long report, or a new reporting artifact. A full report is justified only when the task, risk, client/support/handover value, or explicit acceptance contract requires it.

## Adjacent findings

Examples:

- unrelated status/date bug;
- broader universal lookup improvement;
- generic conversion subsystem;
- cleanup in another report/module;
- expanded regression framework;
- optional refactor.

Record the finding with an exact handle and move on unless it blocks current acceptance.

## Safety is not optional

"Simplest solution" never means:

- bypass rights/RLS;
- mutate production/user data without authority;
- use unstable internal BSP APIs as a shortcut;
- skip required tests/runtime/native proof;
- hide UNKNOWN states;
- ignore data-integrity/security constraints;
- knowingly violate project architecture required by the Task Contract.

Simplicity operates inside correctness and safety boundaries.

## Example

Goal:

> When Project is selected, fill vehicle, driver, price, VAT, quantity=1 and clear "My organization". Do not change carrier.

If current source provides a safe deterministic way to resolve those fields, implement that path and verify one real scenario.

Do not automatically add:

- a universal vehicle/driver search framework;
- carrier synchronization;
- generalized conversion infrastructure;
- unrelated status-file cleanup;
- a new test framework.

Those become separate tasks unless current acceptance actually requires them.

## Relationship to other owners

- `SOURCE_FIRST.md` decides where the mechanism should come from.
- `TASK_CONTRACT.md` freezes scope/acceptance.
- `ORCHESTRATION.md` keeps the technical correction loop local.
- `EVIDENCE_MODEL.md` defines proof.
- This file decides when extra complexity is justified and when to stop.
