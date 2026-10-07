# Vibe Coding Template

A tool-agnostic `AGENTS.md` template for context engineering and planning before you vibe-code.

Most AI coding goes wrong before the first prompt: no clear goal, no shared conventions, no record
of why things are the way they are. This template front-loads that thinking. It gives an AI agent
the context it needs to work without guessing, and gives you a short planning chain to run *before*
any code exists, scaled so a weekend script can skip it entirely.

> **Note:** This is a template, not a library. You copy it into a new project and fill in the
> `{...}` placeholders. Nothing here runs. It's structure and prose.

## What's in it

| File / folder | What it is |
|---------------|-----------|
| **`AGENTS.md`** | The always-loaded core: working rules, code style, writing and security rules. Kept deliberately short, so everything else loads on demand. |
| **`docs/planning/`** | A 6-step planning chain (brief → stack → architecture → extension points → milestones → deploy), run *before* coding. Has a skip-it exit for small projects. |
| **`docs/decisions/`** | ADRs: the long-term memory of *why* a choice was made, so it isn't re-litigated later. |
| **`docs/backend.md`** | Performance, state and API-error rules. Read before writing code that hits a database, renders lists or defines API responses. |
| **`docs/ai-workflow.md`** | How to work with the agent: model routing by capability class, token economy, when to drive step-by-step vs hand off a whole task, and how to delegate to subagents. |
| **`.agent/`** | Reusable context: `skills/` (procedural knowledge, loaded on demand) and `examples/` (real code from the project). |
| **`.github/PULL_REQUEST_TEMPLATE.md`** | A PR checklist that keeps docs in sync. The one mechanism that stops context from rotting. |

This table is a simplified entry point. For the complete, authoritative file map, see the
References section at the bottom of [`AGENTS.md`](AGENTS.md). That's the one kept in sync as files
are added or removed.

The layout is a direct expression of six context types (Instructions, Knowledge, Memory, Examples,
Tools, Guardrails). The reasoning and its source are recorded in
[`docs/decisions/0001-context-engineering-source.md`](docs/decisions/0001-context-engineering-source.md).

## Start here

The fastest path is to hand one of these to your coding agent. Both point it at this repo so it
reads the conventions at the source.

**New project:**

```text
I want to start a new project (roughly: what it is). Use
github.com/Asskildt/vibe-coding-template as the framework. Copy its files in, then read
AGENTS.md and docs/planning/README.md. Before any code, ask me what you need to understand
the project: the goal, who it's for, the constraints. Decide with me whether it needs the
planning chain (it has a skip-it threshold). Walk me through the planning one step at a time
instead of guessing, then fill in the AGENTS.md placeholders. Don't start building until
we've agreed on the plan.
```

**Existing project:**

```text
I have an existing project and want to adopt the conventions from
github.com/Asskildt/vibe-coding-template where they fit. First read the conventions there,
at least AGENTS.md, docs/design.md, docs/ai-workflow.md, and docs/planning/README.md. Then
read my project properly: not just the top-level files, but the real structure, the main
modules, config, and any existing docs, so your read is grounded in how it actually works.
Then talk it through with me: propose which conventions are worth adopting and which don't
fit, and whether to copy files in or just borrow ideas. Don't change anything until we've
agreed.
```

## How to use it

1. **Copy the files** into your new project (or use this repo as a GitHub template).
2. **Decide if you need the planning chain.** Read
   [`docs/planning/README.md`](docs/planning/README.md) first. It tells you when to run the chain
   and when to skip it. A weekend script skips. Anything others will maintain goes through it.
3. **Fill in `AGENTS.md`.** Replace the `{...}` placeholders, delete sections that don't apply, and
   set the owner/date fields. It's meant to be trimmed, not grown.
4. **Add `docs/` files as the project needs them:** architecture, domain, data model. Don't create
   them empty. Add each when there's something real to put in it.
5. **Keep it in sync.** The rule is simple: docs are code. A change that touches an endpoint, a
   page, or a domain flow updates the matching doc in the same session.

## Design principles

- **Static vs dynamic is the main tradeoff.** `AGENTS.md` holds only what *every* task needs.
  Everything else loads on demand. Tokens aren't free.
- **Describe the decision, not the fleeting answer.** Stack, deploy target, and model choices are
  written as decision frameworks, not fixed answers that rot.
- **Tool-agnostic by default.** `AGENTS.md` is the single source. Codex reads it natively;
  `CLAUDE.md` and `GEMINI.md` import it with `@AGENTS.md`. Check that it actually loads: `/context`
  in Claude Code, `/memory show` in Gemini CLI. Skills support varies by tool, see
  [`.agent/README.md`](.agent/README.md).

## Language

The template is written in English (it's instructions to a model, and the ecosystem is English).
Norwegian is kept only where a project's *domain* is Norwegian: user-facing copy and domain docs.

## License

[MIT](LICENSE). Copy it, change it, use it commercially, no need to ask. Just keep the license
notice if you redistribute it. © 2026 M. Asskildt, asskildt.eu

---

Landing page: <https://vibe.asskildt.eu>. It lives in `web/`, which is this repo's own site rather
than part of the template. Don't copy it into your project, though it does serve as a worked example
of the theme and accessibility baselines in [`docs/design.md`](docs/design.md).

`web/index.md` is generated from `web/index.html` by `scripts/build-index-md.py`. Enable the
pre-commit check with `git config core.hooksPath .githooks`. When you copy the template into a
project, delete `web/`, `scripts/` and `.githooks/` unless you reuse them.
