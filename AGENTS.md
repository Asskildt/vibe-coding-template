# AI Agent Guide — Template

> **About this file:** A general `AGENTS.md` template to copy into a new project and adapt.
> Replace `{...}` placeholders, delete sections that don't apply, and keep what fits. Meant
> to cover everything from a small static site to a repo with its own backend, frontend, and
> multiple layers. Start small — add sections when the project actually needs them.
>
> This file is the canonical, English-language source. English is used for section titles and
> directives; Norwegian is kept only where the domain is Norwegian (user-facing copy, the
> AI-signal examples). Domain-language content lives in `docs/`, not here.
>
> **This file loads into every interaction.** Whatever it contains costs tokens each time,
> whether or not it's relevant to the task. Keep it short: delete a section rather than leave it
> "just in case", and move long details into their own files (see "Short file, details in their
> own files" below). A template is meant to be trimmed, not to grow.
>
> **Treat this file as code.** Fill in the fields below and keep them current, so it doesn't rot
> silently:
>
> - **Owner:** {name / role}
> - **Last updated:** {YYYY-MM-DD}
>
> Delete this blockquote once the template is in use.

---

## Project Overview

**What are we building?** — {One or two sentences: what the project is, who it's for, what makes it distinct.}

- **Stack:** {e.g. Hono + TypeScript backend, Drizzle ORM, PostgreSQL. Vue 3 + Nuxt frontend.}
- **Goal:** {The one thing the project has to get right.}
- **Status:** {Planning | early development | in production.} Be explicit whether `docs/` is *design* or *documentation of existing behavior*, so no one mistakes a plan for a fact.

---

## Working Rules

These apply to every task. They come first because they matter most.

1. **Never commit without an explicit request.** `git status` and `git diff` are fine. `git add` and `git commit` require the user to ask. When a task is done, ask: "Want me to create a commit for this?" and suggest a message.
2. **Stop instead of hammering — and save tokens.** If you retry the same thing repeatedly, are unsure of a result, or get stuck: don't brute-force. As a rule of thumb, after two or three failed attempts at the *same* error, stop patching — diagnose the root cause, and if you're still unsure: stop, describe the problem and what you tried, and let the user decide. Many things are faster for a human to check than for an agent. **And when you hit the *same* mistake twice — a forgotten pattern, a broken convention — treat that as the signal to propose a docs update (`docs/` or this file), not just a fix. Repeated agent mistakes are almost always missing context, not model failure.**
3. **Ask, don't guess.** If a decision isn't covered by existing docs or patterns, ask rather than improvise. Never guess at domain logic, numbers, or legal requirements.
4. **Simplicity first.** Build clean, separated modules at the lowest complexity that works. Don't introduce a generic abstraction before three concrete cases have shown what it must handle.
5. **Short, focused files.** A file that does a lot gets split into smaller parts, each with one responsibility. Split rather than let files grow.
6. **Don't over-comment.** Code reflects the current state, not history. Write comments only to explain *why* when it isn't obvious — not what the code does or "changed from X".
7. **Don't add dependencies without clearing it first.** New libraries, frameworks, or heavy tooling get discussed first. Keep the stack small. And verify that a package, library, or API name actually exists (via the lockfile, official docs, or a quick search) before using it — language models sometimes invent plausible names that don't exist.
8. **Keep docs in sync.** Any change that touches an API endpoint, a page, or a domain flow updates the corresponding documentation in the *same* work session. Documentation is code, not an afterthought.
9. **English code, Norwegian domain.** Variables, functions, and comments in English. User-facing text and domain discussion in Norwegian. {Adjust if the project is fully Norwegian or fully English.}
10. **Replace means delete.** When you replace something, delete the old version in the same change — including its tests and unused helper files. Don't leave dead code around "just in case". Git remembers what was there.
11. **Suggest, don't perform, the irreversible.** For actions that are hard to reverse or have broad impact (deleting data, production changes, migrations against real data), the default is to suggest and ask for confirmation — not to execute. Local, reversible changes (editing files, running tests) can be done freely.
12. **Branch workflow:** {Describe what applies — does the agent work directly on the working branch, or create feature branches? Never push to `main`/production without an explicit request. Delete this line if the project is simple enough that it doesn't matter.}
13. **Short file, details in their own files.** This file gives the overview and the rules that apply everywhere. Deep detail — full API reference, data model, migration pipeline, domain knowledge — lives in its own files under `docs/`, linked from here. When a section grows past a few paragraphs, that's a signal to move it out and replace it with a link.

---

## Setup Commands

```bash
{npm install}          # Install dependencies
{npm run dev}          # Dev server
{npm run build}        # Production build
{npm run test:run}     # Test suite, single run (not watch)
{npm run lint}         # Linting
{npx tsc --noEmit}     # Type check
```

{Environment variables in `.env` — see `.env.example`. List the critical ones here.}

### DB Workflow (if applicable)

```bash
# 1. Edit schema
{npm run db:generate}   # 2. Generate migration file
# 3. Review the generated SQL
{npm run db:migrate}    # 4. Run it
```

{Note migration-pipeline pitfalls here — raw SQL that must live in a specific folder, manually
registered migrations, etc. These cost hours if they aren't written down.}

---

## Directory Structure

> This is an *example* layout for the project you're building — replace it with your real one. For
> the template's *own* files (this guide, `docs/`, `.agent/`), see the References section at the
> bottom; that's the map of what's actually here.

{Show the actual structure with one line of explanation per folder. Keep it readable on one screen.}

```
backend/src/
├── index.ts                # Entry point and global router
├── core/                   # Infrastructure: db, middleware, config, shared types
│   ├── db/                 # connection, schema, migrations, seed
│   ├── middleware/         # auth, tenant, error handling, audit
│   └── errors.ts / types.ts
└── modules/                # Domain logic, one folder per domain
    └── {domain}/
        ├── *.routes.ts     # Routes + API definitions (thin)
        ├── *.schemas.ts    # Validation (in/out)
        └── *.service.ts    # Domain logic (all db interaction)

frontend/app/
├── layouts/                # Layouts
├── pages/                  # File-based routing
├── components/ui/          # Reusable UI components
├── composables/ (hooks/)   # Shared logic
└── lib/                    # Utilities
```

**Principle:** Each folder and file has one area of responsibility. New code goes in the right
module, not wherever is easiest.

---

## Code Style

### TypeScript
- Strict mode. Avoid `any`.
- Use a validation library (e.g. Zod) for 100% of runtime validation, and derive types from the schemas (`z.infer`) rather than writing them twice.
- APIs strictly typed.

### Naming
- **Components / pages:** PascalCase (`ProductCard`, `OrderList`)
- **Routes and services:** camelCase (`orders.routes.ts`, `listOrders`)
- **Hooks / composables:** camelCase with `use` prefix (`useAuth`)
- **Schemas:** PascalCase with `Schema` suffix (`OrderStatusSchema`)
- **DB tables:** snake_case in the database, camelCase in the ORM
- **API enums:** SCREAMING_SNAKE_CASE (`DRAFT`, `PUBLISHED`)
- **Constants:** UPPER_SNAKE_CASE

### Thin Routes / Thin Components
Routes parse input, call the service, return the result — no db calls directly in route files.
Components rendered in lists receive data as props, they don't fetch it themselves (see Performance).

---

## Data & State

- **Server state:** {React Query / useFetch / …} — cache with a sensible stale time.
- **Global state:** {Context / Pinia / composables} — only when needed.
- **Local state:** component-local.
- **API contract:** standardize responses and errors. Never return raw exceptions or stack traces to the client.

### Immutability (if the domain requires it)
Data that is final or already handed out is not changed via `UPDATE`/`DELETE`.
Correction happens by creating a new row that references the old one, with a reason, visible in the trail.
Enforce it in the database (constraints/triggers), not just in the application layer.

---

## Performance — Concrete Rules

Follow these for all new code that hits a database or renders lists. They were written after
real problems, not as theory.

1. **Max 2 DB calls per route.** Independent queries run in parallel with `Promise.all` — never wait on one before starting the next if they don't depend on each other.
2. **Never N+1.** Never fetch data inside a loop. Collect the IDs, fetch in one query, build a `Map`.
3. **No per-row relation loading in lists.** If a list needs a summary from a child table, fetch it as one batch query with a hard cap per parent. Full relations only in detail endpoints.
4. **Always paginate with a hard cap.** `{ data, pagination: { total, limit, offset, hasMore } }`. Cap e.g. 200 for CRUD, 500 for reports. Use one shared pagination helper — no home-grown variants.
5. **Select only the columns you need.** `select({ ... })`, not `select()` (SELECT *) in heavy queries.
6. **Lookups outside loops.** Known constants and lookup values are fetched once before the loop.
7. **Header + lines in the same transaction.** Never create a parent and its children in two separate inserts — a failure on the children leaves an orphaned parent.
8. **Idempotent import.** Data that may contain duplicates is imported with `ON CONFLICT DO NOTHING`, not try/catch per row. Batch everything that comes from a file.

**Frontend variant (lists):** a per-item data hook is never called inside a component rendered
in a list — that fires N calls. Batch-fetch at the list level and pass down as props. Verify in
the Network tab that the number of calls doesn't grow linearly with the item count.

**Precision:** don't sum money or physical quantities as `float`. Use integers (the smallest unit,
e.g. cents or grams) or a decimal library. A unit always follows its value — a number without a
unit is meaningless.

---

## AI-First: Make the System Navigable for Agents

Build so an AI agent can understand and operate the system without guessing. Include what fits.

### Error Messages Are Instructions, Not Notices
An error should tell the next attempt what to do. Include:
- `code` — machine-readable (SCREAMING_SNAKE_CASE)
- `message` — what went wrong, with concrete numbers
- `hint` — what the agent should do to fix it (endpoint to call, value to use, action to take)
- `allowedValues` / `affectedField` — when the error is caused by an invalid value

```json
{ "error": {
  "code": "INVALID_STATUS_TRANSITION",
  "message": "Cannot change status from SHIPPED to PENDING",
  "hint": "A shipped order can only move to DELIVERED or RETURNED. Use PATCH /orders/:id/status with one of those values.",
  "allowedValues": ["DELIVERED", "RETURNED"]
}}
```

Make `hint` required at the type level if possible, so the compiler catches errors that lack it.

### Predictable Patterns — No Exceptions
- All list endpoints: the same pagination wrapper.
- All errors: the same `error` shape.
- All dates: ISO 8601 (`YYYY-MM-DD`).
- All enums: SCREAMING_SNAKE_CASE. All IDs: UUID.

### Machine-Readable Documentation
Markdown everywhere. Complete OpenAPI spec available in one call. Examples in every schema.

### Agent Identity and Traceability
Actions performed by an agent are traceable (`createdByAgentId`, a separate marker in the audit log).
An agent never performs an irreversible action without an explicitly configured autonomy level — the default is "suggest".

---

## User-Facing Text — Avoid AI Signals

Text that humans read (UI error messages, descriptions, generated content) loses credibility with
language-model tics. Check for these (examples in Norwegian, since that's the user-facing language):

- **Em dash (—)** in prose — use a period, comma, or «og»/«men».
- **«Ikke bare X, men også Y»** and similar rhetorical pairs.
- **Clichés:** «det er verdt å nevne», «i en verden hvor», «kort sagt», «spiller en viktig rolle».
- **Overblown qualifiers:** «essensielt», «avgjørende», «robust», «helhetlig».
- **Semicolons** in prose — split into two sentences.
- **Decorative emoji** in running text.
- **Over-explaining:** the same point twice with slightly different words.

Does not apply to code comments.

---

## Source Requirements for Factual Claims (for content-heavy / public projects)

> Include this section if the project publishes factual claims humans are meant to trust —
> numbers, statistics, quotes, dates, named institutions. Delete it for pure tools/apps with no
> editorial content.

A claim with a number, an institution, a date, or a quote does not go on the site until the source
has been found and read directly — via `web_fetch` or a search with a hit in the source text itself,
not in an AI-generated summary of the source. If a claim is plausible but not verifiable within
reasonable time, leave it out rather than include it "to be thorough".

The reason is concrete: a language model that can't find a real answer tends to construct a
plausible-sounding one instead — precise numbers and a formal citation that, on inspection, exist
nowhere. Precision makes a fabricated claim *more* convincing, not less. So verify against the
primary source, not against a summary.

If the sources point a different way than you expected, it's the claim that changes — not the
sources that get dropped.

---

## Testing

Don't create new test suites unprompted. But the tests that *exist* are the contract the code must
hold: always run them, and lean on them as proof. Add a test unprompted when you fix a bug a test
would have caught. Test behavior, not implementation details.

- **Run once, not watch:** `{npm run test:run}`. Watch mode blocks.
- **Deep where it matters** (core logic, invariants, legal requirements), light for API endpoints.
- **No checkmark without proof.** A roadmap item is marked done only when a test or runnable command proves it. Written-but-unverified code is not done.

### Definition of Done
A task is done when all of this holds — not before:

- [ ] Code compiles / builds without errors (`{npm run build}`)
- [ ] Existing tests are green (`{npm run test:run}`)
- [ ] No new linting errors (`{npm run lint}`)
- [ ] Documentation touched by the change is updated in the same session
- [ ] No dead code or replaced files left behind

### What Not to Spend Time On
- **Don't run type-check/build after every file.** Run it *once* when all changes are done.
- **Don't start the dev server.** It blocks, and the user runs it themselves.
- **Don't verify that something "looks right".** Verify that it compiles and the tests are green. Leave visual judgment to the user — it's faster for a human. (Reading output to debug *logic* is still fine.)

---

## Security

- **Auth:** explicit. A dev bypass requires a named flag that cannot be combined with production.
- **Tenant/user isolation:** every `update`/`delete`/`findFirst` against a table with an owner ID has it in the `where` — even when the ID comes from an earlier scoped read. That makes the rule greppable. Prefer RLS at the database level where the platform supports it.
- **Secrets:** environment variables only, never in code. Don't echo secret values in responses.
- **CORS:** allow-list, never wildcard in production.
- **Input:** sanitize and validate everything from outside. Parameterized queries, never string interpolation in SQL.

---

## Traps

> Things that cost hours if you don't know about them. Fill in the real ones as they surface —
> a problem that's known but not written down disappears. Write the concrete consequence, not
> just the rule.

- {Example: «Rå SQL må ligge i `drizzle/`, ellers kjører migrasjonen aldri — uten feilmelding.»}

---

## Known Limitations

> Technical debt that exists in the code, with the reason it stands. **Update this section when
> you discover something, or when something is fixed.** Prefer striking through resolved items
> over deleting them, so the history stays visible.

- {Example: «Ingen ekte auth ennå — dev-bypass gjelder til JWT er koblet på.»}

---

## Key Principles (Short Version)

- **Simplicity first** — lowest possible complexity until the spec demands more.
- **Ask, don't guess** — ask rather than improvise on what isn't covered.
- **Suggest the irreversible** — propose and confirm before actions that are hard to reverse.
- **Performance by default** — `Promise.all`, no N+1, always paginate.
- **Keep docs in sync** — documentation is updated in the same task as the code.
- **Never commit without asking** — `git diff` yes, `git commit` only on request.
- **English code, Norwegian domain** — code in English, user-facing text and domain in Norwegian.

---

## References

This is the map of the template's own files — the authoritative, up-to-date index of what's here
and where. Each is loaded on demand, not part of this file (see rule 13). {As you add or remove
docs, keep this list current; it's the one place that's meant to stay complete.}

**Before building (planning phase — see the threshold in `docs/planning/README.md`):**

- `docs/planning/README.md` — when the planning chain applies, and the skip-it exit
- `docs/planning/00-brief.md` — what we're building, for whom, why now
- `docs/planning/01-stack-decision.md` — decision framework for language/framework choice
- `docs/planning/02-architecture.md` — frozen rough sketch (distinct from the living `docs/architecture.md`)
- `docs/planning/03-extension-points.md` — deliberately anticipated growth directions
- `docs/planning/04-milestones.md` — build order and what's deferred
- `docs/planning/05-deploy-strategy.md` — deploy platform, environments, branch mapping (decision framework)

**While building (living truth):**

- `docs/architecture.md` — layering and module structure, kept current
- `docs/domain.md` — domain terms, abbreviations, business rules (Norwegian domain lives here)
- `docs/data-model.md` — entities, relations, invariants
- `docs/api-reference.md` — OpenAPI spec or generated docs
- `docs/ai-workflow.md` — model routing by capability class, token economy, conductor vs orchestrator
- `docs/design.md` — this project's design system + a checklist for avoiding AI tells in UI
- `docs/decisions/` — ADRs ("why X over Y"), starting with the context-engineering source
- `docs/traps.md` / `docs/known-limitations.md` — moved out of this file when those sections grow

**Reusable context (tool support varies — see `.agent/README.md`):**

- `.agent/skills/` — procedural knowledge loaded only when a task matches; see `.agent/skills/README.md` for what a skill *is*
- `.agent/examples/` — real patterns copied from the codebase, not invented ideal code
