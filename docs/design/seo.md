# SEO, sharing and links

> Read for public pages, share previews and external links. Part of the [design system](README.md).

## SEO and sharing (public pages)

Public pages only. App screens behind login get `noindex` or are simply not linked or listed. The
canonical URL, `lang`, JSON-LD and server-rendered content are in the [accessibility baseline](accessibility.md).
- Title: unique per page, under about 60 characters, most specific phrase first, site name last.
- Meta description: 150-160 characters, written for people, not keywords.
- Open Graph and Twitter Card: `og:title`, `og:description`, `og:url`, `og:image`, `og:image:alt`,
  and `twitter:card` set to `summary_large_image`. Image URLs are absolute. The image is
  1200x630 with text that stays readable as a small thumbnail.
- `sitemap.xml` lists canonical URLs only. `robots.txt` points to it with a `Sitemap:` line. Pages
  that shouldn't be indexed (404, thank-you, internal) get `noindex` and stay out of the sitemap.
- Use a display name for humans ("Acme Notes") and keep the slug for URLs and identifiers.
- Before launch: paste the URL into a share preview or Open Graph debugger, validate the
  structured data, submit the sitemap in the search engine's webmaster console (e.g. Google Search
  Console), and check `curl -I` for 200 and the right content types.
- Avoid keyword stuffing, the same title or description on every page, and a share image whose
  text is unreadable at thumbnail size.

## Links: new tab or same tab

Opening external links in a new tab is a UX/product choice, not an accessibility best practice — the
accepted guidance (WCAG 3.2.5, an AAA criterion) only asks that you *warn* the user, not that you do
it. So decide it deliberately:

**Open in a new tab when the user is likely not done with your site — not by a blanket rule.** A
link that continues their journey elsewhere (a linked repo they'll return from, a reference doc)
reasonably opens in a new tab; a link that's the whole point of the visit doesn't need to bring them
back. If you do open in a new tab, pair `target="_blank"` with `rel="noopener"` (security) and warn
before the click — a visible external-link icon for sighted users, an `aria-label` mentioning "opens
in a new tab" for screen readers. Neither cue alone covers both audiences.

**Worked example (this template's landing page):** every link funnels the visitor toward one
destination — the GitHub repo. There's nothing here to return to, so its links stay in the same tab.
The cue is a plain external-link icon on the primary calls to action, signalling "this leaves the
site", with no forced new-tab behavior. Same-tab is the browser's expected default, so it needs no
extra markup.

