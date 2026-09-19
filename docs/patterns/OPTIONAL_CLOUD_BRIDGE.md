# Optional GitHub <-> Cloud-Hosted Coordinator Main Bridge

Status: optional provider-dependent acceleration pattern.

This document does not define core orchestration. Canonical Coordinator Main / Local Main authority remains owned by `.1c-ai/core/ORCHESTRATION.md`.

## Purpose

Use this pattern only when a project wants an optional automation layer that can notify a **cloud-hosted placement** of Coordinator Main after Local Main reaches a material decision boundary.

The bridge carries a notification/handle.

GitHub carries the durable executable task, result, decision, and correction state.

Core orchestration remains valid without this bridge.

## Non-goals

This pattern does not require or promise:

- a cloud chat;
- a specific AI provider;
- a provider-native GitHub connector;
- a bidirectional cloud-chat API;
- Issue-comment wake-up support;
- automatic reuse of an existing cloud conversation;
- unattended cloud-side write approval;
- a webhook service;
- continuous Coordinator monitoring.

Unproven provider behavior remains `UNKNOWN`.

## Canonical state rule

The bridge must never be the only copy of material state.

```text
durable GitHub task
-> Local Main autonomous execution
-> durable GitHub result
-> optional notification
-> Coordinator Main reads durable GitHub state
-> durable GitHub decision/correction
-> Local Main resumes from GitHub
```

Direct chat text, webhook payload text, email, push notification, or another transient bridge message is never executable task state by itself.

## Result packet

Before any notification, Local Main persists one durable result comment.

Minimum fields:

```text
TaskID:
TaskRevision:
ResultID:
CommitSHA:
EvidenceHandles:
LocalVerdict: PASS | CORRECTION_REQUIRED | UNKNOWN | STOP
FirstMaterialUnknown:
DecisionRequired: YES | NO
DecisionClass:
```

`ResultID` is a stable logical idempotency key for that result publication.

The exact GitHub comment ID becomes an additional immutable transport handle after persistence.

### DecisionRequired = NO

Do not wake Coordinator Main.

Finish or continue inside the frozen Task Contract.

Progress/evidence comments do not become approval gates.

### DecisionRequired = YES

Persist the result first.

Then the optional bridge may send only the compact wake-up handle needed to locate the durable state, for example:

```text
TaskID:
TaskRevision:
ResultID:
IssueOrCommentURL:
DecisionClass:
```

Do not duplicate the full technical report into the bridge.

## Coordinator decision packet

Coordinator Main reads the durable GitHub task/result before deciding.

A material response is persisted as a **new append-only GitHub comment**.

Minimum fields:

```text
DecisionID:
ParentTaskID:
ParentTaskRevision:
ParentResultID:
DecisionType: ACCEPT | CORRECTION | STOP | ASK_USER
DecisionOrDelta:
AcceptanceDelta:
NextAuthorizedAction:
```

When a correction changes the frozen contract, use the correction shape from `.1c-ai/core/TASK_CONTRACT.md`.

Do not silently edit an earlier result/decision comment into a different meaning.

Append-only decisions make revision/authority history auditable.

## Resume rule

Local Main resumes only from a new durable GitHub decision/correction that:

- names the expected parent TaskID/TaskRevision;
- names the expected ParentResultID when responding to a result;
- comes from an authorized decision actor/transport;
- is not already consumed.

If the parent revision does not match, STOP with `UNKNOWN`.

If several unseen conflicting decisions exist, STOP with `UNKNOWN`.

Do not choose the newest-looking answer heuristically.

## Dedupe and replay protection

### Result publication

After timeout/reconnect/uncertain response:

1. read/search the exact Issue stream;
2. check whether the same `ResultID` is already persisted;
3. reuse the existing comment handle when found;
4. post only when the logical result is absent.

Never blindly retry a result comment.

### Decision consumption

Track at least:

- GitHub comment ID;
- `DecisionID` / `CorrectionID`;
- parent `TaskRevision`;
- parent `ResultID`.

Never apply the same decision twice.

Never apply a decision to a different task revision.

### Webhook delivery

When a GitHub webhook is used, `X-GitHub-Delivery` may be used as the delivery-level dedupe handle.

Delivery dedupe does not replace logical `ResultID` / `DecisionID` checks.

A redelivered event may represent the same durable state.

## Polling / monitoring

Polling or event monitoring is optional.

If used:

- only monitor after an explicit material `DecisionRequired=YES`;
- use bounded polling/backoff appropriate to the provider;
- do not continuously block Local Main after ordinary progress comments;
- keep an exact last-seen/comment cursor;
- verify parent revision and authority before consuming a response.

No proven monitoring capability -> manual notification/resume.

## Permissions

Start with least privilege.

For the queue/result loop, the Local/Coordinator transport normally needs only the Issue/comment permissions required by that exact workflow.

Add source/PR/Actions **read** only when acceptance requires those evidence classes.

Add repository content/PR/merge writes only for separately authorized workflows.

Do not broaden permissions merely because the integration supports them.

## Credentials and private data

Never place in Issue bodies, comments, repository docs, prompts, result packets, or bridge notifications:

- access tokens;
- webhook secrets;
- connector credentials;
- passwords;
- private client data not already authorized for the durable project channel.

Use the provider/project secret store.

The bridge should carry identifiers/handles, not secrets.

## Smoke test

Before declaring the optional loop available, prove the exact selected transport.

Minimum smoke:

1. Coordinator side can read the exact repository/Issue state required by the workflow.
2. If Coordinator writes are required, it can publish one bounded durable test comment.
3. Local Main side can read that exact comment.
4. Local Main can publish one bounded result comment.
5. The optional notification channel can deliver one test wake-up.
6. If response monitoring is enabled, the consumer distinguishes new durable response from stale history.
7. A material response can be persisted to GitHub and consumed once.
8. Duplicate/retry behavior is tested with the selected ResultID/DecisionID strategy.

Missing proof -> bridge availability is `UNKNOWN`; use manual coordination.

## Manual fallback

The compatibility floor is:

```text
Local Main durable GitHub result
-> human/manual notification
-> Coordinator Main reads GitHub
-> Coordinator decision
-> human/authorized tool persists exact GitHub decision
-> Local Main resumes from GitHub
```

This is slower but preserves the same architecture.

Loss of a provider integration changes transport only.

It does not change Coordinator Main / Local Main authority.

## Provider extension boundary

A provider-specific implementation may add:

- webhook receiver;
- event trigger;
- push notification;
- cloud-task wake-up;
- response-channel monitoring.

Each extension must separately prove:

- supported event type;
- authentication/authorization;
- replay/dedupe behavior;
- delivery guarantees/limits;
- response persistence path;
- approval requirements;
- how it binds to the intended Coordinator context.

Do not generalize one provider's feature matrix into core policy.

## Example state sequence

```text
Task T-42 / revision 3
        |
        v
Local Main result R-42-3-A persisted to GitHub
DecisionRequired=YES
        |
        +---- optional wake notification ---->
        |
Coordinator Main reads exact result comment
        |
        v
Decision D-42-3-A persisted to GitHub
ParentResultID=R-42-3-A
        |
        v
Local Main verifies IDs/revision/authority
        |
        v
resume
```

If the same wake event is delivered twice, no second decision application occurs.

If R-42-3-A already exists after a timeout, Local Main reuses it instead of reposting it.

## Invariants

- optional pattern only;
- GitHub is durable executable state;
- bridge carries wake-up handles, not authority;
- Local Main autonomy remains intact;
- Coordinator Main is invoked only at material decision boundaries;
- result is durable before notification;
- decision is durable before resume;
- append-only material decisions;
- exact revision/parent binding;
- idempotency/replay protection;
- least privilege;
- credentials stay outside task/repository content;
- missing provider capability remains `UNKNOWN`;
- manual fallback always remains valid.
