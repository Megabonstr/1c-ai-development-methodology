# Coordinator Main Portability V1

> Public-release note: references to numbered prototype research tasks were converted to descriptive historical labels. They are provenance only and are not required to use this methodology.

Date: 2026-09-18  
Status: RESEARCH-002 recommendation / research-only  
Repository baseline: `a1fd406f58369c22e2aadc195acf5d5ee418471c`

## 1. Problem

The accepted orchestration semantics are sound, but the canonical upper role is named `Cloud Main`.

That name accidentally binds a logical responsibility to one physical placement:

- persistent cloud chat;
- provider-hosted session;
- provider-specific GitHub connector;
- optional cloud/local bridge.

Those capabilities are useful, but none of them is required to preserve the actual architecture:

```text
Human Owner
-> upper project/scope coordination authority
-> durable GitHub Task Contract
-> one Local Main
-> bounded specialist subagents
```

The reusable methodology must survive the absence or loss of any cloud-specific capability.

## 2. Current accepted semantics that must remain

Current canonical owners already establish:

- Human Owner owns final product/business intent.
- One upper Main owns product/architecture interpretation, Task Contract, material decisions, evidence review, acceptance, and delivery coordination.
- One Local Main owns the complete local implementation/integration/correction/runtime loop.
- Writer / Reviewer / Critic / Integrator are Local Main modes.
- Bounded specialist subagents are optional.
- GitHub Issue/comment + exact SHA/evidence handles are durable project state.
- Ordinary compile/test/metadata/runtime failures stay local.
- Missing evidence remains `UNKNOWN`.
- One writer owns each overlapping write scope.

The portability fix must rename/generalize the upper role, not move its authority into Local Main.

## 3. FACT

### 3.1 Local/desktop placement is technically realistic

Current provider/client documentation proves that capable coding/research agents can run against a local workspace without a persistent cloud chat:

- OpenAI Codex CLI is a coding agent that runs locally on the user's computer:
  https://github.com/openai/codex
- Cursor CLI supports local repository/file access, web access, terminal execution, plan/ask modes, and non-interactive operation:
  https://prod.cursor.com/docs/cli/using
  https://prod.cursor.com/docs/agent/tools/terminal
- Gemini CLI exposes local file tools and `run_shell_command`:
  https://geminicli.com/docs/reference/tools/
  https://geminicli.com/docs/tools/shell/
- Claude Code can be launched from a repository and is not intrinsically a cloud-chat-only workflow:
  https://support.claude.com/en/articles/14554922-claude-code-user-faq

These products differ in permissions and UX. The architecture must not depend on any one of them.

### 3.2 Provider-native GitHub connectors are not required for durable GitHub transport

GitHub CLI can read, create, and comment on Issues from a local terminal:

- view Issue/comments:
  https://cli.github.com/manual/gh_issue_view
- create Issue:
  https://cli.github.com/manual/gh_issue_create
- create Issue comment:
  https://cli.github.com/manual/gh_issue_comment

GitHub REST also supports Issue comments with repository-scoped permissions:

https://docs.github.com/en/rest/issues/comments

Therefore a coordinator with authorized shell/API access can use GitHub durable state without a provider-native cloud connector.

### 3.3 Cloud bridge capability remains provider-dependent

Accepted prototype research item 28 research already established:

- GitHub must remain durable executable state;
- notification-only cloud wake-up is sufficient as the minimal optional bridge;
- direct bidirectional cloud-chat response monitoring is provider-specific and currently not a core-proven capability;
- Local Main resumes from a new durable GitHub decision/correction, not from transient chat text.

prototype research item 28 is therefore an acceleration pattern, not a prerequisite for orchestration.

## 4. INFERENCE

### 4.1 The canonical actor is a logical role, not a host

The upper Main role can be hosted in:

- a cloud chat/session;
- a desktop/local coding agent;
- a terminal/CLI agent;
- another isolated session of the same provider;
- a human-mediated coordinator session that cannot itself write GitHub.

The durable role contract is the same.

### 4.2 "Owns the project context" must not mean "preload the whole project"

The upper Main needs **context ownership**, not unlimited resident context.

For its accepted scope it owns responsibility for:

- authoritative project/domain identity;
- architecture and product invariants;
- current accepted checkpoint;
- durable decision history;
- task boundaries and dependencies;
- knowledge/source indexes and exact handles;
- open material UNKNOWNs;
- acceptance criteria and evidence requirements.

It retrieves exact underlying files/issues/research on demand under Token Diet.

This keeps the coordinator informed without turning every session into a full-repository preload.

### 4.3 Scope must be explicit

A large project may be too broad for one practical coordination context.

Define a `CoordinationScope`.

Examples:

- whole repository/project;
- one product;
- one subsystem/domain;
- one bounded integration area;
- one release/migration program.

For each active task there is exactly one `OwningCoordinator` for its scope.

If a task crosses several peer scopes, it must either:

- move to a common parent coordination scope; or
- have one explicitly selected owning coordinator while the others act only as bounded advisors.

Do not create joint ambiguous ownership.

## 5. Architecture options

### Option A - Keep Cloud Main canonical and document fallbacks

Pros:
- smallest textual migration;
- matches the current proven workflow.

Cons:
- host placement remains encoded in the core role name;
- every non-cloud user starts as an exception;
- provider capability loss appears to break architecture even when it only breaks one transport.

Verdict: rejected. The semantic defect remains.

### Option B - Provider-neutral Coordinator Main; Cloud Main is one placement mode

Pros:
- preserves all prototype research item 22/prototype research item 26 authority semantics;
- survives provider/connector changes;
- supports cloud, desktop, CLI, and human-mediated durable transport;
- no second orchestration architecture;
- prototype research item 28 becomes an optional cloud-host automation pattern;
- prototype research item 47 can become a generic deep-research workflow.

Cons:
- requires one bounded terminology/contract migration across canonical owners and human docs.

Verdict: recommended.

### Option C - Collapse Coordinator Main into Local Main

Pros:
- simplest actor count for tiny projects;
- fewer handoffs.

Cons:
- mixes long-lived project/architecture authority with task-local implementation state;
- encourages context growth;
- weakens independent evidence/acceptance separation;
- increases risk that implementation convenience silently changes product semantics;
- breaks the accepted Local Main bounded-task model.

Verdict: rejected as canonical architecture.

A single physical agent may host both roles sequentially for a small project, but the logical role boundary still exists.

### Option D - Project Main as canonical name

Pros:
- strongly communicates project-context ownership.

Cons:
- misleading when the role owns only a subsystem/domain;
- encourages assumption that one agent must contain the entire repository;
- awkward for nested/bounded scopes.

Verdict: useful human description, weaker canonical technical name.

## 6. RECOMMENDATION

Rename the canonical upper role from `Cloud Main` to:

`Coordinator Main`

Russian human term:

`Главный координатор`

Definition:

> Coordinator Main is the provider-neutral upper coordination authority for one explicit CoordinationScope. It owns the durable project/domain context, architecture/task contracts, material decisions, evidence acceptance, and delivery coordination for that scope. It may be hosted in cloud or local/desktop environments and does not require local runtime or source-write capability.

### Required role fields

A durable project/task context should be able to resolve:

```text
CoordinationScope:
OwningCoordinator:
ProjectOrDomainIdentity:
AcceptedCheckpoint:
KnowledgeIndex:
ArchitectureInvariants:
OpenMaterialUnknowns:
DurableTaskState:
ExecutionRoute:
AcceptanceAuthority:
```

These are responsibilities/handles, not a requirement to create a new file for each field.

`PROJECT_AI.md` is the preferred project-owned index for stable project/scope context when the adopting project needs one.

## 7. Minimum Coordinator Main capability contract

### Required

The role must be able to:

1. reason across the accepted CoordinationScope;
2. resolve authoritative project/source/knowledge handles when material;
3. synthesize current facts, project invariants, research, and user intent;
4. create/freeze/correct exact Task Contracts;
5. distinguish routine Local Main correction from material STOP/ASK;
6. review exact diff/SHA/evidence handles;
7. make or route material architecture/product decisions with Human Owner;
8. accept/reject delivery against the frozen acceptance contract;
9. ensure its material decisions become durable GitHub state through an authorized transport.

### Conditionally required

- web/current research: when the task needs external/current evidence;
- repository/source read: when a material decision depends on source;
- CI/PR read: when acceptance depends on those evidence classes.

These capabilities may be direct or delegated/brokered.

### Not required by the core role

- cloud hosting;
- provider-native GitHub connector;
- direct GitHub write tool;
- source-code write access;
- local IDE/runtime/database access;
- persistent provider chat memory;
- webhook/event trigger support;
- ability to execute 1C;
- ability to edit the local implementation branch.

## 8. Supported placement modes

### A. Cloud-hosted Coordinator Main

Example:

`cloud reasoning/research session + GitHub connector`

This is the current convenient mode.

If prototype research item 28 automation exists, GitHub can wake this host after a material decision request.

### B. Local/desktop Coordinator Main

A separate local/desktop/CLI agent owns project/domain coordination while Local Main owns the bounded implementation task.

Transport may use:

- GitHub CLI;
- GitHub API;
- MCP/plugin;
- another authorized repository integration.

No cloud chat is required.

### C. Coordinator without direct GitHub write capability

The coordinator produces an exact bounded decision/task packet.

An authorized human/tool persists it into GitHub.

Only the durable GitHub form becomes executable task state.

This is the compatibility floor.

### D. Co-located physical agent

For a small project/task, one physical model/session may act sequentially as both Coordinator Main and Local Main.

Required guards:

1. declare the active logical role;
2. freeze/persist the Task Contract before implementation;
3. perform the Local Main technical loop inside that frozen contract;
4. do not use unpersisted internal reasoning as a contract mutation;
5. preserve truthful evidence classes;
6. return to Coordinator mode only for material decision/acceptance.

For high-risk or broad tasks, separate contexts are preferred because they reduce authority/context mixing.

## 9. Coordinator Main vs Local Main

| Concern | Coordinator Main | Local Main |
|---|---|---|
| Time horizon | multi-task / durable scope | one bounded task/execution context |
| Context ownership | project/domain architecture + knowledge index | exact implementation/runtime context |
| Task Contract | owns/finalizes | consumes/executes |
| Product semantics | owns with Human Owner | preserves; escalates material contradictions |
| Source code writes | optional/not required | implementation owner |
| Local runtime/IDE | not required | owns when task requires |
| Routine compile/test/debug loop | does not manage | owns autonomously |
| Final local verdict | reviews evidence | produces |
| Acceptance/merge/close coordination | owns | supplies evidence/result |
| Host | cloud/local/manual-compatible | local execution environment |

## 10. Knowledge ownership and Token Diet

Coordinator Main must know **where the truth is**, not memorize all truth.

Within its CoordinationScope it owns the knowledge map:

```text
PROJECT_AI.md
-> current accepted Git/SHA
-> exact architecture owners
-> exact reusable research/docs
-> source/provenance registry
-> exact active Issues/decisions
-> first material UNKNOWN
```

Load only the handles required for the current decision.

A long-lived coordinator may preserve continuity through durable project files/GitHub instead of relying on provider chat memory.

## 11. Durable state and downgrade path

Canonical rule:

```text
Coordinator decision
-> authorized persistence transport
-> GitHub Issue/comment/PR/commit
-> Local Main consumes exact durable state
```

If a provider capability disappears:

- cloud GitHub write unavailable -> use local GitHub CLI/API or human persistence;
- cloud chat unavailable -> move Coordinator Main to desktop/local/another provider;
- event trigger unavailable -> manual/poll notification; GitHub state is unchanged;
- connector discontinued -> replace transport, not orchestration;
- persistent chat memory unavailable -> reconstruct from PROJECT_AI/GitHub/exact handles;
- cloud source-write unavailable -> no core impact; source writes were never required for Coordinator Main.

No process redesign is required.

## 12. Relationship to prototype research item 28

Keep prototype research item 28 optional.

Rename its conceptual target after coordinator migration to:

`optional GitHub <-> cloud-hosted Coordinator Main bridge`

Minimal bridge:

- durable GitHub result/decision first;
- notification-only wake-up when `DecisionRequired=YES`;
- direct chat-response monitoring only after provider-specific smoke proof;
- dedupe/replay/stale revision safeguards.

prototype research item 28 does not define the core coordinator architecture.

## 13. Relationship to prototype research item 47

prototype research item 47 should become a generic:

`Deep multi-pass research workflow`

It may run:

- inside Coordinator Main;
- as a bounded Researcher subagent delegated by Coordinator Main;
- in a cloud research session;
- in a local/desktop agent with web/source access.

Its result returns to the `OwningCoordinator` / exact GitHub Issue, not specifically to a cloud chat.

No cloud-only dependency is justified by the current evidence.

## 14. Migration surface

A follow-up implementation Issue should atomically reconcile at least:

### Canonical machine owners / bootstrap

- `AGENT_START.txt`
- `.1c-ai/START_HERE.md`
- `.1c-ai/core/ORCHESTRATION.md`
- `.1c-ai/core/STOP_ASK.md`
- `.1c-ai/core/PROJECT_STRUCTURE.md`
- `.1c-ai/core/TOKEN_DIET.md` - state explicitly that coordination-scope ownership does not authorize full-scope preload
- `.1c-ai/router/ROUTER.md`

### Generic skills

- `.agents/skills/1c-ai-github-handoff/SKILL.md`
- `.agents/skills/1c-ai-task-bootstrap/SKILL.md`
- `.agents/skills/1c-ai-bounded-implementation/SKILL.md`
- any other generic skill containing `Cloud Main` after exact scan

### Architecture / human docs

- `docs/architecture/REPOSITORY_MODEL.md`
- `README.md`
- `docs/ru/ORCHESTRATION.md`
- `docs/ru/ARCHITECTURE.md`
- `docs/ru/SKILLS.md`
- `docs/ru/TOKEN_DIET.md` - explain the same context-ownership vs preload boundary for humans
- other human docs containing the old canonical term

### Issue contracts

- prototype research item 28 terminology/host-mode wording
- prototype research item 47 title/contract/return route

The migration must preserve `Local Main` semantics and anti-ping-pong behavior.

## 15. Strongest argument against the change

The current `Cloud Main` model already works well in this repository, gives strong context separation from local implementation, and clearly tells users where architecture/acceptance happens.

Response:

The recommendation keeps exactly that operating mode as Placement A.

The change removes only the false implication that **cloud placement is the source of authority**.

Authority comes from the role contract and CoordinationScope, not from where the model is hosted.

## 16. UNKNOWN / future validation

1. The best exact UI/bootstrap experience for selecting `CoordinationScope` in a newly adopting project is not yet implemented.
2. A fully co-located Coordinator+Local session has not yet been dogfooded on a high-risk 1C task; keep it optional and prefer separation for high-risk work.
3. Provider-specific event/bridge capabilities remain volatile and stay isolated under prototype research item 28.
4. Future installer/update work still needs to decide how it detects/preserves an existing project's coordinator/project overlay blocks.
5. Multi-coordinator large-project hierarchy is intentionally minimal in V1: exactly one OwningCoordinator per task; parent-scope escalation is allowed, but no mandatory coordinator tree is introduced.

## 17. Final decision

Adopt `Coordinator Main` as the canonical provider-neutral upper role.

Freeze these invariants:

- one Coordinator Main per active CoordinationScope/task ownership boundary;
- cloud/local/desktop/manual-compatible placement;
- context ownership means durable knowledge/index/decision responsibility, not full preload;
- GitHub remains durable task/evidence state;
- Local Main remains the autonomous local executor/integrator;
- bounded subagents remain optional;
- Cloud Main becomes only a cloud-hosted Coordinator Main placement;
- prototype research item 28 remains optional automation;
- prototype research item 47 becomes provider-neutral before implementation.
