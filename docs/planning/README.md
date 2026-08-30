# Planning — read this first

This folder holds the thinking that happens **before** any code is written. Six short documents,
filled in order. The point is not waterfall. The point is that a handful of decisions — what we're
building, what stack, where the module boundaries sit — are cheap to make on paper and expensive to
discover halfway through implementation.

Each file should take **10 minutes, not an hour**. If filling one out feels heavier than skipping
it, the file is too long — trim it. Half a page each is the target.

---

## Do you even need this? (the skip-it exit)

**Skip the whole folder if any of these is true:**

- It's a script, a spike, or a throwaway you'll delete in a week.
- It takes less than a weekend, *and* no one but you will touch it.
- You're prototyping to learn, and the code is disposable.

**Go through the chain if any of these is true:**

- It takes **more than a weekend**, or
- **Someone other than you** will use, run, or maintain it, or
- It handles real data, money, auth, or anything with legal weight.

When in doubt, the threshold is: *"Would a wrong structural choice here cost me a rewrite later?"*
If yes, spend the hour it takes to go through the chain. If no, delete this folder and start coding.

There is no shame in skipping. A planning chain applied to a weekend script is exactly the kind of
bureaucracy that makes people skip it when it actually matters. Use it where it pays.

---

## The chain

Fill in order. Each links to the next.

1. **[00-brief.md](00-brief.md)** — what we're building, for whom, why now. Forces the goal to be
   articulated before any tech talk starts.
2. **[01-stack-decision.md](01-stack-decision.md)** — a decision *framework*, not a fixed answer.
   Where the "which language/framework" question is answered, and the answer written up as an ADR.
3. **[02-architecture.md](02-architecture.md)** — a rough sketch of modules, data layers, and
   boundaries. **Explicitly expected to change.** This is *not* `docs/architecture.md` (that one is
   the living truth after coding starts).
4. **[03-extension-points.md](03-extension-points.md)** — the 3–5 growth directions you already
   expect, so future abstractions aren't a surprise. Does not mean building for them now.
5. **[04-milestones.md](04-milestones.md)** — what gets built first, what's deliberately deferred.
6. **[05-deploy-strategy.md](05-deploy-strategy.md)** — where the code lands: platform, environments,
   branch mapping. A decision framework, not committed infra. Extends rule 12.

When the chain is done, `AGENTS.md` and `docs/architecture.md` are written (or generated) from it,
and coding starts.

---

## Why this exists

The split between static context (`AGENTS.md`, always loaded) and dynamic context (`docs/`, loaded
on demand) is the backbone of this whole template. The reasoning — and the six context types it
comes from — is recorded once in
[`docs/decisions/0001-context-engineering-source.md`](../decisions/0001-context-engineering-source.md).
Read that if you want the *why* behind the folder layout.

---

## Ownership

Treat these files as code — versioned, owned, reviewed. Each carries an owner and a date so it
doesn't rot silently.

- **Owner:** {name / role}
- **Last updated:** {YYYY-MM-DD}
