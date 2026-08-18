---
title: "Ethereum Warns Developers Over Glamsterdam Gas Changes"
date: 2026-08-18T05:12:18Z
category: "crypto"
translationKey: "4c061b26b9f56658d28a7a30dffe695c"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/ethereum-foundation-warns-some-tools-may-break-with-glamsterdam-upgrade?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://s3-images.ctmedia.io/media/article-covers/eth-bitmine-1.jpg"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

Developers have been urged to test on Plataberget before Glamsterdam’s new gas model reaches Ethereum’s other testnets and mainnet.

The Ethereum Foundation (EF) has warned that some wallets, indexers and gas estimators may break because of gas-model changes in the upcoming Glamsterdam upgrade.

On Monday, the EF’s Protocol DevOps team said any tool relying on a hardcoded maximum gas limit “will break” and must be updated. It urged developers to test their systems on Plataberget, a public testnet intended to operate for several months.

According to upgrade tracker Forkcast, Plataberget launched on Aug. 13. Meanwhile, the Glamsterdam fork is scheduled to activate on the network on Thursday, before its deployment on the Sepolia and Hoodi testnets.

The EF’s Protocol DevOps team said EIP-8037 would introduce a separate state-gas dimension for operations that create new state. Under the changes, a plain ETH transfer to an existing account would still cost 21,000 gas, while sending ETH to a new account would incur an additional state-gas charge.

The foundation said developers should revisit software that assumes 21,000 gas covers every ETH transfer or uses only one gas dimension when estimating transaction costs.

Glamsterdam also includes enshrined proposer-builder separation, block-level access lists and increased limits for contract and initialization-code sizes.

Related: Ethereum Foundation hits ‘Glamsterdam’ milestones, names new protocol leads

Cointelegraph is committed to providing independent, high-quality journalism across the crypto, blockchain, AI, and fintech industries.

All news, reviews, and analyses are produced with full journalistic independence and integrity. For more details on our standards and processes, please read our Editorial Policy
