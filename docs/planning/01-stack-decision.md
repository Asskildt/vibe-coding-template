# 01 — Stack decision

> **A decision framework, not a fixed answer.** This template deliberately does *not* recommend a
> language or framework — that would rot, and it would violate "simplicity first". Instead, answer
> the questions below for *this* project, then record the outcome as an ADR in `docs/decisions/`.
> The questions are the durable part; the answer is specific to you.
>
> - **Owner:** {name / role}
> - **Last updated:** {YYYY-MM-DD}

## Questions to answer

Work through these. The answers, taken together, point at a stack far more reliably than starting
from a favourite framework.

1. **Where does it run?** Serverless vs your own server, edge vs a single region. This constrains
   language choice more than anything else — some runtimes are effectively ruled out by the hosting
   target.
2. **What does the team already know?** And what's the real cost of learning something new *for this
   project specifically* — not in the abstract? A stack the team is fluent in usually beats a
   "better" one they'd learn on the job.
3. **Expected scale and concurrency.** Do we need anything beyond a simple monolith? Be honest — most
   projects don't, and premature distribution is expensive.
4. **Real-time needs.** Websockets, streaming, live updates? This drives framework choice more than
   language choice.
5. **How mature is AI-tool support for the stack you're considering?** This is real: some stacks get
   markedly better agent results than others, because of training-data volume and clear, consistent
   conventions. A stack the agent handles well is a force multiplier for this whole template.
6. **Ecosystem maturity for this domain.** Payments, PDF generation, real-time, geo, whatever your
   domain leans on — is there a mature, maintained library, or would you be building primitives?
7. **UI surface and design tooling.** Answer only if there's a real user-facing UI — for an API,
   CLI, or script, skip this one.
   - Is visual quality something users actually judge the project on, or is "functional and
     consistent" enough (an internal admin panel vs a product or landing page people meet)?
   - Is the UI work ongoing or a one-off? A dependency pays off through repetition. One landing
     page rarely needs its own tool; a product built over months might.
   - Is there a documented design system already, or is the agent the only thing standing between
     "nothing specified" and generic AI defaults?
   - Will it support light/dark/system themes? The recommended default is yes — see the theme
     section in `docs/design.md`. If you skip it, that's a decision to record here.

   **Default:** start with the "Avoid AI Tells" checklist in `docs/design.md` — it's free and needs
   no dependency. Consider adopting a dedicated design tool (e.g.
   [Impeccable](https://impeccable.style), a cross-tool skill that runs a deterministic version of
   that checklist against a `DESIGN.md`/tokens file) only if UI work is ongoing *and* the checklist
   isn't keeping up manually — concrete threshold: you check against it more than once a week, or
   you keep hitting the same tell across sessions. Adopting it is a dependency decision like any
   other (rule 7), not a default inclusion.

## Decision (write as an ADR)

Once answered, record the choice in `docs/decisions/` as `NNNN-chose-X-over-Y.md`:

- **What** you chose (language, framework, key libraries).
- **Why** — tied back to the questions above.
- **What you considered and rejected**, and the reason.

That ADR is what makes "why did we pick X?" answerable later without guessing — the exact scenario
the "ask, don't guess" rule and long-term memory (see
[`../decisions/0001-context-engineering-source.md`](../decisions/0001-context-engineering-source.md))
exist to prevent.

---

Next: **[02-architecture.md](02-architecture.md)** — sketch how the chosen stack is arranged.
