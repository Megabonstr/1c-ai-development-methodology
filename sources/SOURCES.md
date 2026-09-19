# Source registry

Status: private development. This is a provenance registry, not a list of automatically accepted rules.

## Usage modes

- `REFERENCE` - read as evidence; repository content is not copied.
- `ADAPTED` - a pattern or structure is materially adapted; attribution and license compatibility must be reviewed.
- `COPIED` - text/code is copied; allowed only after explicit license/provenance review and required notices.

Default mode is `REFERENCE`.

## Project references

| Source | Role | Initial mode |
|---|---|---|
| [DitriXNew/EDT-MCP](https://github.com/DitriXNew/EDT-MCP) | EDT/MCP execution upstream; rules/skills/tool-guide layering | REFERENCE |
| [Nikolay-Shirokov/cc-1c-skills](https://github.com/Nikolay-Shirokov/cc-1c-skills) | XML/Configurator execution reference; 1C XML formats, CLI workflows and agent skills | REFERENCE |
| [1c-syntax/ssl_3_1](https://github.com/1c-syntax/ssl_3_1) | Open source view of 1C Standard Subsystems Library (BSP/SSL) for standard implementation research | REFERENCE |
| [1C-Company/v8-code-style](https://github.com/1C-Company/v8-code-style) | Official 1C EDT checks and development-standard tooling | REFERENCE |
| [Agent Skills](https://agentskills.io/) / [agentskills/agentskills](https://github.com/agentskills/agentskills) | Portable skill format/specification and progressive-disclosure reference | REFERENCE |
| [AGENTS.md](https://agents.md/) | Cross-agent repository instruction convention | REFERENCE |
| [anthropics/skills](https://github.com/anthropics/skills) | Agent Skills implementation/examples and packaging reference | REFERENCE |
| [brake71/1c-ssl-skills](https://github.com/brake71/1c-ssl-skills) | BSP public-vs-internal API discipline; pinned managed skill lifecycle; routed references and behavioral evaluation patterns | REFERENCE |
| [vandalsvq/edt1c-ai-template](https://github.com/vandalsvq/edt1c-ai-template) | Adopting-project bootstrap and project-vs-template ownership/idempotent synchronization patterns used by ADOPTION-002; reference only pending top-level license clarity | REFERENCE |
| [Arman-Kudaibergenov/1c-ai-development-kit](https://github.com/Arman-Kudaibergenov/1c-ai-development-kit) | Contrast/reference for skill-surface consolidation and overlap reduction; not a package surface to inherit wholesale | REFERENCE |
| [obra/superpowers](https://github.com/obra/superpowers) | Workflow-oriented skills, review/verification, and evidence-driven agent-development reference | REFERENCE |

## Policy

Before public release, every material external influence must be classified and reviewed for provenance, license, attribution, and whether it belongs in the public artifact.

Private/client/purchased sources, credentials, dumps, or business data must never be introduced into the public source layer.
