# Token Diet

Token discipline means minimizing irrelevant or repeated context while preserving everything required for correctness.

It applies to both INPUT and OUTPUT cost. It is not a blind character limit: material constraints, risks, blockers, authority boundaries, acceptance conditions, and evidence requirements must still be preserved.

## Read path

Default:

```text
START_HERE
-> TOKEN_DIET
-> exact task
-> exact core owner section
-> one profile/skill when needed
-> exact source/evidence
```

Do not preload:

- the whole repository;
- full Issue history;
- all core owners;
- all execution profiles;
- all skills;
- broad donor repositories;
- old research or logs.

## Progressive disclosure

Prefer the smallest context that can answer the current question:

```text
index / summary / count
-> exact owner / file / section / method
-> immediately required adjacent context
```

Stop expanding when the current question is resolved.

Source authority, source packets, donor selection, bounded source expansion, and `SOURCE_GAP` are owned by `SOURCE_FIRST.md`; do not create a parallel source-retrieval policy here.

## Coordinator context ownership

Owning a `CoordinationScope` does not authorize full-scope preload.

Coordinator Main owns the scope knowledge map, accepted checkpoint, architecture/decision context, durable task states, material decision/research handles, open material UNKNOWNs, and acceptance/closeout state. It loads only the material sources required for the current decision.

A long-lived coordinator should reconstruct continuity from `PROJECT_AI.md`, the selected durable task state, exact source/version identities, and durable project owners rather than depend on provider chat memory. For Git-backed projects, GitHub handles and exact SHAs are the recommended/default realization.

Coordinator Main does not preload the whole repository, full donor repositories, all research bodies, all Issue histories, all skills/profiles, Local Main debug narration, or raw runtime logs when an exact evidence handle is sufficient.

## Human input / semantic noise

Token Diet applies before execution too.

Natural conversation, voice input and exploratory thinking may be verbose when that helps the human think. Do not optimize for minimum characters at the cost of ambiguity.

Before executable handoff:
- normalize raw transcript/history once instead of forwarding it wholesale;
- remove abandoned alternatives, repeated filler and already-known context from the downstream packet;
- preserve necessary reasoning/constraints by exact handle when they still matter;
- if the human changes a decision, carry the current rule plus explicit supersession instead of two competing full discussions;
- treat contradiction/unclear precedence as more expensive than a few extra explanatory words;
- keep several unrelated goals out of one execution packet.

The target is semantic density and unambiguous current intent, not robotic shorthand.

## Local Main execution context

Local Main receives the executable task, not the process that created it.

Normal working set:

```text
TaskHandle
SourceVersionIdentity
Goal
ExactScope / OwnedTargets
DirectlyNecessaryRelatedImplementation (implicit unless narrowed)
SourceHandles (when needed)
MaterialConstraints (only when applicable)
VerificationProfile / RequiredGates
STOP_ASK_Boundary (material choices only)
DeliveryBoundary
ExecutionProfile (when needed)
```

Resolve `CoordinationScope`, `OwningCoordinator`, writer ownership, mechanism details, and other execution facts through the TaskHandle/bootstrap packet when they are not already needed in working context.

`DoNotTouch / ProhibitedChanges` is **optional and sparse**. Include it only for a concrete material boundary the executor could plausibly cross while solving the task. Do not spend tokens enumerating the complement of the positive scope; for ordinary work, `Preserve unrelated existing behavior` is enough when a preservation reminder is useful.

Prefer exact handles over repeated prose; fields already resolvable from the TaskHandle do not need to be copied again. Positive scope is the default boundary.

Local Main does **not** read by default:

- README philosophy or broad human documentation;
- raw Human Owner transcript or Coordinator conversation history;
- full Issue/project history;
- broad roadmap or unrelated research;
- full deep-research bodies when an exact accepted conclusion/evidence handle exists;
- all canonical skills or all execution profiles;
- product rationale that does not affect the frozen task;
- closeout/reporting philosophy.

Open additional context only for one concrete execution question. If resolving it would change frozen product/architecture/data/safety/acceptance semantics, escalate instead of widening Local Main context into a new product discussion.

### Simple Local fast path

If the TaskHandle is already ready and the next skill/profile is fixed, prefer:

```text
exact TaskHandle/bootstrap packet
-> exact sections named by the selected Local skill
-> exact sections of one execution profile
-> task-specific source
-> focused verification sections
-> compact Local verdict/evidence packet
```

Do not reopen the router, full `ORCHESTRATION.md`, full profiles, or unrelated core owners merely because they are linked. Load the exact named section/anchor when the retrieval tool supports it. Expand only when a concrete boundary/UNKNOWN triggers that owner.

## Transport

Prefer exact handles over copied context:

- durable task/decision handle;
- exact source/version + path;
- symbol/section/line range;
- Git-backed projects: repository + ref/SHA + path / commit SHA;
- job/run/artifact identifier.

Do not repeat context that the next actor can resolve reliably from the supplied handle.

## Corrections

A correction packet carries the delta, not the full original task.

Use the contract in `TASK_CONTRACT.md`.

## Tool documentation

Do not preload every tool guide or schema.

Load the exact live guide/section only when the selected profile or skill needs a version-sensitive, uncertain, or high-risk operation.

## Quality-preserving exception

Never omit a material constraint, risk, authority boundary, acceptance condition, or evidence requirement merely to save tokens.

If the necessary detail is too large for a compact task packet, store it once in one bounded artifact and pass its exact handle.

## Silent work / output economy

For Local Main and other token-metered executors, ordinary bounded work defaults to `SILENT_WORK`.

Do not emit step-by-step narration of file/source reads, tool calls, routine edits, compile/test/debug cycles, internal planning, or repeated progress restatements.

Emit intermediate output only when a material STOP/ASK boundary is reached, a Human Owner/Coordinator decision is required, a material failure/UNKNOWN changes the authorized route, or a handoff/result packet is actually required.

Otherwise continue working and return one compact final verdict with exact handles.

Do not duplicate long logs/reports in chat. Store required detail once in durable state and pass its handle.
