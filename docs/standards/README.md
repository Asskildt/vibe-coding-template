# Standards: how we adopt them and follow them

> Read when considering a new standard, format, tool or platform feature, or when running the
> quarterly review. The current list and its status is [`watchlist.md`](watchlist.md).
>
> - **Owner:** {name / role}
> - **Last review:** {YYYY-MM-DD}
> - **Next review:** {YYYY-MM-DD, three months after the last}

The template should be modern without chasing every announcement. The test for each candidate is
the cost of being wrong.

## Adoption rule: weigh by cost to switch away

Ask two questions: **how mature is it**, and **how much does it cost to remove if it doesn't
become the standard?**

| Switching cost | What it looks like | Bar for adoption |
|---|---|---|
| **Low** | One file or config. Removed by deleting it. An external service with no code in the repo. A progressive enhancement behind `@supports` | Adopt early, once it works and has a primary source. Being modern is worth the small risk |
| **Medium** | A data format or build step. Files are portable between tools. A few days to swap | Adopt when a stable version is published and at least two independent tools support it. Avoid tool-specific extensions |
| **High** | Shapes the architecture, the whole codebase, or the team process. Costly to migrate away from | Adopt only when it is mature: stable spec, broad support, a track record. Otherwise watch |

Rules that follow from this:

- **Adopt the format, not the tool**, where possible. A token format is cheaper to keep than a
  token build tool.
- **A standard in draft is not adopted.** A Working Draft or a feature supported by one browser
  engine goes on the watchlist.
- **A primary source is required** (the spec, the vendor's documentation, the law, the package
  registry). A blog post or a forum thread may point to a question, not settle it.
- **Mark what is unverified.** If a claim could not be checked, say so in the watchlist rather
  than leaving it out (rule 3).
- **Adopting a tool is a dependency decision** (rule 7). Record it as an ADR in `docs/decisions/`
  with the switching cost and the date it was checked.
- **Scale to the project.** A standard that suits a product with a design team may be overhead for a
  landing page. The design tiers in [`../design/README.md`](../design/README.md) and the structure
  tiers in [`../structure.md`](../structure.md) set which apply.

## Quarterly review

Once every three months, or when a project starts from this template, whoever owns the template
runs this routine. Budget a few hours.

1. **Re-check every row in [`watchlist.md`](watchlist.md)** against its primary source. Update
   status, date and verdict. Use the web, not memory: this field moves faster than model training.
2. **Move rows** between "Adopted", "Optional", "Watching" and "Rejected" using the adoption rule.
   Each move gets a one-line reason.
3. **Look for what is missing.** Search for new standards in the areas the template covers:
   design tokens, CSS, accessibility, agent instruction formats, agent skills, MCP, and code-
   structure tooling. Add candidates to "Watching" with the primary source.
4. **Apply adopted changes** to the template docs in the same change. Keep `web/index.html`,
   `web/llms.txt`, the file table in `README.md` and the references in `AGENTS.md` in sync (see
   "Traps" in `AGENTS.md`), and regenerate `web/index.md` with `scripts/build-index-md.py`.
5. **Check links and versions** quoted in the template still resolve and are current.
6. **Update the dates** at the top of this file and in the watchlist.

If a review changes a rule in the template, record the reason as an ADR when the decision is
costly to reverse, or as a line in the watchlist when it isn't.

## Where adopted standards end up

An adopted standard becomes a rule in `AGENTS.md` only if it applies to every task. Otherwise it
lives in the doc that covers its area (`docs/design/`, `docs/structure.md`) with a pointer from
"Read on Demand". The watchlist holds the status and evidence, not the rule itself.
