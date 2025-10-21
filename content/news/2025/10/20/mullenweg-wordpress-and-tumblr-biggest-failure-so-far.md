---
title: "Mullenweg: WordPress and Tumblr — my ‘biggest failure’ so far"
slug: "mullenweg-wordpress-and-tumblr-biggest-failure-so-far"
date: 2025-10-20T16:21:50Z
category: "ai"
translationKey: "7dd70dc2c082c409ed8b7ae2672a12d9"
source: "TechCrunch"
source_url: "https://techcrunch.com/2025/10/20/automattic-ceo-calls-tumblr-his-biggest-failure-so-far/"
author: "TechCrunch"
analysis_by: "Metaadvisor.eu"
image_url: "/images/tumblr.png"
featured_image: "/images/tumblr.png"
image: "/images/tumblr.png"
thumbnail: "/images/tumblr.png"
image_alt: "Tumblr — logo, illustrative"
image_credit: "Illustrative image."
tags: ["tumblr", "wordpress", "automattic", "matt mullenweg", "migration", "wordpress backend", "fediverse", "activitypub", "open source", "cms", "technology", "restructuring", "monetization", "saas", "cloud", "cdn", "seo", "id mapping"]
summary: "Automattic CEO Matt Mullenweg calls the Tumblr acquisition — and its continued separation from WordPress infrastructure — his 'biggest failure'. The large-scale move to a WordPress back end is paused but remains the strategic goal."
---

WordPress co-founder and Automattic CEO **Matt Mullenweg** said out loud what many suspected: acquiring **Tumblr** and failing to fully merge it into the **WordPress infrastructure** remains his “**biggest failure so far**.” A failure — but **not a surrender**. The vision stands: move Tumblr onto the WordPress back end, simplify development, cut costs, and plug Tumblr deeper into the **fediverse**. The plan is currently **paused** — too costly and complex for Tumblr’s state today — yet the strategic endgame is intact.

## Why the plan has stalled for years
**Technical debt** and **divergent stacks**: over time, Tumblr and WordPress.com built separate systems for identity, media storage, comments, recommendations, and moderation — doubling code, teams, and maintenance. Then there’s **scale**: **hundreds of millions of blogs**, billions of URLs, slugs, images, GIFs, and videos across very different Tumblr eras.

Economically, the reality bites: Tumblr **spends more than it earns**. Ads and subscriptions don’t cover operating costs. Automattic has **cut spend**, shifted people into healthier lines (WordPress.com, WooCommerce, Jetpack), and timed migration work so it **doesn’t jeopardize** the profitable core.

## What a WordPress back end would actually bring
- **One platform instead of two**: shared auth, media, billing, anti-spam, security & observability — less technical debt, faster time-to-feature.  
- **Economies of scale**: shared teams and tools, stronger CDN/caching, unified storage, lower unit costs.  
- **Cleaner data pipelines**: standardized APIs, stable schemas, easier A/B testing across both services.  
- **Path to the fediverse**: once the core is consolidated, **ActivityPub** becomes more robust and interoperability with decentralized social grows.

## Biggest technical risks
1. **ID mapping & permanent redirects:** any shift in permalinks/IDs needs precise mapping, or **SEO and social signals** suffer.  
2. **Media migration & deduplication:** Tumblr is media-heavy (especially GIFs). Requires aggressive **caching**, **dedup**, and cold storage for legacy sets.  
3. **Comments, reblogs, notes:** Tumblr’s social layer; semantics must survive for community health.  
4. **Moderation & security:** fast mod tools, anti-spam, and protection against hostile campaigns.  
5. **Privacy & compliance:** **GDPR**, retention policies, and media licenses before retro-migration; clear separation of private/public signals.

<p style="text-align:center; margin:20px 0;">
  <a href="/go/mexc" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:white; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:600; display:inline-block;">
     👉 Trade crypto on MEXC
  </a>
</p>

## Operational recovery plan (phases, no cuts)
**Phase 0 — stabilize costs**  
Standardize CDN, implement aggressive caching, archive inactive media, reduce duplicates, unify observability (logs, metrics, tracing).

**Phase 1 — “new goes forward”**  
Write all **new posts** and media into WordPress services; legacy content remains readable without growing old storage.

**Phase 2 — vertical pilots**  
Migrate **one content type** (e.g., text + images without video) for a limited cohort. Establish the **ID map**; measure loss/perf (TTFB, CTR, retention).

**Phase 3 — horizontal expansion**  
Add formats (video, GIFs, polls), introduce a **comment bridge**, preserve reblog/like semantics. From here, **permanent redirects** and canonical URLs.

**Phase 4 — social layer & fediverse**  
Start with one-way ActivityPub publishing, then two-way flows (follow/replies) with granular privacy and spam controls.

**Phase 5 — clean the long tail**  
Deduplicate legacy media, close edge cases, consolidate analytics and reporting.

## What this means for Tumblr users
The ideal is **Tumblr stays Tumblr**: same look & feel, stronger stability and speed. Changes happen **under the hood** — fewer outages, more consistent feeds. For creators, that means **predictable reach**, better posting tools, and intact URLs through transitions.

## Impact on the WordPress ecosystem
