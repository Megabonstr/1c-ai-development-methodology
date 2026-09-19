# Git and GitHub flow

Machine-facing canonical owner for branch lifecycle and Git/GitHub delivery when the project uses the recommended/default Git-backed route.

This file does not make GitHub a universal methodology requirement. Gitless semantics are designed/degraded, but this package does not ship a durable-state backend. Use a Gitless route only when the adopting project already supplies an operational durable task/source-state mechanism; otherwise report the durable lifecycle `UNKNOWN/BLOCKED` and do not invent Git-equivalent provenance.

## Default branch model

For this repository:

```text
main    = stable accepted state
preprod = integration / release-candidate state
feature/<task> = one bounded task from current preprod
```

Normal lifecycle:

```text
exact Issue/task
-> branch from current preprod
-> bounded implementation
-> focused task checks
-> PR feature -> preprod
-> merge after required feature gates pass
-> integration/applicable full checks on preprod
-> PR preprod -> main
-> main only when required gates are PASS or explicit NOT_REQUIRED
-> close Issue
```

Direct feature -> main is not normal delivery.

Another adopting project may override branch names only through its explicit project instructions / Task Contract. Do not silently infer a different branch model.

## Feature branch

One coherent task -> one bounded feature branch by default.

Before writes verify:

- repository/remote;
- current `preprod`;
- feature branch/HEAD;
- dirty/untracked state;
- active writer ownership.

Preserve unrelated work.

## Feature -> preprod

Merge strategy:
- squash merge is allowed/preferred when one bounded task should become one integration commit;
- keep the exact accepted feature evidence/SHA in the Issue/PR even when the resulting preprod SHA changes.

Before PR/merge:

- task scope matches the Issue/Task Contract;
- focused required gates for the changed scope are complete;
- Local Main review/critic pass is complete as required;
- exact head SHA is known;
- remaining UNKNOWNs are explicit.

The feature branch proves the task itself is ready for integration.

## Preprod

`preprod` proves integration/release-candidate quality.

Run the repository/project checks required for combined state, such as:

- mandatory CI;
- affected subsystem tests;
- build/package;
- deployment to authorized test environment;
- runtime/native critical scenarios;
- compatibility/integration checks.

Do not require every possible gate when the project contract marks it NOT_REQUIRED.

## Preprod -> main

Merge only when required integration/release gates are green and acceptance permits release.

Promotion must preserve preprod ancestry:
- use a normal merge commit;
- do NOT squash or rebase the preprod promotion;
- after the main push CI succeeds, fast-forward preprod to the accepted main SHA;
- do not force-reset or rewrite either branch to synchronize them.

This keeps the next feature based on the exact accepted main history and prevents old release diffs from replaying in later promotions.

`main` is stable accepted state, not a routine development target.

## Handoff identity

Use exact commit SHA when work crosses Coordinator Main, Local Main, subagents, CI, build, deploy, or runtime environments.

A moving branch name alone is not sufficient evidence.

## Emergency exception

Direct stable/production repair is outside normal flow.

If explicitly authorized, record the emergency task, exact change/SHA/evidence, and reconcile the change back through Git branches immediately after stabilization.

## Unsafe Git operations

No force-push, blind hard reset, broad clean, or unrelated deletion without explicit authority.

Never discard unique unmerged/unpushed work.
