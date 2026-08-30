# 04 — Milestones

> **Build order, and what's deferred on purpose.** Turns the brief, stack, and architecture into a
> sequence. Keep it coarse — phases, not a task tracker.
>
> - **Owner:** {name / role}
> - **Last updated:** {YYYY-MM-DD}

## Phases

Order by dependency and by what proves the riskiest assumption earliest. Build the thing you're most
unsure about first, so you fail cheap if it doesn't work.

### Phase 1 — {walking skeleton}
{The smallest end-to-end slice that proves the core works. Not feature-complete — just proof the
architecture holds. What's in it?}

### Phase 2 — {core feature set}
{The features that make it useful for the primary user from the brief.}

### Phase 3 — {...}
{...}

## Deliberately deferred

{What you're consciously *not* building yet, and why. This is the honest counterpart to the
extension points — the growth directions you named but are choosing not to act on now. Writing them
here stops them from creeping in early.}

- {Feature X — deferred until {condition}.}

## Definition of done per phase

A phase is done on the same terms as any task (see the Definition of Done in `AGENTS.md`): it
compiles, existing tests are green, no new lint errors, docs touched are updated, no dead code left
behind. A phase is not "done" because the code exists — it's done when a test or runnable command
proves it.

> **Milestones vs a living roadmap.** This file is planning *before* — a frozen build order. Once
> the project is in flight, ongoing steering (what's next, what's parked, loose ideas) is a
> different, living document. Add a `docs/roadmap.md` for that when you're actually running the
> project and this frozen list no longer reflects reality — not now.

---

Next: **[05-deploy-strategy.md](05-deploy-strategy.md)** — where the code lands once it's built.
