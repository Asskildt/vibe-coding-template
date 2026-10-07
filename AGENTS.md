# AI Agent Guide — Template

> **About this file:** A general `AGENTS.md` template to copy into a new project and adapt.
> Replace `{...}` placeholders, delete sections that don't apply. Covers a small static site up
> to a repo with backend and frontend. Start small; add sections when the project needs them.
>
> English is used for section titles and directives; Norwegian only where the domain is Norwegian
> (user-facing copy, writing examples). Domain-language content lives in `docs/`.
>
> **This file loads into every interaction** and costs tokens each time. Delete a section rather
> than keep it "just in case"; move long details into their own files (rule 13).
>
> **Treat this file as code.** Keep these fields current so it doesn't rot:
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

These apply to every task.

1. **Never commit without an explicit request.** `git status` and `git diff` are fine. `git add` and `git commit` require the user to ask. When a task is done, ask: "Want me to create a commit for this?" and suggest a message.
2. **Stop instead of hammering.** After two or three failed attempts at the *same* error, stop patching and diagnose the root cause. Still unsure: describe the problem and what you tried, and hand back to the user. **If you repeat the same mistake (a forgotten pattern, a broken convention), propose a docs update (`docs/` or this file), not just a fix. It is usually missing context.**
3. **Ask, don't guess.** If a decision isn't covered by existing docs or patterns, ask rather than improvise. Never guess at domain logic, numbers, or legal requirements.
4. **Simplicity first.** Build clean, separated modules at the lowest complexity that works. Don't introduce a generic abstraction before three concrete cases have shown what it must handle. See "Code — Proportional Diffs".
5. **Short, focused files.** A file that does a lot gets split into smaller parts, each with one responsibility. **Length:** start splitting around 200 lines and stay under roughly 300. Not a hard limit, but long files are harder to read, review and change safely. Split along responsibilities; don't compress code or text until it becomes unclear. Generated files, lockfiles, migrations and fixtures are exempt.
6. **Don't over-comment.** Code reflects the current state, not history. Write comments only to explain *why* when it isn't obvious — not what the code does or "changed from X".
7. **Don't add dependencies without clearing it first.** New libraries, frameworks, or heavy tooling get discussed first. Keep the stack small. And verify that a package, library, or API name actually exists (via the lockfile, official docs, or a quick search) before using it — language models sometimes invent plausible names that don't exist.
8. **Keep docs in sync.** Any change that touches an API endpoint, a page, or a domain flow updates the corresponding documentation in the *same* work session. Documentation is code, not an afterthought.
9. **English code, Norwegian domain.** Variables, functions, and comments in English. User-facing text and domain discussion in Norwegian. {Adjust if the project is fully Norwegian or fully English.}
10. **Replace means delete.** When you replace something, delete the old version in the same change — including its tests and unused helper files. Don't leave dead code around "just in case". Git remembers what was there.
11. **Suggest, don't perform, the irreversible.** For actions that are hard to reverse or have broad impact (deleting data, production changes, migrations against real data), the default is to suggest and ask for confirmation — not to execute. Local, reversible changes (editing files, running tests) can be done freely.
12. **Branch workflow:** {Describe what applies — does the agent work directly on the working branch, or create feature branches? Never push to `main`/production without an explicit request. Delete this line if the project is simple enough that it doesn't matter.}
13. **Short file, details in their own files.** Rule 5's length numbers apply here too, and this file has one more reason: every line loads in every session, and long instruction files are followed less reliably. It holds the overview and the rules that apply everywhere. Deep detail (API reference, data model, migration pipeline, domain knowledge) lives under `docs/`, linked from here. Move out sections only some tasks need and leave a pointer that says when to read them.

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

---

## Directory Structure

> An *example* layout; replace it with your real one. The template's own files are listed under
> References.

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

## Code — Proportional Diffs

Rules 4, 6 and 10 set the baseline. Also:

- **Diff size follows the task.** A bug fix touches the bug.
- **No drive-by changes.** Don't reformat, rename or "improve" lines outside the task.
- **No speculative code.** No options, parameters, fallbacks or abstractions for needs that don't exist yet.
- **No defense against impossible states.** If types or validation rule it out, don't check again.
- **Catch only what you can handle.** No try/catch that just logs and rethrows.
- **Reuse before writing.** Search for an existing helper before adding one.
- **No unrequested artifacts:** summary `.md` files, demo scripts, extra READMEs.
- **Cut pass on the diff.** Before reporting done, reread it and delete what the task doesn't need.

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
Components rendered in lists receive data as props, they don't fetch it themselves (see `docs/backend.md`).

---

## Read on Demand

Moved out of this file (rule 13). Read the file when the task matches:

- Before writing code that hits a database or renders lists, or defines API responses and errors: `docs/backend.md` (performance rules, state and immutability, agent-navigable errors).
- Before building or changing UI or public pages: `docs/design.md` (design system, accessibility and agent-readable UI, machine-readable content, SEO and sharing).
- Before changing the database schema: `.agent/skills/migrate-database/SKILL.md` (steps and migration-pipeline traps). Only if the project has a database. The skill ships as an example: fill it in, or delete it together with this line.
- Before putting a number, date, quote or named institution in a doc or on the site: `.agent/skills/verify-sources/SKILL.md`. Only for content-heavy or public projects.

---

## Writing — Precision Over Volume

Applies to all text you write: replies, docs, commit messages, PR text, comments, UI copy. The
goal is text people read to the end.

- **Answer first.** Result or conclusion in the first sentence; background after, only if needed.
- **One point per paragraph, said once.** Two sentences making the same point: delete one.
- **Every sentence adds something the reader lacks.** Cut sentences that announce («Her er ...»), restate, or summarize what was just said.
- **Concrete over general.** A number, name, path or example: not «raskere», but «800 ms → 120 ms».
- **Assessments: problems first, plainly.** No praise padding around the findings.
- **Stop when done.** No closing summary, no «si fra hvis ...», no offers of further variants.
- **Don't narrate process or list your changes** unless asked.
- **Length follows content, not effort.** A short question gets a short answer.
- **Structure follows the reader's need.** No fixed template. Answer first; scannable headings only in longer docs.
- **Editing someone else's text: change only what was asked.** A language wash fixes errors and keeps the author's words, rhythm and quirks. It is not a rewrite.
- **Cut pass before finishing.** Reread and delete what the reader doesn't need.

---

## User-Facing Text — Avoid AI Signals

Text that humans read (UI error messages, descriptions, generated content) loses credibility with
language-model tics. Check for these (examples in Norwegian, since that's the user-facing language):

- **Em dash (—)** in prose: use a period, comma, or «og»/«men».
- **«Ikke bare X, men også Y»** and similar rhetorical pairs.
- **Rhetorical setups:** «Resultatet? ...», «Hva betyr dette? Jo, ...».
- **Clichés:** «det er verdt å nevne», «i en verden hvor», «kort sagt», «spiller en viktig rolle».
- **Overblown qualifiers:** «essensielt», «avgjørende», «robust», «helhetlig».
- **Reflexive lists of three** when the content has two or four items.
- **Uniform rhythm:** every sentence the same length and shape. Vary it.
- **Semicolons** in prose: split into two sentences.
- **Decorative emoji** in running text.

**Scope:** this list covers text a *user or visitor* reads: UI copy, generated content, public-facing
docs like the repo `README` and a landing page. It doesn't apply to code comments or internal docs
like this file and `docs/*`. "Writing — Precision Over Volume" applies everywhere.

---

## Testing

Don't create new test suites unprompted. Existing tests are the contract: always run them. Add a
test when you fix a bug a test would have caught. Test behavior, not implementation details.

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
- **Local agent credentials:** token or credential files for agents (e.g. a dev token under `.agent/`) are gitignored before first use.
- **CORS:** allow-list, never wildcard in production.
- **Input:** sanitize and validate everything from outside. Parameterized queries, never string interpolation in SQL.

---

## Files: Free to Edit vs Sign-Off Required

Rule 11 covers irreversible *actions*; this covers protected *artifacts*: settled decisions such as
a signed-off design spec, an approved logo, legal or contractual text. Edit them only after asking.
List the real ones so the boundary is greppable, not guessed.

**Needs sign-off before editing:**

- {`docs/design.md` — the approved design spec}
- {`assets/logo.svg` — approved logo (a color swap via CSS vars is fine; the mark's form is not)}
- {legal / contractual / compliance copy}

**Free to edit:**

- {source under `src/` — following the rules above}
- {`docs/**` — documentation and procedures}
- {tests, config, templates}

---

## Traps

> Things that cost hours if you don't know about them. Fill in the real ones as they surface —
> a problem that's known but not written down disappears. Write the concrete consequence, not
> just the rule.

- {Example: «Rå SQL må ligge i `drizzle/`, ellers kjører migrasjonen aldri — uten feilmelding.»}
- Promptene i `web/index.html` viser til AGENTS.md-seksjoner og filstier ved navn. Gir du en seksjon nytt navn eller flytter en fil, slutter promptene å virke uten feilmelding. Oppdater dem i samme endring.
  `web/index.md` er generert: kjør `scripts/build-index-md.py`, aldri rediger for hånd (pre-commit-hooken sjekker). `web/llms.txt` vedlikeholdes fortsatt for hånd og oppdateres i samme endring.

---

## Known Limitations

> Technical debt that exists in the code, with the reason it stands. **Update this section when
> you discover something, or when something is fixed.** Prefer striking through resolved items
> over deleting them, so the history stays visible.

- {Example: «Ingen ekte auth ennå — dev-bypass gjelder til JWT er koblet på.»}

---

## References

The index of the template's own files, loaded on demand (rule 13). {Keep this list current as docs
change. Once `docs/` passes six to eight files or gains subfolders, add a `docs/README.md` table
of contents.}

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
- `docs/backend.md` — performance rules, state and immutability, agent-navigable errors
- `docs/data-model.md` — entities, relations, invariants
- `docs/api-reference.md` — OpenAPI spec or generated docs
- `docs/ai-workflow.md` — model routing by capability class, token economy, conductor vs orchestrator, delegating to subagents
- `docs/design.md` — this project's design system, accessibility and agent-readable UI, machine-readable content, SEO and sharing, AI-tells checklist
- `docs/decisions/` — ADRs ("why X over Y"), starting with the context-engineering source
- `docs/traps.md` / `docs/known-limitations.md` — moved out of this file when those sections grow

**Reusable context (tool support varies — see `.agent/README.md`):**

- `.agent/skills/` — procedural knowledge loaded only when a task matches; e.g. `verify-sources` (source checks for factual claims); see `.agent/skills/README.md` for what a skill *is*
- `.agent/examples/` — real patterns copied from the codebase, not invented ideal code
