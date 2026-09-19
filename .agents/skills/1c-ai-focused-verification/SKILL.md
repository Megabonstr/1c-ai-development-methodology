---
name: 1c-ai-focused-verification
description: Coordinate or run only the high-signal verification gates required for the changed scope. Use after implementation or correction to prove specific STATIC, TEST, BUILD, DEPLOY, RUNTIME, NATIVE, or acceptance states without broad regression by default.
compatibility: Requires the 1c-ai-development core/router files to be available at the documented repository paths.
---

# Focused Verification

## Role

**Primary owner: Local Main.** Local Main integrates the required verification gates and exact evidence; Coordinator Main consumes that evidence for acceptance rather than rerunning Local verification by default.

## Minimal read path

Start from the exact verification packet and selected profile.

Read only:

- `.1c-ai/core/EVIDENCE_MODEL.md` -> `Evidence classes`, `Truthfulness rules`, `Evidence identity`, `Completion`;
- `.1c-ai/core/VERIFICATION_PROFILES.md` -> the selected profile section plus `Broad rerun rule`, `Report cadence`, `Failure handling`;
- `.1c-ai/core/ORCHESTRATION.md` -> `Evidence responsibility`; add `Escalation` only if the gate exposes a material boundary;
- `.1c-ai/core/TASK_CONTRACT.md` only if required gates/acceptance are missing or contradictory.

Use only the verification/evidence sections of the already-selected execution profile. Do not reopen the router or full implementation owners for a routine final verification pass.

## Preflight

Resolve the exact source/version/artifact identity under test, required gates, `VerificationProfile`, priority, test budget, and cadence overrides from the Task Contract. For Git-backed projects this normally includes the exact commit SHA. For Gitless work use only a project-supplied snapshot/fingerprint or explicit `UNVERSIONED_CURRENT_STATE`, preserving weaker provenance truthfully; this label does not create a durable-state backend.

Default verification profile: `STANDARD`.

Local Main owns verification integration and may delegate exact test/runtime/log work to a bounded specialist.

## Workflow

1. Apply cadence/depth from `VERIFICATION_PROFILES.md`.
2. Start with the cheapest required high-signal gate.
3. For `FAST_CLIENT_SLICE`, reach a safe real/native scenario early once code compiles; do not build a broad suite first.
4. Run or delegate only gates relevant to the changed scope.
5. Bind results to exact source/version/artifact/environment identities. Use the commit SHA for Git-backed projects; when Git is absent, use only a project-supplied source snapshot/fingerprint or explicit `UNVERSIONED_CURRENT_STATE`.
6. Keep evidence classes separate.
7. Verify load-bearing delegated claims before Local Main verdict.
8. If a required physical/local gate cannot run in the current actor, hand off the exact target to local-runtime-validation.
9. On failure, preserve the first actionable failure and route a bounded correction.
10. Do not repeat broad/already-green suites without a concrete dependency or profile/final-gate reason.
11. Respect the task test budget; exceeding a FAST default budget requires a concrete current-task reason.

## Completion

Return each required gate as `PASS`, `FAIL`, `NOT_REQUIRED`, or explicit `UNKNOWN`, with exact evidence handles.

Do not collapse partial verification into `DONE`.
