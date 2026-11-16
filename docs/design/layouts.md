# Layout templates (page shells)

> Read when creating a page or screen. Applies from tier 2 (see [`README.md`](README.md)). At tier
> 1, one shared header/footer include and one content width does the same job.

**Agents don't design page layout. They pick a shell and fill its slots.** A page that needs a
shape no shell offers is a decision: add or extend a shell, then use it. Don't build the structure
inside the page.

## Shells

Skeletons below. Layout styles live next to the shell as `{Shell}.css`.

- **AppShell:** authenticated app. Header, side navigation, main, optional aside.
- **PublicShell:** marketing, docs, articles. Header, main, footer.
- **AuthShell:** login, sign-up, reset. Centered narrow column.
- **FocusShell:** checkout, wizard, editor. Minimal chrome, one task.

Keep the set small. Start with the shells the project needs now, not all four. Each shell is a
component with named slots (`header`, `nav`, `default`, `aside`, `footer`), not a page with
copy-pasted markup. List the project's shells under "Your system" in [`README.md`](README.md).

## Skeletons (a starting point)

These are structure specs, not project code: framework-independent HTML with landmarks, a skip
link and named slots. Adapt them to the stack and project. When the project has its own shells,
those replace these skeletons, and `.agent/examples/` points to the real code. Width, gutters and
breakpoints go in `{Shell}.css`, with tokens only.

**AppShell**

```html
<a class="skip-link" href="#main">Skip to content</a>
<header><!-- slot: header --></header>
<nav aria-label="Main"><!-- slot: nav --></nav>
<main id="main" tabindex="-1">
  <!-- slot: title (the single h1) -->
  <!-- slot: default -->
</main>
<aside aria-label="Details"><!-- slot: aside (optional) --></aside>
```

**PublicShell**

```html
<a class="skip-link" href="#main">Skip to content</a>
<header><!-- slot: header --><nav aria-label="Main"><!-- slot: nav --></nav></header>
<main id="main" tabindex="-1">
  <!-- slot: title (the single h1) -->
  <!-- slot: default -->
</main>
<footer><!-- slot: footer --></footer>
```

**AuthShell**

```html
<a class="skip-link" href="#main">Skip to content</a>
<header><!-- slot: header (logo only) --></header>
<main id="main" tabindex="-1">
  <!-- slot: title (the single h1) -->
  <!-- slot: default (the form, one narrow column) -->
</main>
<footer><!-- slot: footer (help and legal links) --></footer>
```

**FocusShell**

```html
<a class="skip-link" href="#main">Skip to content</a>
<header><!-- slot: header (logo, exit link, progress) --></header>
<main id="main" tabindex="-1">
  <!-- slot: title (the single h1) -->
  <!-- slot: default (the one task) -->
</main>
<footer><!-- slot: footer (back and next actions) --></footer>
```

## What a shell owns

- Landmarks (`header`, `nav`, `main`, `aside`, `footer`), one `main` per page, and the skip link
  to it.
- Page width, gutters and the spacing between regions, all from tokens.
- Responsive behavior: breakpoints, when navigation collapses, column changes.
- Sticky and scroll regions.
- The page title slot, where the single `h1` goes.

## What a page owns

Content only: the `h1`, the sections inside `main`, and the data. A page does not set its own
width, define landmarks, or add breakpoints. If it needs to, the shell is missing something.

## Layout primitives

Inside `main`, compose with a few layout primitives instead of ad hoc flex and grid per page:

- **Stack**: vertical rhythm with a token gap.
- **Cluster/Row**: wrapping horizontal group with a token gap.
- **Grid**: responsive columns, preferably with container queries so a component adapts to its
  container, not the viewport.
- **Container**: max width and padding.

Each takes `gap`, `align` and similar props from a closed set that maps to tokens. They live in
`components/ui/` with the other primitives.

## Responsive rules

- Mobile first. Verify at roughly 360, 768 and 1280 px wide.
- Prefer container queries for components and media queries only for shell-level changes.
- No horizontal scroll at 320 px for content. Target size at least 24 by 24 CSS px (WCAG 2.2 AA).
- Breakpoints are tokens or one shared constant, not numbers repeated across files.

## Adding or changing a shell

1. Check whether an existing shell with a slot covers it.
2. Add the shell with the same slot names as the others.
3. Update the shell list under "Your system" in [`README.md`](README.md) and note the change in the PR text.
4. Every page using the shell must still pass the accessibility floor.
