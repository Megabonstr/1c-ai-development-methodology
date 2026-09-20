---
name: 1c-ai-github-handoff
description: Transfer exact task state between Coordinator Main, Local Main, and bounded specialist subagents using GitHub Issue/comment and commit/artifact handles without replaying project history.
compatibility: Requires the 1c-ai-development core/router files to be available at the documented repository paths.
---

# GitHub Handoff

## Role

**Shared / delegable Git-backed transport utility.** This skill transfers exact durable state between Coordinator Main, Local Main, and bounded specialists. It is not a workflow intent and does not own task semantics, implementation, evidence meaning, or acceptance.

Gitless work does not use this skill. It requires an already operational project-supplied durable transport; the methodology package does not ship that backend.

## Required core

Read:

- `.1c-ai/core/ORCHESTRATION.md`
- `.1c-ai/core/GIT_GITHUB_FLOW.md`
- `.1c-ai/core/TASK_CONTRACT.md`
- `.1c-ai/core/TOKEN_DIET.md`

## Preflight

Identify the exact current task packet, current actor/context, destination actor/context, and exact state being handed off.

## Handoff budget

For one bounded task, prefer:

- one Coordinator Main -> Local Main handoff;
- no intermediate Coordinator round trips for ordinary technical correction;
- one Local Main -> Coordinator Main final result/evidence handoff.

Progress comments may be durable evidence without becoming approval checkpoints.

Use another Coordinator/Local round trip only for a material escalation or an explicit new/correction contract.

## Workflow

Pass only the material transport packet:

```text
Task:
From:
To:
Repository:
Branch:
CommitSHA:
ExecutionProfile:
DelegatedGoalOrNextGate:
Permission:
EvidenceHandles:
FirstUnknownOrSTOP:
```

Omit fields that do not materially apply.

For a subagent, prefer the fresh bounded delegation packet in `ORCHESTRATION.md`.

Use one exact Issue comment when a correction or next-step delta is enough.

When the task/output contract assigns a GitHub Issue, PR, or exact comment as the result destination, write the required detailed result there and return to the invoking chat only a compact status + exact handle. If GitHub write is unavailable, return `CAPABILITY_BLOCKER`; do not dump the full result into chat for manual copy/paste unless the Human Owner explicitly requests that fallback.

Do not use this skill to turn compile/test/debug iterations into repeated Coordinator Main requests.

Do not replay chat history, broad Issue history, donor bodies, or already-addressable source content.

## Completion

The receiving actor must reproduce the exact state and know the next authorized action from supplied handles.

A branch name without exact SHA is not sufficient when the branch can move.
