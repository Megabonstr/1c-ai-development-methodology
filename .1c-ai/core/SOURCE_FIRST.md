# Source First

Do not invent a mechanism from model prior when a relevant current implementation, official source, proven donor, or standard already answers the material question.

Source-first means choosing the narrowest applicable source, not reading every source layer.

## Generic source order

For the material fact being decided:

1. **Current project / accepted seam** - current source, runtime, tests, and already accepted project behavior.
2. **Official framework, platform, or standard implementation** - the upstream mechanism the project is expected to follow.
3. **Pinned proven donor/reference** - a bounded external implementation or evidence snapshot with provenance.
4. **Proven community evidence** - useful when official/current sources leave a concrete gap.
5. **Custom implementation** - only after the preceding relevant sources do not provide a fitting mechanism.

A future execution profile may specialize this order for its technology, but must not weaken current-project authority or provenance rules.

## Source packet

A task should pass exact source handles instead of broad instructions to "research everything".

A source entry should contain, when applicable:

```text
RepositoryOrSource:
RefOrSHA:
PathOrURL:
SymbolSectionOrRange:
WhatItProves:
LicenseOrAccessNote:
```

Use immutable refs/SHAs for donor/reference material when practical. Use a live branch only when current-head behavior is intentionally required.

## Bounded expansion

1. Open the exact supplied handle.
2. If insufficient, open only its immediate owner/context or perform one narrow search inside the named source.
3. If the material fact is still absent, return `SOURCE_GAP`.

Do not silently substitute a different source because it is easier to access.

## Donor boundary

A donor is evidence and implementation reference.

It does not automatically:

- become project architecture;
- authorize copying;
- prove runtime compatibility;
- grant permission to mutate data or configuration;
- override current project behavior.

Material adaptation or copying requires provenance/license review.

## Review

Review a change against the same bounded sources that informed the design.

Do not perform a second broad research pass after focused acceptance succeeds unless new evidence creates a real contradiction.

## Research routing boundary

Source First is not "research everything before coding".

If the current project/source already proves the mechanism and no material blocking UNKNOWN remains, proceed with the bounded task.

One material source/mechanism UNKNOWN may route to `1c-ai-source-first-research`. Use `1c-ai-deep-research` only for genuinely broad/high-impact uncertainty. Do not reopen broad research after a concrete fact is already proven.
