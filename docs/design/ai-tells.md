# Avoid AI tells

> Read before shipping a UI change. Part of the [design system](README.md).

## Avoid AI Tells

Check a UI change against these before shipping. They're the patterns that recur across generated
interfaces — recognizable precisely because they're the default reach, not a considered choice.

**Color**
- Purple/violet gradients, cyan-on-dark — the generic "AI palette"
- Cream/beige background reached for as the "safe tasteful" default
- Gradient text on headings or numbers
- Dark mode with glowing colored shadows as decoration

**Typography**
- Italic serif as the hero headline
- A small uppercase "kicker"/eyebrow label above a heading (fine once; a tell when it's on every section)
- One font for everything, with no hierarchy between heading and body
- Inter / Geist / Space Grotesk used by default rather than by deliberate choice

**Layout & components**
- Thick colored border on one side of a rounded card (the "side-tab" — the single most recognizable tell)
- Cards nested inside cards inside cards
- A rounded icon tile above a heading in every feature block
- Identical card grids (icon + heading + short text) repeated without variation
- Big number + small label + 2–3 supporting stats as the default hero layout

**Motion**
- A pulsing status dot on something that isn't actually changing
- Bounce/elastic easing on dialogs and cards
- Image scale/rotate on hover, used as decoration rather than purposeful interaction

**Copy** — see the "User-Facing Text — Avoid AI Signals" section in `AGENTS.md`. The same tells
(em-dash overuse, marketing buzzwords, aphoristic "Not a feature. A platform." cadence) apply to
interface copy. One source, not duplicated here.

## How to check

Manual review against this list works but is easy to skip under time pressure. The tells are what
appear when nothing was specified, so the real defense is [`README.md`](README.md) (your system),
[`tokens.md`](tokens.md) and [`layouts.md`](layouts.md) filled in. If the project has a real
frontend surface where visual quality matters, evaluate a dedicated design tool as a decision in
[`../planning/01-stack-decision.md`](../planning/01-stack-decision.md) (question 7), not silently
(rule 7). The checklist is the safety net, not the plan.
