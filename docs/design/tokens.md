# Design tokens and themes

> Read when defining or changing colors, type, spacing, radii, motion or themes.
> Tier labels refer to [`README.md`](README.md).

## Rule: no hardcoded design values

Components and pages never contain a raw color, font size, spacing, radius, shadow, duration or
z-index. They reference a token. A literal value in component code is a bug, the same way a
hardcoded secret is. Enforce it mechanically where the stack allows (see "Enforcement").

## Modes

Color schemes are the `light`, `dark` and `system` modes, switched by the `data-theme` attribute
and persisted (see "Theme support"). The semantic layer holds one value per mode for every token.

## Token layers (tier 1: one `:root` block. tier 2: primitive + semantic. tier 3: + component)

Tokens reference upward, never sideways or down. A component token points to a semantic token, and
a semantic token points to a primitive. Components use semantic tokens only.

1. **Primitive** (raw palette and scales). `blue-500`, `space-4`, `radius-2`. Named by what it
   *is*. Components never use these directly.
2. **Semantic** (role). `color-bg-surface`, `color-text-muted`, `color-action-primary`,
   `color-border-focus`. Named by what it is *for*. **This layer is where modes differ**:
   `color-bg-surface` resolves to a different primitive per mode.
3. **Component** (optional, tier 3). `button-primary-bg`. Added only for a component that needs
   its own value that no semantic token expresses. Do not create one per component by default.

Naming: `category-role-variant-state` in kebab-case, e.g. `color-action-primary-hover`. In CSS the
token is `--color-action-primary-hover`. One name per concept across code, design files and docs.

## Where tokens live

- **Tier 1:** a single `:root { ... }` block of CSS custom properties in the main stylesheet.
- **Tier 2:** `styles/tokens/` with `primitives.css`, `semantic.css`, and the mode overrides.
- **Tier 3:** token source files in DTCG format under `tokens/` (`primitives.json`,
  `semantic.json`), compiled to the same CSS custom properties by a build step. The CSS is
  generated output: never edit it by hand, and the generated file is exempt from the length rule
  (rule 5). Use it when the project syncs with Figma or has a design team.

### DTCG format (tier 3)

The Design Tokens Community Group format 2025.10 is the first stable version. It is a Community
Group Report, not a W3C Standard, and tool support lags the spec. Use the format (`$value`,
`$type`, `$description`, aliases like `{color.blue.500}`) and keep the choice of build tool open.
Avoid tool-specific extensions: they are what makes switching expensive. Tracked in
[`../standards/watchlist.md`](../standards/watchlist.md).

## Theme support (recommended default)

**Support system, light, and dark modes unless you have a specific reason not to.** Most users
expect it, but it is a project decision. Skip it deliberately when the fixed palette is proven in
both contexts, or the surface is trivial (a one-off internal tool). If you skip it, record why in
`docs/decisions/` so "why no dark mode?" isn't re-litigated.

Once you support it, these are firm:

- **`system`** follows the OS via `prefers-color-scheme`. It is the default for a first-time
  visitor with no stored choice.
- **`light` / `dark`** are explicit user choices that override the system preference and persist
  (e.g. `localStorage`).
- **No flash on load.** Apply the chosen theme before first paint: a small synchronous script in
  `<head>`, ahead of `<body>`.
- **`system` stays live.** If the OS switches while the user is on `system`, the page follows
  without a reload (a `matchMedia` change listener).

Design both modes deliberately. Dark mode is its own set of semantic values, not inverted light.
`web/index.html` and `web/styles.css` show this pattern working (tier 1). Read them as a pattern,
not as code to copy.

## CSS baseline

Use CSS features that are Baseline Widely available: cascade layers (`@layer`), container queries,
`:has()`, `color-mix()`, `oklch()`, nesting, subgrid. Use newer features (Baseline Newly, such as
`light-dark()` and `@scope`) only as progressive enhancement behind `@supports`. Do not build
`@function`, `if()`, anchor positioning or cross-document view transitions into the token system
or the layouts: they are not Baseline yet. Check the current status in
[`../standards/watchlist.md`](../standards/watchlist.md) before relying on a feature.

Order styles with `@layer` (`reset, tokens, base, components, utilities`) so specificity fights
are structural rather than ad hoc.

## Optional: white label

Not a default. If the project must ship several brands, override semantic tokens per brand in CSS,
scoped by an attribute or class on `<html>`, with a value for every semantic token in both modes.
Components and layouts stay untouched: a brand that needs a component change is a new variant or a
new semantic token, not a fork. Check contrast for each text and background pair
([`accessibility.md`](accessibility.md)). Record the decision in `docs/decisions/`.

## Enforcement (by tier)

| Tier | Check |
|---|---|
| 1 | Review. `grep` for hex colors outside the `:root` block |
| 2 | A lint rule that forbids literal color, spacing and font values outside the token files (for example Stylelint `color-no-hex` and `declaration-property-value-disallowed-list`, or the stack's equivalent) |
| 3 | Tier 2 plus a CI check that every semantic token has a value in every mode |

These are examples of tools that exist. Verify the name and version before adding one (rule 7).

## Migrating an existing UI

Moving hardcoded values into tokens is a mechanical step. Keep it mechanical.

- **A counter that only goes down.** A check counts hardcoded values (colors, spacing, font sizes) outside the token files and fails when the count rises. Lower the limit as the count drops.
- **Move values unchanged.** Each token gets the exact value it replaces. Don't merge nearly equal colors during the move. That is a separate, later step with its own review, since it changes how the UI looks.
- **Prove nothing changed.** A script resolves every token in every mode and compares it with the value in the old code. Every value must be identical before and after. This gives confidence without screenshots. Write it with the project's own tooling, no new dependency.
