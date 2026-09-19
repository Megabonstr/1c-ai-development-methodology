# Verification Profiles

Canonical machine-facing owner for verification depth, cadence, and urgency/risk matching.

This file does not redefine evidence meaning. Evidence classes remain owned by `EVIDENCE_MODEL.md`.

## Select one profile

Task Contract may set:

```text
VerificationProfile: FAST_CLIENT_SLICE | STANDARD | HIGH_RISK
Priority: WORKING_NATIVE_RESULT | NORMAL | SAFETY_FIRST
TestBudget:
ParityCadence:
```

Default when not specified: `STANDARD`.

A project may specialize the names/thresholds only through explicit project instructions/Task Contract.

## FAST_CLIENT_SLICE

Use for a narrow, urgent client-visible slice with bounded blast radius.

Typical examples:

- fill several fields from an existing object;
- add/fix one form command;
- change one bounded filter;
- correct one narrow mapping;
- fix one local report/form behavior.

Do not select FAST merely because the user is impatient when the task is materially destructive/high-risk.

### Default cadence

1. one initial Git/source cleanliness/identity check;
2. one exact source/native preflight for load-bearing targets;
3. compile/static/model validation after relevant source edits;
4. as soon as code compiles and a safe runtime path exists, exercise the real/native client scenario early;
5. during iteration, add/run only tests directly justified by changed behavior or a discovered defect;
6. run the full **focused** regression once at final acceptance;
7. prove full parity/publication only:
   - initially when repository/publication state is uncertain;
   - after structural metadata/form/source-representation changes;
   - at final publication/delivery;
8. return one final compact result/evidence packet by default.

Do not rerun broad/full suites, full parity hashes, or large reports after every BSL micro-fix.

### Test budget

Default **new-test budget: 0-3**.

This is not a universal hard cap.

Exceed it only with an explicit reason tied to:
- discovered defect/risk;
- required contract behavior;
- multiple materially distinct branches that need protection;
- existing project testing policy.

Do not create a new test framework merely to satisfy a narrow urgent slice unless the Task Contract requires it.

### Native-first rule

For UI/client behavior, early safe native/runtime proof outranks building an exhaustive test suite before the real scenario has been exercised once.

Native proof does not replace final required tests.

## STANDARD

Use for normal development.

Typical cadence:

- exact source/preflight as needed;
- focused static checks during implementation;
- targeted tests during meaningful checkpoints;
- appropriate focused regression before feature acceptance;
- build/deploy/runtime/native gates required by the task;
- integration checks on `preprod`;
- one final compact result/evidence packet.

Avoid broad reruns after every micro-edit unless a concrete dependency requires them.

## HIGH_RISK

Use for materially high blast radius, for example:

- destructive/mass data operations;
- migrations;
- security/RLS-sensitive changes;
- legal/exchange documents;
- broad metadata/global architecture changes;
- replacement of a shared standard mechanism;
- production-facing operations with difficult rollback.

May require as applicable:

- broader regression;
- independent critical review;
- explicit backup/rollback;
- staged deploy/runtime proof;
- repeated gates at meaningful phase boundaries;
- stronger parity/audit evidence;
- stricter human acceptance.

HIGH_RISK still follows Token Diet: load only evidence needed for the risk.

## Priority

Priority tunes optimization inside the selected verification profile.

### WORKING_NATIVE_RESULT

Use when the user explicitly needs a narrow working client result quickly.

Rules:

- do not expand architecture/test/report scope without a concrete failure/risk;
- reach safe native/runtime proof early;
- keep ordinary corrections local;
- final required evidence remains mandatory.

### NORMAL

Balance delivery speed and normal project evidence.

### SAFETY_FIRST

Prefer additional evidence/rollback/review where the cost of a wrong result is materially high.

Priority never authorizes bypassing rights/RLS, security, data integrity, destructive-action authority, or required evidence.

## Broad rerun rule

Do not rerun a broad/full suite merely because any file changed.

Rerun when:

- the changed slice has a known dependency on that suite;
- a meaningful integration checkpoint was reached;
- the Task Contract requires it;
- final acceptance requires it.

## Parity cadence

Full source/scaffold/file/hash parity is not a micro-edit gate.

Default full parity:

1. initial proof if source/publication state is uncertain;
2. after structural metadata/form/source-layout changes;
3. final publication/delivery.

For ordinary BSL micro-fixes in a clean task-owned branch, branch/status/diff + touched-file verification is normally enough between required final gates.

## Report cadence

Default: verification returns one final compact result/evidence packet.

Coordinator closeout later persists one authoritative durable accepted summary and emits the concise human projection. Do not create two full reports for the same task.

Intermediate durable comments should record only material decisions, blockers, accepted corrections, or phase evidence.

Do not publish a full result report after every technical correction. A full closeout report is optional and belongs to the Coordinator lifecycle boundary, not verification.

## Failure handling

A failing required gate creates a local correction loop under `ORCHESTRATION.md`.

Do not automatically escalate to Coordinator Main or upgrade the verification profile because one technical check failed.

Upgrade profile/depth only when the failure reveals materially higher risk/scope.

## Completion

Verification profile controls cadence/depth.

Task completion still requires every Task Contract gate to be:
- `PASS`;
- explicit `NOT_REQUIRED`;
- or explicitly accepted with named remaining `UNKNOWN`.
