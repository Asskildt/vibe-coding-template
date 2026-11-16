# Design system

> Knowledge file, loaded on demand. Records *this project's* design system so the agent matches it
> instead of inventing one. The rules below are recommendations in tiers, not hard requirements:
> pick the tier that fits the project and record it in `AGENTS.md` (Project Overview).
>
> - **Owner:** {name / role}
> - **Last updated:** {YYYY-MM-DD}

## Files

| File | Read it when |
|---|---|
| [`tokens.md`](tokens.md) | Defining or changing colors, type, spacing, themes |
| [`components.md`](components.md) | Creating or changing a UI component |
| [`layouts.md`](layouts.md) | Creating a page or screen. Has shell skeletons |
| [`accessibility.md`](accessibility.md) | Any UI work. It is the correctness floor for every tier |
| [`seo.md`](seo.md) | Public pages, sharing previews, external links |
| [`ai-tells.md`](ai-tells.md) | Before shipping a UI change |

## Tiers

The template fits a static page and a product with a design team. Scale the system to the project.
Moving up a tier keeps token names and component code, so it is cheap if the lower tier was
followed. These design tiers (1 to 3) are independent of the structure tiers (A to C) in
[`../structure.md`](../structure.md). Choose both once, in `AGENTS.md` (Project Overview).

| Tier | Project | Design system scope |
|---|---|---|
| **1. Minimal** | Static site, landing page, one-off tool | One CSS file with custom properties for color, type, spacing. Fill in "Your system" below. Accessibility floor. No component library, no token build. [`web/`](../../web/) is a real example: read it as a pattern (theme, tokens, landing page), don't copy it |
| **2. Standard** | App with a real UI | Tier 1 plus primitive and semantic tokens in separate files, `components/ui/` with variant and size props, page shells in `layouts/`, light/dark/system. Lint rule against hardcoded values |
| **3. Design team** | A design team, Figma sync, or a design system shared across projects | Tier 2 plus optional component tokens, tokens as DTCG source files with a build step, optional Figma link |

Default to tier 2 for any app. Tier 3 is a decision: it adds a build step, so adopt it when a
design team's handoff or a Figma sync is real, not expected.

## Your system (fill in: this is what the agent should match, not invent)

Most AI-generated interfaces default to generic patterns *because nothing else was specified*.
Fill these in first. At tier 2 and up they are tokens in code, and this section points to them.
If the project keeps a `DESIGN.md` ([google-labs-code/design.md](https://github.com/google-labs-code/design.md),
alpha, optional), it can be the source for these fields. Then this section points to it instead of
repeating the values.

- **Palette:** {your actual colors, as tokens, not "purple gradient"}
- **Type scale:** {your font(s), sizes, and the ratio between steps}
- **Corner radii:** {your actual scale, e.g. 0 / 4 / 8px, or "square, no radius"}
- **Spacing scale:** {your actual base and steps, e.g. 4px base}
- **Motion:** {what's allowed (durations, easing) and what isn't}
- **Shells:** {the project's page shells, one line each, e.g. AppShell, PublicShell. See [`layouts.md`](layouts.md)}

If this section is empty, the agent has nothing to match and will reach for defaults, which is
exactly what [`ai-tells.md`](ai-tells.md) flags.

## Optional: design tool integration

If the project designs in Figma, the Figma MCP server can give an agent variables, components and
layout data, and Code Connect links Figma components to code components. Reading is usable.
Writing to the canvas is beta. It is an external service with no code in the repo, so it is cheap
to add and drop. Adding it is a dependency decision (rule 7). Status is tracked in
[`../standards/watchlist.md`](../standards/watchlist.md).
