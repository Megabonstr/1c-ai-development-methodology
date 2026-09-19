---
name: 1c-ai-source-first-research
description: Resolve one bounded fact from current project, official, standard, donor, or community evidence. Use in Coordinator-decision mode before freezing/correcting task semantics or in Local-technical mode during frozen execution when broad research is not justified.
compatibility: Requires the 1c-ai-development core/router files to be available at the documented repository paths.
---

# Source-First Research

## Role

**Shared / delegable skill with two explicit modes. Do not duplicate it.**

- **Coordinator-decision mode** - resolve one material fact before freezing/correcting task semantics or choosing among product/architecture/data/safety routes. Decision authority remains with Coordinator Main / Human Owner.
- **Local-technical mode** - resolve one bounded API/signature/metadata/mechanism fact while executing an already frozen task. Local Main may act on the result only when frozen product/architecture/data/safety/scope/acceptance semantics remain unchanged.

If Local-technical research would change those semantics, stop Local execution and escalate the result to Coordinator Main.

## Required core

Read:

- `.1c-ai/core/SOURCE_FIRST.md`
- `.1c-ai/core/TOKEN_DIET.md`
- `.1c-ai/core/STOP_ASK.md`
- `.1c-ai/core/ORCHESTRATION.md`

Use `.1c-ai/core/EVIDENCE_MODEL.md` when the result affects acceptance evidence.

## Preflight

State the active mode (`COORDINATOR_DECISION` or `LOCAL_TECHNICAL`), one material `UNKNOWN` or `SOURCE_GAP`, and the decision or implementation fact it blocks.

Start from the exact source packet supplied by the durable task/decision state.

If delegated to a Researcher/Scout, use the fresh bounded subagent packet from `ORCHESTRATION.md`.

## Workflow

1. Inspect current project evidence first.
2. Follow the source order and bounded-expansion rules in `SOURCE_FIRST.md`.
3. Separate documented facts, observed project/runtime facts, and inference.
4. Stop when the material fact is proven strongly enough for the blocked decision.
5. If bounded evidence remains insufficient, return `SOURCE_GAP`.

## Completion

Return:

- active role mode;
- answer to the exact unknown;
- exact evidence handle(s);
- confidence boundary / remaining unknown;
- smallest next action.

Coordinator-decision mode returns to the OwningCoordinator for the durable decision. Local-technical mode returns to Local Main; if the result crosses frozen semantics, return an escalation instead of an implicit redesign.

Read-only by default.

Do not roam the repository/KB, inherit the full parent transcript, redesign architecture, or turn research into implementation without explicit authority.
