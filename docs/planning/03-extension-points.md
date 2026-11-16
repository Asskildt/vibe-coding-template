# 03 — Extension points

> **Where this might grow — without building for it now.** This is the deliberate counterweight to
> "simplicity first". The tension is real, so name it instead of pretending it isn't: build the
> simplest thing today, but don't paint yourself into a rewrite when the growth you already expect
> actually arrives.
>
> - **Owner:** {name / role}
> - **Last updated:** {YYYY-MM-DD}

## Likely growth directions

List 3–5 directions the project might realistically grow. **Do not build for these now.** Just name
them, and for each, note the one boundary or data-model choice that must hold if it materializes.

| Direction | Likelihood | What must hold today (cheap now, expensive later) |
|-----------|-----------|---------------------------------------------------|
| {Multi-tenant} | {likely} | {`tenantId` on the data model from day one — the column is free now, adding it later is a migration. Isolation logic stays unbuilt until needed.} |
| {White label / several brands} | {possible} | {Components use semantic tokens only and never hardcode values, so a brand later is a CSS override of semantic tokens. See "Optional: white label" in `docs/design/tokens.md`.} |
| {i18n / new language} | {possible} | {Keep user-facing strings out of logic; don't hardcode copy into components.} |
| {New integrations} | {possible} | {Talk to external services through one adapter seam, not scattered calls.} |
| {More user types / roles} | {?} | {A role field and one authorization checkpoint, not permission checks sprinkled everywhere.} |
| {...} | {?} | {...} |

## When the project grows
Not built now. Each line says when it becomes relevant and where its rules go when it does. Tiers
are the structure tiers A to C in [`../structure.md`](../structure.md).

- **Queues and background jobs:** when work outlasts a request (email, import, reports). Jobs become a module under `modules/`, with a rule file in `docs/` for retries and idempotency. Typically tier B.
- **Caching:** when a measured query or call is too slow. Rules go in `docs/backend.md` (what is cached, how it is invalidated). Measure first.
- **Feature flags:** when you ship unfinished work to production or roll out gradually. Flags are read through `core/config`, never as ad hoc `if` checks. Rules go in `docs/foundations.md`.
- **i18n:** when a second language is real. Copy moves to message files, one lookup function. Rules go in `docs/code-style.md`, UI side in `docs/design/`. Type the messages: the reference language decides the keys, and a missing or extra key in another language fails the type check or build (in TypeScript, for example, `satisfies` on each language file). Add a lint rule against hardcoded text in the UI.
- **Observability beyond logging (tracing, metrics):** when logs no longer explain slow or failing flows across services. Extends "Logging and errors" in `docs/foundations.md`, usually tier C.
- **Multiple tenants:** when a second customer shares the system. Isolation rules already sit in "Security" in `AGENTS.md`. Add tests that prove isolation and a tenant section in `docs/data-model.md`.
- **Event-driven architecture:** when several modules react to the same fact and direct calls form cycles. Events are a public export of the module that emits them. Record the decision as an ADR in `docs/decisions/` first.

## The rule this produces

Build the simplest solution **today**, but choose interfaces and a data model that don't force a
rewrite when directions 1–2 of the five actually happen. Deliberately ignore the other 3–4.

This is a *refinement* of "simplicity first", not a contradiction. That rule already says: don't
introduce an abstraction before three concrete cases have shown what it must handle. This file is
where you write down the cases you *already* expect — so the abstraction, when it comes, isn't a
surprise, and the cheap-now/expensive-later choices (like a nullable `tenantId`) are made on day one
instead of discovered in a migration.

---

Next: **[04-milestones.md](04-milestones.md)** — what gets built first.
