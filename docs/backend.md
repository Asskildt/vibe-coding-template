# Backend Rules — Performance, Data & Agent-Navigable APIs

> Moved out of `AGENTS.md` (rule 13). Read it before writing code that hits a database, renders
> lists, or defines API responses and errors. The list-fetching and state rules apply to the
> frontend too. Adapt to the stack; delete what doesn't apply.

---

## Request flow

One direction per request, the same in every module: route → service → database.

1. **Route/handler** (`{domain}.routes`): parse and validate input with the module's schema, call
   one service function, map the result or error to an HTTP response through the shared error
   mapping. No domain logic, no db calls.
2. **Service** (`{domain}.service`): domain rules and all db access. Owner-scoped queries have the
   owner ID in `where` (see "Security" in `AGENTS.md`). Throws typed errors, never HTTP responses.
3. **Shared error types** (`core/errors`): the typed errors every service throws, each with `code`,
   `message` and `hint` (shape under "Error Messages Are Instructions"), and the one mapping from
   error type to HTTP status.
4. **Cross-cutting** (`core/middleware`, `core/config`): auth, config and logging. Modules read
   config and the current user from `core/`, never from env vars or request headers directly.

No repository layer, base classes or dependency-injection container by default. Add one when three
concrete cases show what it must handle (rule 4). Folder layout and dependency direction:
[`structure.md`](structure.md).

---

## Performance — Concrete Rules

Follow these for all new code that hits a database or renders lists.

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

The UI side of agent-navigability (accessible controls, state in the URL, `llms.txt`, markdown versions) lives in `docs/design/accessibility.md`.
