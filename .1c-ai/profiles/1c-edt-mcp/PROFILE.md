# 1C:EDT + MCP execution profile

Status: PROFILE-EDT-001.

## Progressive-disclosure read path

For a narrow already-routed Local Main task, do not preload this whole profile.

Start with `Select this profile when` + `Required identity`. Before a write add `Mutation boundary`; for verification add only `Verification ladder` / `Evidence mapping`. Open `1C target preflight`, `Source-first specialization`, `EDT-MCP routing`, or `STOP conditions` only when the exact task triggers that concern.

This profile translates the tool-neutral core into a 1C:EDT workflow executed through structured MCP capabilities. It does not replace the core Task Contract, selected source/version transport, source policy, evidence model, or STOP/ASK rules.

## Select this profile when

Use this profile when the authoritative project source is maintained in 1C:EDT and the task will inspect, modify, validate, build, debug, or run that project through EDT/MCP capabilities.

Do not select it merely because EDT or MCP is available. If the project's authoritative source and delivery path are XML/Configurator-based, use the XML profile instead.

## Required identity

Before mutation, resolve as applicable:

- exact authoritative source/version identity;
- for Git-backed projects: exact Git repository, base, branch, and commit;
- for Gitless work: a project-supplied source snapshot/fingerprint or explicit `UNVERSIONED_CURRENT_STATE`; the methodology package does not ship the Gitless durable-state backend and must not invent provenance;
- exact EDT workspace/project;
- target metadata object/module/form/report/query;
- linked application/infobase when runtime proof is required;
- current EDT/MCP server surface and version-sensitive tool contract;
- writer ownership and Task Contract acceptance gates.

The source/version identity, EDT project, and runtime infobase are different identities. In Git-backed projects the source identity normally includes the Git commit. Do not silently substitute one identity for another.

## 1C target preflight

For managed-form, data-mapping, filtered-choice, and referenced-object tasks, read `.1c-ai/profiles/1c-common/TASK_PREFLIGHT.md`.

Before the first material BSL mutation, resolve the exact load-bearing target identity from current EDT/project evidence: data path, type, execution context, cardinality, ownership, preserve/create policy, and filter contract as applicable.

Use structured EDT/MCP inspection for this native preflight when available. Do not infer a data target from a UI caption/control name.

## Source-first specialization


Apply `.1c-ai/core/SOURCE_FIRST.md` with the narrowest relevant 1C sources:

1. current project source/runtime/tests and accepted project seam;
2. exact standard configuration or BSP implementation when the mechanism is standard;
3. applicable official 1C standard/check, including `1C-Company/v8-code-style` where relevant;
4. a bounded pinned donor/reference only for a concrete remaining gap;
5. the current EDT-MCP task skill and live tool guide/schema for the execution contract;
6. focused EDT/model/runtime proof.

Do not preload every layer. Open only the sources that constrain the current material decision.

Useful upstream references:

- https://github.com/DitriXNew/EDT-MCP
- https://github.com/1c-syntax/ssl_3_1
- https://github.com/1C-Company/v8-code-style

## EDT-MCP routing

EDT-MCP already separates standing rules from task-oriented workflows.

Use its current upstream routing rather than copying it into this repository:

```text
this repository core
-> this EDT profile
-> current EDT-MCP business-project router
-> one matching EDT-MCP task skill
-> live tool guide/schema when needed
-> tool
```

The current upstream `agent/ROUTER.md`, `agent/skills/COMMON.md`, installed project rules, and live MCP schema/help outrank examples copied into a task description.

Load more than one EDT-MCP skill only when the task genuinely crosses workflow boundaries.

## Mutation boundary

Prefer structured EDT/MCP mutation when the current tool contract supports the required change.

Do not make raw XML editing the default path inside an EDT-owned project.

Before mutation:

- inspect the exact target and current state;
- preserve returned previews, hashes, job IDs, launch IDs, cursors, and other operation identities;
- obtain explicit authority for destructive, cascading, runtime-data, database-update, or user-affecting operations.

Read-only discovery never authorizes mutation.

If the structured EDT/MCP surface cannot represent a required change, return the limitation or route to an explicitly authorized alternative. Do not silently bypass the profile.

## Verification ladder

First apply cadence/depth from `.1c-ai/core/VERIFICATION_PROFILES.md`.

Select only the gates required by the Task Contract. Prefer the cheapest high-signal gate first:

```text
EDT/model/query/form validation
-> applicable focused static checks
-> focused automated tests
-> build/artifact
-> runtime/debug
-> native client/UI observation
-> conditional RLS/performance/volume gates
-> user acceptance when required
```

A successful EDT model write or static validation is not runtime proof.

A successful build is not native/UI acceptance.

Project-specific frameworks such as YAxUnit are selected by the project/task contract; this profile does not make one framework mandatory for every repository.

## Evidence mapping

Use `.1c-ai/core/EVIDENCE_MODEL.md`.

Examples:

- model/query/form validation -> `STATIC`;
- focused test runner result -> `TEST`;
- EPF/ERF/application build -> `BUILD`;
- debugger or application execution -> `RUNTIME`;
- real managed-form/client behavior -> `NATIVE`;
- developer/product-owner approval -> `USER_ACCEPTANCE`.

Bind runtime evidence to the exact source/version identity and relevant application/runtime identity whenever possible. Use the exact Git commit for Git-backed projects; when Git is absent, use only a project-supplied snapshot/fingerprint or explicit truthful unversioned state.

## STOP conditions

In addition to `.1c-ai/core/STOP_ASK.md`, stop the affected path when:

- the exact EDT project or target object cannot be resolved;
- installed EDT-MCP capabilities differ materially from the task's assumed tool contract;
- project source and EDT model are demonstrably out of sync and safe ownership is unclear;
- a required operation is destructive/cascading and authority is absent;
- a static/model result is being used as a substitute for required runtime/native proof.

## Not owned here

This profile does not own:

- generic Task Contract/Git/token/source/evidence policy;
- the full EDT-MCP tool catalogue or skill definitions;
- EDT-MCP plugin development;
- XML/Configurator execution rules;
- project-specific architecture, metadata names, tests, branches, or release policy;
- model-specific agent orchestration.
