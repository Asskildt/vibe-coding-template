## What & why

{One or two sentences: what this change does and why. Link the issue/brief if there is one.}

## How to verify

{The command(s) or steps a reviewer runs to confirm it works. "It looks right" is not verification.}

## Definition of Done

(from `AGENTS.md` — all must hold before merge)

- [ ] Builds without errors
- [ ] Existing tests are green
- [ ] No new lint errors
- [ ] No dead code or replaced files left behind

## Context upkeep

The one checkpoint that keeps context from rotting. Docs are code — reviewed here, not "later".

- [ ] Does this change touch an API endpoint, a page, a domain flow, or a schema? If yes, the matching `docs/` file is updated **in this PR**.
- [ ] Did a decision get made here that a future "why did we do X?" would ask about? If yes, there's an ADR in `docs/decisions/`.
- [ ] Did the agent hit the **same mistake twice** while building this? If yes, the relevant `docs/` file (or `AGENTS.md`) is updated so it doesn't recur — the repeated mistake is the signal, not a calendar date.

## Notes for the reviewer

{Anything risky, any tradeoff you made, anything you're unsure about. Say it here rather than making the reviewer find it.}
