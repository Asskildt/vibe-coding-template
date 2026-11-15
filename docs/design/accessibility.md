# Accessibility and machine-readability

> Read for any UI work. Applies to every tier: it is the correctness floor, not a feature decision.
> Part of the [design system](README.md).

**Target: WCAG 2.2 level AA.** For legal requirements, follow the regulation that applies to the
project and check it with the supervising authority (in Norway: uutilsynet.no) or a legal adviser.
Don't state a legal status from memory (rule 3). WCAG 3 is a Working Draft: follow it, don't adopt it.

## Baseline

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
  [`backend.md`](../backend.md).
- Respect `prefers-reduced-motion`.

**Machine-readable by default**
- Meaningful `alt` text on images that carry information; empty `alt=""` on purely decorative ones.
- Structured data (JSON-LD) where it fits the content type. This mirrors the "Machine-Readable
  Documentation" principle in [`backend.md`](../backend.md), applied to the page itself, not just the API.
- A stable canonical URL, and a `lang` attribute that matches the actual content language.

**Public, content-heavy pages**

Applies to marketing pages, docs and articles. Not to app screens behind login.
- Optionally put an `/llms.txt` at the site root that summarizes the site and links the key pages. It is a proposal, not a standard, with no proven effect on search (see `../standards/watchlist.md`).
- Optionally offer markdown versions of content pages: worth it when the page is public,
  content-heavy, meant to be read or cited, and the HTML is heavy. Link them with
  `<link rel="alternate" type="text/markdown" href="...">` and list them in `llms.txt`. The HTML
  page stays canonical, and the markdown versions stay out of the sitemap.
- One source generates the other, never hand-maintain both: generate the markdown from the HTML (or
  the page's source files) in the build, or keep the content as markdown/data and render the HTML.
- For dynamic public content (e.g. products or articles from a CMS), render the markdown from the
  same data as the HTML, on its own route (e.g. `/products/123.md`) or via `Accept: text/markdown`.
- Screens behind login need none: the API is the machine-readable version (see AI-First in
  [`backend.md`](../backend.md)), and the accessibility tree covers agents that operate the UI.
- The server must serve `.md` as `text/markdown; charset=utf-8` (e.g. `AddType` in Apache, a
  headers rule on other hosts). Otherwise it may download or garble non-ASCII text. Verify with
  `curl -I`.

This list is the floor, not a full audit. For anything beyond it, a real WCAG or Lighthouse pass is
the right tool, not a hand-maintained checklist.

