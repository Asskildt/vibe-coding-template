# Design tokens, themes and brands

> Read when defining or changing colors, type, spacing, radii, motion, themes, or adding a brand.
> Tier labels refer to [`README.md`](README.md).

## Rule: no hardcoded design values

Components and pages never contain a raw color, font size, spacing, radius, shadow, duration or
z-index. They reference a token. A literal value in component code is a bug, the same way a
hardcoded secret is. Enforce it mechanically where the stack allows (see "Enforcement").

## Two independent axes

A theme is not a brand. Keep them separate, so `brands × modes` works without writing every
combination by hand.

| Axis | Values | Decided by | Switched by |
|---|---|---|---|
| **Mode** | `light`, `dark`, `system` | The user | `data-theme` attribute, persisted |
| **Brand** (white label) | `default`, `acme`, ... | The deployment or the tenant | `data-brand` attribute, or a build-time choice |

Each brand supplies a value for every semantic token in both modes. A brand that skips dark mode
is a decision recorded in `docs/decisions/`, not a silent gap.

## Three token layers (tier 2: semantic only. tier 3: all three)

Tokens reference upward, never sideways or down. A component token points to a semantic token, and
a semantic token points to a primitive.

1. **Primitive** (raw palette and scales). `blue-500`, `space-4`, `radius-2`. Named by what it
   *is*. Components never use these directly.
2. **Semantic** (role). `color-bg-surface`, `color-text-muted`, `color-action-primary`,
   `color-border-focus`. Named by what it is *for*. **This layer is where modes and brands differ**:
   `color-bg-surface` resolves to a different primitive per mode and per brand.
3. **Component** (optional, tier 3). `button-primary-bg`. Added only for a component that needs
   its own value that no semantic token expresses. Do not create one per component by default.

Naming: `category-role-variant-state` in kebab-case, e.g. `color-action-primary-hover`. In CSS the
token is `--color-action-primary-hover`. One name per concept across code, design files and docs.

## Where tokens live

- **Tier 1:** a single `:root { ... }` block of CSS custom properties in the main stylesheet.
- **Tier 2:** `styles/tokens/` with `primitives.css`, `semantic.css`, and the mode overrides.
- **Tier 3:** token source files in DTCG format under `tokens/` (`primitives.json`,
  `semantic.json`, `brands/{brand}.json`), compiled to CSS custom properties by a build step. The
  CSS is generated output: never edit it by hand, and the generated file is exempt from the length
  rule (rule 5).

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
`web/index.html` is a worked reference for this pattern. Copy from it rather than reinventing it.

## CSS baseline

Use CSS features that are Baseline Widely available: cascade layers (`@layer`), container queries,
`:has()`, `color-mix()`, `oklch()`, nesting, subgrid. Use newer features (Baseline Newly, such as
`light-dark()` and `@scope`) only as progressive enhancement behind `@supports`. Do not build
`@function`, `if()`, anchor positioning or cross-document view transitions into the token system
or the layouts: they are not Baseline yet. Check the current status in
[`../standards/watchlist.md`](../standards/watchlist.md) before relying on a feature.

Order styles with `@layer` (`reset, tokens, base, components, utilities`) so specificity fights
are structural rather than ad hoc.

## Adding a brand (tier 3)

1. Copy `tokens/brands/default.json` to `tokens/brands/{brand}.json`.
2. Override semantic tokens only. If a brand needs a primitive that doesn't exist, add the
   primitive, then alias it.
3. Build, then check contrast for every text/background pair in both modes (see
   [`accessibility.md`](accessibility.md)).
4. Components and layouts stay untouched. If a brand needs a component change, that is a new
   variant or a new semantic token, not a brand-specific fork.

## Enforcement (by tier)

| Tier | Check |
|---|---|
| 1 | Review. `grep` for hex colors outside the `:root` block |
| 2 | A lint rule that forbids literal color, spacing and font values outside the token files (for example Stylelint `color-no-hex` and `declaration-property-value-disallowed-list`, or the stack's equivalent) |
| 3 | Tier 2 plus a CI check that every semantic token exists in every brand and mode |

These are examples of tools that exist. Verify the name and version before adding one (rule 7).
