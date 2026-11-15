# Standards watchlist

> Status of the standards the template depends on or follows. Rules for adding and moving rows are
> in [`README.md`](README.md). Re-check every row each quarter.
>
> - **Last verified:** 2026-11-15 (first entry, from the research behind the design-system and
>   structure rules)
> - **Switching cost:** Low = delete a file. Medium = days to swap. High = shapes the codebase.
> - **Source quality:** P = primary (spec, vendor docs, law, registry). S = secondary.
>   **Unverified** = could not be confirmed. Don't state it as fact.

## Adopted (default in the template)

| Standard | Status 2026-11-15 | Cost | Source | Used in |
|---|---|---|---|---|
| WCAG 2.2 AA as target | W3C Recommendation. 2.2 conformance also meets 2.0 and 2.1 | Low | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (P) | `design/accessibility.md` |
| Norwegian ICT accessibility regulation | Private web solutions must meet WCAG 2.0 A and AA (minus 1.2.3 to 1.2.5). Public bodies follow EN 301 549 and need an accessibility statement | Not optional | [Lovdata FOR-2013-06-21-732](https://lovdata.no/dokument/SF/forskrift/2013-06-21-732) (P), [uutilsynet.no](https://www.uutilsynet.no/regelverk/) (P) | `design/accessibility.md` |
| AGENTS.md | Stewarded by the Agentic AI Foundation (Linux Foundation). Plain Markdown, no required fields | Low | [agents.md](https://agents.md/) (P), [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) (P) | `AGENTS.md` |
| Agent Skills (`SKILL.md`) | Donated to the Agentic AI Foundation 2026-10-22. Folder with `SKILL.md` plus optional `scripts/`, `references/`, `assets/` | Low to medium | [agentskills.io spec](https://agentskills.io/specification) (P) | `.agent/skills/` |
| CSS Baseline Widely: `@layer`, container queries, `:has()`, `color-mix()`, `oklch()`, nesting, subgrid | Baseline Widely available | Low | [web-features](https://registry.npmjs.org/web-features) v3.46.0 (P), [web.dev/baseline](https://web.dev/baseline) (P) | `design/tokens.md` |
| Machine checks for structure and hardcoded values | ESLint, Stylelint, `eslint-plugin-boundaries`, `dependency-cruiser`, `knip` have recent npm releases. For `knip` and `ls-lint` only the version was checked | Low to medium | npm registry (P), [ESLint max-lines](https://eslint.org/docs/latest/rules/max-lines) (P), [Stylelint color-no-hex](https://stylelint.io/user-guide/rules/color-no-hex) (P) | `structure.md`, `design/tokens.md` |

## Optional (adopt by project tier or need)

| Standard | Status 2026-11-15 | Cost | Source | Condition |
|---|---|---|---|---|
| DTCG design tokens 2025.10 | First stable version. A Community Group Report, not a W3C Standard. The group's own page lists Figma, Penpot, Sketch, Tokens Studio, Style Dictionary and Terrazzo as supporters. Style Dictionary does not fully support 2025.10 yet. Figma's own docs were not checked | Medium | [W3C announcement](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/) (P), [Style Dictionary DTCG page](https://styledictionary.com/info/dtcg/) (P) | Design tier 3 (several brands) |
| Figma MCP server and Code Connect | Reading design context is usable. Writing to the canvas is beta. Seat and plan limits apply | Low | [Figma developer docs](https://developers.figma.com/docs/figma-mcp-server/) (P) | Project designs in Figma |
| `llms.txt` | A proposal, not a standards-body spec. Published by many developer-documentation sites, not all. No proven effect on search. Google Search does not use it, per secondary sources | Low | [llmstxt.org](https://llmstxt.org) (P for the proposal), own HTTP check 2026-11-15 | Public documentation or content sites only |

## Watching (not adopted yet)

| Item | Status 2026-11-15 | Cost if built in early | Source | Revisit when |
|---|---|---|---|---|
| WCAG 3.0 | Working Draft. Final requirements will differ | Low (criteria, not architecture) | [W3C history](https://www.w3.org/standards/history/wcag-3.0/) (P) | It reaches Candidate Recommendation |
| CSS `@function` | Not Baseline (Chrome/Edge only) | High in a token system | [web-features](https://registry.npmjs.org/web-features) (P) | Baseline Newly in all three engines |
| CSS `if()` | Not Baseline (Chrome/Edge only) | High | same | same |
| Cross-document view transitions | Not Baseline (Firefox missing) | Low as enhancement | same | Baseline Newly |
| CSS anchor positioning | Not Baseline as a whole. Core is in all three engines, parts are still pending | Low as enhancement | same | Baseline Newly |
| `@scope`, `light-dark()`, relative color syntax, container style queries | Baseline Newly (all engines, under 30 months) | Low | same | Baseline Widely. Until then, only behind `@supports` |
| Other design-system MCP servers (e.g. for Storybook) | Not researched | Low | n/a | Next review |
| Agent skills folder name | The spec doesn't prescribe a folder. `.agents/skills/` is described as a widely adopted convention. This template uses `.agent/skills/`. Which agent clients scan which folder is **unverified** | Low (move one folder and update links) | [agentskills.io client guide](https://agentskills.io/client-implementation/adding-skills-support.md) (P) | Next review. Decide whether to rename |

## Unverified (do not state as fact)

- Whether and how the European Accessibility Act (directive 2019/882, applies in the EU from
  2025-06-28) is part of Norwegian law, and what it means for a Norwegian company selling in the
  EU. Check with uutilsynet.no or a legal adviser. The Norwegian ICT regulation above refers only
  to directive 2016/2102.
- Figma's own documentation for DTCG import and export. Only a forum report was found, claiming
  that composite tokens (typography, gradient, shadow) are not exported.
- ISO/IEC 40500:2025 (WCAG 2.2 as an ISO standard).
- A ready-made lint rule for "maximum files per folder", and a Stylelint plugin that checks
  Baseline support.
- `eslint-plugin-design-tokens` (MetaMask): exists, maintenance not assessed.

## Rejected

- `madge` for dependency checks: last release 2024-08, not maintained. Use `dependency-cruiser`
  or `eslint-plugin-boundaries`.
