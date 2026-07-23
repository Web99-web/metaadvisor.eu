---
title: "Arbitrum-based AFX Trade drained of $24 million after bridge keys compromised"
date: 2026-07-23T05:01:06Z
category: "ai"
translationKey: "ab3a02f48e67018b54a2e94cf520378e"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/07/23/arbitrum-based-afx-trade-drained-of-usd24-million-after-bridge-keys-compromised"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F6923046d9a52fac72269f7dd0d26ff84da658711-3240x1823.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["ai"]
_build:
  publishResources: false
  render: never
  list: never
---

Another week, another multi-million-dollar hack in DeFi, and once again, it’s an off-chain compromise rather than a smart contract exploit.

AFX Trade, a decentralized perpetuals exchange that settles in dollar-pegged stablecoin USDC, was drained of about $24.15 million on Wednesday after an attacker compromised the validator signing keys behind a bridge the protocol operates on Arbitrum, blockchain data shows.

In other words, the smart contract did what it’s supposed to do – verify the signature and execute the transaction. The problem was with the private keys that generated those signatures, as attackers compromised the private validator signing keys (hot keys held offchain by the bridge operators or validators).

Steven Goldfeder, co-founder of Offchain Labs, which develops and maintains the network, said the Arbitrum native bridge "has not been hacked or exploited in any way" and that the transaction originated from a third-party protocol.

A hack of Arbitrum's own bridge would signal risk across the entire layer-2 network, but a compromised protocol running on top of it is a contained failure.

Nothing in the bridge's own code logic was broken. Bridges are blockchain-based tools for transferring tokens between various networks, including those they were not initially supported on.

Security firm Blockaid said the on-chain logic was not bypassed. Instead, five of the bridge's hot-validator signatures, the approvals that authorize a withdrawal, signed off on moving 24,150,000 USDC to the attacker's wallet, clearing the roughly two-thirds quorum the bridge requires.

This incident, therefore, is similar to the roughly $285 million Drift Protocol loss in April, where attackers spent months working their way to privileged access rather than breaking any
