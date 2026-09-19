# Repository model

Status: current architecture.

## Layering

```text
Human Owner + Coordinator Main
        |
durable Task Contract / exact task-state handle
        |
   one Local Main
        |
 canonical core + orchestration
        |
     compact router
   +---------+---------+----------------+
   |         |         |                |
workflow  execution  optional bounded subagent
intent    profile    Researcher / Quick Fixer /
   |         |       Docs / Test-Log / specialist
 skill    upstream
   +---------+---------+----------------+
             |
      Local Main implementation
      review / critic / integration
             |
     build / deploy / runtime
             |
        local verdict
             |
Coordinator Main + Human acceptance
```

Writer / Reviewer / Critic / Integrator are operating modes of the same Local Main.

Coordinator Main is a logical provider-neutral role for one explicit `CoordinationScope`; it may be cloud-hosted or local. Each active task has exactly one `OwningCoordinator`. Scope ownership means durable context/index/decision responsibility, not full-scope preload.

## 1. Human-facing layer

Russian-first documentation explains methodology, setup, examples, limitations, and adoption.

It is not a machine policy owner.

## 2. Client adapters

`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and Copilot instructions are thin adapters to the canonical machine entry.

They must not become parallel copies of policy.

## 3. Tool-neutral core

Owns process invariants independent of execution technology:

- Task Contract and scope;
- Coordinator Main / Local Main authority;
- Local Main modes and bounded subagents;
- delegation/write ownership;
- durable task-state / handoff / evidence contracts;
- source-first;
- token discipline;
- evidence;
- review/verification/acceptance;
- STOP/ASK.

## 4. Orchestration

`.1c-ai/core/ORCHESTRATION.md` is the single owner for:

- Human Owner / Coordinator Main / Local Main boundary;
- CoordinationScope / OwningCoordinator authority;
- cloud/local/manual-compatible Coordinator Main placement;
- Writer/Reviewer/Critic/Integrator as Local Main modes;
- bounded specialist subagents;
- delegation/result packets;
- default read-only child permission;
- Quick Fixer exact write exception;
- parallel ownership and integration responsibility.

Other files reference this owner instead of redefining orchestration.

## 5. Router and generic skills

The router resolves workflow intent, execution profile, and optional bounded delegation.

Generic skills package repeatable workflows but do not replace core owners.

## 6. Execution profiles

Accepted first-class profiles:

- `.1c-ai/profiles/1c-edt-mcp/PROFILE.md`
- `.1c-ai/profiles/1c-xml-configurator/PROFILE.md`

Hybrid remains unproven.

## 7. Source/provenance

External repositories, official docs, Infostart materials, standards, and research are evidence/reference, not silent project policy.

## Public-release boundary

Private repository is the development laboratory.

The planned public artifact is a separate clean public release after dogfooding and provenance/license/security review.
