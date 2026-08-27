---
title: "StarkWare Tests Quantum-Resistant Bitcoin Transaction"
date: 2026-08-27T04:14:48Z
category: "crypto"
translationKey: "6b22e108f15390aa94bb3ff19dfdfee7"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/starkware-quantum-resistant-bitcoin-transaction-mainnet?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://s3-images.ctmedia.io/media/article-covers/hi-bitcoins-quantum-problem.jpg"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

StarkWare said the experimental transaction demonstrated quantum-resistant Bitcoin spending without a fork, but it cost up to $200 and required direct miner submission.

StarkWare researcher Avihu Levy has tested an experimental quantum-resistant transaction on the Bitcoin mainnet, in what the company described as the first transaction of its kind.

According to StarkWare, the transaction was confirmed Wednesday in Bitcoin block 964,199. Onchain data shows that it spent a 10,000-satoshi output protected by Levy’s Quantum Safe Bitcoin (QSB) scheme, with MARA Pool mining the block after receiving the transaction through its Slipstream service.

Levy’s paper and code repository said QSB combines hash-based one-time signatures with computational searches that bind an authorization to a specific transaction. The construction is intended to prevent forgery even if a quantum computer breaks the elliptic-curve cryptography Bitcoin uses.

The test moves Levy’s April proposal from theory to an onchain demonstration, showing that Bitcoin’s existing consensus rules can accommodate one form of quantum-resistant spending without a protocol change.

In March, Google researchers estimated that a sufficiently capable quantum computer could theoretically derive a Bitcoin private key nine to 12 minutes after its public key becomes visible. Google said that could allow an attacker to replace a pending transaction during Bitcoin’s confirmation window.

Levy then introduced QSB in April , estimating at the time that generating a transaction would require between $75 and $150 in GPU computation. He described it as a last-resort measure rather than a replacement for protocol-level protections.

StarkWare spokesperson Nathan Jeffay told Cointelegraph that the completed transaction cost “low
