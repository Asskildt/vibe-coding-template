# Component system

> Read when creating or changing a UI component. Applies from tier 2 (see [`README.md`](README.md)).
> At tier 1, keep the same habits in plain HTML and CSS classes.

## Placement

Three levels, each importing only from the level below.

```
components/
├── ui/          # Primitives: Button, Input, Badge, Dialog. No domain knowledge, no data fetching
├── patterns/    # Compositions of ui/: FormField, DataTable, EmptyState. Still no domain knowledge
└── {domain}/    # Domain components: OrderCard, ProductList. Live with the module they serve
```

- `ui/` and `patterns/` import tokens and each other (downward only). They never import from a
  domain module, a page, or an API client.
- Domain components may use `ui/` and `patterns/`. A domain component that turns out to be
  generic moves down, and the old copy is deleted (rule 10).
- Before creating a component, search `ui/` and `patterns/`. Reuse before writing. Create a new
  primitive only after the third concrete need (rule 4).

## One folder per component when it has more than one file

```
ui/Button/
├── Button.{tsx|vue|svelte}   # Component
├── Button.css                # Styles, tokens only
├── Button.test.{ts}          # Only if it has behavior worth testing
└── index.ts                  # Public export
```

Other code imports from `ui/Button` (the `index.ts`), never from a file inside it. A single-file
component stays a single file.

## Variants and sizes

Express differences through a small, closed set of props, not through one-off classes or style
overrides at the call site.

- **`variant`** for intent: `primary`, `secondary`, `ghost`, `danger`. Named by role, not by look
  (`danger`, not `red`).
- **`size`** for scale: `sm`, `md`, `lg`. One shared set across all components. `md` is the
  default.
- **State** is not a variant. Hover, focus, disabled, loading, invalid and selected come from
  attributes (`disabled`, `aria-invalid`, `aria-busy`) and styled from them, so styling and
  accessibility cannot drift apart.
- Define the allowed values as a typed union or enum next to the component. Passing a value outside
  the set is a type error, not a silent fallback.
- Do not add a prop for a one-off need. Pass `children` or a slot instead.

## No hardcoded values

Component styles use tokens only (see [`tokens.md`](tokens.md)). No hex colors, no pixel spacing,
no inline `style` with design values, no utility classes with arbitrary values (`w-[13px]`). If no
token fits, that is a signal to add a token or reuse an existing one. It is not permission to
hardcode.

## Contract for every component

- Renders correct semantic HTML and has an accessible name for icon-only controls
  ([`accessibility.md`](accessibility.md)).
- Visible `:focus-visible` state, keyboard reachable.
- Works in every mode and brand with no component-level condition on theme or brand. If the code
  checks `brand === 'acme'`, the design belongs in a token.
- Components in lists receive data as props and don't fetch it themselves.

## Documenting components

Keep a short list in `docs/design/` or in the code (a catalog page, or Storybook if the project
already uses it) of the components in `ui/` and `patterns/`, with their variants and sizes. An
agent should find what exists without reading every file. Adding a catalog tool is a dependency
decision (rule 7).
