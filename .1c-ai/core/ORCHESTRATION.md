# Orchestration

This file owns the reusable multi-agent authority, delegation, and integration model.

It is tool-neutral and model-neutral.

## 1. Canonical control chain

```text
Human Owner + Coordinator Main
-> frozen durable Task Contract
-> one Local Main
   -> optional bounded specialist subagents
   -> implementation
   -> self-review
   -> critical analysis when material
   -> focused verification / runtime evidence
   -> local integration verdict
-> Coordinator Main verifies required evidence
-> required Human Owner / Coordinator Main acceptance
-> promotion / delivery when required
-> final accepted / delivered identity
-> Coordinator Main persists one durable closeout and emits the concise human result
-> task close
```

There is one Local Main per local task context.

Writer, Reviewer, Critic, and Integrator are operating modes of the same Local Main. They are not four mandatory agents.

## 2. Human Owner

Owns final product/business intent and explicit authority for destructive or user-affecting decisions.

## 3. Coordinator Main

Coordinator Main is the provider-neutral upper coordination authority for one explicit `CoordinationScope`.

It may be hosted in a cloud chat/session, local desktop/CLI agent, another isolated provider context, or a human-mediated coordination context. Host placement does not create authority; the role contract and durable project state do.

### Coordination scope and ownership

`CoordinationScope` may be:

- the whole repository/project;
- one product;
- one subsystem/domain;
- one bounded integration area;
- one release/migration program.

Every active task has exactly one `OwningCoordinator`.

If a task crosses peer scopes, either move ownership to a common parent scope or select one OwningCoordinator explicitly while other scope coordinators act only as bounded advisors.

Do not create ambiguous joint ownership or a mandatory coordinator hierarchy.

### Role and context boundary

Coordinator Main owns **what must be achieved, what may not change, which material decisions are frozen, and what proves acceptance**.

Local Main owns **how to make that frozen outcome correct in the real project**: execution-side bootstrap, bounded technical discovery, implementation, local correction, review, verification/runtime evidence, integration, and the final local verdict.

Local Main does not reopen raw intent, broad product rationale, broad research, or semantic Task Contract decisions by default. It works from the frozen durable task and exact handles. Positive scope defines the owned outcome/targets; unrelated behavior is not a target by default. If current source/runtime requires a change to observable behavior, architecture/product boundary, rights/RLS/data semantics, destructive authority, material preservation/prohibition boundary, or acceptance meaning, Local Main escalates a material correction instead of silently redesigning the task.

One physical actor may perform Coordinator Main and Local Main sequentially. The durable task/decision boundary, not a mandatory new chat or agent, separates the roles.

### Context ownership

Coordinator Main owns the durable context for its scope:

- raw-intent readiness/framing when no valid durable task exists;
- project/domain identity;
- architecture and product invariants;
- accepted Git/source checkpoint;
- durable decision history;
- knowledge/source/research indexes and exact retrieval handles;
- open material UNKNOWNs;
- Task Contract creation/correction;
- material STOP/ASK decisions with the Human Owner;
- evidence/acceptance review;
- final accepted/delivered identity;
- lifecycle closeout/reporting coordination;
- merge/close/delivery coordination.

Context ownership means knowing what is authoritative, where it is, what state is accepted, and how to retrieve exact material on demand.

It does **not** mean preloading the whole repository, all research, all Issue history, or relying on provider chat memory. Token Diet remains mandatory.

### Required vs optional capabilities

Coordinator Main must be able to reason across its CoordinationScope, resolve material authoritative handles, freeze/correct Task Contracts, review evidence, route material decisions, and ensure those decisions become durable task state through an authorized transport.

Coordinator Main does **not** require:

- cloud hosting or cloud chat;
- a provider-native GitHub connector;
- direct GitHub write capability;
- source-code write access;
- local IDE/runtime/database access;
- persistent provider conversation memory;
- webhook/event support.

When the selected durable transport cannot be written directly, an authorized human/tool may persist the exact Coordinator decision. For Git-backed projects, GitHub Issue/comment state is the recommended/default carrier. For Gitless work, only an already operational project-supplied durable carrier may serve this role; the methodology package itself does not ship one. Only the authorized durable form becomes executable task state.

### Placement modes

Supported placements include:

1. cloud-hosted Coordinator Main;
2. local/desktop/CLI Coordinator Main;
3. Coordinator Main with human/authorized-tool durable-state persistence;
4. one physical agent acting sequentially as Coordinator Main and Local Main for a small task.

For co-located physical execution, preserve the logical boundary: declare the active role, freeze/persist the Task Contract before implementation, keep Local Main inside the frozen contract, and return to Coordinator mode only for material decision/acceptance.

### Material acceptance independence

Co-located Coordinator Main + Local Main remains valid for small/low-risk work, and Local Main self-review/critic passes remain valid technical evidence input.

When the same physical actor authored a **material** change, that actor must not be the sole final acceptance/promotion authority for that material change. Final material acceptance must come from either:

- the Human Owner; or
- a genuinely independent explicitly authorized acceptance context that did not author the material change.

This rule creates an acceptance boundary only. It does not require a separate writer/reviewer/critic agent for every task and does not invalidate Local Main self-review.

For broad/high-risk work, separate contexts are preferred.

Coordinator Main must not claim local Git, IDE, runtime, database, or native UI state without evidence from the local execution side.

Coordinator Main does not silently redesign a frozen local task after execution starts. Material changes require an explicit correction or new contract version.

## 4. Local Main

Local Main is the root local executor and integrator.

It owns:

- task-bootstrap as the execution-side ingress from an already frozen durable task;
- exact local repository/worktree/project/runtime identity;
- local execution planning inside the frozen Task Contract;
- bounded source-first technical discovery inside accepted semantics;
- implementation;
- bounded delegation;
- review of its own and delegated changes;
- adversarial/critical analysis when useful;
- focused verification coordination;
- runtime/native evidence;
- correction loop;
- integration of all subagent results;
- the final local verdict.

Local Main escalates material semantic/architectural contradictions to Coordinator Main instead of redesigning product semantics.

### Local autonomy and correction loop

After Coordinator Main hands off a frozen Task Contract, Local Main owns the ordinary technical correction loop until it can return one local verdict.

Local Main does **not** return to Coordinator Main for routine technical issues such as:

- syntax or compile failures;
- ordinary metadata/type/signature/query/form mismatches;
- test failures that can be debugged inside the accepted task;
- small refactors or implementation corrections;
- small directly necessary adjacent technical changes that are required to deliver the frozen Goal without changing product/business semantics;
- adapting draft code to the actual project/API/tool contract;
- replacing an implementation detail with a better proven mechanism while preserving frozen semantics, scope, invariants, and acceptance;
- repeated validate/fix/retest/debug cycles.

Coordinator Main's draft code or skeleton is an implementation input, not an immutable line-by-line contract.

Local Main may substantially rewrite that code when necessary to make the accepted task correct and maintainable, provided product semantics, agreed architecture boundaries, safety constraints, and acceptance remain intact.

The default control pattern is:

```text
Coordinator Main
-> frozen task / architecture / useful code skeleton
-> Local Main
   -> integrate
   -> inspect actual source/metadata/runtime
   -> fix
   -> verify
   -> debug/refactor
   -> repeat locally as needed
   -> local verdict + exact evidence
-> Coordinator Main
```

The forbidden default pattern is repeated Coordinator Main round trips for each ordinary technical failure.

Intermediate GitHub comments may record useful progress, but they do not create a wait-for-Coordinator approval gate unless a material escalation condition is met.

### Handoff budget

Coordinator <-> Local handoffs are expensive control-boundary crossings.

Default expectation:

- one initial task handoff;
- zero intermediate round trips for ordinary technical correction;
- one final local-verdict/evidence handoff.

Additional round trips are justified only by a named material escalation, explicit correction contract, or new task. This is a default efficiency rule, not a hard numeric cap when real product/architecture ambiguity exists.

### Writer mode

Local Main writes inside the exact authorized scope.

It preserves unrelated work, follows the frozen mechanism, and produces exact diff/SHA/evidence.

### Reviewer mode

Local Main re-reads the bounded diff against the Task Contract, source packet, invariants, compatibility, safety, and evidence claims.

Review is a distinct pass even when performed by the same Local Main.

### Critic mode

For material/high-risk/architecture/process changes, Local Main performs an adversarial pass:

- challenge hidden assumptions;
- look for missing evidence;
- look for unnecessary complexity or parallel mechanisms;
- look for scope creep and authority inversion;
- test whether a simpler proven route exists.

Local Main may delegate an independent bounded critique when extra independence is useful, but that is optional.

### Integrator mode

Local Main reconciles implementation, review, critique, tests/runtime, and subagent results.

It returns one local verdict:

- `PASS`;
- `CORRECTION_REQUIRED`;
- `UNKNOWN`;
- `STOP`.

## 5. Bounded specialist subagents

Subagents are optional children of Local Main.

They are used when specialization, context reduction, cost, or parallel read-only work makes them useful.

### Researcher / Scout

Typical work:

- exact repository/source search;
- bounded donor or official-doc reading;
- extraction and comparison;
- narrow technical fact finding.

Read-only by default.

### Quick Fixer

Use only for an exact trivial/localized change where the mechanism is already frozen.

Requirements:

- one concrete file/object/location;
- exact requested delta;
- exclusive non-overlapping write scope;
- no redesign;
- compact result with diff/SHA/evidence.

Local Main remains responsible for reviewing and integrating the change.

### Documentation worker

May:

- read exact documentation/specification sources;
- summarize a bounded topic;
- write one bounded documentation artifact when explicitly authorized.

Returns the artifact/evidence handle to Local Main.

### Test / Runtime / Log worker

May:

- run exact focused checks;
- inspect bounded logs/data;
- collect runtime evidence;
- report the first material failure/UNKNOWN.

It records only observed evidence and does not infer product acceptance.

### Other specialist

Allowed only with the same bounded packet, permission, ownership, and STOP rules.

## 6. Delegation packet

Every subagent receives a fresh bounded packet.

Do not pass the full parent transcript by default.

```text
Goal:
SpecialistRole:
ExactHandles:
Bounds:
Permission: READ_ONLY | WRITE_EXACT_SCOPE
AcceptanceOrQuestion:
OutputShape:
STOP:
```

A subagent resolves supplied handles before work.

Missing/stale/contradictory material context returns a context/source gap instead of being filled from memory.

No repository/KB roaming.
No architecture redesign.
No child trees unless explicitly authorized.

## 7. Result packet

Subagent output stays compact:

```text
Result:
MaterialFindings:
EvidenceHandleOrSHA:
FirstUnknownOrBlocker:
NextAction:
RouteDeviation:
```

Detailed reports/logs/artifacts are stored once at a durable task-specified location and referenced by handle.

When the task/output contract assigns an exact durable result destination, that destination owns the detailed result. The invoking chat receives only the compact status/result handle. If the actor cannot write the assigned destination, return `CAPABILITY_BLOCKER` instead of dumping the full result into chat for manual relay; manual-relay fallback requires an explicit Human Owner request.

Do not repeat the input packet.

## 8. Permission and write ownership

Default subagent permission is read-only.

A subagent write is allowed only when Local Main explicitly assigns:

- exact isolated scope;
- exact mechanism/delta;
- no overlap with another active writer;
- known repository/worktree identity;
- explicit acceptance/STOP boundary.

One writer owns each overlapping file/object/worktree scope at a time.

A Quick Fixer is not a second Local Main.

Local Main always reviews/integrates delegated writes before the local verdict.

## 9. Parallelism

Parallel subagents are allowed only when:

- scopes are truly disjoint;
- shared contract is frozen first;
- no overlapping write ownership;
- tasks do not depend on hidden mutable state from each other;
- Local Main remains the integration owner.

Parallel reading is cheap.

Parallel writing is exceptional.

## 10. Evidence responsibility

Subagent self-report is evidence input, not proof by itself.

Local Main verifies load-bearing subagent claims before its final local verdict.

Coordinator Main verifies evidence required by the acceptance contract before final acceptance.

Evidence classes remain owned by `EVIDENCE_MODEL.md`.

Static/source success must not be promoted to build/deploy/runtime/native success.

## 11. Lifecycle closeout

After Local Main returns its final local verdict/result/evidence, Coordinator Main owns lifecycle closeout.

Canonical order:

```text
Local Main verdict + exact result/evidence
-> Coordinator Main evidence review
-> required acceptance
-> promotion/delivery when required
-> exact final accepted/delivered identity
-> one durable closeout
-> concise human result
-> task close
```

Closeout does not create evidence. Verification and runtime work remain on the Local Main side; evidence meaning remains owned by `EVIDENCE_MODEL.md`.

Coordinator Main persists one authoritative compact closeout in the task's accepted durable carrier:

```text
TaskHandle:
Outcome:
ChangedTargets:
MaterialDecisionSummary:        # optional when obvious
AcceptedSourceVersionOrArtifact:
EvidenceHandles:
AcceptanceHandleOrAction:
RemainingUnknowns:
FollowUpHandles:
ClosedAt:
```

Do not duplicate full diffs, PR/CI history, logs, research, or evidence bodies. The closeout is an index/projection over exact existing handles.

Default human projection is concise Russian:

```text
Что сделано:
Где изменено:
Как проверено:
Что осталось неизвестным / ограничения:
Принятая версия / результат:
```

A full report is optional and justified only by an explicit task requirement, material risk/architecture, or real client/support/handover value.

One physical actor may switch back from Local Main to Coordinator Main for closeout; this does not waive the material acceptance-independence rule. Required acceptance, evidence, and final identity must exist before the task is represented as closed. `UNKNOWN` remains `UNKNOWN`.

Use `.agents/skills/1c-ai-task-closeout/SKILL.md` for the thin repeatable closeout workflow.

## 12. Escalation

Do not escalate merely because implementation failed once, compilation/test/runtime returned an ordinary technical error, or Coordinator Main's draft code needs local correction.

Escalate upward when:

- a material semantic/product decision has multiple plausible paths;
- the frozen mechanism conflicts with current source/runtime facts;
- destructive/user-affecting authority is missing;
- write ownership overlaps;
- required evidence remains unavailable after bounded investigation;
- the necessary fix would expand into materially unrelated objects/modules/systems beyond the accepted scope;
- a required acceptance gate is impossible/inapplicable and replacing it would materially change the acceptance contract;
- continuing requires architecture redesign.

Cheap technical facts are investigated from source/tools/runtime before asking the Human Owner.

Use `STOP_ASK.md` for canonical STOP/ASK policy.

## 13. Durable transport

For Git-backed projects, GitHub Issue or exact Issue comment is the recommended/default carrier for the frozen task/correction. Gitless work requires an already operational project-supplied durable carrier; otherwise durable handoff is `UNKNOWN/BLOCKED`.

If the active task names a specific Issue/PR/comment/artifact as its result destination, write the detailed result there. Lack of write capability is a `CAPABILITY_BLOCKER`, not permission to replace the durable delivery with a full chat report.

Exact source/version identity and artifact identity carry executable state between Coordinator Main and Local Main and between Local Main and bounded subagents. For Git-backed projects, the commit SHA is the recommended/default source identity.

Do not use chat history as durable project state when exact durable task/source handles exist.

When the Git-backed route is selected, use `GIT_GITHUB_FLOW.md` and the GitHub handoff skill for transport details. A Gitless project may integrate its own operational carrier with truthful weaker provenance; do not treat the research design as a shipped fallback.

## 14. Invariants

- Human Owner + Coordinator Main own product/architecture/acceptance/closeout, subject to the material acceptance-independence rule when an accepting Coordinator is the same physical actor that authored the material change.
- Closeout references existing evidence and final accepted/delivered identity; it does not create or upgrade evidence.
- One Local Main owns local execution/integration/final local verdict.
- Writer/Reviewer/Critic/Integrator are Local Main modes.
- Subagents are optional bounded specialists.
- Subagents are read-only by default.
- Exact Quick Fixer writes are allowed only with explicit isolated ownership.
- Local Main reviews and integrates every delegated write.
- One writer owns each overlapping scope.
- No actor claims evidence it did not observe or verify.
- Material authority escalates upward instead of being guessed.
- Ordinary technical correction stays local until Local Main reaches a verdict.
- Coordinator Main is not an RPC endpoint for compile/test/metadata/runtime micro-failures.

## 15. Communication and silent work

For ordinary bounded implementation, Local Main defaults to `SILENT_WORK`: no routine narration of reads, edits, tool calls, compile/test cycles, internal planning, or repeated progress summaries.

Intermediate output is justified only by a material STOP/ASK boundary, a route-changing failure/UNKNOWN, or a required handoff/result packet. Otherwise Local Main continues and returns one compact final result.

Agent-to-agent/machine-facing packets use compact technical English and exact handles. Human-facing progress/results use concise plain Russian by default; expand technical detail only when requested or materially required for a decision.

Detailed reports/logs/evidence are stored once at the authorized durable location when required and referenced by handle instead of duplicated into chat.
