# `.agent/` — reusable context

This folder holds two of the six context types from
[`../docs/decisions/0001-context-engineering-source.md`](../docs/decisions/0001-context-engineering-source.md):
**Examples** (`examples/`) and procedural **Knowledge** as skills (`skills/`).

## An honest note on tool support

**This is one convention, not a cross-tool standard.** The `.agent/skills/SKILL.md` layout below is
a concrete, workable pattern — but AI tools do not all read it out of the box.

- Some tools have their own skills mechanism and their own location (e.g. under a tool-specific
  config folder). If yours does, treat the files here as the **source of truth** and map/symlink
  them into whatever format your tool expects, rather than duplicating the content.
- Some tools have no skills concept at all. There, these files are still useful as plain docs an
  agent can be pointed at manually.

The point is progressive disclosure — load procedure only when the task needs it. *How* your tool
discovers these files varies; the content and the intent don't. Record your tool's mapping in a
short ADR if it's non-obvious, so the next person doesn't have to rediscover it.

## Layout

```
.agent/
├── skills/                 # Procedural knowledge, loaded only when a task matches
│   └── <skill-name>/
│       └── SKILL.md
└── examples/               # Real code copied from this project, not invented ideals
```

See the README in each subfolder for what goes there and when.
