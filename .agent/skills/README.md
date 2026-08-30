# Skills

Procedural knowledge for **repeated, well-scoped tasks** — "migrate the database", "add an API
endpoint", "cut a release". A skill is loaded only when its task comes up (progressive disclosure),
so it keeps step-by-step detail *out* of the always-loaded `AGENTS.md`.

## When to add one

Add a skill when you catch yourself giving the agent the **same instructions more than once**. That
repetition is the signal — before then, a skill is premature. Don't pre-write skills for tasks you
haven't actually done twice.

## Format

One folder per skill, each with a `SKILL.md`:

```
skills/
└── migrate-database/
    └── SKILL.md
```

Keep each `SKILL.md` focused on *how to do this one task in this project* — the exact commands, the
order, the traps. Link out to `docs/` for background rather than restating it.

> **`migrate-database/` is a single illustrative example, not a complete list.** It ships with this
> template only to show the shape of a `SKILL.md`. There are no other skills here yet — replace it
> with your project's real skills, or delete it, once you have one. Skills only earn their place
> after you've given the same instruction twice (see above).

> Tool support for auto-loading skills varies — see [`../README.md`](../README.md).
