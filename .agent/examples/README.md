# Examples

**Real code, copied from this project — never invented "ideal" code.** An example here is a file
that already works in the codebase and shows the pattern new code should follow. The whole value is
that it's real: an idealized example that was never run drifts out of sync with reality and quietly
teaches the wrong thing.

## What goes here

A handful of canonical files that answer "how do we do X in *this* project?":

- `{good-route.ts}` — the shape every route/endpoint should follow.
- `{good-service.ts}` — the service-layer pattern (all DB access, thin routes).
- {...whatever pattern you find yourself pointing at repeatedly.}

## Rules

- **Copy from the codebase, don't write from scratch.** If it isn't running somewhere in the repo,
  it doesn't belong here.
- **Keep it small.** Two or three exemplary files beat a folder no one reads.
- **Update it when the pattern changes.** A stale example is worse than none — it teaches the old
  way with full confidence. This is exactly the "docs are code" upkeep from `AGENTS.md`.
