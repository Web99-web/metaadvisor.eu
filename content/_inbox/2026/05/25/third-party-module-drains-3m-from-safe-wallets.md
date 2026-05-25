---
title: "Third-Party Module Drains $3M From Safe Wallets"
date: 2026-05-25T15:26:20Z
category: "ai"
translationKey: "b1765d774c4fe418916f95d4b5e85dec"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/squid-safe-labs-third-party-module-3-2-million-exploit?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://s3-images.ctmedia.io/media/article-covers/hi-how-scammers-exploit-trusted-platforms-for-crypto-fraud.jpg"
tags: ["ai"]
_build:
  publishResources: false
  render: never
  list: never
---

A third-party module drained about $3 million from Safe wallets, with Squid attributing the incident to an external Safe module, saying its core systems were unaffected.

A suspected third-party Safe module exploit has drained about $3.2 million from wallets across Ethereum and Base, with multiple teams pointing to an external module as the cause.

Blockchain security platform Blockaid reported the incident on Monday, saying it involved a contract labeled “SquidRouterModule,” which initially led to confusion over a possible link to the cross-chain protocol Squid.

Squid later said on X that the issue was unrelated to its core protocol and instead involved a third-party module integrated into Safe wallets.

“A third-party SquidRouterModule was exploited, not Squid’s Router contract,” Squid said, adding that the contract shares its name but not its code.

The incident highlights how a trusted wallet module can be used to move funds if it has been granted broad execution permissions within a smart account.

Safe, formerly Gnosis Safe, is a multi-sign wallet running on multiple networks, which requires a minimum number of users to approve a transaction before execution.

It can also be extended with optional modules, which are smart contracts that allow approved code to execute actions on behalf of the wallet.

Related: DeFi hacks shake institutional confidence as risks outpace yields

According to Blockaid, the attack affected at least 86 Safe accounts within roughly two hours, with all stolen tokens swapped to Dai (DAI) via attacker-controlled Uniswap V3 pools.

The suspected root cause is a vulnerability in SquidRouterModule, which allegedly allowed the attacker to impersonate authorized delegates and trigger unauthorized token swaps, Blockaid said.

Safe Labs CEO Rahul
