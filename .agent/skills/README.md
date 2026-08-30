# Skills

> **What this is, in short:** a skill is a packaged, repeatable procedure — "how you do this
> specific task" — kept out of `AGENTS.md` so it only costs tokens when the task actually comes up.
> If `docs/` explains what something *is*, a skill explains how you *do* something, the same way,
> more than once.

## Skills vs `docs/` — the distinction that matters

| | `docs/*.md` | `.agent/skills/` |
|---|---|---|
| **Kind of knowledge** | Declarative — what things *are*, why a decision was made | Procedural — *how* you do a specific, recurring task |
| **Example** | "Here's what the data model looks like" | "Here's how you migrate the database, step by step, including the traps" |
| **Loaded** | When the agent needs context on a topic | When a concrete task type is triggered |

Rule of thumb: if it's something you *explain*, it goes in `docs/`. If it's something you *do, the
same way, more than once*, it's a skill candidate. A common mistake is pushing everything into
skills because it feels "agent-friendly" — resist that.

## When to write one

Write a skill when a task is all three of:

- **Repeated** — you'd otherwise explain the same procedure again next time.
- **Procedural** — it's a sequence of steps, not a fact to know.
- **Has pitfalls worth capturing** — a wrong order, an easy-to-miss step, a gotcha that cost time
  once and shouldn't cost it again.

If it's none of these — a one-off, or something you'd *explain* rather than *do* — it belongs in
`docs/`, not here. Don't pre-write skills for tasks you haven't actually done twice.

## How loading works

A skill loads in three stages, so the agent isn't carrying full instructions for every skill at all
times:

1. **At startup** — the agent sees only the skill's name and a one-line description. Nearly free.
2. **When a task matches** — the agent loads the full `SKILL.md` for that one skill.
3. **Only if `SKILL.md` says so** — deeper reference material (a separate file, a script) is
   fetched, but only then.

This is the same static-vs-dynamic tradeoff as rule 13 in `AGENTS.md`, applied at the level of a
single task instead of the whole project. See
[`../../docs/decisions/0001-context-engineering-source.md`](../../docs/decisions/0001-context-engineering-source.md)
for where this pattern comes from.

## Format

One folder per skill, each with a `SKILL.md`:

```
skills/
└── migrate-database/
    └── SKILL.md
```

Keep each `SKILL.md` focused on *how to do this one task in this project* — the exact commands, the
order, the traps. Link out to `docs/` for background rather than restating it.

**[`migrate-database/SKILL.md`](migrate-database/SKILL.md) is the reference example for structure.**
Read it to see the shape a skill takes: name, when-to-use trigger, steps, traps, verify.

**It is also a placeholder for content, not a fixed inventory.** There are no other skills here
yet. Replace or delete it once you have a real, recurring task worth capturing — don't treat it as
the one skill this template ships with. It's an example of the *pattern*, not a starter kit.

## A note on tool support

This is one convention for organizing procedural knowledge, not a standard every AI tool
understands natively. Some tools have their own skills mechanism; others have none at all. Check
what your tool actually supports — and if it needs a different format, treat `.agent/skills/` as the
source you translate *from*, not something every tool reads directly. See
[`../README.md`](../README.md).
