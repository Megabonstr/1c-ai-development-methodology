---
name: 1c-ai-deep-research
description: Run Coordinator-owned broad multi-pass research that needs multi-source synthesis, counter-evidence, and adversarial follow-up. May be delegated to a Researcher; Local Main escalates this need instead of using deep research as its primary execution workflow.
compatibility: Requires the 1c-ai-development core/router files to be available at the documented repository paths and a research-capable context with authorized source access.
---

# Deep Multi-Pass Research

## Role

**Primary owner: Coordinator Main; execution may be delegated to a bounded Researcher context.**

This is not a Local Main primary workflow. If Local Main discovers that a genuine broad V1/V2/V3 research decision is required, it pauses execution and escalates to Coordinator Main. A co-located physical actor may switch back to Coordinator role without opening a new chat, but the durable decision/task boundary must be updated before Local execution resumes.

## Required core

Read:

- `.1c-ai/core/SOURCE_FIRST.md`
- `.1c-ai/core/TOKEN_DIET.md`
- `.1c-ai/core/EVIDENCE_MODEL.md`
- `.1c-ai/core/ORCHESTRATION.md`
- `.1c-ai/core/PROJECT_STRUCTURE.md`
- `.1c-ai/core/DELIVERY_DISCIPLINE.md`

Read `.1c-ai/core/STOP_ASK.md` when source/privacy/authority boundaries may be crossed.

## Trigger gate

Use this skill only when at least one is true:

- the exact task explicitly requires broad multi-pass research;
- an architecture/product/technology decision needs comparison of several credible approaches;
- source quality/ecosystem state is uncertain enough that one bounded lookup cannot support the decision;
- the decision is expensive/high-impact enough to justify adversarial multi-source review.

Do **not** use this skill for:

- one API/signature/version lookup;
- one material UNKNOWN that bounded `1c-ai-source-first-research` can prove;
- an ordinary implementation defect;
- compile/test/runtime debugging;
- broad browsing without a named decision.

If the trigger gate is not met, route to `1c-ai-source-first-research` or the implementation workflow instead.

## Preflight

Resolve:

```text
ResearchQuestion:
DecisionBlocked:
CoordinationScope:
OwningCoordinator:
SourcePrivacyBoundary:
RequiredPrimarySources:
TargetCompatibilityOrVersion:
PersistenceMode: ISSUE_ONLY | REPO_ARTIFACTS | ISSUE_PLUS_EXTERNAL_BACKUP
FinalDecisionOwner:
```

Start from exact current project/source evidence when it materially applies.

Never disclose private project/client source, data, credentials, or proprietary implementation details to public research channels without explicit authority.

## Source uniqueness

Default target for each pass: **10-15 new unique credible sources**.

This is a research-depth target, not a quota.

A source counts as new/unique when it provides materially independent evidence or a distinct authoritative version/origin.

Do not pad counts with:

- mirrors;
- reposts;
- copied articles;
- multiple URLs for the same underlying source;
- the same repository/version reread without new independent evidence.

Revisiting an earlier source is allowed but does not count as a new source for the later pass.

If the topic genuinely has fewer credible sources, return `SOURCE_LIMIT` with the exact search boundary instead of inventing/padding sources.

## Evidence labels

Keep these separate:

- `DOCUMENTED_FACT` - directly supported by source/documentation;
- `PROJECT_OBSERVATION` - observed in current project/runtime evidence;
- `INFERENCE` - reasoned interpretation;
- `RECOMMENDATION` - proposed decision;
- `UNKNOWN` - materially unresolved;
- `SOURCE_LIMIT` - credible source pool exhausted below the default target.

Do not promote inference into fact.

## Pass V1 - broad evidence map

Goal: understand the landscape before choosing a direction.

1. Start with current project/current source when material.
2. Prioritize applicable official/primary sources.
3. Add primary source repositories/specifications.
4. Use proven community/Infostart/practice evidence only where it contributes a distinct practice fact or fills a primary-source gap.
5. Gather 10-15 new unique credible sources by default.
6. Record exact date/version/ref when it changes meaning.
7. Maintain a compact source ledger.

Minimum source-ledger fields:

```text
SourceID:
SourceOrRepository:
DateOrRef:
Class: PRIMARY | OFFICIAL | PROJECT | COMMUNITY
WhatItProves:
Limits:
```

### V1 critique

Before V2, explicitly record:

- contradictions;
- weak/circular evidence;
- missing primary evidence;
- version/population/compatibility mismatch;
- claims still based on inference;
- strongest alternative interpretation;
- exact V2 questions.

Do not call V1 a final recommendation.

## Pass V2 - targeted correction and counter-evidence

Goal: attack the weaknesses found in V1.

1. Search specifically for V1 gaps and contradictions.
2. Gather another 10-15 new unique credible sources by default.
3. Prefer counter-evidence and primary sources that could overturn the emerging direction.
4. Test the strongest alternative interpretation.
5. Reconcile version/compatibility differences instead of averaging incompatible evidence.

### V2 critique

Record:

- what V1 got wrong or overstated;
- evidence that changed the direction;
- unresolved contradictions;
- remaining UNKNOWNs;
- strongest surviving counterargument;
- exact V3 falsification/failure-mode questions.

## Pass V3 - adversarial follow-up

Goal: try to falsify the emerging conclusion.

1. Gather another 10-15 new unique credible sources by default.
2. Focus on edge cases, compatibility, failure modes, security/safety boundaries, adoption risks, and counterexamples.
3. For 1C:Fresh-targeted work, include applicable current official Fresh evidence.
4. Prefer evidence that could prove the emerging recommendation wrong.

### Final critique

Before final synthesis:

- identify evidence that most strongly opposes the recommendation;
- state what remains unproven;
- distinguish robust conclusions from environment/version-specific conclusions;
- run a simplicity/scope check from Delivery Discipline;
- verify that research did not turn into unauthorized implementation.

## Persistence

The selected durable task state remains canonical for task-specific research.

For Git-backed projects, GitHub Issue/comment state is the recommended/default carrier.

For Gitless work, this package does not ship a durable-state backend. Persist research only through an already operational project-supplied durable carrier and bind source claims to the project-supplied snapshot/fingerprint actually available. `docs/research/GITLESS_LOCAL_STATE_V1.md` is design evidence only, not executable storage. If no operational carrier exists, durable persistence is `UNKNOWN/BLOCKED`; do not invent journal paths, GitHub Issues, commit SHAs, branch ancestry, review history, or Git-equivalent provenance.

### ISSUE_ONLY

Default when the result is task-specific and does not need reusable repository artifacts.

Persist compact V1/V2/V3 critique checkpoints and final synthesis in the exact durable task record. For Git-backed projects this is normally the exact GitHub Issue/comment chain.

### REPO_ARTIFACTS

Use when research has durable reuse/audit value.

Store bounded research artifacts under the project-approved research location (default only when applicable: `docs/research/`) and place compact exact handles in the selected durable task state.

Do not create V1/V2/V3 Markdown files merely for ceremony when one final reusable artifact plus Issue checkpoints is sufficient.

### ISSUE_PLUS_EXTERNAL_BACKUP

Same canonical durable task state plus an explicitly authorized independent backup/export. For Git-backed projects the canonical task state is normally GitHub; for Gitless work it must be the already operational project-supplied durable carrier.

External Drive/Yandex/S3/NAS/etc. is optional transport/backup only and never canonical task state.

## Token discipline

The research context may read broadly; the parent context should not.

Do not forward full articles, repository histories, or long transcripts to Coordinator Main/Local Main.

Return compact pass critiques, source-ledger handles, and final conclusions.

Context ownership by `OwningCoordinator` does not require the coordinator to preload all research sources.

## Final synthesis

Return:

```text
ResearchQuestion:
DecisionBlocked:
FinalStatus: PASS | SOURCE_LIMIT | UNKNOWN
DocumentedFacts:
ProjectObservations:
CounterEvidence:
Recommendation:
StrongestCounterargument:
ConfidenceBoundary:
RemainingUnknowns:
SourceLedgerHandle:
ArtifactHandles:
NextAction:
```

Bind conclusions to exact evidence handles.

A recommendation is not implementation authority unless the Task Contract grants it.

## Completion

Complete only after V1 critique, V2 critique, V3/final critique, and final synthesis are persisted according to the selected mode.

Return the compact result to the exact durable task state and its `OwningCoordinator`. A delegated Researcher returns to Coordinator Main; Local Main does not consume deep research as an implicit task redesign. For Git-backed projects this normally means the exact GitHub Issue/comment.

Do not redesign unrelated architecture, create a crawler/RAG framework, or continue searching after the research decision is sufficiently bounded and the selected protocol is complete.
