---
title: "Aptos introduces post-quantum signatures before they’re urgently needed"
date: 2025-12-18T16:40:32Z
category: "news"
translationKey: "68decbd8fc41c469bfce364e7ac0c29d"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/aptos-introduces-post-quantum-signatures-proposal?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://images.cointelegraph.com/cdn-cgi/image/format=auto,onerror=redirect,quality=90,width=1434/https://s3.cointelegraph.com/uploads/2025-12/019b3210-e1b5-74da-81b4-4d6d13af8959.jpg"
tags: []
_build:
  publishResources: false
  render: never
  list: never
---

Aptos has proposed an optional post-quantum signature scheme, citing long-term risks that advances in quantum computing could pose to existing cryptography.

Blockchain network Aptos is moving toward a post-quantum signature option, reflecting growing concern that advances in quantum computing are no longer purely theoretical and could eventually affect how blockchain networks secure accounts and transactions.

On Thursday, Aptos outlined a proposal to introduce post-quantum signatures, addressing the network’s reliance on digital signatures for ownership, transaction authorization and overall security.

While existing cryptographic schemes remain secure against classical computers, researchers warn that sufficiently powerful quantum machines could one day forge them, potentially compromising account security retroactively.

“Quantum computing is not a distant spectre anymore,” Aptos Labs wrote in a post on X, pointing to early discussions around quantum scaling by IBM and growing regulatory momentum, including the publication of post-quantum cryptography standards by the US National Institute of Standards and Technology (NIST).

“This matters for networks like Aptos because Cryptographically Relevant Quantum Computers (CRQCs) can make today’s signature schemes forgeable, possibly breaking security models,” the post said.

In response, developers have proposed AIP-137, an Aptos Improvement Proposal authored by cryptographers at Aptos Labs, which would add support for a post-quantum signature scheme at the account level.

If approved through governance, AIP-137 would introduce SLH-DSA, a hash-based digital signature scheme standardized as FIPS 205, as an optional account signature type. The change would make Aptos one of the earliest production blockchains to natively
