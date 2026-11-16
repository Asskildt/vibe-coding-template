# Security

> Read when the project uses Firebase or Supabase as its backend. General rules are in "Security"
> in `AGENTS.md`. The claims were checked against the official documentation (linked below) when
> written. Re-check before you rely on a detail, since both products change.

## Backend-as-a-service (Firebase, Supabase)

With a backend-as-a-service the browser talks to the database directly. The server side is the
security rules: Firestore and Storage rules in Firebase, Row Level Security (RLS) policies in
Supabase. If a rule is missing or too wide, no other code stops the request.

- **Rules are the only server side.** Treat them as production code: in the repo, reviewed, and changed with the same care as an API.
- **Test the rules in CI.** Run them against the Firebase Local Emulator Suite, or a local Supabase instance, never against the live project. Test both what is allowed and what must be denied.
- **Collections with user data can't be listed.** In Firestore, allow `get` on a document the user owns, and don't allow `list` on the collection beyond the user's own documents. Rules are not filters: a query is rejected unless it can only return allowed documents, so the query must match the rule. In Supabase, enable RLS on every table in an exposed schema and add a policy per operation.
- **A public client key is normal.** The Firebase API key and the Supabase publishable (anon) key identify the project and are meant to ship in the client. Protection comes from the rules, not from hiding the key.
- **Service role keys never reach the client.** The Supabase secret or `service_role` key bypasses RLS. Use it only on a server, as a secret environment variable, never in a `NEXT_PUBLIC_`-style variable or a client bundle. Firebase server SDKs and the Admin SDK also bypass Firestore rules, so they get their access from IAM.
- **Data from the database is untrusted in the client.** Validate it before use, and don't render it as HTML. A user who can write a document can write anything the rules allow.
- **App Check is not rate limiting.** App Check checks that a request comes from your genuine app. It doesn't cap how often a valid client calls. Limiting request volume needs its own mechanism, such as quotas, budget alerts, or a rate limit in a backend function you control.

## Sources

- Firebase, API keys: https://firebase.google.com/docs/projects/api-keys
- Firebase, rules and queries: https://firebase.google.com/docs/firestore/security/rules-query
- Firebase, test rules with the emulator: https://firebase.google.com/docs/firestore/security/test-rules-emulator
- Firebase App Check: https://firebase.google.com/docs/app-check
- Supabase, securing your data: https://supabase.com/docs/guides/database/secure-data
- Supabase, API keys: https://supabase.com/docs/guides/getting-started/api-keys
