# Design system & AI tells

> Knowledge file, loaded on demand. Two jobs: (1) record *this project's* actual design system so
> the agent matches it instead of inventing one, and (2) catch the generic patterns that make an
> interface read as AI-generated.
>
> - **Owner:** {name / role}
> - **Last updated:** {YYYY-MM-DD}

## Your system (fill in — this is what the agent should match, not invent)

The single best defense against generic output is not the checklist below — it's an actual system
for the agent to follow. Most AI-generated interfaces default to generic patterns *because nothing
else was specified*. Fill these in first; the checklist catches drift after that.

- **Palette:** {your actual colors, as tokens — not "purple gradient"}
- **Type scale:** {your font(s), sizes, and the ratio between steps}
- **Corner radii:** {your actual scale, e.g. 0 / 4 / 8px — or "square, no radius"}
- **Spacing scale:** {your actual base and steps, e.g. 4px base}
- **Motion:** {what's allowed — durations, easing — and what isn't}

If this section is empty, the agent has nothing to match and will reach for defaults — which is
exactly what the checklist below flags.

## Theme support (recommended default)

**Support system, light, and dark theme modes unless you have a specific reason not to.** This is
the default assumption in 2026 — most users expect it — but like everything else in this file, it's
a project decision, not something the template hard-requires.

Skip it deliberately when, for example:

- The product's fixed palette is proven to read well in both light and dark contexts (rare — worth
  confirming, not assuming).
- The UI surface is trivial enough that theme support wouldn't be noticed (a one-off internal tool,
  a script's minimal output page).

If you skip it, note the reason next to the stack ADR in `docs/decisions/`, so "why no dark mode?"
isn't re-litigated later.

### Once you do support it, these are firm

- **`system`** follows the OS via `prefers-color-scheme`. This is the default a first-time visitor
  gets, with no stored choice.
- **`light` / `dark`** are explicit user choices that override the system preference and persist
  (e.g. `localStorage`).
- **No flash on load.** The chosen theme is applied before first paint — a small synchronous script
  in `<head>`, ahead of `<body>`, not after the page renders.
- **`system` stays live.** If the user is on `system` and the OS switches, the page follows without
  a reload (a `matchMedia` change listener).

How you implement it is a project choice: CSS custom properties toggled by a `data-theme` attribute,
a framework's own theming, or whatever fits the stack. The landing page for this template
(`web/index.html`) is a worked reference implementation of exactly this pattern — copy from it
rather than reinventing it (see `.agent/examples/`: real code beats invented ideal code).

Design both themes deliberately. Dark mode is not "light mode with inverted colors" — it's its own
set of tokens. A tell to avoid: glowing colored shadows used as decoration in dark mode (see the
checklist below).

## Accessibility & machine-readability (baseline)

This is a correctness bar, not a feature decision — the same category as the Security section in
`AGENTS.md`. It's cheap to get right from the start and expensive to retrofit. The practices below
serve three readers at once: someone with a screen, someone using a screen reader, and a crawler or
agent parsing the page without rendering it at all. Browser agents mostly read the accessibility
tree, not pixels, so accessibility and agent-navigability are the same work.

**Structure**
- Semantic HTML (`header`/`main`/`nav`/`section`/`footer`), not `div` soup. A screen reader and an
  LLM/crawler both use this to understand the page's shape.
- Real elements for controls: `button`, `a`, form controls. Never a clickable `div`.
- No skipped heading levels (h1 → h3 with no h2). Screen readers navigate by heading hierarchy.
- Content is never gated behind client-side JS. A crawler or agent that doesn't execute JavaScript
  gets near-empty HTML from a client-rendered page, so render the real content on the server (or
  at build time), not an empty shell.

**Contrast and readability**
- WCAG AA minimums: 4.5:1 for body text, 3:1 for large text (18pt+ / 14pt bold+) and UI components.
- Body text at least 14px, ideally 16px. Line height 1.5–1.7 for multi-line copy.

**Interaction**
- Every interactive element has a visible `:focus-visible` state. Don't rely on the browser default
  if the design has removed or clashes with it. Keyboard-only users need this as much as the CTA
  needs a hover state.
- Every control has an accessible name. Icon-only controls (a theme toggle, a close button) get an
  `aria-label`. Text ones don't need one redundantly.
- Expose state, not only color: `aria-expanded`, `disabled`, `aria-invalid`, and error text linked
  with `aria-describedby`.
- Nothing is reachable only on hover.
- State that matters (filters, tabs, selected item, pagination) lives in the URL, so an agent can
  deep-link to it.
- Validation messages say what is valid ("Use 3-20 letters"), the same idea as the API `hint` in
  `backend.md`.
- Respect `prefers-reduced-motion`.

**Machine-readable by default**
- Meaningful `alt` text on images that carry information; empty `alt=""` on purely decorative ones.
- Structured data (JSON-LD) where it fits the content type. This mirrors the "Machine-Readable
  Documentation" principle in `backend.md`, applied to the page itself, not just the API.
- A stable canonical URL, and a `lang` attribute that matches the actual content language.

**Public, content-heavy pages**

Applies to marketing pages, docs and articles. Not to app screens behind login.
- Put an `/llms.txt` at the site root that summarizes the site and links the key pages.
- Optionally offer markdown versions of content pages: worth it when the page is public,
  content-heavy, meant to be read or cited, and the HTML is heavy. Link them with
  `<link rel="alternate" type="text/markdown" href="...">` and list them in `llms.txt`. The HTML
  page stays canonical, and the markdown versions stay out of the sitemap.
- One source generates the other, never hand-maintain both: generate the markdown from the HTML (or
  the page's source files) in the build, or keep the content as markdown/data and render the HTML.
- For dynamic public content (e.g. products or articles from a CMS), render the markdown from the
  same data as the HTML, on its own route (e.g. `/products/123.md`) or via `Accept: text/markdown`.
- Screens behind login need none: the API is the machine-readable version (see AI-First in
  `backend.md`), and the accessibility tree covers agents that operate the UI.
- The server must serve `.md` as `text/markdown; charset=utf-8` (e.g. `AddType` in Apache, a
  headers rule on other hosts). Otherwise it may download or garble non-ASCII text. Verify with
  `curl -I`.

This list is the floor, not a full audit. For anything beyond it, a real WCAG or Lighthouse pass is
the right tool, not a hand-maintained checklist.

## SEO and sharing (public pages)

Public pages only. App screens behind login get `noindex` or are simply not linked or listed. The
canonical URL, `lang`, JSON-LD and server-rendered content are in the baseline above.
- Title: unique per page, under about 60 characters, most specific phrase first, site name last.
- Meta description: 150-160 characters, written for people, not keywords.
- Open Graph and Twitter Card: `og:title`, `og:description`, `og:url`, `og:image`, `og:image:alt`,
  and `twitter:card` set to `summary_large_image`. Image URLs are absolute. The image is
  1200x630 with text that stays readable as a small thumbnail.
- `sitemap.xml` lists canonical URLs only. `robots.txt` points to it with a `Sitemap:` line. Pages
  that shouldn't be indexed (404, thank-you, internal) get `noindex` and stay out of the sitemap.
- Use a display name for humans ("Acme Notes") and keep the slug for URLs and identifiers.
- Before launch: paste the URL into a share preview or Open Graph debugger, validate the
  structured data, submit the sitemap in the search engine's webmaster console (e.g. Google Search
  Console), and check `curl -I` for 200 and the right content types.
- Avoid keyword stuffing, the same title or description on every page, and a share image whose
  text is unreadable at thumbnail size.

## Links: new tab or same tab

Opening external links in a new tab is a UX/product choice, not an accessibility best practice — the
accepted guidance (WCAG 3.2.5, an AAA criterion) only asks that you *warn* the user, not that you do
it. So decide it deliberately:

**Open in a new tab when the user is likely not done with your site — not by a blanket rule.** A
link that continues their journey elsewhere (a linked repo they'll return from, a reference doc)
reasonably opens in a new tab; a link that's the whole point of the visit doesn't need to bring them
back. If you do open in a new tab, pair `target="_blank"` with `rel="noopener"` (security) and warn
before the click — a visible external-link icon for sighted users, an `aria-label` mentioning "opens
in a new tab" for screen readers. Neither cue alone covers both audiences.

**Worked example (this template's landing page):** every link funnels the visitor toward one
destination — the GitHub repo. There's nothing here to return to, so its links stay in the same tab.
The cue is a plain external-link icon on the primary calls to action, signalling "this leaves the
site", with no forced new-tab behavior. Same-tab is the browser's expected default, so it needs no
extra markup.

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

Manual review against this list works but is easy to skip under time pressure. If this project has
a real frontend surface where visual quality matters, evaluate a dedicated design tool as a proper
decision in [`planning/01-stack-decision.md`](planning/01-stack-decision.md) (question 7) — not
silently, per rule 7. The gain from writing this file, though, comes mostly from filling in *your
system* above; the checklist is the safety net, not the plan.
