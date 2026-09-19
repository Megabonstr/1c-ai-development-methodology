---
name: 1c-ai-local-runtime-validation
description: Validate an exact source/version identity or artifact in the selected local 1C execution environment. Use when source/static evidence is insufficient and BUILD, DEPLOY, RUNTIME, NATIVE, or user-facing behavior must be proven.
compatibility: Requires the 1c-ai-development core/router files to be available at the documented repository paths.
---

# Local Runtime Validation

## Role

**Primary owner: Local Main.** Local Main may delegate one exact runtime/test/log operation to a bounded specialist, but retains verification integration and the local verdict.

## Minimal read path

Start from the exact runtime-validation packet and already-selected execution profile.

Read only:

- `.1c-ai/core/EVIDENCE_MODEL.md` -> `Truthfulness rules`, `Evidence identity`, and the evidence classes required by this gate;
- `.1c-ai/core/VERIFICATION_PROFILES.md` -> the selected profile + `Failure handling`;
- `.1c-ai/core/ORCHESTRATION.md` -> `Evidence responsibility`; add `Escalation` only if a material boundary appears;
- `.1c-ai/core/GIT_GITHUB_FLOW.md` only for Git-backed source/branch operations;
- `.1c-ai/core/TASK_CONTRACT.md` only if runtime authority/required gate is unclear.

Do not reopen the router when the execution profile is already fixed. Read only the runtime/build/deploy/native sections of that profile needed by the exact gate.

## Preflight

Local Main owns the local verdict and may delegate an exact test/runtime/log step while retaining integration responsibility.

Resolve:

- exact task;
- exact source/version identity and artifact identity when applicable;
- for Git-backed projects: exact commit SHA;
- for Gitless work: a project-supplied source snapshot/fingerprint or explicit `UNVERSIONED_CURRENT_STATE`, without inventing Git provenance or a durable backend;
- exact execution profile;
- target local project/environment;
- authorized build/deploy/runtime/native gates;
- verification profile / priority when specified.

Do not validate an unspecified moving source state. For Git-backed projects pin the exact commit when required; for Gitless work use the project-supplied snapshot/fingerprint when available, or report `UNVERSIONED_CURRENT_STATE` explicitly.

## Workflow

1. Reproduce or fetch the exact source state.
2. Verify the local environment/project identity.
3. Follow the selected execution profile and verification profile for the required build/deploy/runtime/native route.
4. For FAST_CLIENT_SLICE UI/client work, exercise the safe real/native path early when authorized instead of postponing it until after broad test construction.
5. Record only gates actually executed and observed.
6. Bind evidence to source/version/artifact/environment identities. Use Git commit identity only for Git-backed projects; use only the project-supplied Gitless source identity when Git is absent.
7. Return failures and environment limitations truthfully; do not substitute source/static evidence for a missing runtime gate.

## Completion

Return gate-specific evidence for the exact target, remaining `UNKNOWN` states, and the next acceptance or correction action to Local Main.

Do not mutate an unauthorized target environment.
