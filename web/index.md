<!-- Generated from index.html by scripts/build-index-md.py. Do not edit by hand. -->

Canonical page: https://vibe.asskildt.eu/

# Plan before you vibe-code

An `AGENTS.md` template and a short planning chain. Give your coding agent real context to work from, and settle the decisions worth making before the first line of code.

Repository: https://github.com/Asskildt/vibe-coding-template

## Start here

Try it with the prompts below, from scratch or on an existing project.

### New project

```text
I want to start a new project (roughly: what it is). Use github.com/Asskildt/vibe-coding-template as the framework. Copy its files in, then read AGENTS.md and docs/planning/README.md. Before any code, ask me what you need to understand the project: the goal, who it's for, the constraints. Decide with me whether it needs the planning chain (it has a skip-it threshold). Walk me through the planning one step at a time instead of guessing, then fill in the AGENTS.md placeholders. Don't start building until we've agreed on the plan.
```

### Existing project

```text
I have an existing project and want to adopt the conventions from github.com/Asskildt/vibe-coding-template where they fit. First read the conventions there, at least AGENTS.md, docs/backend.md, docs/design.md, docs/ai-workflow.md, and docs/planning/README.md. Then read my project properly: not just the top-level files, but the real structure, the main modules, config, and any existing docs, so your read is grounded in how it actually works. Then talk it through with me: propose which conventions are worth adopting and which don't fit, and whether to copy files in or just borrow ideas. Don't change anything until we've agreed.
```

### Take just one part

Each prompt below pulls in one part of the template and leaves the rest.

#### Writing rules

```text
I want the writing rules from github.com/Asskildt/vibe-coding-template. Read the sections "Writing — Precision Over Volume" and "User-Facing Text — Avoid AI Signals" in https://raw.githubusercontent.com/Asskildt/vibe-coding-template/main/AGENTS.md. Then put the rules where your instructions live. In a coding agent, add them to my project's AGENTS.md or CLAUDE.md. In a chat assistant, condense them into custom instructions that fit the character limit: keep the rules, drop the explanations. The examples in the AI-signal list are Norwegian, so adapt them to my language. Show me the result before you save or add anything.
```

#### Code discipline

```text
I want the code discipline rules from github.com/Asskildt/vibe-coding-template. Read the section "Code — Proportional Diffs" and Working Rules 2 ("Stop instead of hammering"), 4 ("Simplicity first") and 10 ("Replace means delete") in https://raw.githubusercontent.com/Asskildt/vibe-coding-template/main/AGENTS.md. Compare them with the instruction file I already use, then propose adding only what is missing or conflicts with mine. Don't duplicate rules I already have. Don't change anything until we've agreed.
```

#### Fact-checking

```text
I want the source-checking routine from github.com/Asskildt/vibe-coding-template. Read https://raw.githubusercontent.com/Asskildt/vibe-coding-template/main/.agent/skills/verify-sources/SKILL.md. Add it to my project in the form my tool supports: a skill file if it has skills, otherwise a short section in my instruction file. Adapt the trigger to the kinds of claims my project publishes. Ask me before you add anything.
```

#### Agent-friendly APIs

```text
I want my API to be easy for AI agents to use, following github.com/Asskildt/vibe-coding-template. Read the section "AI-First: Make the System Navigable for Agents" in https://raw.githubusercontent.com/Asskildt/vibe-coding-template/main/docs/backend.md. Then read how my API actually returns errors, paginates lists and formats dates, enums and IDs. Show me where it differs from those rules, starting with error responses that don't tell the caller what to do next. Propose changes in order of impact. Don't change anything until we've agreed.
```

#### UI and accessibility

```text
I want to review my frontend against the design rules in github.com/Asskildt/vibe-coding-template. Read https://raw.githubusercontent.com/Asskildt/vibe-coding-template/main/docs/design.md, mainly the sections "Your system (fill in — this is what the agent should match, not invent)", "Accessibility & machine-readability (baseline)" and "Avoid AI Tells". Then read my actual UI code: styles, components and the main pages. Tell me whether I have a real design system or the agent is inventing one, and draft it from what the code already does if it's missing. Then list accessibility gaps and generic AI-looking patterns, worst first. Don't change anything until we've agreed.
```

#### SEO and sharing

```text
I want my public pages to show up well in search and look right when shared, following github.com/Asskildt/vibe-coding-template. Read the section "SEO and sharing (public pages)" and the "Public, content-heavy pages" part of "Accessibility & machine-readability (baseline)" in https://raw.githubusercontent.com/Asskildt/vibe-coding-template/main/docs/design.md. Then check each public page: title, description, canonical URL, Open Graph tags and image, structured data, sitemap.xml, robots.txt and llms.txt. Leave pages behind login out. Give me a short table of what's missing or wrong per page, and propose fixes. Don't change anything until we've agreed.
```

## 01 What it is

Good results come from planning the work and keeping the codebase tidy, so the agent can navigate it and grasp how the system fits together. On bigger projects it also needs to know what you're building before it starts, or you burn expensive tokens on code that gets rewritten. The bigger the project, the more this pays off.

What you get is plain Markdown: a short `AGENTS.md` holding the rules that apply everywhere, a planning chain for the decisions worth making up front, decision records, and checklists for design, accessibility and AI workflow. Nothing to install, no dependencies, and it works with whichever agent you already use.

- The agent works from real context, not guesses, so there's less to undo.

- Decisions get written down once, not re-argued three sessions later.

- The always-loaded core stays short, so unused context costs you nothing.

## 02 Six context types

Every piece of context has one home, so nothing gets lost or duplicated. The six types come from Google's 2026 report on agentic engineering, and the repo records that source in a decision record rather than leaving it as folklore.

- **Instructions:** `AGENTS.md`. Always loaded, kept short.

- **Knowledge:** `docs/`. Loaded when a task needs it.

- **Memory:** ADRs. Why a choice was made.

- **Examples:** Real code from the project, not invented.

- **Tools:** MCP and API definitions, plus when to use them.

- **Guardrails:** Hooks, lint rules, the security section.

## 03 The planning chain

Six short documents, filled in order before coding starts, about ten minutes each. Small project? The chain tells you to skip it.

1. **Brief.** What we're building, for whom, why now.

2. **Stack decision.** A set of questions to answer, not a fixed answer.

3. **Architecture sketch.** Rough, and expected to change.

4. **Extension points.** Growth you expect, without building for it yet.

5. **Milestones.** Build order, and what waits.

6. **Deploy strategy.** Where the code lands.

## 04 Get it

Copy the files in, or use the repo as a GitHub template. Start with `docs/planning/README.md`: it tells you when to run the chain and when to skip it. Everything is [MIT licensed](https://github.com/Asskildt/vibe-coding-template/blob/main/LICENSE).

[View on GitHub](https://github.com/Asskildt/vibe-coding-template)

Built at [asskildt.eu](https://asskildt.eu/) / [GitHub](https://github.com/Asskildt/vibe-coding-template) / MIT / 2026
