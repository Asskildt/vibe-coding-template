# 05 — Deploy strategy

> **A decision framework, not a fixed answer — same as the stack decision.** This template does
> *not* ship a `docker-compose.yml`, a Railway config, or a Vercel setup. Those are good answers
> *today* and stale answers in two years. Deploy platform is exactly the kind of volatile choice
> the template deliberately keeps out of committed infrastructure. Answer the questions below for
> *this* project, then record the outcome as an ADR in `docs/decisions/`.
>
> This extends rule 12 in `AGENTS.md` (branch workflow): that rule covers how you branch
> internally; this file covers *where the code actually lands* when it deploys.
>
> - **Owner:** {name / role}
> - **Last updated:** {YYYY-MM-DD}

## Questions to answer

1. **Containerized or platform-native?** Some platforms (e.g. Vercel, Railway) build straight from
   the repo with no Dockerfile of your own; others expect a container. Don't add a Dockerfile you
   don't need — but know which model your target uses before you commit to it.
2. **Which branch triggers which environment?** The common shape is `main` → production, and
   `dev`/feature branches → preview/staging. Write down the mapping so it's not folklore. This is
   the deploy-side of rule 12.
3. **How many environments do you actually need?** dev / staging / prod — or is staging overkill for
   a project this size? More environments cost real maintenance; add them when there's a reason, not
   by default (simplicity first).
4. **Secrets and environment variables — where do they live, and how are they rotated?** Never in
   the repo (see the Security section of `AGENTS.md`). Name the store (platform env config, a
   secrets manager) and who can rotate them.
5. **What does a rollback look like?** If a deploy goes bad, what's the one command or button that
   reverts it? A deploy strategy without a rollback path is half a strategy.

## Decision (write as an ADR)

Record the choice in `docs/decisions/` as `NNNN-deploy-on-X.md`:

- **What** you chose (platform, containerized or not, environment/branch mapping).
- **Why** — tied back to the questions above and to the hosting constraint from
  [`01-stack-decision.md`](01-stack-decision.md).
- **What you considered and rejected**, and the reason.

Keeping the *decision* here and the volatile *config* in the project (not in this template) is the
same principle as the stack and model-routing choices: describe the decision, not the fleeting
answer.

---

Planning chain complete. Now write (or generate) `AGENTS.md` and `docs/architecture.md` from these
documents, and start building.
