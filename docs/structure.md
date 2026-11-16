# Code structure

> Read before creating files or folders, moving code between modules, or adding an import across
> module boundaries. The short rules are in `AGENTS.md` ("Directory Structure"). This file has the
> detail and the checks.

The goal: a person or an agent opens the repo, reads the folder names, and knows where code
belongs and what it may depend on, without reading the code first.

## Dependency direction

```
modules/*   →   core/        allowed
core/       →   modules/*    never
modules/a   →   modules/b    only through b's public export (index file)
```

- **`core/`** holds infrastructure shared by every module: db connection, config, middleware,
  base types, error classes. It knows nothing about any domain. If `core/` needs something from a
  module, the thing it needs is infrastructure and moves into `core/`, or it is passed in as a
  parameter or interface.
- **A module** is one domain: its routes, schemas, service and tests together. It exposes a small
  public surface through one file (`index.ts`, `__init__.py`, `mod.rs`, the stack's equivalent).
  Everything else in the module is internal.
- **Cross-module use goes through the public export.** Module A never imports `b/b.service.ts` or
  any other internal file of B. If A needs more from B, widen B's public export on purpose.
- **No cycles.** If A and B depend on each other, extract what they share into `core/` or a third
  module, or merge them.
- **Optional features** (billing, email, analytics, an integration) are modules that depend on
  `core/`. `core/` never imports them. Removing a feature is deleting its folder plus the one line
  that registers it.
- **Frontend:** the same direction. `components/ui/` and `lib/` import nothing from pages or
  domain components. Pages import components, never the other way. See
  [`design/components.md`](design/components.md).

## Folder width

When a folder has **10 or more files at the same level**, consider grouping by responsibility
into subfolders. This is a prompt to look, not an automatic split. Leave a flat folder alone when
the files really are peers (ten route files with one shared shape).

- **What counts:** files directly in the folder, including tests, styles and `index` files.
  Subfolders and generated files don't count.

- Group by what the files do (`auth/`, `billing/`), not by type (`helpers/`, `utils/`, `misc/`).
  A `utils` or `helpers` folder that keeps growing is a missing module.
- Prefer a folder per concept once a concept has three or more files (`orders.routes.ts`,
  `orders.service.ts`, `orders.schemas.ts` move into `orders/` and keep their names).
- A folder with one file inside has no reason to exist, unless it is a module's public entry.
- Keep nesting shallow. Past three or four levels below `src/`, the grouping is wrong.
- Folders and files are named for what they hold, in the style under "Naming" in
  [`code-style.md`](code-style.md). A file keeps the domain name (`orders.service.ts`, not
  `service.ts`), so editor tabs and search results are unambiguous.

## Files stay cohesive

Rules 5 and 6 in `AGENTS.md` apply unchanged: one responsibility per file, comments only for *why*.
Line count is a signal to look, not a reason to split. Split when the part gets its own
responsibility, is reused, or holds logic you can test alone. A split that only moves lines
around makes more files, more imports and a bigger total. Files of ten or twenty lines with no
responsibility of their own are a sign of that. New files follow the same dependency direction,
and the split is weighed against folder width above.

## Readable for people and agents

- A file's name says what is in it. An agent should be able to pick the right file from a
  directory listing.
- Prefer explicit imports and named exports over side-effect imports and wildcard re-exports.
  Both hide where things come from.
- Each module may carry a short `README.md` only when its purpose isn't clear from the folder
  name and file names. Don't add one by default (no unrequested artifacts).
- Keep `docs/architecture.md` current when a module is added, removed or changes what it exposes.

## Checks, by structure tier

Structure tier is chosen per project and recorded in `AGENTS.md` (Project Overview). It is
independent of the design tier in [`design/README.md`](design/README.md): a large app with one
brand can be structure C and design 2.

State the checks in the project's `AGENTS.md` setup commands. The tools below are examples:
verify the name and version before adding one (rule 7), and see
[`standards/watchlist.md`](standards/watchlist.md) for their status. For other stacks, use the
equivalent.

| Tier | Project | Checks |
|---|---|---|
| **A** | One small package: static site, script, tool | Review against this file. `wc -l` on changed files. No tooling |
| **B** | One team, one app: a backend, a frontend, or both in one package | Lint rules for file length (ESLint `max-lines`, or equivalent) and import restrictions (`no-restricted-imports` blocking `core → modules` and imports of another module's internal files). Run in the lint command |
| **C** | Several packages or several teams | Tier B plus an architecture check that fails CI on boundary violations and cycles (`eslint-plugin-boundaries` or `dependency-cruiser`), a check for unused files and exports (`knip`) to back "replace means delete", and a folder-width check |

No ready-made rule for folder width is confirmed (listed as unverified in the watchlist). No script
for it ships with the template. This shell one-liner lists folders at the limit and can run in CI:

```bash
find src -type d -exec sh -c 'n=$(find "$1" -maxdepth 1 -type f | wc -l); [ "$n" -ge 10 ] && echo "$n $1"' _ {} \;
```

Record the chosen checks in an ADR when you adopt them. Checks run once in the lint step. Don't
write a parallel checking harness.

## When the rules and the code disagree

Existing code that breaks these rules is listed under "Known Limitations" in `AGENTS.md`, not
quietly copied as precedent. New code follows the rules. Fix old code only as part of a task that
touches it, in a separate change from the feature.
