# Methodology Evaluation and Manual Adoption

Canonical machine-facing owner for evaluating and manually adopting `1c-ai-development` into another project before an executable TaskHandle exists.

Current product state:

```text
AdoptionMode: MANUAL_PINNED_COPY
InstallerUpdateUninstall: NOT_SHIPPED
InstalledPackageValidator: NOT_SHIPPED
GitlessDurableBackend: NOT_SHIPPED
```

Installer/update/uninstall/manifest/hash automation is separate future work ([#2](https://github.com/Megabonstr/1c-ai-development-methodology/issues/2)). The Gitless durable-state backend is separate future work ([#1](https://github.com/Megabonstr/1c-ai-development-methodology/issues/1)). Do not invent either capability here.

## Entry condition

Use this owner when the user supplies this methodology repository URL/ref and asks whether it should be used, merged with, or adopted into another project.

A pre-install evaluation **does not require an existing TaskHandle**.

Evaluation is read-only by default. Do not mutate the adopting project until the user authorizes the exact adoption action.

## Evaluation flow

1. Resolve the exact methodology source revision being evaluated.
   - Prefer an exact commit SHA.
   - If the supplied URL points to a moving branch/default branch, resolve its current commit before recommending a pinned copy.
   - If an exact revision cannot be established, evaluation may continue read-only, but adoption must not be described as pinned.
2. Inspect the adopting project before recommending changes:
   - authoritative 1C source ownership: EDT, XML/Configurator, mixed/unclear;
   - Git-backed vs deliberately Gitless;
   - existing root agent instructions/adapters;
   - existing `.1c-ai` and `1c-ai-*` skills;
   - existing project-owned skills, knowledge owners, test/build/runtime conventions;
   - obvious overlap or conflict with current project process.
3. Classify the recommendation:
   - `NONE` - do not install; current project already owns the needed behavior or the package is a poor fit.
   - `SELECTIVE` - adopt only an exact non-conflicting package component whose dependency closure is understood; do not create a partial broken methodology tree.
   - `FULL` - adopt the current complete machine package when it does not create a competing policy owner.
4. Explain overlap/conflict and current limitations before requesting writes.
5. State the current adoption mode exactly: `MANUAL_PINNED_COPY`.
6. Ask for write permission only after the recommendation is clear.
7. After authorization, materialize only the approved package-owned surfaces and minimal adapter route.
8. Record the exact methodology revision in project-owned state.
9. Perform the manual structural checks in this file.
10. Return one concise Russian human result.

Do not recommend installation merely because this repository describes itself as useful.

## What the agent discovers without asking

When accessible, inspect these facts directly:

- project layout and authoritative source;
- Git/no-Git state;
- existing instructions/adapters;
- existing skills and namespace ownership;
- existing methodology installation/version markers;
- EDT/XML route evidence;
- project knowledge owners and obvious duplicated policy.

Do not ask the human to supply technical facts that current source/tools can establish cheaply.

## What requires the Human Owner

Ask only for:

- permission to write/adopt;
- a real conflict between legitimate project policies;
- product/business/architecture/data/safety choices source cannot determine;
- destructive/production authority;
- explicit acceptance of degraded provenance when using an externally provided Gitless route.

## Current manual pinned-copy boundary

Before copying, resolve and retain:

```text
MethodologyPackage: Megabonstr/1c-ai-development-methodology @ <exact 40-char SHA>
```

Without that exact SHA, do not claim `MANUAL_PINNED_COPY` completed.

Current package-owned surfaces:

- `.1c-ai/**`;
- `.agents/skills/1c-ai-*/**`.

Root client adapters are project files unless the project explicitly authorizes a minimal methodology route. Preserve all unrelated existing instructions.

`PROJECT_AI.md` is project-owned. When created/updated for adoption, include the exact `MethodologyPackage` line above.

There is no shipped manifest/hash ownership database today. Therefore:

- a first authorized pinned copy may be performed manually;
- repeated update/uninstall must not be presented as deterministic or merge-safe;
- if managed package files already exist, compare/stop rather than overwrite blindly;
- do not claim installer validation.

## Manual structural validation

After an authorized manual adoption, check only what can actually be proven today:

- exact methodology SHA is recorded in `PROJECT_AI.md` or another explicit project-owned package marker;
- approved `.1c-ai/**` / `.agents/skills/1c-ai-*/**` surfaces exist;
- the selected root adapter resolves to `.1c-ai/START_HERE.md`;
- no duplicate methodology-owned `1c-ai-*` mirror was created in another client-specific skill tree;
- unrelated project-owned instructions/skills were preserved as far as the observed diff shows.

Report this as `MANUAL_STRUCTURE_CHECK`, not as deterministic installer validation.

## Gitless status

Gitless compatibility is currently **designed/degraded**, not a shipped end-to-end backend.

The core/profile semantics can work with an externally supplied durable task carrier and truthful source identity. However this package does not currently ship the writer/replay/lock/snapshot/recovery backend described in `docs/research/GITLESS_LOCAL_STATE_V1.md`.

Therefore:

- do not claim that installing this package creates a complete Gitless lifecycle;
- if the adopting project already has an operational durable carrier/source identity, integrate it explicitly and preserve weaker provenance truthfully;
- if no such carrier exists, keep durable Gitless lifecycle support `UNKNOWN/BLOCKED` rather than inventing storage mechanics.

## Human-facing result

Default evaluation/adoption result is concise Russian:

```text
Что проверено:
Что методика добавит:
Что уже есть / пересекается:
Конфликт или ограничение:
Рекомендация: NONE | SELECTIVE | FULL
Текущий режим: MANUAL_PINNED_COPY
Изменения: не вносились | <точно что разрешено и сделано>
Версия методики: <exact SHA, если adoption выполнен>
Проверка структуры: MANUAL_STRUCTURE_CHECK PASS | UNKNOWN
```

Omit lines that do not materially apply. Do not expose machine packets by default.
