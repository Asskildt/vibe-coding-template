# Adopting the template in an existing project

> Read when you bring this template into a project that already has code. For a new project,
> follow "How to use it" in `README.md` instead. The prompt "Existing project" on the landing page
> points here.

Don't reshape the project in one pass. Work in small steps, each one reviewable and reversible.

1. **Measure where the project differs today.** Check it against the rules in `AGENTS.md` and
   `docs/structure.md`: oversized or mixed-responsibility files, imports against the dependency
   direction, hardcoded design values, missing tests. List what you find under "Known Limitations"
   in `AGENTS.md`, with the reason it stands. Don't mark the files themselves with comments (rule 6).
2. **Copy what fits.** `AGENTS.md`, the `docs/` files the project needs, and `docs/decisions/`
   (with the empty template `0000-template.md`) so the links work. Record each choice to adopt or
   skip as an ADR when someone could ask "why" later.
3. **Lock current behavior before changing logic.** Write characterization tests, known bugs
   included (see `docs/testing.md`). Without them a refactor has nothing to be checked against.
4. **Move mechanically first, change content afterwards.** Moving and renaming files, with imports
   updated, is one step with no logic changes. Splitting, merging and rewriting come in a later
   step. Splitting is judged by rule 5: only when it gives a separate responsibility, reuse or
   testable logic.
5. **One step per task.** One task is one kind of change (a move, a split of one file, a new lint
   rule), small enough to review at once. Verify after each step.
6. **Use limits that can only tighten.** Set a lint or CI limit at today's level (for example the
   number of files over the size where you look harder, or the count of hardcoded colors) and fail
   the build when the number goes up. Lower the limit whenever the count drops. Never raise it.
   Use the project's existing tooling, or a small script, before adding a dependency (rule 7).

For UI values, see "Migrating an existing UI" in `docs/design/tokens.md`.
