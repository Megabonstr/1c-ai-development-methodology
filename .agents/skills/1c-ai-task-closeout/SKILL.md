---
name: 1c-ai-task-closeout
description: Persist one Coordinator-owned durable closeout after Local Main verdict/evidence and required acceptance, then emit a concise human result without creating new evidence or a reporting subsystem.
compatibility: Requires the 1c-ai-development core/router files to be available at the documented repository paths.
---

# Task Closeout

## Role

Primary owner: Coordinator Main

This is a post-execution workflow. It starts only after Local Main returned its final local verdict/evidence and the required acceptance boundary has been satisfied.

One physical actor may switch from Local Main back to Coordinator Main for closeout. This does not waive the material acceptance-independence rule in `.1c-ai/core/ORCHESTRATION.md`.

## Required core

Read only as needed:

- `.1c-ai/core/ORCHESTRATION.md`
- `.1c-ai/core/EVIDENCE_MODEL.md`
- `.1c-ai/core/DELIVERY_DISCIPLINE.md`
- `.1c-ai/core/TASK_CONTRACT.md`
- `.1c-ai/core/TOKEN_DIET.md`

## Preflight

Resolve exact handles for:

```text
TaskHandle:
LocalVerdict:
ResultSourceVersionOrArtifact:
EvidenceHandles:
RequiredAcceptance:
FinalAcceptedOrDeliveredIdentity:
RemainingUnknowns:
FollowUpHandles:
```

Do not manufacture missing evidence or acceptance.

If a required gate/acceptance/final identity is unavailable, keep it `UNKNOWN`/pending and do not falsely close the task.

## Durable closeout

Persist exactly one authoritative compact closeout in the task's accepted durable carrier:

```text
TaskHandle:
Outcome:
ChangedTargets:
MaterialDecisionSummary:
AcceptedSourceVersionOrArtifact:
EvidenceHandles:
AcceptanceHandleOrAction:
RemainingUnknowns:
FollowUpHandles:
ClosedAt:
```

Omit `MaterialDecisionSummary` when the decision is obvious/non-material.

The closeout is an index/projection over existing task, source and evidence state. Do not copy full diffs, CI logs, test logs, PR history, research bodies, or evidence payloads into it.

For Git-backed work, the task's GitHub Issue/comment is the normal durable carrier. Gitless closeout is available only when the adopting project already supplies an operational durable carrier; this package does not ship that backend. Otherwise durable closeout remains `UNKNOWN/BLOCKED`.

## Workflow

1. Consume the exact Local Main verdict/result/evidence packet.
2. Verify that required evidence and acceptance are represented by exact handles; do not rerun verification merely for reporting.
3. Apply the material acceptance-independence rule when the same physical actor authored the change.
4. Resolve the exact final accepted/delivered source or artifact identity.
5. Persist one compact durable closeout.
6. Emit the concise human-facing result below.
7. Mark/close the task only when authorized.

## Human result

Default plain-Russian projection:

```text
Что сделано:
Где изменено:
Как проверено:
Что осталось неизвестным / ограничения:
Принятая версия / результат:
```

Keep it short. For a trivial task this may be 3-5 short lines.

A full report is optional and justified only by an explicit task requirement, high-risk/architectural work, or material client/support/handover value. Generate it from the same durable task/evidence handles rather than reconstructing old chat history.

## Boundaries

Do not:

- implement or correct product/source changes;
- rerun verification without a separate concrete reason;
- create a new evidence class;
- upgrade `UNKNOWN` to `PASS`;
- invent rationale or acceptance;
- treat an ImplementationMap as evidence;
- self-accept a material change authored by the same physical actor;
- create a second report/history database;
- keep an accepted technical task open for prose polish.

## Completion

Complete when one authoritative durable closeout is persisted, its accepted/delivered identity and evidence/acceptance handles are truthful, remaining UNKNOWNs are preserved, and the concise human projection has been emitted.
