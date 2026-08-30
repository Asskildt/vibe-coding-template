# 0001 — Context engineering: the source and the six context types

- **Status:** Accepted
- **Date:** 2026-08-30
- **Owner:** {name / role}

## Context

This template splits agent context into a small always-loaded core (`AGENTS.md`) and a larger set
of load-on-demand files (`docs/`, `.agent/`). That split is not arbitrary — it comes from a
specific framing of what "context" is made of. This ADR records the source so the reasoning never
has to be reconstructed or guessed at later.

## Source

The framing comes from a report read directly (primary source, not a summary of it):

- **Title:** *The New SDLC With Vibe Coding: From ad-hoc prompting to Agentic Engineering*
- **Authors:** Addy Osmani, Shubham Saboo, Sokratis Kartakis
- **Content contributors:** Elia Secchi, Julia Wiesinger, Anant Nawalgaria
- **Publisher:** Google
- **Date:** May 2026
- **Published:** Kaggle, as part of the Google/Kaggle "5-Day AI Agents" course ("Day 1" paper).
  <https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding>
- **Relevant section:** "Context engineering: the real skill" (pp. 15–16). The six context types
  are listed as bullet points on p. 15; the static/dynamic distinction follows on p. 16, in the
  same section.

**Verified:** 2026-08-30, read directly against the primary source (the uploaded PDF, `Day_1_v3.pdf`),
pp. 15–16 — not against an AI-generated summary, per the "Source Requirements for Factual Claims"
rule in `AGENTS.md`. Title, authors, and the May 2026 date were cross-checked against the public
Kaggle listing.

## Decision

Adopt the report's six context types as the organizing principle for where every piece of context
lives in this repo. Each type maps to a concrete location:

| Context type     | Where it lives                        | Why there |
|------------------|---------------------------------------|-----------|
| **Instructions** | `AGENTS.md`                           | Rules and working method, needed in *every* task, so always loaded. |
| **Knowledge**    | `docs/*.md`                           | Architecture, data model, domain, API. Loaded only when a task needs it. |
| **Memory**       | `docs/decisions/` (ADRs) + `docs/known-limitations.md` | Long-term memory: why things are the way they are, so it isn't rediscovered each time. |
| **Examples**     | `.agent/examples/`                    | Real code from the project, not invented ideal code. |
| **Tools**        | MCP config / API definitions          | With precise prose about *when* each tool applies. |
| **Guardrails**   | Hooks / lint rules + the Security section of `AGENTS.md` | Enforced automatically where possible. |

The single most important consequence: **static vs dynamic is the primary tradeoff.** `AGENTS.md`
holds only what every task needs. Everything else is dynamic — loaded via a link, a `docs/` file,
or a skill, only when the task actually requires it. This is the "progressive disclosure" pattern
from the report, and it's what rule 13 in `AGENTS.md` enforces in practice.

## Consequences

- The folder layout (`docs/`, `docs/decisions/`, `.agent/skills/`, `.agent/examples/`) is a direct
  expression of this mapping. Changing the layout means revisiting this ADR.
- Other planning and context files reference *this* document instead of restating the six types, so
  the premise lives in one place and doesn't drift.
- If the mapping proves wrong for a given project (e.g. a tool that ships its own skills mechanism),
  that's a new ADR superseding or amending this one — not a silent edit.

## Alternatives considered

- **No explicit framework, organize by feel.** Rejected: leads to context sprawl and to the same
  "where does this go?" question being answered differently each time.
- **A single large context file.** Rejected: everything costs tokens on every interaction, and the
  file rots because no one wants to trim a wall of text. The static/dynamic split exists precisely
  to avoid this.
