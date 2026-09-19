---
name: 1c-ai-focused-review
description: Perform the Local Main review or critic pass for one bounded implementation diff, commit, or pull request. Use before merge, after a correction, or for adversarial technical review without reopening unrelated product/architecture decisions.
compatibility: Requires the 1c-ai-development core/router files to be available at the documented repository paths.
---

# Focused Review

## Role

**Primary owner: Local Main.** Normally this is a distinct review/critic pass of the same Local Main; an independent bounded critic may be delegated when useful or required. Technical review evidence does not replace Coordinator/Human acceptance.

## Required core

Read only what the review needs:

- `.1c-ai/core/ORCHESTRATION.md`
- `.1c-ai/core/TASK_CONTRACT.md`
- `.1c-ai/core/SOURCE_FIRST.md`
- `.1c-ai/core/EVIDENCE_MODEL.md`
- `.1c-ai/core/STOP_ASK.md`

Use the selected execution profile when the diff depends on profile-specific invariants.

## Preflight

Resolve the exact task packet and exact reviewed commit/diff/PR.

This skill is normally a distinct **mode/pass of Local Main**, not a mandatory separate reviewer agent.

Self-review and self-critique remain valid technical review inputs, but they do not satisfy the independent final acceptance/promotion boundary when the same physical actor authored a material change. That boundary is owned by `ORCHESTRATION.md`.

## Reviewer mode

1. Check scope against the Task Contract.
2. Check material implementation choices against the bounded source packet.
3. Check correctness, compatibility, safety, and evidence claims.
4. Look for duplicated ownership, hidden scope expansion, and unproven assumptions.
5. Produce actionable correction findings or PASS.

## Critic mode

Use for material/high-risk/architecture/process changes:

1. challenge assumptions and missing evidence;
2. look for simpler proven mechanisms;
3. look for hidden coupling and authority inversion;
4. check whether token/context shortcuts damaged correctness;
5. optionally delegate one bounded independent critique when added independence is useful.

## Completion

Return `PASS` when no material defect remains, or exact findings with evidence and acceptance delta.

Local Main remains integration owner. An optional critic subagent is evidence input, not the final local verdict.
