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
| {i18n / new language} | {possible} | {Keep user-facing strings out of logic; don't hardcode copy into components.} |
| {New integrations} | {possible} | {Talk to external services through one adapter seam, not scattered calls.} |
| {More user types / roles} | {?} | {A role field and one authorization checkpoint, not permission checks sprinkled everywhere.} |
| {...} | {?} | {...} |

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
