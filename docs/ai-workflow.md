# AI workflow

> How to work *with* the agent: which class of model for which job, how to spend tokens, and when to
> drive step-by-step versus hand off a whole task. Loaded on demand, not part of `AGENTS.md`.
>
> - **Owner:** {name / role}
> - **Last updated:** {YYYY-MM-DD}

## Model routing — by capability class, not by name

Route work to a class of model, not a named one. **Model names date themselves; capability classes
don't.** Map the classes to whatever models your tools actually offer in the one table below, and
update *only that table* when a provider ships something new. The routing rules underneath never
change.

### The mapping (the one place that changes)

| Class | Your current model | Notes |
|-------|--------------------|-------|
| **High-reasoning** | {e.g. the strongest model your tool offers} | Slow, expensive, best judgment. |
| **Fast / cheap** | {e.g. a smaller, faster model} | Quick, cheap, good at well-specified work. |

### Routing rules (stable)

**High-reasoning class** — planning, architecture, hard debugging:

- The planning chain (`docs/planning/`) and any architecture decision.
- Debugging where the cause isn't obvious, or that spans multiple modules.
- Anything touching invariants, security, or money.
- Reviewing a risky change before it ships.

**Fast / cheap class** — well-specified, mechanical work:

- Boilerplate, scaffolding, simple CRUD endpoints that follow an existing pattern.
- Test generation against a spec that already exists.
- Formatting, renames, mechanical refactors.
- Anything where the answer is "follow the pattern in the file next door".

Rule of thumb: **the clearer the spec and the more it resembles existing code, the cheaper the model
can be.** Novel judgment goes up a class.

## Token economy

Context isn't free — every token in `AGENTS.md` costs on *every* interaction. Treat context as a
budget:

- **Keep `AGENTS.md` tight.** It's static context, loaded every time (rule 13). Trim rather than
  hoard.
- **Use `.agent/skills/` for task-specific procedure** instead of pushing everything into the static
  file. A skill loads only when its task comes up — progressive disclosure.
- **Link, don't paste.** Point at a `docs/` file or a summary instead of re-pasting a whole file
  into the conversation. Re-pasting the same file repeatedly is the most common quiet token leak.
- **Prune stale context.** If a long thread has drifted, a fresh session with the right `docs/`
  links loaded is often cheaper and sharper than continuing.

## Conductor vs orchestrator

Two ways to work, and the choice depends on how well-defined the task is.

**Conductor (interactive, step-by-step)** — you stay in the loop, reviewing each move:

- Unfamiliar code you don't yet understand.
- Hard debugging where the next step depends on what the last one revealed.
- Anything where a wrong turn is expensive to unwind.

**Orchestrator (hand off a whole task to a background agent)** — you define it, then let it run:

- Well-defined features with a clear spec and an existing pattern to follow.
- Migrations, test generation, mechanical refactors across many files.
- Work where the acceptance criteria are checkable without your judgment mid-flight.

The decision rule: **if you can write down the acceptance criteria completely before it starts,
orchestrate. If the criteria only become clear as you go, conduct.**

**State the scope in the request, either way.** Agents read vague verbs at their widest: "improve
this" can become a rewrite. Say which level you mean: fix errors, tighten, or rewrite; fix the bug,
or clean up the module.

## Verification threshold

Ties directly to the Definition of Done in `AGENTS.md`. One addition specific to model routing:

**The cheaper the model used to generate something, the stricter the verification before it ships.**
Fast-class output following a pattern still has to compile, pass existing tests, and clear lint —
and it earns *less* benefit of the doubt on logic than high-reasoning output does. A green check
comes from a test or a runnable command, never from "it looks right".

---

## References

- [`decisions/0001-context-engineering-source.md`](decisions/0001-context-engineering-source.md) —
  the six context types and the static/dynamic split this workflow assumes.
- `AGENTS.md` — the Definition of Done and rule 13 (short static file) that this file builds on.
