# 1C AI Development - Router

Use this file only when the next workflow/profile/delegation route is not already fixed. Pre-install evaluation/adoption is the one route that may begin before a durable TaskHandle exists.

## 0. External methodology evaluation / adoption

When the user provides this methodology repository URL/ref and asks whether/how to use it in another project:

```text
methodology URL/ref
-> .1c-ai/core/ADOPTION.md
-> inspect adopting project read-only
-> NONE | SELECTIVE | FULL
-> state MANUAL_PINNED_COPY + exact methodology SHA
-> ask write permission
-> manual adoption only if authorized
```

Do not route this through task-bootstrap, require a pre-existing TaskHandle, or invent installer/update/uninstall behavior.

The router does not create `CoordinationScope`, `OwningCoordinator`, product semantics, or acceptance meaning. Those belong to Coordinator Main / the durable Task Contract.

Role separation is logical. One physical agent may act sequentially as Coordinator Main and Local Main when appropriate; a new chat/agent is not required for small work.

## 1. Coordinator Main - pre-execution

Coordinator Main owns intake/readiness, semantic task state, material decision research, Human Owner decisions, and freezing/correcting the durable Task Contract.

| Coordinator intent | Generic skill / owner | Core authority |
|---|---|---|
| Normalize raw/noisy/materially unclear human intent and decide readiness | `.agents/skills/1c-ai-task-framing/SKILL.md` | Task Intake + Orchestration + Token Diet |
| Resolve one bounded fact that blocks a Coordinator decision | `.agents/skills/1c-ai-source-first-research/SKILL.md` - Coordinator-decision mode | Source First + Orchestration |
| Run broad multi-source architecture/product/technology research | `.agents/skills/1c-ai-deep-research/SKILL.md` - Coordinator primary / Researcher delegated | Source First + Token Diet + Evidence Model + Orchestration |
| Resolve adopting-project instruction/knowledge ownership or initialization layout | no separate skill | Project Structure + Task Contract |
| Freeze/correct task semantics or route a material Human Owner decision | no separate skill | Task Contract + Orchestration + STOP/ASK |

Cheap technical facts are checked automatically. Do not ask the Human Owner whether to research when one bounded lookup can resolve the fact. Ask only when a real product/architecture/data/safety/acceptance choice or explicit authority remains.

## 2. Handoff boundary - Local Main ingress

A materially ready task crosses the boundary as an exact durable TaskHandle plus exact handles/material execution fields.

| Ingress intent | Generic skill | Core authority |
|---|---|---|
| Validate/open an already Coordinator-frozen task for execution | `.agents/skills/1c-ai-task-bootstrap/SKILL.md` | Task Contract + Orchestration + Token Diet (+ Git/GitHub Flow when Git-backed) |

Task bootstrap may resolve/verify execution facts. It must not silently create or change Coordinator-owned product/architecture/data/safety/acceptance semantics.

## 3. Local Main - execution

Local Main owns technical execution inside the frozen Task Contract and remains integration owner for implementation-side work.

| Local execution intent | Generic skill | Core authority |
|---|---|---|
| Resolve one bounded technical implementation fact without changing task semantics | `.agents/skills/1c-ai-source-first-research/SKILL.md` - Local-technical mode | Source First + Orchestration |
| Make one bounded change | `.agents/skills/1c-ai-bounded-implementation/SKILL.md` | Task Contract + Orchestration + Source First + Delivery Discipline |
| Review/critique the bounded implementation | `.agents/skills/1c-ai-focused-review/SKILL.md` | Orchestration + Task Contract + Evidence Model |
| Coordinate/run required verification gates | `.agents/skills/1c-ai-focused-verification/SKILL.md` | Orchestration + Evidence Model + Verification Profiles |
| Prove physical local build/deploy/runtime/native behavior | `.agents/skills/1c-ai-local-runtime-validation/SKILL.md` | Orchestration + Evidence Model + selected profile |
| Task scope/complexity is expanding beyond the business goal | no separate skill | Delivery Discipline |
| Current source/runtime contradicts frozen semantics or authority | stop Local execution and escalate | STOP/ASK + Orchestration |

If Local Main discovers a genuine need for broad V1/V2/V3 research, it pauses execution and escalates to Coordinator Main. It does not make `1c-ai-deep-research` its primary execution workflow.

## 4. Execution profile

Resolve a profile only when execution-specific source, mutation, build, deploy, runtime, or native behavior matters.

| Authoritative project route | Profile |
|---|---|
| 1C:EDT project + structured EDT/MCP execution | `.1c-ai/profiles/1c-edt-mcp/PROFILE.md` |
| XML source tree + 1C Configurator/CLI execution | `.1c-ai/profiles/1c-xml-configurator/PROFILE.md` |
| Tool-neutral policy/docs/research | no execution profile |
| Mixed or unclear source ownership | resolve explicitly; do not guess hybrid |

Do not select a profile from tool availability alone.

## 5. Shared transport and specialist delegation

`1c-ai-github-handoff` is a **shared Git-backed transport utility**, not a workflow intent. Use it only when exact state must cross Coordinator/Local/specialist contexts through GitHub. Gitless work requires an already operational project-supplied durable carrier; this package does not provide that backend.

Coordinator Main or Local Main may delegate a bounded specialist task when useful.

| Bounded need | Specialist |
|---|---|
| exact search/probe/source comparison | Researcher / Scout |
| exact trivial localized code change with frozen mechanism | Quick Fixer |
| bounded documentation reading/writing | Documentation worker |
| focused tests/runtime/log/data evidence | Test / Runtime / Log worker |
| another exact specialist task | bounded specialist |

Rules:
- no delegation ceremony when the owning role can do the task cheaply;
- subagents are read-only by default;
- Quick Fixer writes only an exact isolated scope explicitly assigned by Local Main;
- Local Main reviews/integrates delegated implementation writes;
- use the fresh packet/result contract from `.1c-ai/core/ORCHESTRATION.md`.

## 6. Coordinator Main - post-execution

After Local Main returns the final local verdict/evidence and required acceptance is satisfied, Coordinator Main owns finalization.

| Coordinator intent | Generic skill | Core authority |
|---|---|---|
| Persist one accepted durable closeout and emit the concise human result | `.agents/skills/1c-ai-task-closeout/SKILL.md` | Orchestration + Evidence Model + Delivery Discipline + Token Diet |

Closeout consumes exact evidence/acceptance/final-identity handles. It does not rerun verification or create evidence.

## 7. Compose the lifecycle route

Raw/unclear request:

```text
Human Owner
-> Coordinator Main
   -> Task Intake / framing only when needed
   -> bounded or deep research only when a material decision needs it
   -> frozen durable Task Contract
-> handoff
```

Ready task / Local execution:

```text
exact frozen TaskHandle
-> Local Main task-bootstrap
-> zero/one primary execution skill
-> zero/one execution profile when needed
-> optional bounded specialist
-> review / verification / runtime evidence
-> Local Main verdict + exact result/evidence
-> Coordinator Main
```

Post-execution:

```text
Coordinator Main
-> evidence review / required acceptance
-> promotion/delivery when required
-> final accepted/delivered identity
-> 1c-ai-task-closeout
-> one durable closeout + concise human result
-> task close
```

## Boundaries

- Do not route raw intent directly into Local Main execution.
- Do not make task framing or deep research Local Main primary workflows.
- Do not make GitHub handoff a workflow intent.
- Do not load both execution profiles by default.
- Do not load several generic skills when one intent is sufficient.
- Do not route one API/signature/version lookup or ordinary implementation defect into deep research.
- Do not turn logical roles into mandatory separate agents/chats.
- Do not delegate without a bounded goal/handles/permission/STOP.
- Local Main receives the executable task, not the process/history that created it.
