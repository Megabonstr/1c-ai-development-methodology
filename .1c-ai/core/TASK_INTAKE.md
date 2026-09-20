# Task Intake

Owns the boundary between raw/noisy human intent and an executable durable Task Contract.

**Primary owner: Coordinator Main.** Local Main should not receive raw/noisy intake as its normal execution input; it receives an already frozen durable task and enters through task bootstrap.

It is lightweight and trigger-based. It is not a second planner, research subsystem, or Task Contract.

## Fast path

If an already durable bounded task has a clear observable result, sufficient material constraints/acceptance, no unresolved Human Owner decision, and no material blocking source/mechanism UNKNOWN:

```text
durable ready task
-> 1c-ai-task-bootstrap
-> Local Main
```

Do not invoke framing, broad research, alternative generation, or ceremonial plan approval.

## Framing trigger

Use task framing only when input is materially raw/noisy/unclear, for example:
- stream-of-thought or voice-like input;
- desired behavior is mixed with a guessed mechanism;
- observable result is materially unclear;
- a material preservation/prohibition boundary is unclear;
- a real product/architecture/data/safety choice remains;
- the human explicitly asks to formulate the task first.

Informal wording alone is not a framing trigger. Exploratory/creative discussion may remain discussion until it is being converted into executable work.

## Interactive clarification

When executable intent contains material contradictions, an unmarked change of direction, several competing goals, or unclear acceptance semantics, Coordinator Main may use a short clarification dialogue inside task framing.

Rules:
- the human does not need to name a skill or internal mode;
- extract what is already clear before asking anything;
- ask the first material question in plain language, normally one at a time;
- when useful, offer a few concrete choices plus an open alternative;
- do not ask for a cheap technical fact that current project/source can resolve;
- if a new answer appears to replace an earlier decision, make the supersession explicit rather than guessing;
- stop questioning as soon as Goal, positive scope, material constraints and acceptance are sufficient for the next route.

This dialogue does not add a new readiness state. It resolves ambiguity before the existing `READY | RESEARCH_NEEDED | HUMAN_DECISION_NEEDED | EXPLORATION` result.

## Framing output

Allowed readiness results: `READY`, `RESEARCH_NEEDED`, `HUMAN_DECISION_NEEDED`, `EXPLORATION`.

If discussion resolves the need without implementation, STOP instead of manufacturing a coding task.

For framed work, preserve only materially applicable fields:

```text
RawIntentHandle:
DesiredOutcome:
ObservedProblem:
UserSuggestedMechanism:
Scope:
MaterialConstraints:
DoNotTouch: <optional material exception only>
AcceptanceChecks:
MaterialUnknowns:
ReadinessState:
NextRoute:
```

`UserSuggestedMechanism` is non-authoritative until current project/source evidence supports it or explicit product/architecture authority freezes it.

Exact implementation files/objects are not universally required at intake.

## Research routing

Framing does not perform generic research.

One cheap material technical fact is checked automatically through bounded `1c-ai-source-first-research`; do not ask the Human Owner merely whether to research. Genuinely broad/high-impact named uncertainty routes to Coordinator-owned `1c-ai-deep-research`.

Ask the Human Owner only when a real product/architecture/data/safety/acceptance choice remains, or when explicit authority is needed to freeze an uncertain route.

Research returns to Coordinator/intake for the durable decision/task.

## Raw intent and continuity

For noisy/raw input that proceeds toward implementation:

```text
raw input
-> durable authorized RawIntentHandle
-> compact framed result
-> durable Task Contract
-> executor
```

Do not keep the only raw intent in ephemeral provider chat memory. Do not delete the only original after normalization. Do not send the whole raw transcript/history to Local Main by default. Re-open raw input only for a concrete omission/contradiction.

Git/GitHub is the recommended/default durable path for Git-backed projects. Explicitly Gitless projects reuse their accepted degraded durable-state contract without claiming Git-equivalent provenance.

## Human decision

Explicit Human Owner confirmation is required only when framing/research materially changed behavior, selected among materially different product/architecture/safety/data choices, inferred important acceptance semantics, or needs destructive/user-affecting authority.

A clear low-risk ready task does not require a ceremonial round trip.

## Exploration

`EXPLORATION` may use loose/provisional interaction but has no production-readiness or acceptance claim. Exploratory code cannot silently graduate into accepted project code; it must pass normal readiness, source, review, verification and acceptance.

## Communication

Agent-to-agent/machine packets: compact technical English with exact handles.
Human-facing output: concise plain Russian by default; expand technical detail only when requested or materially required.

Large technical contracts/reports belong in durable state and are referenced by handle instead of pasted repeatedly into human chat.

## Invariants

- already-ready task bypasses framing;
- no research without a material UNKNOWN;
- framing never implements;
- readiness is based on observable contract facts, not model confidence;
- raw intent is retained by durable authorized handle when normalization is material;
- critical state does not depend on one chat/provider memory;
- missing proof remains `UNKNOWN`.