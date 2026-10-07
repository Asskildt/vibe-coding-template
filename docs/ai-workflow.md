# AI workflow

> How to work *with* the agent: which class of model for which job, how to spend tokens, when to
> drive step-by-step versus hand off a whole task, and how to delegate to subagents. Loaded on
> demand, not part of `AGENTS.md`.
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

## Delegating to subagents and workflows

Most agent tools can now hand a task to a subagent that works in its own context and returns only
the result (subagents in Claude Code, Codex, Gemini CLI and Cursor, workflows in Kiro). The formats
differ and change often. These patterns don't.

- **Delegate breadth, do precision yourself.** Broad reading, investigation and independent
  subtasks go to a subagent, which keeps the main session's context clean. A one-line fix costs
  more to brief than to do.
- **The brief stands alone.** A subagent knows nothing of the conversation. Give it the goal,
  exact file paths, decisions already made, what not to touch, and how to verify its own work. Too
  long beats too short.
- **Read before build.** A read-only mapping step on a cheap model before an expensive coding step.
  The coder starts from findings instead of searching.
- **Implement and review in a loop, reviewer last.** The reviewer's verdict ends the loop, so a
  rejection always goes back to the coder. Cap the number of rounds.
- **Set the model per step.** A step without an explicit model often inherits the session's, which
  is usually the most expensive. Route each step by the classes above.
- **A subagent's finding is a claim, not a fact.** Check it against the source before it feeds the
  next step or lands in a doc. Typical failure: a confident, plausible statement about how a tool
  behaves, which turns out to be the opposite of its current documentation. Without a review step,
  that error gets copied into every file the next step writes. Research needs a check too, not
  just code.
- **Parallel only when independent.** Branches that touch the same files conflict. Split by file
  or module, or run them in sequence.

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
