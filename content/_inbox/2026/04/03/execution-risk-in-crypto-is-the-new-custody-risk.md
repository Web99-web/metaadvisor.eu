---
title: "Execution Risk In Crypto Is The New Custody Risk"
date: 2026-04-03T15:00:00Z
category: "crypto"
translationKey: "d642127f11c6524eabbf42d4a6dc1cf8"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/execution-risk-is-new-custody-risk?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://zoa.cointelegraph.com/pixel?postId=257052&regionId=1"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

Execution risk in crypto is the new custody risk. Live credentials, not just private keys, are now the main attack surface.

Opinion by: Ido Sofer, founder and CEO at Sodot.

The crypto industry is normally well ahead of its game when it comes to pure innovation and functionality, but security is a different matter.

For years, custody risk in crypto was defined by a single fear: the theft of private keys. The industry responded by hardening storage with cold storage, air-gapped systems, MPC and other methods. It then recognized that protecting only the keys is not enough, introducing transaction security and policies to prevent malicious transactions that steal funds, although the keys remain safe. Both of these remain a serious threat, but focusing solely on private keys obscures a deeper shift.

Custody itself has expanded far beyond private keys.

“Custody” once meant protecting private keys. That definition no longer reflects reality. Custody has evolved into a complex, automated system that operates different kinds of transactions, across multiple venues, custodians, vendors and internal systems. Modern trading firms operate across exchanges, staking platforms, liquidity venues and infrastructure providers, each with API keys, validator keys, deployment credentials and system-level secrets that can move capital directly or indirectly.

Many of these credentials are stored in secret managers that, by design, return the full key to any authenticated process. Convenient, yes, but structurally fragile. If the execution environment is compromised, either by an external attacker, an employee that was threatened or a malicious dependency, the full key is compromised. Custody risk has expanded beyond dormant on-chain keys into a live execution layer, where capital moves
