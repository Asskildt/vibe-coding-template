# Code style

> Read before writing or reviewing code. Short rules that apply to every task are in `AGENTS.md`
> (Working Rules, "Code — Proportional Diffs"). Examples assume a TypeScript stack: adapt them to
> yours.

## TypeScript
- Strict mode. Avoid `any`.
- Use a validation library (e.g. Zod) for 100% of runtime validation, and derive types from the schemas (`z.infer`) rather than writing them twice.
- APIs strictly typed.

## Naming
- **Components / pages:** PascalCase (`ProductCard`, `OrderList`)
- **Routes and services:** camelCase (`orders.routes.ts`, `listOrders`)
- **Hooks / composables:** camelCase with `use` prefix (`useAuth`)
- **Schemas:** PascalCase with `Schema` suffix (`OrderStatusSchema`)
- **DB tables:** snake_case in the database, camelCase in the ORM
- **API enums:** SCREAMING_SNAKE_CASE (`DRAFT`, `PUBLISHED`)
- **Constants:** UPPER_SNAKE_CASE

## Thin Routes / Thin Components
Routes parse input, call the service, return the result — no db calls directly in route files.
Components rendered in lists receive data as props, they don't fetch it themselves (see `docs/backend.md`).

## UI
*Applies only to projects with a user interface. Skip it for APIs, CLIs and libraries.*

- **No hardcoded design values.** The rule and its enforcement are in `docs/design/tokens.md`.
- **Reuse components** from `components/ui/`. Variants and sizes are props, not one-off classes.
- **Pages use a layout shell.** No page structure, landmarks or breakpoints inside a page.
- Scope follows project size: design tiers 1 to 3 in `docs/design/README.md`.
