---
title: "ETH news: Ethereum’s ‘Glamsterdam’ upgrade aims to fix MEV fairness"
date: 2025-12-20T19:00:00Z
category: "crypto"
translationKey: "e77c4dd805eb97049aa3a6a1419c8cab"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2025/12/20/ethereum-s-glamsterdam-upgrade-aims-to-fix-mev-fairness"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F84f6f9958db6e2cd492c8fb9bfb15de3ba851ae7-3600x2400.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

Ethereum developers, fresh off last month’s successful Fusaka upgrade, which cut down costs for nodes , are already moving full-steam ahead on planning the blockchain’s next major change.

The name is a portmanteau of two simultaneous upgrades taking place on Ethereum’s two core layers. The execution layer, where transaction rules and smart contracts live, will undergo the Amsterdam upgrade, while the consensus layer, which coordinates validators and finalizes blocks, will see an upgrade known as Gloas.

At the heart of Glamsterdam is enshrined Proposer-Builder Separation (ePBS), formally tracked as EIP-7732. The proposal would bake into Ethereum’s core protocol a rule that separates nodes who build blocks from those who propose them, preventing any single actor from controlling which transactions are included or how they are ordered.

Today, this separation largely relies on off-chain services known as relays, which introduces trust assumptions and centralization risks. Under ePBS, block builders would assemble blocks and cryptographically seal their contents, while proposers would simply choose the highest-paying block without being able to see or tamper with what’s inside. The transactions would only be revealed after the block is finalized, reducing opportunities for manipulation and abuse related to MEV, or maximal extractable value — the extra profit validators or builders can make by reordering, inserting or censoring transactions.

Another proposal slated for Glamsterdam is Block-level Access Lists (EIP-7928), an under-the-hood change that allows a block to declare in advance which accounts and smart-contract data it will access. Rather than discovering this information transaction by transaction, Ethereum software — known as clients — can preload and reuse
