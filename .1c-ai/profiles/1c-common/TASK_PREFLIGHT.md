# 1C Target Preflight

Shared 1C-specific contract for managed forms, data mapping, selection filters, and referenced-object resolution.

Use with either execution profile:
- `.1c-ai/profiles/1c-edt-mcp/PROFILE.md`
- `.1c-ai/profiles/1c-xml-configurator/PROFILE.md`

This file does not replace the tool-neutral Task Contract.

## Trigger

Use this preflight when a task materially changes or reads one or more of:

- managed-form controls bound to data;
- form attributes;
- tabular-section/table-row values;
- metadata requisites;
- referenced catalogs/documents;
- filtered selection/list behavior;
- mappings between source and target 1C objects.

Do not require this packet for unrelated tasks.

## Rule

A human/UI label is not a proven data target.

Before the first material BSL/XML implementation for a load-bearing target, resolve the exact target identity from current source/runtime/native project evidence.

Do not infer:

- control name == form attribute;
- caption == data path;
- same-looking names == same type;
- scalar == table/indexed target;
- client method == server method;
- referenced object exists.

## Target packet

Resolve fields that materially apply:

```text
TargetID:
BusinessMeaning:
UIElement:
DataPath:
OwningObjectOrFormAttribute:
Type:
ExecutionContext:
Cardinality:
Action:
Source:
```

### Action values

Use one explicit action per target where applicable:

- `SET`
- `PRESERVE`
- `RESOLVE`
- `REUSE_ONLY`
- `REUSE_OR_CREATE`
- `WARN_AND_LEAVE_BLANK`
- `FAIL_TASK`
- project-defined explicit action

Do not hide create/reuse/preserve policy inside prose.

## OWNED_TARGETS

Positive target identity is the primary boundary.

List the exact fields/objects/business target the task owns. Local Main may make the smallest directly necessary related technical adjustment when it is required to make those owned targets work and frozen semantics do not change.

Ownership is write authority, not merely "mentioned in the Issue". Do not enumerate every neighboring field merely to prove that it is not owned.

## Optional material PRESERVE / DO_NOT_TOUCH

Do not create a neighboring-field blacklist by default.

Use explicit `PRESERVE` / `DO_NOT_TOUCH` only when a materially relevant nearby value has a real overwrite/safety risk that Local Main could plausibly cross while solving the task.

For ordinary tasks, positive `OWNED_TARGETS` plus a compact rule such as `Preserve unrelated existing behavior` is sufficient.

Legitimate example:

```text
DO_NOT_TOUCH:
- Carrier: preserve the legally significant incoming document value; project mapping must never overwrite it.
```

When a materially relevant value must remain unchanged, explicit `PRESERVE` is preferred over an implied prohibition.

## MISSING_TARGET_POLICY

When a referenced target may not exist, freeze the policy before implementation.

Examples:

```text
MissingTargetPolicy:
- Vehicle: REUSE_OR_CREATE
- Driver: REUSE_OR_CREATE
- Carrier: PRESERVE
```

Do not leave the implementation to guess between reuse/create/warn/blank.

## FILTER_CONTRACT

For filtered choice/list behavior, freeze as applicable:

```text
FilterContract:
  SourceFields:
  TargetFields:
  MatchRule:
  UniquenessPolicy:
  DeletedInvalidPolicy:
  FallbackPolicy:
  UnrestrictedFallbackAllowed: true | false
```

Semantic text such as "filter by customer/company" is not enough when actual field identity is load-bearing.

## Execution context

For methods/events involved in the change, resolve the relevant execution context before first implementation when context materially affects callable APIs or data access.

Examples:

- client;
- server;
- server-no-context;
- form event;
- command handler;
- asynchronous/background execution.

Do not create a Coordinator/Local round trip for an ordinary missed directive after Local Main owns fix-forward execution; Local Main corrects it locally.

## Cardinality

When the target is not a scalar value, freeze cardinality/shape.

Examples:

- scalar;
- first row only;
- all rows;
- exact indexed path such as `Table[0].Field`;
- unique collection element by a frozen key.

## Native preflight packet

A Local Main may collect one compact packet before Coordinator Main authors the first source-dependent BSL skeleton:

```text
Object/FQN:
OwnedTargets:
DoNotTouch: <optional material exceptions only>
TargetPackets:
ExecutionContexts:
MissingTargetPolicy:
FilterContract:
ExactSourceHandles:
FirstUnknown:
```

No tests are required merely to collect this identity packet.

## Coordinator / Local boundary

Coordinator Main may define business mapping and architecture before exact native target identity is known.

Coordinator Main must not present guessed 1C target identity as confirmed implementation detail.

Once Local Main returns exact target evidence, Coordinator Main may freeze the skeleton/contract.

After handoff, ordinary context/signature/compile/runtime corrections remain Local Main fix-forward work under `ORCHESTRATION.md`.

## One task = one business outcome

Do not interpret one technical defect as a new task.

Compile errors, context corrections, exact API fixes, and task-owned runtime defects are internal iterations of the same business outcome unless they cross a material scope/semantic/safety boundary.

## Evidence

Exact target identity is `SOURCE` evidence.

It does not prove the final implementation is correct at STATIC/TEST/RUNTIME/NATIVE levels.
