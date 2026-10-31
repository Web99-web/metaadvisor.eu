# Tag archive policy

This is a local proposal for editorial approval. It has not been deployed.

The additional review is in `audit-2026-10-27-tag-policy-review` beside the repository. It examines all 1,147 previously proposed archives with two to five distinct bodies, plus the seven-article HR `kapital` example. The revised registry retains 1,832 basic indexable language URLs and moves 279 ambiguous, overlapping or incidental-subject archives to noindex. Small archives are not automatically rejected: Bank of America retains its two substantively relevant articles. All 3,978 legacy production-only URLs have a separate HTTP/evidence and migration decision ledger; they are not silently restored, redirected or counted as implemented noindex pages by this registry. Deployment remains gated on handling those routes.

Article `tags` arrays remain editorial metadata. Hugo still generates the existing term URLs. Only archives explicitly present in `data/tag_policy.json` under `archives.<language>` are indexable and included in the sitemap. All other tag terms, including newly published terms, render with `noindex, follow` and a self canonical. Categories are outside this policy.

## Review and promotion

The initial proposal examines every term and its unique news URL membership, distinct source body hashes, title/slug and body word matches, identical membership groups, known entities and editorial themes, and the available GSC exports. This is screening, not a proof of semantic quality or Google indexing. No maximum number of archives is imposed. Low word matching does not prove an article is irrelevant; the review tables retain the article titles and membership for editorial checks.

The full decision table and source evidence are in the sibling audit directory `audit-2026-10-27-tag-policy`. Positive GSC impressions are retained as evidence. Missing performance rows or URL Inspection records mean unknown, not zero lifetime traffic or confirmed exclusion. This project currently has no saved individual indexed tag controls.

To promote a useful new topic, review its members and title, add an entry with `title`, `topic`, and `terms`, and add its language entry to `topics`. Count alone must not promote a future tag. A single original article can justify an exception if its archive has a clear editorial purpose and development plan. Companies, banks, exchanges and crypto projects are eligible under the same review; the seed entity list used in the audit is not a closed permission list.

`title` is the proposed display title in that language. International brands and tickers retain their names. Generic titles outside the explicitly localized topic families are humanized existing tag names and need editorial language review before release. The audit identifies these separately rather than presenting them as professionally translated titles.

## Synonyms and different concepts

`terms` is the explicit union of terms belonging to the primary topic in the same language. Union membership is deduplicated by Hugo page identity. All member article URLs remain, including articles tagged only with a ticker. Source tags are not rewritten. A title such as Bitcoin (BTC) describes the umbrella topic, rather than claiming that the network and asset are identical in every context.

`aliases.<language>` changes article tag links to the primary topic. The old archive keeps its own original membership and URL, with self canonical and noindex. Its page includes a link to the combined topic. No 301, 410 or deletion is activated. Never map an old paginator page N to a new paginator page N without checking its membership and ordering.

Do not automatically equate Ripple with XRP, Binance with BNB, Hyperliquid with HYPE, Tether with USDT, Alphabet with Google, AI safety with AI security, or a hardware wallet with every cold wallet. An identical list of members alone is not proof that two topics are synonyms.

## Navigation and indexing

The tag directory shows the selected primary topics and their union counts. Articles retain every visible tag label. Synonym labels link to their primary archive; other valid term links remain available. A tag without a resolved Hugo term is rendered as text rather than a broken link. Internal search still receives the original tag arrays.

Indexable topic hreflang and the language switch use the explicit topic identity across languages. Paginators use self canonical URLs and only link to language pages with the corresponding paginator. Noindex tag archives omit hreflang metadata; their language switch offers only the current page. Article translation relationships and category metadata are unchanged.

The robots.txt file continues to allow crawling. A crawler must be able to fetch a page to see noindex. Noindex is not a promise that crawling resources will move to articles or that article indexing will recover. RSS feeds and Hugo's existing page-one aliases remain generated; the HTML archive counts in the audit do not count feeds as articles.

## Before a possible production release

1. Approve or revise the archive proposal, localized titles and synonym families.
2. Resolve the separate old-production-only URL inventory; it must not be silently treated as removed by this change.
3. Run a clean build using the pinned Hugo 0.128.0 in the production Linux environment. The Windows validation uses four read-only virtual source mounts. Earlier trailing-dot output failures are checked explicitly in the current validation; consult its actual missing-output count rather than assuming those failures persist.
4. Compare all article/source hashes and URLs, sitemaps, noindex scope, categories, topic members, pagination and links.
5. Obtain explicit authorization for push/deploy and any URL migration. No redirects are included in this proposal.

Rollback should restore only the tag-policy changes from the saved pre-change files, preserving all earlier SEO corrections. Do not reset the repository to HEAD. Deployed noindex changes would also require Google recrawling after rollback; recovery timing cannot be promised.
