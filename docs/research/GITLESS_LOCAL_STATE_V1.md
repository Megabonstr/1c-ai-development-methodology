# Gitless Local Durable State V1

> **СТАТУС: ДИЗАЙН / НЕ РЕАЛИЗОВАНО**
>
> Этот документ фиксирует исследование и выбранную схему возможного долговременного состояния для проектов без Git. Встроенный рабочий механизм записи/блокировок/восстановления/снимков в пакет **пока не поставляется**. Реализация отслеживается в [public Issue #1](https://github.com/Megabonstr/1c-ai-development-methodology/issues/1). Не используйте этот документ как инструкцию к уже существующей функции.

Date: 2026-09-18  
Status: frozen research decision / documentation-only  Repository baseline: historical prototype checkpoint (not required for public use)  ## 1. Scope

This artifact records the frozen research decision for the **Gitless compatibility fallback** from the private prototype phase.

The recommended/default methodology remains:

```text
Git repository
+ durable Issue/task tracker
+ exact commit/SHA
+ PR/review/CI evidence when applicable
```

Gitless mode is explicitly **not recommended** and is not Git-equivalent. It exists only for projects that deliberately operate without Git and without a durable remote task tracker.

This document does not define implementation code, scripts, a database schema, runtime dependencies, or new core policy. It consolidates the accepted research only.

Research inputs:

- private prototype research and synthesis records (not required for public use);
- the accepted conclusions are preserved self-contained in this document.

## 2. FACT

### 2.1 Current project contracts that the fallback must preserve

The current accepted repository already requires:

- project-owned state/knowledge outside installer-managed `.1c-ai/**` and `.agents/skills/1c-ai-*/**`;
- optional `PROJECT_AI.md` as a compact project-owned context/index owner rather than a growing history file;
- one explicit `CoordinationScope`;
- exactly one `OwningCoordinator` for an active task ownership boundary;
- one Local Main for bounded implementation/integration;
- one writer for each overlapping mutable scope;
- bounded context loading rather than whole-history preload;
- evidence classes kept separate;
- evidence bound to the strongest source/artifact identity actually available;
- missing proof represented as `UNKNOWN`.

Exact accepted owner handles at the research baseline:

- PROJECT_STRUCTURE: [current owner](../../.1c-ai/core/PROJECT_STRUCTURE.md)
- ORCHESTRATION: [current owner](../../.1c-ai/core/ORCHESTRATION.md)
- TASK_CONTRACT: [current owner](../../.1c-ai/core/TASK_CONTRACT.md)
- TOKEN_DIET: [current owner](../../.1c-ai/core/TOKEN_DIET.md)
- EVIDENCE_MODEL: [current owner](../../.1c-ai/core/EVIDENCE_MODEL.md)

### 2.2 Local file-based state is a practical pattern

The bounded donor research confirms that local project files can carry planning/task state even when no external task tracker is configured.

Pinned donor:

`vandalsvq/edt1c-ai-template @ db6809f375e70750f5ee582f00a83b01aac5e3c0`

Exact handles:

- transient planning boundary: https://github.com/vandalsvq/edt1c-ai-template/blob/db6809f375e70750f5ee582f00a83b01aac5e3c0/planning/README.md
- project initialization and explicit "нет трекера" path: https://github.com/vandalsvq/edt1c-ai-template/blob/db6809f375e70750f5ee582f00a83b01aac5e3c0/docs/project-init.md

This proves practicality of local file-backed task/planning state. It does not by itself prove the final storage model chosen here.

### 2.3 File replacement primitives exist, but durability is environment-sensitive

The file research identified platform primitives suitable for a same-filesystem temp-write + replace design:

- POSIX directory-operation atomicity/serialization context:
  https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html
- POSIX `rename()`:
  https://pubs.opengroup.org/onlinepubs/9799919799/functions/rename.html
- Windows `ReplaceFileW`:
  https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-replacefilew
- Windows `MoveFileEx`:
  https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-movefileexa

These sources support the design direction. They do **not** prove identical flush/crash-durability semantics on every filesystem, network share, cloud-sync folder, or future runtime wrapper.

### 2.4 SQLite has stronger built-in multi-entity transaction semantics

SQLite research establishes that:

- SQLite transactions are atomic across related updates:
  https://sqlite.org/atomiccommit.html
  https://sqlite.org/lang_transaction.html
- SQLite remains single-writer:
  https://sqlite.org/lockingv3.html
  https://sqlite.org/isolation.html
- WAL improves reader/writer concurrency but still permits only one writer and introduces persistent `-wal` / `-shm` operational state:
  https://sqlite.org/wal.html
- SQLite is a portable application-file format:
  https://sqlite.org/onefile.html
  https://sqlite.org/appfileformat.html
- consistent live backup requires SQLite-aware mechanisms:
  https://sqlite.org/backup.html
  https://sqlite.org/lang_vacuum.html
- unsafe copying/corruption risks are documented:
  https://sqlite.org/howtocorrupt.html
- integrity checking and salvage/recovery are available but recovery is not certainty:
  https://sqlite.org/pragma.html#pragma_integrity_check
  https://sqlite.org/recovery.html

Therefore SQLite is technically stronger than independent mutable files for atomic multi-record commits.

## 3. INFERENCE

### 3.1 A files-only store is coherent only if it behaves as a small event store

A folder of free-form Markdown notes would not provide the required state/revision/recovery semantics.

The coherent file-backed model is:

- append-only structured transition history;
- deterministic materialized projections;
- one writer;
- monotonic IDs/revisions;
- stale-revision STOP;
- explicit replay/recovery;
- derived human summaries;
- independent versioned backups.

### 3.2 Cross-file atomicity is not required if only the transition log is authoritative

The critical refinement from the Coordinator synthesis is to avoid treating several mutable files as independently canonical.

If one valid journal event is canonical and task/state files are materialized projections, then a crash between:

```text
journal append
-> task projection rewrite
-> STATE projection rewrite
```

does not require pretending the whole file set committed atomically.

Instead, startup detects that the canonical journal is ahead and deterministically replays/rebuilds the projections.

This does not make files as transactionally robust as SQLite. It changes the truth model so file projection rewrites are recoverable rather than co-canonical.

### 3.3 Dual-canonical hybrid storage is unsafe

Two independently writable canonical representations would create split-brain state.

A hybrid is acceptable only when one representation is canonical and every other representation is a replaceable projection/export.

For V1, there is only one canonical backend: the file-backed event store.

## 4. DECISION

For **Gitless V1**, use a **file-backed append-only event store as the single canonical fallback backend**.

This is a portability decision.

The fallback is intended for users who deliberately reject Git/GitHub and should require only the minimum common capability available to adopting agents/projects: bounded local file read/write.

SQLite has stronger transactions, but making SQLite mandatory would introduce another runtime/binding/CLI dependency whose uniform availability has not been proven for the future implementation environment.

SQLite is therefore retained as strong research evidence and a possible future V2/profile, not as a second V1 backend.

## 5. Frozen V1 candidate layout

Project-owned state stays outside installer-managed `.1c-ai/**`.

```text
PROJECT_AI.md

.project-ai-state/
  STATE.json
  journal.jsonl

  tasks/
    <TaskID>.json

  daily/
    YYYY-MM-DD.md

  snapshots/
    <SourceSnapshotID>.manifest.json

  backups/
    <BackupID>.manifest.json

  recovery/
    ...

  .writer.lock
```

`.project-ai-state/` is the frozen V1 candidate root for the research artifact and follow-up implementation unless implementation preflight identifies a concrete collision/problem.

`.writer.lock` is runtime coordination metadata only. It is not historical truth and not evidence by itself.

## 6. Canonical vs derived ownership

### Canonical transition/history truth

`journal.jsonl`

- append-only by default;
- one complete structured event per line;
- global chronological transition history;
- every state-changing event carries enough bounded structured delta to reconstruct affected current projections;
- no full chat transcripts;
- no proprietary source dumps.

### Canonical immutable evidence artifacts

`snapshots/<SourceSnapshotID>.manifest.json`  
`backups/<BackupID>.manifest.json`

These are immutable evidence manifests referenced by journal events.

### Materialized current-state projection

`STATE.json`

Purpose:

- small first-read snapshot;
- current `StateRevision`;
- accepted source snapshot;
- `LastEventID`;
- active task IDs;
- material UNKNOWNs;
- knowledge/source indexes;
- last daily/backup checkpoint.

It is not a historical log.

### Materialized task projections

`tasks/<TaskID>.json`

Each task record separates:

- requested goal/constraints/acceptance;
- actions actually taken;
- changed targets;
- checks/evidence;
- result;
- remaining UNKNOWNs;
- next action.

If a task projection conflicts with a valid canonical journal sequence, the projection is rebuilt from the journal.

### Derived human view

`daily/YYYY-MM-DD.md`

The daily Markdown is generated from durable records and is not a second source of truth.

If missing or damaged, it may be regenerated.

### Recovery evidence

`recovery/**`

Damaged tails, uncertain temp files, or other recovery artifacts are quarantined evidence. They are never silently promoted to canonical truth.

## 7. IDs and revision semantics

Freeze these V1 identities:

### EventID

- one global monotonically increasing sequence;
- immutable after append;
- every valid journal event has exactly one `EventID`;
- `PrevEventID` makes ordering/gaps explicit.

### TaskID

- immutable stable identifier;
- independent of mutable task title;
- allocated once under the single-writer boundary.

### StateRevision

- each state-changing journal event carries:
  - `BaseStateRevision`;
  - `TargetStateRevision`;
- journal-event `TargetStateRevision` is the canonical logical transition revision;
- `STATE.StateRevision` is the materialized-through projection cursor/revision;
- `STATE.LastEventID` identifies the canonical journal event through which STATE is known to be materialized;
- before normal mutation, the writer must verify the canonical journal tail against both `STATE.LastEventID` and `STATE.StateRevision`;
- if the journal is ahead or inconsistent, normal mutation STOPs until the existing recovery/replay path reconciles projections and the repaired STATE + journal tail are re-read;
- only after journal/STATE consistency is proven does the writer compare caller `ExpectedStateRevision`;
- stale `ExpectedStateRevision` means STOP/re-read/recover;
- no silent overwrite, EventID reuse, or transition-revision fork.

## 8. Bounded startup/read path

Normal startup:

```text
PROJECT_AI.md
-> STATE.json
-> bounded journal tail around/after STATE.LastEventID
-> recovery if journal is ahead/inconsistent
-> exact active task record(s)
-> current/previous daily summary only when useful
-> exact source/evidence handles needed for the current decision
```

Rules:

- never load the full journal/history into model context on routine startup;
- normal journal-tail boundary is cursor/revision driven;
- no arbitrary fixed "last N events" is frozen;
- if `STATE.LastEventID` cannot be resolved from a bounded physical tail, use a mechanical recovery/search path rather than expanding model context indiscriminately;
- task-history questions should retrieve/filter only the exact `TaskID` slice needed.

This preserves the existing Token Diet contract.

## 9. V1 write order

Under exclusive writer ownership:

```text
1. acquire exclusive writer ownership
2. read STATE
3. inspect/verify the canonical journal tail against STATE.LastEventID + STATE.StateRevision
4. if journal is ahead or otherwise inconsistent:
   STOP normal mutation
   -> run the existing recovery/replay path
   -> rebuild/reconcile affected projections
   -> re-read repaired STATE + verified journal tail
5. after consistency is proven, compare caller ExpectedStateRevision
6. allocate next EventID from the verified canonical journal tail
   and allocate the next canonical logical TargetStateRevision
7. append one complete recoverable JSONL event
8. flush/sync using the implementation/runtime primitive proven by follow-up preflight
9. rewrite affected task projection via same-filesystem temp + supported replace
10. rewrite STATE.json LAST via temp + supported replace
11. regenerate/update daily Markdown when material
12. release writer ownership
```

Why `STATE.json` is written last:

- `STATE.LastEventID` states the canonical journal event through which STATE is materialized;
- `STATE.StateRevision` states the corresponding materialized-through logical transition revision;
- if a flushed canonical journal event is ahead after a crash, the next writer must recover/replay and re-read before allocating another EventID/revision;
- allocation therefore comes from the verified canonical journal tail, never from stale STATE alone;
- a stale writer cannot legitimately advance the projection when caller revision validation fails.

Implementation must prove exact append/flush/lock/replace behavior for the chosen runtime and target filesystem. This research artifact does not select those APIs.

## 10. One-writer / multi-reader boundary

V1 freezes:

- one logical writer owns `.project-ai-state/` at a time;
- multiple readers are allowed;
- delegated agents must not independently append/mutate shared canonical state;
- stale revision must STOP rather than overwrite;
- a lock file timestamp/PID alone is not proof that another writer is safely dead;
- exact file-lock/stale-lock mechanics remain implementation UNKNOWNs.

This is intentionally conservative and does not claim safe multi-writer semantics.

## 11. Recovery semantics

### 11.1 Truncated/incomplete final journal record

If only the final JSONL record is incomplete/invalid:

1. preserve the raw damaged tail under `recovery/`;
2. truncate only back to the last complete valid event;
3. compare last valid `EventID` / revision against projections;
4. rebuild/reconcile projections from valid history or a known-good backup;
5. append `RECOVERY` only after consistency is restored.

### 11.2 Invalid record in the middle

STOP.

Do not silently skip a middle record because later history may depend on it.

### 11.3 Valid journal ahead of STATE/tasks

STOP normal mutation.

Replay valid events in order and rebuild affected projections.

Normal writes may resume only after repaired `STATE.LastEventID` / `STATE.StateRevision` are consistent with the verified canonical journal tail and both STATE and tail have been re-read under writer ownership.

### 11.4 STATE ahead of valid journal

Do not invent missing history.

Restore from a known-good independent backup when possible. Otherwise mark the affected interval/history `UNKNOWN` and require a recovery decision.

### 11.5 Damaged task/STATE projection

Reconstruct from the valid canonical journal whenever possible.

### 11.6 Missing daily Markdown

Regenerate from durable records. This is not canonical state loss.

### 11.7 Orphan temp file

Accept it only if its revision/content can be validated against canonical journal history. Otherwise quarantine/remove it during recovery.

## 12. Source snapshot identity and evidence limits

Without Git there is no commit SHA.

A Gitless source snapshot may use an immutable file-tree manifest containing:

```text
SourceSnapshotID
CapturedAt
SourceRoot
relative path
size
cryptographic content hash
Exclusions
ManifestDigest
ArtifactHandle?
```

Exact hashing, path normalization, exclusions, and canonical manifest serialization are implementation/preflight decisions.

A source snapshot proves only a captured tree fingerprint.

It does **not** prove:

- authorship;
- branch ancestry;
- merge history;
- review history;
- Git-equivalent provenance.

If no reliable snapshot/fingerprint exists:

```text
AcceptedSourceSnapshot = UNVERSIONED_CURRENT_STATE
```

and commit-level reproducibility remains `UNKNOWN`.

Existing evidence classes degrade truthfully:

- `SOURCE` may point to exact path + Gitless snapshot/fingerprint;
- `STATIC / TEST / BUILD / DEPLOY / RUNTIME / NATIVE` may be bound only to the source snapshot identity actually available;
- backup existence does not prove runtime/native behavior;
- local log text alone does not prove an external action happened.

## 13. Daily summary and daily close

The derived daily Markdown should answer quickly:

- tasks touched/completed;
- material decisions;
- checks/evidence;
- blockers/UNKNOWNs;
- source snapshots;
- next action.

A daily-close operation may:

```text
1. summarize durable events for the calendar day
2. append DAY_CLOSED
3. update STATE.LastDailyLog
4. generate daily/YYYY-MM-DD.md from durable records
5. optionally create source snapshot and/or independent backup checkpoint
6. record BACKUP only after the external/versioned artifact identity exists
```

The global journal remains append-only in V1. Daily close does not delete/compact canonical history.

## 14. Backup model

Minimum Gitless durability:

```text
active local project/state
+
independent versioned backup/snapshot
```

At a consistency checkpoint:

1. quiesce the state writer;
2. verify current revision and journal tail;
3. create a versioned archive/export of the durable state root;
4. optionally create a separately controlled source snapshot/archive;
5. bind the backup manifest to:
   - `StateRevision`;
   - `LastEventID`;
   - `SourceSnapshotID`;
   - artifact hashes;
6. append/record `BACKUP` only after the backup artifact exists and its identity is known.

The active state directory should not be treated as safely backed up merely because it is inside a continuously synchronized folder.

Network/SMB/cloud-sync active-store durability remains `UNKNOWN` until specifically proven.

Credentials, tokens, private keys, database credentials, and unnecessary client personal data must not be copied into generic state logs/manifests.

## 15. SQLite disposition

### FACT

SQLite provides materially stronger built-in transaction/atomicity semantics for updates that would otherwise touch several file projections.

It also provides efficient indexed queries and explicit database-aware backup/recovery tools.

### DECISION

Do **not** make SQLite mandatory in Gitless V1.

Do **not** implement a second SQLite backend alongside the file backend.

Do **not** introduce a WAL/default DB profile in V1.

Reason:

- Gitless mode exists primarily for portability and minimum infrastructure;
- future implementation language/runtime is not yet selected;
- availability of a uniform SQLite binding/CLI across all intended adopting environments is not yet proven;
- the accepted file event-store truth model makes projection failure recoverable without pretending cross-file rewrites are atomic.

This is not a claim that file storage is more robust than SQLite transactions.

### Revisit SQLite only after concrete dogfood evidence

A future V2/profile may revisit SQLite if one or more of these become material:

- file recovery protocol is too error-prone;
- journal/task querying becomes materially expensive;
- locking/concurrency pressure exceeds the one-writer design;
- a future installer/runtime proves SQLite availability uniformly enough to justify the dependency.

If SQLite is revisited, the research already establishes that one writer remains the correct baseline and that WAL should not be enabled merely by default without measured need.

## 16. Migration to Git/GitHub later

The fallback must not trap the project.

Migration path:

```text
quiesce local writer
-> final daily close + independent backup
-> final SourceSnapshotID
-> initialize Git
-> create first accepted source commit
-> record mapping SourceSnapshotID -> first Git SHA
-> optionally create/import Issues only for active/material tasks
-> retain .project-ai-state as read-only historical evidence/archive
-> switch PROJECT_AI/task/source authority to Git/GitHub
```

Do not rewrite old local events into fabricated Git commits.

The historical local journal remains evidence of the pre-Git period; future canonical task/source transport becomes normal Git/GitHub state.

## 17. UNKNOWN

The following are intentionally unresolved and belong to bounded implementation/preflight:

1. exact cross-platform runtime/API for append, durable flush/sync, file lock, temp write, and replace;
2. exact stale-lock detection/recovery primitive;
3. exact source-manifest path normalization, exclusions, canonical serialization, and hash rules;
4. retention policy for canonical journal, recovery artifacts, source snapshots, and backups;
5. active-store semantics on network shares, SMB, cloud-sync folders, or other non-local filesystems;
6. whether any generated human export beyond `daily/YYYY-MM-DD.md` is worth implementing;
7. exact physical field serialization/versioning details for future JSON records.

These UNKNOWNs do not change the frozen research architecture and must not be guessed by this documentation task.

## 18. Research verdict

**PASS - architecture frozen for follow-up implementation design.**

Git/GitHub remains the preferred/default methodology.

For the intentionally degraded Gitless compatibility mode, V1 uses one project-owned file-backed append-only event store:

- `journal.jsonl` = canonical transition history;
- immutable snapshot/backup manifests = canonical evidence artifacts;
- `STATE.json` and task JSON = replayable materialized projections;
- daily Markdown = derived human view;
- one writer / multiple readers;
- stale revision = STOP;
- bounded startup by cursor/task, not whole-history preload;
- recovery preserves damaged/uncertain evidence and never invents missing history;
- independent versioned backup is required for meaningful durability;
- SQLite is documented as transactionally stronger but deferred unless dogfood proves the file backend insufficient;
- later migration to Git preserves local history as historical evidence without fabricating Git ancestry.
