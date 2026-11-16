# Foundations
> Read before adding configuration, logging, an API endpoint, or frontend data fetching. Rules for
> every project, independent of framework. Larger projects extend them: see
> [`planning/03-extension-points.md`](planning/03-extension-points.md). Secrets and input
> validation: "Security" in `AGENTS.md`. Request flow and error shape: [`backend.md`](backend.md).

## Configuration
- Read environment variables in one place: `core/config`, or a single config file when the project has no `core/`. Nothing else touches `process.env` or its equivalent.
- Validate with a schema at startup. A missing or malformed value stops the process with a message naming the variable.
- Export one typed config object. Modules import that object.
- Commit `.env.example` with every variable and no real values.

## Logging and errors
- Log to stdout, one line per event, structured (key-value or JSON). The platform collects it.
- Log: requests (method, path, status, duration), unexpected errors with stack, and important domain events (created, approved, failed).
- Every request gets an ID. Include it in each log line and in the error response, so a user report maps to one log trail.
- Never log tokens, passwords, API keys, full request bodies or personal data (name, email, national ID). Log an internal ID instead.
- The user sees the shared error shape (`code`, `message`, `hint`), never a stack trace. Unexpected errors return a generic message plus the request ID, with details only in the log.
- A caught error is either handled or rethrown. Don't swallow it.

## API contract
- The schemas are the single source of truth. Routes validate with them and responses are typed from them.
- Generate the OpenAPI spec and the frontend types from the schemas. Don't write either by hand, and don't keep a second copy of a type.
- Pick the generator when the project needs one, and check the dependency first (rule 7).
- A breaking change to a schema updates the frontend in the same change. Where to put the spec: `api-reference.md`.

## Frontend data and state
- **Server state** (data owned by the backend) is fetched in one data layer: composables or hooks, not inline in components. One cache, no copies in local state.
- **UI state** (open menu, form input, selected tab) stays in the component. Put it in the URL when it should survive a reload or be shared.
- Pages or containers fetch. Components in lists receive props (see `code-style.md`, `backend.md`).
- Every fetch has three visible states: loading (skeleton shaped like the content), error (the `message` and `hint` from the API, with a retry) and empty (says what to do next).
- Don't block the whole page for a partial failure. Show the error where the data would have been.
