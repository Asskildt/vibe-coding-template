# 02 — Architecture sketch

> **Rough, and expected to change.** This is a first sketch made before code exists. It *will* be
> wrong in places — that's fine, that's what sketches are for.
>
> **This is not `docs/architecture.md`.** That file is the living truth, kept current as the code
> evolves. This one is frozen at planning time and read as "what we thought going in". Don't confuse
> the two, and don't update this one after coding starts — update the living one instead.
>
> - **Owner:** {name / role}
> - **Last updated:** {YYYY-MM-DD}

## Modules and boundaries

{The main pieces and what each is responsible for. One line each. A boundary is where one module
stops knowing about another's internals — name those explicitly.}

- {`module-a` — responsibility}
- {`module-b` — responsibility}

## Data layers

{Where data lives and how it flows. Database, cache, external services. What's the source of truth
for each entity?}

## Key boundaries that must hold

{The seams the whole design leans on. If these blur, the design falls apart. Example: "the service
layer owns all DB access; routes never touch the DB directly." These become the rules the agent
enforces later.}

## Known unknowns

{What you're unsure about and expect to resolve during implementation. Naming them here beats
pretending the sketch is complete.}

---

Next: **[03-extension-points.md](03-extension-points.md)** — where might this need to grow, and how
do we leave room without over-building?
