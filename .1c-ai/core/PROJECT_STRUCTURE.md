# Adopting Project Structure

Canonical machine-facing owner for separating methodology-owned content, project-owned source/knowledge, durable task state, evidence, artifacts, and transient execution material.

This file defines ownership and storage defaults only. It does not create directories or replace a project's coherent existing layout.

## Core principle

Organize by **semantic ownership**, not by a mandatory folder tree.

Use the smallest structure that keeps truth unambiguous:

- task state lives with the task;
- reusable project knowledge lives in the project repository;
- durable cross-task decisions/policies have explicit project owners;
- evidence stays bound to exact source/artifact/environment identities;
- generated artifacts are not authoritative editable source;
- transient execution output stays local/CI unless explicitly promoted.

A new directory is justified only when that semantic class has recurring durable content.

## Ownership classes

### Project source

The adopting project's existing authoritative 1C source layout remains project-owned.

Do not move EDT projects, XML sources, configuration files, tests, or build scripts merely to fit this methodology.

Source representation is selected by actual project ownership:

- EDT + MCP -> `.1c-ai/profiles/1c-edt-mcp/PROFILE.md`;
- XML + Configurator -> `.1c-ai/profiles/1c-xml-configurator/PROFILE.md`.

Generated EPF/ERF/CFE/build output is not authoritative editable source merely because it is convenient to distribute.

### Package-managed methodology (manual today)

Current adoption mode is `MANUAL_PINNED_COPY`; no installer/update/uninstall implementation is shipped yet.

Package ownership belongs to:

- `.1c-ai/**`;
- `.agents/skills/1c-ai-*/**`;
- only the explicitly managed blocks/imports inserted into root client adapters.

Project code and project knowledge must not be stored inside those managed trees.

A project must not locally fork a managed methodology file as an undocumented customization. A future updater ([#2](https://github.com/Megabonstr/1c-ai-development-methodology/issues/2)) must detect modified managed files from manifest/hash ownership and STOP instead of silently overwriting them. Until then, repeated manual copy/update must compare existing managed files and must not claim merge-safe updater behavior.

### Project-owned machine overlay

Recommended canonical project-owned machine file:

`PROJECT_AI.md`

It is optional but, when present, is owned entirely by the adopting project.

Keep it compact. It may contain or point to:

- project identity;
- exact installed methodology revision, for example `MethodologyPackage: Megabonstr/1c-ai-development-methodology @ <exact SHA>`;
- authoritative source representation and selected execution profile;
- project-specific invariants and DO_NOT_TOUCH boundaries;
- exact current project knowledge/policy/source indexes;
- durable task-state location;
- project-specific verification/runtime handles;
- material deviations explicitly accepted for this project.

It must not copy the generic `.1c-ai/core/*` policy or become a growing knowledge dump.

Package install/update/uninstall must never overwrite or delete `PROJECT_AI.md`.

### Coordinator scope context

When stable project/domain coordination context is needed, `PROJECT_AI.md` may carry or point to:

```text
CoordinationScope:
OwningCoordinator:
ProjectOrDomainIdentity:
AuthoritativeSource:
AcceptedCheckpoint:
KnowledgeIndex:
ArchitectureInvariants:
OpenMaterialUnknowns:
DurableTaskState:
ExecutionRoute:
AcceptanceAuthority:
```

Do not require every field when the information is already explicit in another durable project owner.

Coordinator Main context ownership means responsibility for the authoritative map and accepted state of its scope. It does not authorize loading the whole project/domain into model context.

### Project-owned skills and client-specific rules

The directory `.agents/skills/` is a shared discovery surface, not wholly package-owned.

Ownership is namespaced:

- `.agents/skills/1c-ai-*/**` - methodology-managed generic skills;
- other project-specific skill directories - project-owned unless another installed package explicitly owns its namespace.

Project-specific skills should use clear project/domain names and must not use the reserved `1c-ai-` prefix.

Existing project-owned content already present outside managed blocks in `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Copilot instructions, or another native instruction surface remains project-owned. Do not silently migrate or normalize it.

If project-specific instruction sources materially conflict, return the conflict to the Task Contract owner instead of guessing precedence.

## Storage planes

### 1. Durable task state

For Git-backed projects, GitHub Issue/PR/commit/CI is the recommended/default durable task/evidence transport.

Use:

- Issue/task comment - Goal, scope, material decisions/corrections, blockers, acceptance, closeout;
- commit SHA - exact source state;
- PR - bounded diff/review/integration;
- CI/job/artifact handle - generated test/build evidence and artifacts.

Do not mirror the same task into a default repository `tasks/` tree.

A repository task/spec file is valid only when the adopting project deliberately uses spec-as-code or when that document itself is a reusable contract beyond one task.

### 2. Reusable project knowledge

Versioned repository documentation owns facts that multiple future tasks should reuse.

Typical durable classes, created only when needed:

- architecture/subsystem/integration knowledge;
- project instructions and stable policies;
- reusable accepted research;
- cross-task decisions/ADRs;
- cross-task plans/roadmaps;
- reusable client/support/audit reports;
- source/donor provenance.

Use the project's existing coherent documentation layout when one already exists.

### 3. Evidence

Evidence proves a specific claim and remains bound to the exact applicable identity.

Default owner:

- PR/CI/job/artifact/task evidence handle.

Commit a human-readable evidence document only when it has explicit reuse, audit, support, or Task Contract value.

Evidence is not the same as a report:

- **evidence** proves;
- **report** explains/projects existing evidence.

A report does not create or upgrade evidence.

### 4. Generated artifacts

Generated deliverables/output belong to the appropriate artifact plane:

- working build -> ignored local storage;
- CI result -> CI artifact store;
- accepted distributable -> Release/package/artifact store or approved external archive.

The task records the exact source/artifact identity/hash when material.

Generated artifacts must not become canonical editable source, project policy, or a substitute for evidence.

### 5. Transient/runtime output

Do not treat local execution material as project knowledge.

Keep out of Git unless the project explicitly owns it:

- IDE/workspace caches;
- generated intermediate builds;
- transient logs;
- temporary exports;
- debugger output;
- local runtime state;
- machine-specific paths/settings;
- local credentials/tokens;
- database copies/backups.

If the project has no transient convention, `.tmp/1c-ai/` is the default suggested ignored location.

## Semantic project-owned classes

These classes describe meaning. They do not require one folder each.

### Instructions

Purpose: route humans/agents through this project.

Owner: `PROJECT_AI.md` plus existing project-native instruction owner(s).

Do not duplicate generic methodology, task history, or stable project policy text when an exact policy owner can be linked.

### Rules / policies

Purpose: stable cross-task constraints.

Owner: project-owned versioned policy documents or existing project engineering standards.

Typical examples: rights/RLS invariants, release constraints, coding/project conventions, safety boundaries.

Do not store per-task acceptance criteria here.

### Reusable docs / knowledge

Purpose: durable project facts and mechanisms needed by more than one task.

Owner: existing project documentation layout, often `docs/` or domain-specific subtrees.

Do not place scratch, raw logs, or copied Issue history here.

### Research

Task-only research stays with the task.

Reusable accepted research may be committed, typically under the project's existing research/docs area such as `docs/research/`.

Research remains evidence/provenance for a decision; it does not become a competing architecture owner.

### Plans

A plan for one task stays with that task.

A cross-task initiative/rollout/dependency plan may be versioned when it has value beyond one Issue. An optional path such as `docs/plans/` is appropriate only when that class recurs.

Do not create a default `plans/` folder for small projects.

### Decisions

Task-scoped decisions stay in the task.

Cross-task architecture/product decisions may use an existing ADR/decision owner such as `docs/decisions/` when the project needs one.

Retain explicit supersession rather than silently rewriting historical decisions.

### Notes / scratch

Scratch is not a durable knowledge class.

Keep it local/transient. Before task close, either delete it or promote the useful content into its real owner: task decision, plan, reusable knowledge, research, or evidence.

Do not create a durable generic `notes/` bucket.

### Reports

Ordinary task result/closeout stays with the task.

Commit a report only when it has independent reusable/client/support/audit/handoff value.

A report must link existing evidence rather than duplicate full CI logs, diffs, or task history.

### Evidence

Use exact task/PR/CI/artifact handles by default.

A committed `docs/evidence/`-style area is optional and only for intentionally durable audit/reuse evidence.

Do not create one merely because the methodology recognizes evidence as a class.

### Features / roadmap

GitHub Issues/Projects/Milestones normally own feature/task portfolio state.

A versioned roadmap is optional when a durable narrative is needed beyond the tracker.

Executable `.feature` files used by Vanessa/BDD are test/spec source, not roadmap knowledge.

### Donors / sources

Use an optional `sources/SOURCES.md` or existing provenance registry when external sources materially affect project decisions.

Record exact repository/version/path/what-it-proves/license-or-access notes where applicable.

Do not vendor donor trees merely to create a registry.

## Minimal project profile

A normal small/medium project should remain small.

Example:

```text
<existing authoritative 1C source>      project-owned
PROJECT_AI.md                           compact project router/index

docs/                                   reusable project docs, only as needed
sources/SOURCES.md                      optional, only when provenance tracking is useful

.1c-ai/**                               methodology-managed
.agents/skills/1c-ai-*/**               methodology-managed

.tmp/1c-ai/**                           optional ignored transient output
```

Outside the repository tree:

```text
GitHub Issue     -> task contract / material decisions / closeout
PR + commit      -> source diff / accepted source identity
CI/job/artifact  -> verification evidence / generated artifacts
```

Do not create by default:

- `tasks/`;
- `notes/`;
- `plans/`;
- `reports/`;
- `evidence/`;
- `artifacts/`;
- `features/`;
- separate instruction/policy trees when direct owners already work.

## Long-lived / complex project profile

A long-lived project grows semantic owners only when direct files stop being sufficient.

Possible projection:

```text
PROJECT_AI.md

docs/
  architecture/          optional current architecture/knowledge
  engineering/           optional project instructions/policies/runbooks
  research/              reusable accepted research
  decisions/             cross-task durable decisions/ADRs
  plans/                 cross-task initiative/rollout plans
  reports/               reusable/client/support/audit reports
  evidence/              small durable audit evidence only
  roadmap/               optional when tracker alone is insufficient
  <domain>/              optional domain knowledge

sources/
  SOURCES.md              optional provenance registry

.tmp/1c-ai/               ignored transient output
```

This is an example, not a required tree.

If an existing project already has coherent `docs/integrations/`, `adr/`, `knowledge/`, or other owners, preserve them and point to them.

Domain-oriented ownership is valid when clearer than generic taxonomy.

## PROJECT_AI routing and index rule

`PROJECT_AI.md` should route to **exact current owners**, not trigger broad workspace scans.

Preferred fresh-agent path:

```text
AGENT_START
-> PROJECT_AI.md when project context is needed
-> exact TaskHandle
-> one exact project owner/index entry relevant to the task
-> exact section/file/evidence
```

Do not route:

```text
PROJECT_AI
-> scan docs/**
-> scan research/**
-> scan all old reports/evidence
```

Use direct paths while they remain sufficient.

Create an `INDEX.md` only when:

- there are enough sibling owners that direct pointers become unreliable;
- the index materially reduces search/context cost.

An index lists current owner handles and supersession state. It must not copy owner content.

## Anti-duplication rules

1. One fact -> one canonical owner; other files link it.
2. One-task state stays with the task.
3. Task plan stays with the task unless it has cross-task value.
4. Notes/scratch must be promoted or deleted, not accumulated indefinitely.
5. Report != evidence.
6. Artifact != authoritative source.
7. Instructions route; policies constrain.
8. Research supports a decision; it does not compete with the current owner.
9. Roadmap groups/prioritizes; task owns execution contract.
10. Source registry stores provenance, not donor copies.

## Incremental adoption / migration

Do not reorganize an existing project wholesale.

1. Inspect the current layout and identify existing coherent owners.
2. Classify existing material semantically without moving it.
3. Point `PROJECT_AI.md` to the accepted current owners.
4. Stop creating new duplicates.
5. Move/reclassify old material only when it is next materially touched.
6. Add indexes only when retrieval actually needs them.
7. Preserve Git/task history; do not rewrite history merely to make the tree prettier.

Examples:

- a durable `notes/*workplan*` may become a task plan or cross-task plan;
- a repository task file duplicating an Issue should become a pointer or a reusable contract;
- markdown placed under `artifacts/` but actually containing proof/reporting should move only when touched to its semantic owner;
- stable rules should converge on one current policy owner.

## Durable task state and Gitless boundary

GitHub Issue/PR/commit/CI is the recommended/default durable task/evidence transport for Git-backed projects.

Git/GitHub is not a universal architecture requirement, but the package currently ships **no operational Gitless durable-state backend**.

Gitless status: `DESIGNED_DEGRADED_COMPATIBILITY`.

An explicitly Gitless project may use this methodology only when the adopting project already supplies an operational durable task/source-state mechanism with stable identity/versioning, explicit permissions and one-writer/conflict rules. Preserve weaker provenance/diff/review guarantees truthfully.

`docs/research/GITLESS_LOCAL_STATE_V1.md` is a design/research contract, not a shipped writer/replay/lock/snapshot/recovery backend. If the project has no operational durable carrier, keep the Gitless lifecycle `UNKNOWN/BLOCKED` rather than inventing one. Backend implementation is tracked separately in [#1](https://github.com/Megabonstr/1c-ai-development-methodology/issues/1).

The same semantic classes still apply in Gitless projects, but `PROJECT_AI.md` must point to the actual operational carrier for task state, source identity, evidence transport, conflict/writer rules, and backup/recovery.

A local `tasks/` folder must not be presented as Git-equivalent provenance by itself.

## Initialization preflight

Before an agent creates or reorganizes project-structure files, resolve:

```text
ExistingProjectLayout:
CoordinationScope:
OwningCoordinator:
AuthoritativeSource:
AcceptedCheckpoint:
PackageOwned:
ProjectOwned:
ExistingProjectInstructions:
ExistingKnowledgeOwners:
DurableTaskState:
EvidenceTransport:
GitTracked:
LocalOnly:
RequestedNewKnowledge:
FirstMaterialUnknown:
```

Rules:

1. inspect existing paths first;
2. reuse coherent project owners;
3. create only the smallest missing owner;
4. never overwrite project-owned content silently;
5. rerunning initialization must be idempotent in meaning;
6. no empty taxonomy tree without current need;
7. prefer pointer/classification first; move files only when materially touched.

## Update/promotion boundary

Project-specific improvements may reveal reusable methodology improvements.

Do not edit installed `.1c-ai` package files in-place and call that an upstream change.

Instead:

1. record the project evidence/problem;
2. generalize away client/project identifiers, secrets, absolute paths, and task-only details;
3. raise a bounded change in the methodology repository;
4. update the adopting project later through the package update mechanism.

## Backup model

Normal durability:

`local working copy + primary Git remote`.

An optional independent third backup may be used, for example:

- second Git remote/mirror;
- versioned `git bundle`;
- versioned archive/export to an approved independent storage provider.

Rules:

- the backup is not canonical task state;
- do not infer RUNTIME/NATIVE evidence from backup presence;
- do not place credentials/client secrets in generic backups;
- avoid live synchronization of an active `.git` working tree through a generic sync client when lock/conflict/partial-sync behavior is uncertain;
- database/runtime backups follow their own security/retention policy.

## Invariants

- current project source remains authoritative for project facts;
- `.1c-ai` and `.agents/skills/1c-ai-*` remain methodology-managed;
- the reserved `1c-ai-` prefix belongs to this methodology package;
- project-specific skills may coexist outside that namespace;
- project-owned instructions/knowledge remain outside managed package trees;
- `PROJECT_AI.md` is a compact router/index, not a knowledge dump;
- task state, reusable knowledge, evidence, generated artifacts, and transient output remain semantically distinct;
- existing coherent project layouts remain valid;
- no default repository `tasks/notes/artifacts` tree is required;
- indexes are introduced only when exact direct paths stop being sufficient;
- GitHub is the recommended/default durable task state for Git-backed projects;
- Gitless semantics are designed/degraded only; an operational project-supplied durable carrier is required until [#1](https://github.com/Megabonstr/1c-ai-development-methodology/issues/1) ships a backend;
- external backup is optional and provider-neutral;
- missing evidence remains UNKNOWN.
