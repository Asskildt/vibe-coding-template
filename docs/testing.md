# Testing and Definition of Done

> Read before writing tests, running checks, or reporting a task as done. Replace the `{...}`
> commands with the project's real ones (see "Setup Commands" in `AGENTS.md`).

Don't create new test suites unprompted. Existing tests are the contract: always run them. Add a
test when you fix a bug a test would have caught. Test behavior, not implementation details.

- **Run once, not watch:** `{npm run test:run}`. Watch mode blocks.
- **Deep where it matters** (core logic, invariants, legal requirements), light for API endpoints.
- **Lock behavior before refactoring.** Before you refactor logic that has no tests, write characterization tests that pin down what it does today, known bugs included. Mark a test that pins a bug as such (a name or comment saying "known bug"), so a later fix changes it on purpose.
- **No clock, no randomness.** A test does not depend on the current time or on random values. Pass time and seed in as parameters, or use fake timers. Example: a test that read `Date.now()` passed locally and failed only in CI.
- **No checkmark without proof.** A roadmap item is marked done only when a test or runnable command proves it. Written-but-unverified code is not done.

## Definition of Done
A task is done when all of this holds — not before:

- [ ] Code compiles / builds without errors (`{npm run build}`)
- [ ] Existing tests are green (`{npm run test:run}`)
- [ ] No new linting errors (`{npm run lint}`)
- [ ] Documentation touched by the change is updated in the same session
- [ ] No dead code or replaced files left behind

## What Not to Spend Time On
- **Don't run type-check/build after every file.** Run it *once* when all changes are done.
- **Don't start the dev server.** It blocks, and the user runs it themselves.
- **Don't verify that something "looks right".** Verify that it compiles and the tests are green. Leave visual judgment to the user — it's faster for a human. Agents don't take screenshots by default. The PR lists 3 to 5 things the human should check visually. (Reading output to debug *logic* is still fine.)
