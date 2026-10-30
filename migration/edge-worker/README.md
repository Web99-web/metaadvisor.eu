# Prepared HTTP migration layer — NOT DEPLOYED

Origin: GitHub Pages behind Cloudflare, verified by public DNS and HEAD on 30.10.2026. Static origin configuration is not an HTTP 301 engine. This Worker is a local tested option, not an active rule.

Exact paths are case-sensitive; `/file` and `/images/file` remain separate. Query strings are preserved. The prepared map is flattened and must have no cycles/conflicts. GET/HEAD return actual 301; other methods pass through. Existing RSS `index.xml` responses receive `X-Robots-Tag: noindex, follow`; sitemaps do not. No missing feed is regenerated as an empty HTTP 200.

Cloudflare activation requires Sonja's separate approval, account/plan/request-capacity checks, route selection, initial production tests and rollback plan. Workers Free: 100000 requests/day; scripts up to 64 MiB under current 04.09.2026 change. Bulk Redirects alternative: Free 10000, Pro 25000 records across account lists; existing usage must also fit. RSS headers require a separate supported header layer if Bulk Redirects is used. `_redirects`/`_headers` are Cloudflare Pages features and are not assumed to work on GitHub Pages.

No `_redirects` file is placed in static content, and no HTML refresh is described as HTTP 301. Keep routing behind a short operational rollback window and an approved exact map. Restore original edge configuration to roll back; image/source backups remain outside the published package.
