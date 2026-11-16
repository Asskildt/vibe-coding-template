# Architecture
> The living description of how the code is layered and split into modules. Keep it current as the
> code changes (rule 8). The folder rules in [`structure.md`](structure.md) build on it. Not the
> same as the frozen sketch in `planning/02-architecture.md`: don't copy that one here, write what
> exists.
>
> - **Owner:** {name / role}
> - **Last updated:** {YYYY-MM-DD}

## Layers
{One line per layer and what it may depend on. Example: route → service → database, `core/` below
all modules. Request flow: [`backend.md`](backend.md).}

## Modules
{One line each: name, responsibility, public export.}

- {`module-a` — responsibility}

## Where things live
{Where config, auth, logging, errors and the API contract sit. Rules: [`foundations.md`](foundations.md).}

## External services
{Each integration and the one adapter that talks to it. Delete if none.}
