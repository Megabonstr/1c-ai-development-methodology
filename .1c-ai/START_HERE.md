# 1C AI Development - Detailed Machine Routing

Normally start from root `AGENT_START.txt`.

Read this file only when the current route needs more detail than the compact bootstrap provides.

## Pre-install evaluation / adoption

A user may start with only this methodology repository URL/ref and an adopting project. No durable TaskHandle is required for that read-only evaluation.

Route directly to `.1c-ai/core/ADOPTION.md`: resolve the exact methodology revision, inspect the adopting project, classify `NONE | SELECTIVE | FULL`, state `MANUAL_PINNED_COPY`, and request write permission only after the recommendation is clear.

Do not invent installer/update/uninstall or a Gitless durable backend.

## Role entry

**Coordinator Main** may begin from raw/noisy human intent before a durable Task Contract exists. It owns intake/readiness, semantic task state, material decision routing, acceptance and closeout.

**Local Main** begins from an exact already-frozen durable TaskHandle. Task bootstrap is its execution ingress; it owns bounded technical discovery, implementation, review, verification/runtime and the local verdict.

One physical agent may perform both roles sequentially. The durable task/decision boundary separates authority; a new chat is not mandatory.

## Read order

1. resolve the active route and exact durable handle available for that phase; pre-install evaluation may use the methodology URL/ref instead of a TaskHandle;
2. `PROJECT_AI.md` when it exists and project-specific identity/constraints are materially needed but not already supplied;
3. only the exact required core owner section(s);
4. `.1c-ai/router/ROUTER.md` when route/profile/delegation is not already fixed;
5. at most one primary workflow skill;
6. at most one execution profile when execution-specific behavior matters;
7. exact source/evidence handles.

Local Main does not preload README philosophy, raw/Coordinator conversation history, broad human docs, full Issue/project history, unrelated research, all skills/profiles, or closeout philosophy.

Do not preload README, all core files, all skills, all profiles, Issue history, donor trees, or old reports.

## Human-facing output default

When answering the Human Owner/user:

- use concise plain Russian by default;
- answer only the current question/decision/task;
- do not dump machine contracts, Issue history, internal identifiers, long evidence packets, or implementation narration unless they are materially required or explicitly requested;
- do not narrate routine reads, edits, tool calls, tests, or internal planning;
- store detailed technical material once in durable state and reference it only when useful.

For task framing, show only the materially applicable plain-Russian fields:

```text
Что хотим получить:
Что сейчас не так:
Что предлагает пользователь:
Границы задачи:
Что нельзя менять (только если это реальная материальная граница):
Как проверим результат:
Известные существенные ограничения:
Что пока неизвестно:
Готова ли задача к работе:
Что делать дальше:
```

Omit empty/non-applicable fields. Do not expose the machine packet unless requested.

## Core owners

- pre-install evaluation/manual pinned adoption: `.1c-ai/core/ADOPTION.md`;
- raw/noisy human intent and readiness routing: `.1c-ai/core/TASK_INTAKE.md`;
- task/acceptance contract: `.1c-ai/core/TASK_CONTRACT.md`;
- adopting-project ownership/knowledge layout: `.1c-ai/core/PROJECT_STRUCTURE.md`;
- Coordinator Main / Local Main / subagents: `.1c-ai/core/ORCHESTRATION.md`;
- branch lifecycle and GitHub delivery: `.1c-ai/core/GIT_GITHUB_FLOW.md`;
- context/token discipline: `.1c-ai/core/TOKEN_DIET.md`;
- source/donor choice: `.1c-ai/core/SOURCE_FIRST.md`;
- minimal sufficient scope / complexity / stop-after-DONE: `.1c-ai/core/DELIVERY_DISCIPLINE.md`;
- evidence classes: `.1c-ai/core/EVIDENCE_MODEL.md`;
- verification depth/cadence: `.1c-ai/core/VERIFICATION_PROFILES.md`;
- material STOP/ASK: `.1c-ai/core/STOP_ASK.md`.

## Default repository branch route

`feature/<task> -> preprod -> main`.

Feature branches start from current `preprod`.

## 1C target preflight

For managed-form/data mapping/filter/reference tasks, use `.1c-ai/profiles/1c-common/TASK_PREFLIGHT.md` before the first source-dependent implementation when exact target identity is not already frozen.

## Execution profiles


- EDT + MCP: `.1c-ai/profiles/1c-edt-mcp/PROFILE.md`;
- XML + Configurator: `.1c-ai/profiles/1c-xml-configurator/PROFILE.md`.

Do not select a profile from tool availability alone. Select it from authoritative source/delivery ownership.

## Evidence

Missing proof remains `UNKNOWN`.

Never promote SOURCE/STATIC/BUILD/DEPLOY into RUNTIME/NATIVE proof.
