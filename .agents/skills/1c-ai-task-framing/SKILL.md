---
name: 1c-ai-task-framing
description: Normalize raw/noisy/materially unclear human intent into a decision-ready route before Task Contract/bootstrap. Skip when a durable bounded task is already ready. Never implement.
compatibility: Requires the 1c-ai-development core/router files to be available at the documented repository paths.
---

# Task Framing

## Role

**Primary owner: Coordinator Main.**

This is pre-execution work. Local Main does not use task framing as an implementation workflow; if raw/noisy intent reaches Local execution, return to the Coordinator/intake boundary instead of interpreting product intent locally.

## Required core

Read only as needed:
- `.1c-ai/core/TASK_INTAKE.md`
- `.1c-ai/core/ORCHESTRATION.md`
- `.1c-ai/core/TOKEN_DIET.md`
- `.1c-ai/core/SOURCE_FIRST.md`
- `.1c-ai/core/STOP_ASK.md`

## Fast bypass

If an already durable bounded task is materially ready, STOP this skill and route directly to `1c-ai-task-bootstrap`. Do not re-frame a ready task.

Do not invoke framing merely because the user is conversational, verbose or informal. Exploratory discussion can remain discussion until an executable task is actually being formed.

## Route ownership

The agent owns skill selection. The Human Owner does not need to say `1c-ai-task-framing` or know internal route names.

Use this skill automatically when executable intent is materially raw/noisy/contradictory. An advanced user may request the skill or clarification mode explicitly, but that is optional.

## Clarification dialogue mode

Use a short interactive dialogue when the current executable intent cannot yet be normalized truthfully because a material human decision/meaning is unclear.

1. Extract everything already clear first.
2. Ask the first material question in plain language, normally one at a time.
3. When it reduces friction, offer 2-4 concrete choices plus an open alternative.
4. Do not ask the human for project/source/API/type/path facts that bounded source inspection can answer cheaply.
5. After each answer, update the normalized framing state without replaying the conversation.
6. If the new answer appears to contradict an earlier instruction, ask whether the new decision replaces it; record the supersession explicitly.
7. Stop asking when the existing readiness route can be selected.
8. Return one compact current task/route, not a transcript of the interview.

Do not create a new readiness state for this mode.

## Workflow

1. Preserve the authorized raw input through an exact durable `RawIntentHandle` when normalization is material; do not forward the full raw/voice stream downstream by default.
2. Extract the desired observable outcome, positive bounded scope, material constraints, acceptance expectations and user-suggested mechanism. Add DO_NOT_TOUCH only for a concrete material exception.
3. Keep `UserSuggestedMechanism` non-authoritative unless supported by current project/source or explicit Human Owner/architecture authority.
4. Identify only material UNKNOWNs.
5. Return exactly one route: `READY`, `RESEARCH_NEEDED`, `HUMAN_DECISION_NEEDED`, or `EXPLORATION`.
6. For one material blocking source/mechanism UNKNOWN, route to `1c-ai-source-first-research`; use deep research only for genuinely broad/high-impact uncertainty.
7. When READY, persist/confirm the compact durable task and hand off to `1c-ai-task-bootstrap`.

## Framed result

When framing is material, return only the materially applicable fields from the canonical intake packet:

```text
RawIntentHandle:
DesiredOutcome:
ObservedProblem:
Scope:
UserSuggestedMechanism:
MaterialConstraints:
DoNotTouch: <optional material exception only>
AcceptanceChecks:
MaterialUnknowns:
ReadinessState:
NextRoute:
```

Do not manufacture a `DoNotTouch` list for ordinary adjacent fields. When a material prohibition really matters, keep it explicit and compact. Keep `AcceptanceChecks` explicit when materially relevant.

For a human-facing framing result, return only the materially applicable plain-Russian fields below by default. Do not prepend the machine packet, framing commentary, or internal identifiers unless the human explicitly asks for them:

```text
Что хотим получить:
Что сейчас не так:
Что предлагает пользователь:
Границы задачи:
Что нельзя менять (только если это реально важная граница):
Как проверим результат:
Известные существенные ограничения:
Что пока неизвестно:
Готова ли задача к работе:
Что делать дальше:
```

Omit an empty/non-applicable line rather than invent content. `RawIntentHandle` is normally a durable internal handle and does not need to be shown to the human unless it is useful for continuity or review.

## Output discipline

Do not implement product/source changes. Do not narrate routine framing steps. Do not paste the full raw transcript/history downstream.
Agent-facing packet: compact technical English + exact handles.
Human-facing result: concise plain Russian by default.

## Completion

Complete when the request is either ready for durable Task Contract/bootstrap, routed to one bounded research/decision path, explicitly marked exploration, or stopped because no implementation is needed.