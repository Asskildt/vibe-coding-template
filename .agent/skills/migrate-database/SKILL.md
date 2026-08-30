# Skill: migrate the database

> **Example skill — replace with your real one or delete.** Shows the shape: exact steps, the order,
> and the traps that cost hours if unknown. Delete the `{...}` placeholders once filled.

## When to use

When the schema changes. Do not hand-write SQL migrations — generate, review, then run.

## Steps

1. Edit the schema in `{path/to/schema}`.
2. Generate the migration: `{npm run db:generate}`.
3. **Read the generated SQL before running it.** The generator gets destructive changes (column
   drops, type changes) wrong often enough that this step is not optional.
4. Run it: `{npm run db:migrate}`.

## Traps

- {Raw SQL must live in `drizzle/` or the migration never runs — with no error. If a migration
  "did nothing", check the file location first.}
- {A renamed column is generated as drop + add, which loses data. Edit the migration to a rename
  by hand when that happens.}

## Verify

- {The migration appears in the migrations table.}
- Existing tests are green (`{npm run test:run}`) — schema changes break queries silently otherwise.

## Related

- `docs/data-model.md` — what the schema *means*, as opposed to how to change it.
