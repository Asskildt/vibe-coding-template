# Skill: verify sources for factual claims

> For content-heavy or public projects that publish claims humans are meant to trust: numbers,
> statistics, quotes, dates, named institutions. Delete this skill for pure tools/apps with no
> editorial content.

## When to use

Before any claim with a number, an institution, a date, or a quote goes on the site or into a doc.

## Steps

1. Find the source. Read it directly, via `web_fetch` or a search with a hit in the source text
   itself, not in an AI-generated summary of the source.
2. Check that the source actually says what the claim says, with the same numbers and wording.
3. If the claim is plausible but not verifiable within reasonable time, leave it out rather than
   include it "to be thorough".
4. If the source contradicts your expectation, change the claim, not the source.

## Traps

- A model that can't find a real answer tends to construct a plausible one, with precise numbers
  and a formal citation that exist nowhere. Precision makes a fabricated claim more convincing.
- A summary or snippet of a source is not the source. Open the page.

## Verify

- Every number, date, quote and institution in the change has a source you read.
- Claims you couldn't verify are removed, not softened.
