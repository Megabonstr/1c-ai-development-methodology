# STOP and ASK

The executor should continue independently through bounded technical work, but must not invent a material decision that belongs to the task owner.

## ASK

Ask one short, concrete question when user intent can resolve a material ambiguity, for example:

- multiple plausible product or semantic behaviors;
- a destructive action has more than one valid scope;
- the requested UX/business meaning is not determined by source;
- acceptance depends on a preference rather than a technical fact.

Offer a small set of options only when it helps the decision.

## Investigate before asking

Do not ask the user for a fact that can be obtained cheaply and safely from:

- the exact project source;
- the assigned source packet;
- the selected tool/profile;
- focused runtime evidence.

Technical uncertainty should be reduced before escalating a product decision.

## STOP

Stop the affected write/delivery path when:

- actual source contradicts the frozen Task Contract;
- repository/base/target/writer ownership cannot be resolved safely;
- a required source remains unavailable after bounded expansion;
- a destructive or user-affecting action lacks authority;
- required evidence fails and the next correction would change the accepted mechanism or scope;
- provenance/license constraints make the proposed reuse unsafe.

Return the first material blocker or `UNKNOWN`, exact evidence handle, and the smallest next decision/action.

## Do not over-stop

Routine low-level implementation choices that preserve the frozen contract do not require Coordinator Main or user approval.

Ordinary compile errors, metadata mismatches, test failures, debugger findings, small refactors, and local rewrites inside frozen semantics are Local Main correction-loop work, not escalation triggers.

Do not turn every missing detail into a blocker when the exact source/tool/runtime can resolve it safely.

Do not create Coordinator Main <-> Local Main ping-pong for technical micro-decisions. Return upward only for a material semantic/product/architecture/safety/authority/acceptance boundary described above.
