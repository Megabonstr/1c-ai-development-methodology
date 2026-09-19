# XML sources + 1C Configurator execution profile

Status: PROFILE-XML-001.

## Progressive-disclosure read path

For a narrow already-routed Local Main task, do not preload this whole profile.

Start with `Select this profile when` + `Required identity`. Before a source write add `Mutation boundary`; for verification add only the applicable `Build / deploy / runtime boundary` and `Verification ladder`. Open `1C target preflight`, `Source-first specialization`, `Upstream skill/spec routing`, `Safety`, or `STOP conditions` only when the exact task triggers that concern.

This profile translates the tool-neutral core into a workflow where the authoritative project source is an XML source tree and build/deploy/runtime operations are performed through 1C Configurator/CLI or compatible automation.

This is a first-class execution route. It is not a fallback for projects that do not use EDT.

## Select this profile when

Use this profile when:

- the authoritative 1C source is an XML/source tree, whether Git-backed or using an already operational project-supplied Gitless durable carrier;
- configuration, extension, external processing/report, form, role, DCS, or related artifacts are created or changed through that source representation;
- 1C Configurator/CLI or compatible automation is the normal build/load/update/run path.

Do not select this profile merely because XML files exist somewhere in an EDT-owned project.

## Required identity

Before mutation, resolve as applicable:

- exact authoritative source/version identity;
- for Git-backed projects: exact Git repository, base, branch, and commit;
- for Gitless work: a project-supplied source snapshot/fingerprint or explicit `UNVERSIONED_CURRENT_STATE`; the methodology package does not ship the Gitless durable-state backend and must not invent provenance;
- authoritative XML source root;
- target artifact kind: configuration, extension, EPF, ERF, or another supported source family;
- exact object/file(s) to change;
- 1C platform/Configurator version or executable route when build/deploy behavior is version-sensitive;
- target infobase only when deployment/runtime proof is required and authorized;
- writer ownership and Task Contract acceptance gates.

The XML source tree, generated binary artifact, Configurator state, and target infobase are different identities. Do not silently treat one as proof of another.

## 1C target preflight

For managed-form, data-mapping, filtered-choice, and referenced-object tasks, read `.1c-ai/profiles/1c-common/TASK_PREFLIGHT.md`.

Before the first material source mutation, resolve the exact load-bearing target identity from current XML/project evidence: data path, type, execution context, cardinality, ownership, preserve/create policy, and filter contract as applicable.

Do not infer a data target from a UI caption/control name or guess XML structure from that label.

## Source-first specialization


Apply `.1c-ai/core/SOURCE_FIRST.md` with the narrowest relevant 1C sources:

1. current XML project source, accepted project conventions, tests, and known runtime behavior;
2. exact standard configuration or BSP implementation when the mechanism is standard;
3. applicable official 1C documentation/standard/check for platform or Configurator semantics;
4. exact `Nikolay-Shirokov/cc-1c-skills` skill/spec/guide when it provides the required XML structure or automation workflow;
5. another bounded pinned donor/reference only for a concrete remaining gap;
6. focused structural/build/deploy/runtime proof.

Do not preload all XML specifications or the whole upstream skill tree.

Useful references:

- https://github.com/Nikolay-Shirokov/cc-1c-skills
- https://github.com/1c-syntax/ssl_3_1
- https://github.com/1C-Company/v8-code-style

Official 1C/platform documentation outranks reverse-engineered or community documentation for platform semantics.

## Upstream skill/spec routing

`cc-1c-skills` already provides task-oriented skills and detailed specifications for many 1C XML families and Configurator workflows.

Use it on demand instead of copying those specifications into this repository:

```text
this repository core
-> this XML/Configurator profile
-> exact upstream task skill or exact XML/build specification
-> its script/tooling or Configurator/CLI operation
```

Select only the upstream skill/spec required by the exact task.

Examples of possible domains include forms, metadata, roles/RLS, DCS, extensions, EPF/ERF, configuration source, and Configurator build/load workflows. Their exact current contracts remain upstream-owned.

## Mutation boundary

XML is an authoritative source representation only when the project says it is.

For a material XML mutation:

- inspect the exact current source and project convention first;
- use a proven structure/spec/skill for the object being changed;
- do not invent XML element shape, namespaces, UUIDs, references, ordering, or cross-file relationships from memory;
- preserve project-required source manifests and related generated/source metadata;
- keep writes inside the authorized files/objects;
- re-read or validate the changed source before build/deploy.

If the required XML format is not proven by current source, official documentation, or a bounded accepted reference, return `SOURCE_GAP`.

## Build / deploy / runtime boundary

Keep these facts separate.

### Source / static

XML parses and passes the required structural/schema/project checks.

This is `STATIC` evidence, not platform acceptance.

### Build

Configurator/tooling successfully creates the required configuration, extension, EPF/ERF, or other artifact.

This is `BUILD` evidence.

### Deploy

The accepted source/artifact is successfully loaded/applied to an explicitly authorized target environment, including a test infobase when required.

This is `DEPLOY` evidence.

Deployment may change a target infobase and therefore requires the authority defined by the Task Contract.

### Runtime

The application or artifact is actually executed and the required behavior is observed.

This is `RUNTIME` evidence.

### Native / user acceptance

Real client/UI behavior that matters to the task is observed and, when required, accepted by the task owner.

These are `NATIVE` / `USER_ACCEPTANCE` evidence.

## Verification ladder

First apply cadence/depth from `.1c-ai/core/VERIFICATION_PROFILES.md`.

Select only required gates and prefer the cheapest high-signal check first:

```text
XML / structural validation
-> applicable focused static checks
-> focused automated tests when available
-> build/package
-> deploy/apply to an authorized target when required
-> runtime execution
-> native client/UI observation
-> conditional RLS/performance/volume gates
-> user acceptance when required
```

A valid XML file is not proof that Configurator accepts it.

A successful build is not proof that the target infobase was updated.

A successful deployment is not proof that application behavior is correct.

## Safety

Never place credentials in committed task instructions, scripts, or source examples.

Destructive or user-affecting operations such as database update, replacement, deletion, restore, extension administration, or production-target actions require explicit task authority and the narrowest safe target.

Prefer a disposable/test environment for risky proof when the Task Contract allows it.

## STOP conditions

In addition to `.1c-ai/core/STOP_ASK.md`, stop the affected path when:

- the authoritative source root or target artifact kind is ambiguous;
- the XML structure required for mutation is not proven;
- generated/source ownership is unclear and a write may be overwritten by the normal toolchain;
- the requested Configurator/platform operation is version-sensitive and its current contract is not established;
- deployment would affect an unauthorized infobase/environment;
- source/static/build/deploy evidence is being used as a substitute for required runtime/native proof.

## Not owned here

This profile does not own:

- generic Task Contract/Git/token/source/evidence policy;
- the full `cc-1c-skills` skill set or XML specifications;
- EDT/MCP execution rules;
- project-specific XML layout or build scripts;
- project-specific test/release policy;
- model-specific agent orchestration.
