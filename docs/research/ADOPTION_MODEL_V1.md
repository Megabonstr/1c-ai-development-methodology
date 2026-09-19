# Adoption Model V1

Date: 2026-09-18  
Status: RESEARCH-001 recommendation / no implementation authority yet

## 1. Question

How should an existing 1C project adopt the 1c-ai-development core, profiles, adapters, and generic workflow skills across Codex, Claude Code, Cursor, Gemini CLI, and GitHub Copilot without creating several manually maintained copies?

## 2. Current project constraints

The accepted repository currently has:

- one tool-neutral core under `docs/core/`;
- one compact router;
- two execution profiles;
- seven generic Agent Skills under `skills/`;
- thin root/client adapters;
- structural CI;
- skills that reference repository-owned core paths and are therefore not standalone.

The installation model must preserve:

- one canonical policy owner;
- progressive disclosure;
- exact-source/update provenance;
- Windows-heavy 1C development;
- existing project instructions rather than overwriting them;
- client neutrality.

## 3. Current official client facts

All facts below were checked on 2026-09-18.

### 3.1 OpenAI Codex

Official documentation:

- https://developers.openai.com/de-DE/docs/build-skills
- https://developers.openai.com/de-DE/docs/customization/overview

Relevant facts:

- repository skills are discovered from `.agents/skills`;
- user skills are discovered from `~/.agents/skills`;
- Codex progressively exposes skill metadata first and loads the full `SKILL.md` only when selected;
- symlinked skill directories are supported.

Implication: `.agents/skills` is a native project-level path for Codex.

### 3.2 Cursor

Official documentation:

- https://prod.cursor.com/docs/skills

Relevant facts:

- project skills are discovered from `.agents/skills/` and `.cursor/skills/`;
- Cursor also supports compatibility locations such as Claude/Codex skill directories;
- Agent Skills are described as portable and progressively loaded.

Implication: `.agents/skills` is a native project-level path for Cursor.

### 3.3 Gemini CLI

Official documentation:

- https://geminicli.com/docs/cli/using-agent-skills/
- https://google-gemini.github.io/gemini-cli/docs/cli/skills.html
- https://geminicli.com/docs/cli/creating-skills/

Relevant facts:

- workspace skills are discovered from `.gemini/skills/` or the `.agents/skills/` alias;
- the documentation explicitly calls `.agents/skills` an interoperable path;
- skill metadata is used for discovery and the body is loaded only on activation.

Implication: `.agents/skills` is a native project-level path for Gemini CLI.

### 3.4 GitHub Copilot

Official documentation:

- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- https://docs.github.com/en/copilot/concepts/agents/about-agent-skills

Relevant facts:

- project skills may live in `.github/skills`, `.claude/skills`, or `.agents/skills`;
- current `gh skill` can preview/install/update/pin skills and target agent hosts;
- GitHub warns that third-party skills should be inspected because skills may contain executable resources or malicious instructions.

Implication: `.agents/skills` is a native project-level path for Copilot.

### 3.5 Claude Code

Official documentation:

- https://code.claude.com/docs/en/skills

Relevant facts:

- project skills live in `.claude/skills/<name>/SKILL.md`;
- Claude Code follows the Agent Skills standard;
- detailed skill content loads on demand;
- the documented project discovery path is Claude-specific.

Implication: Claude Code is the one reviewed client that does not give us an official `.agents/skills` project path.

## 4. Upstream implementation references

### 4.1 cc-1c-skills

Repository:
https://github.com/Nikolay-Shirokov/cc-1c-skills

Reviewed ref:
`e2c7f385187e7774c518c6dffc130f4474422395`

Relevant implementation evidence:

- canonical source skills are stored in one source tree;
- `scripts/switch.py` maps skills into client-specific target directories;
- copy mode rewrites target paths;
- link mode uses junctions on Windows / symlinks on Unix;
- the current implementation deliberately limits link mode because some target platforms need content/path rewriting.

What this proves:

- one source + generated client materialization is practical;
- Windows junction support is possible;
- links are not universally transparent once client-specific path semantics exist.

What it does not prove:

- that its platform map should be copied;
- that Claude-first source layout is best for this project.

### 4.2 EDT-MCP business-project skills

Repository:
https://github.com/DitriXNew/EDT-MCP

Reviewed ref:
`681718a9ba93671546e058a9e761e2e087ad4703`

Relevant file:
`agent/README.md`

Relevant evidence:

- the upstream keeps a client-neutral business-workflow source tree;
- installation may copy or link skills into the directory recognized by the chosen client;
- the router is installed separately and referenced by root instructions;
- installed path validity must be checked rather than assuming source-relative links still work.

What this proves:

- neutral authoring and client-specific installation can be separated cleanly;
- cross-file references are a real installation constraint.

## 5. Additional constraint discovered by this research: skill-name collisions

Our current generic skill names include examples such as:

- `task-bootstrap`;
- `focused-review`;
- `bounded-implementation`.

These are reasonable inside this repository but too generic for broad installation into an existing project.

Clients differ in duplicate-name behavior and precedence. A reusable package should avoid relying on collision resolution.

Recommendation:

Prefix public/project-installable skills with:

`1c-ai-`

Examples:

- `1c-ai-task-bootstrap`;
- `1c-ai-source-first-research`;
- `1c-ai-bounded-implementation`;
- `1c-ai-focused-review`;
- `1c-ai-focused-verification`;
- `1c-ai-github-handoff`;
- `1c-ai-local-runtime-validation`.

This is a compatibility improvement, not branding decoration.

## 6. Viable options

### Option A - Keep current neutral source tree and generate every client layout

Source:

`skills/*`

Target examples:

- `.agents/skills/*`;
- `.claude/skills/*`;
- other client paths if required.

Pros:

- authoring layout is independent from any client;
- installer controls all materialization.

Cons:

- this repository itself does not dogfood native skill discovery;
- every installation path needs generation;
- path rewriting remains a permanent installer responsibility;
- more generated copies than needed.

Verdict: viable, but not minimal.

### Option B - Make .agents/skills the canonical skill tree only

Source and target:

`.agents/skills/1c-ai-*`

Pros:

- native for Codex, Cursor, Gemini, Copilot;
- repository itself dogfoods the interoperable path;
- fewer transformations;
- aligns with current open-agent ecosystem direction.

Cons:

- Claude still needs a compatibility installation;
- non-skill core/router/profile paths remain an adoption problem if they stay under generic `docs/`.

Verdict: strong improvement, but incomplete by itself.

### Option C - Installable namespaced machine package + canonical .agents/skills

Recommended.

Source/adopting-project shape:

```text
.1c-ai/
  START_HERE.md
  core/
  router/
  profiles/
  manifest.json

.agents/
  skills/
    1c-ai-task-bootstrap/
    1c-ai-source-first-research/
    ...

AGENTS.md                         # existing/create managed pointer
CLAUDE.md                         # existing/create managed pointer/import
GEMINI.md                         # existing/create managed pointer/import
.github/copilot-instructions.md   # existing/create managed pointer

# Claude Code uses CLAUDE.md -> .1c-ai/START_HERE.md -> router -> exact .agents skill path
```

Pros:

- one namespaced machine-policy package avoids collision with an adopting project's own `docs/`;
- `.agents/skills` is directly usable by 4 of the 5 reviewed clients;
- source repository can dogfood the same layout used by adopting projects;
- skills can reference stable `.1c-ai/...` paths without per-client rewriting;
- Claude can follow the deterministic repository router to the exact skill file without a second committed skill tree;
- future installer becomes mostly deterministic copy + merge-safe adapters rather than content transformation.

Cons:

- requires a one-time migration of the current repository layout;
- Claude does not get native project-skill auto-discovery from `.agents/skills` under its currently documented paths;
- installer must track managed files and refuse unsafe overwrites.

Verdict: best private-beta model.

### Option D - Git submodule/symlink-first installation

Example:

- add this repository as a submodule under `tools/`;
- link agent directories to the submodule.

Pros:

- upstream update identity is explicit;
- little copied content.

Cons:

- submodule initialization is an extra failure mode for cloud/local agents;
- native skill discovery does not automatically traverse arbitrary nested submodules;
- root adapters still need integration;
- Windows link/junction behavior and Git representation increase operational risk;
- link behavior is not uniform across client ecosystems.

Verdict: useful optional advanced mode later, not the default.

## 7. Recommended private-beta model

Adopt **Option C** with the following rules.

### 7.1 Canonical machine package

Move machine-facing core/router/profiles to a dedicated namespace:

`.1c-ai/`

This directory is owned by the package installer/update process.

Human-facing project documentation remains outside it.

### 7.2 Canonical generic skills

Move and rename generic skills to:

`.agents/skills/1c-ai-*/SKILL.md`

This makes the private repository itself a real adoption fixture for Codex, Cursor, Gemini, and Copilot.

### 7.3 Claude compatibility

Do not create a committed `.claude/skills` mirror for the private-beta project layout.

Reason:

- Claude's documented native project skill path is `.claude/skills`;
- Cursor and Copilot also scan Claude-compatible skill paths;
- a project containing the same names under both `.agents/skills` and `.claude/skills` can expose duplicate skill candidates and make behavior depend on client-specific precedence.

Private-beta Claude route:

```text
CLAUDE.md
-> .1c-ai/START_HERE.md
-> .1c-ai/router/ROUTER.md
-> exact .agents/skills/1c-ai-*/SKILL.md
```

Claude can read and apply the selected skill as repository content even though it is not natively auto-discovered from `.agents/skills`.

Native Claude skill packaging may be added later as a separately installed user/plugin distribution after cross-client behavior is tested. It must not create a second committed project skill tree by default.

This is a deliberate trade-off: one canonical project skill tree is more important for private beta than native automatic skill discovery in every client.

### 7.4 Installation mode

Default: **vendored pinned snapshot** committed into the adopting project.

Why:

- self-contained source state;
- works offline after installation;
- easy PR review;
- cloud agents do not depend on submodule initialization;
- exact package version/SHA is reviewable with the project.

The installed package should contain a manifest recording at least:

- package version;
- upstream repository;
- upstream tag/SHA;
- installed profile(s);
- installed agent adapters;
- hashes of managed files.

Before public v1.0.0, installs may pin an exact private-source commit.

### 7.5 Update safety

Updater must not blindly replace project-owned instruction files.

For root adapters:

- create the file when absent;
- when present, insert/update one clearly delimited managed block or exact managed import line;
- preserve all user/project-owned content outside the managed block;
- refuse ambiguous duplicate/conflicting managed blocks.

For package-owned files:

- compare current file hash with the previously recorded manifest hash;
- unchanged managed file -> replace/update;
- locally modified managed file -> STOP and report the conflict;
- removed upstream managed file -> delete only when the installed copy still matches the old managed hash.

### 7.6 Uninstall safety

Uninstall only:

- package-owned files verified by manifest;
- managed adapter blocks created by this package.

Never delete whole pre-existing adapter/instruction files merely because they contain the package block.

## 8. Why not make symlink/junction the default

1C development is disproportionately Windows-based.

Windows directory junctions can be useful for a single developer's local workflow, but the installation must also work for:

- GitHub/cloud agents;
- cloned repositories on other machines;
- CI;
- contributors without identical filesystem layout;
- users who do not enable symlink-specific Git/Windows behavior.

Therefore:

- copy/vendor is the safe default;
- link mode may be an explicit local-development optimization later.

## 9. Source-repository migration implied by the recommendation

A later implementation task should migrate the private repository itself so it becomes the reference installed shape:

From:

```text
docs/START_HERE.md
docs/core/*
router/*
profiles/*
skills/*
```

Toward:

```text
.1c-ai/START_HERE.md
.1c-ai/core/*
.1c-ai/router/*
.1c-ai/profiles/*
.agents/skills/1c-ai-*
```

Human-facing architecture/research documents may remain under `docs/`.

All adapters, router links, validators, Issue/PR templates, and skill references must be reconciled in the same bounded migration so no split-brain path remains.

## 10. Implementation sequence for later ADOPTION work

Recommended separate implementation tasks:

### ADOPTION-001A - package-layout migration

- move canonical machine package to `.1c-ai/`;
- move/rename generic skills to `.agents/skills/1c-ai-*`;
- update adapters/router/validator atomically;
- prove no stale canonical paths remain;
- no installer yet.

### ADOPTION-001B - deterministic installer/update/uninstall

- standard-library Python;
- target project path;
- selected execution profile(s);
- selected clients;
- manifest/hash ownership;
- merge-safe adapter blocks;
- Claude router-based access without a second project skill tree;
- dry-run before writes;
- install/update/uninstall;
- tests with synthetic fixture repositories.

### ADOPTION-001C - real-project dogfood

Install a pinned private build into at least:

- one EDT/MCP 1C project;
- one XML/Configurator-style fixture or real project.

Verify fresh-session discovery and actual routing with more than one client before public release.

## 11. Remaining UNKNOWN / risks

- Exact installer UX and command names: not decided by this research.
- Whether public distribution should later also expose Agent Plugin / marketplace packaging: future research, not required for private beta.
- Whether Claude will adopt `.agents/skills` as a native alias later: current official documentation does not establish that; do not assume it.
- Native Claude automatic skill discovery is intentionally not provided by the private-beta project layout; Claude uses deterministic router-based loading instead.
- Whether a hybrid 1C execution profile is required: still unproven.
- Windows junction/link mode behavior across every Git/client environment: not required for default copy mode.

## 12. Recommendation

`ACCEPT OPTION C FOR PRIVATE BETA`

Use:

`namespaced .1c-ai machine core + one canonical .agents/skills tree with 1c-ai- names + Claude router-based loading + pinned vendored install + manifest/hash ownership + merge-safe root adapter blocks`.

This minimizes manually maintained duplication while keeping the adopting repository self-contained and reviewable.
