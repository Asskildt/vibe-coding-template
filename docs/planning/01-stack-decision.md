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
