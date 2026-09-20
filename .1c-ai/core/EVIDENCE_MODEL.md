# Evidence Model

Verification itself is ordinary engineering practice. This model does not introduce a new requirement to "check that the task works"; the Task Contract and verification profile already determine what must be checked for the task.

Its purpose is durable handoff and reporting: record exactly what kind of check or observation exists, and on which source/artifact/environment, so a later agent or person does not flatten different facts into a vague "verified" state or infer a stronger result than was actually observed.

Different checks answer different questions. Keep their states separate only when materially useful for task acceptance, handoff, or history.

Verification depth/cadence is selected by `.1c-ai/core/VERIFICATION_PROFILES.md`.

A verification profile may change when/how often a gate runs. It never changes what SOURCE/STATIC/TEST/BUILD/DEPLOY/RUNTIME/NATIVE/USER_ACCEPTANCE means.

## Evidence classes

Use the classes that materially apply:

- **SOURCE** - source/design/contract inspection supports the intended mechanism.
- **STATIC** - syntax, schema, model, query, lint, or other non-runtime validation.
- **TEST** - focused automated tests for the changed behavior.
- **BUILD** - package/artifact/build creation succeeded and its identity is known when relevant.
- **DEPLOY** - the accepted source/artifact/configuration was successfully applied or deployed to the intended target environment; this proves deployment/application success, not application behavior.
- **RUNTIME** - behavior was exercised in the real runtime or equivalent execution environment.
- **NATIVE** - real client/UI/IDE interaction was observed when static/runtime automation is insufficient.
- **USER_ACCEPTANCE** - the task owner accepted the required observable behavior.

## State

Evidence classes are independent.

A valid state may be:

```text
SOURCE=PASS
STATIC=PASS
TEST=PASS
BUILD=PASS
DEPLOY=NOT_REQUIRED
RUNTIME=UNKNOWN
NATIVE=NOT_REQUIRED
USER_ACCEPTANCE=PENDING
```

Do not collapse this into `DONE`.

## Truthfulness rules

- Static/model success is not runtime proof.
- Build success is not deployment proof.
- Deployment success is not functional runtime proof.
- A successful agent/tool call is not evidence for a different layer.
- Missing/unavailable/incomplete data is not a clean zero or a pass.
- Historical evidence does not prove a newer commit unless the relevant artifact/source is unchanged and that reuse is explicit.

## Evidence identity

Bind evidence to the exact target whenever possible:

- commit SHA;
- artifact hash;
- test run/job ID;
- environment/profile;
- runtime version;
- exact acceptance action.

## Completion

A task is ready for delivery only when every required gate from its Task Contract is:

- `PASS`;
- explicitly `NOT_REQUIRED`; or
- explicitly accepted with a named remaining `UNKNOWN`.

Unstated skipped gates are not acceptance.

## ImplementationMap is not evidence

For material AI-written changes, an `ImplementationMap` may use this compact shape:

```text
WhatChanged:
WhyThisMechanism:
ReusedStandardOrProjectMechanism:
KeyFilesObjects:
MaterialRightsRLSDataAssumptions:
WhatWasNotChanged:
VerificationPerformed:
RemainingUnknowns:
```

It is a human review/navigation aid only.

Do not create a new evidence class for it and do not treat generated explanation as proof. Technical truth remains bound to the applicable exact SOURCE/STATIC/TEST/BUILD/DEPLOY/RUNTIME/NATIVE/USER_ACCEPTANCE evidence.

## Closeout is not evidence

A lifecycle closeout or human final report may summarize and index exact evidence handles, but it is not an evidence class and cannot create or upgrade proof.

Rules:

- verification owns the evidence packet;
- closeout references the exact accepted source/version/artifact and applicable evidence/acceptance handles;
- missing or unavailable proof remains `UNKNOWN`;
- an accepted remaining `UNKNOWN` must stay explicit in the closeout;
- concise human wording must not imply runtime/native/user acceptance that the evidence does not contain;
- do not duplicate full logs, diffs, CI output, or test bodies into the closeout.

The Coordinator-owned closeout workflow is defined by `ORCHESTRATION.md` and packaged by `.agents/skills/1c-ai-task-closeout/SKILL.md`.

