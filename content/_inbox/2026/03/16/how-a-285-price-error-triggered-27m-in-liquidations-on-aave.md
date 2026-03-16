---
title: "How a 2.85% Price Error Triggered $27M in Liquidations on Aave"
date: 2026-03-16T14:39:06Z
category: "news"
translationKey: "08e6e19f960578b070d3fdc93e290736"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/how-a-2-85-price-error-triggered-27m-in-liquidations-on-aave?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://zoa.cointelegraph.com/pixel?postId=255019&regionId=1"
tags: []
_build:
  publishResources: false
  render: never
  list: never
---

A small pricing error in wstETH collateral caused $27 million in Aave liquidations, highlighting the critical role of price oracles and automated risk systems in DeFi.

A temporary 2.85% pricing discrepancy in wstETH collateral triggered about $27 million in liquidations on Aave, showing how even small technical issues can have major financial consequences in automated DeFi lending systems.

The liquidation wave occurred because Aave’s system briefly valued wstETH at about 1.19 ETH instead of its market value near 1.23 ETH, making some borrowing positions appear undercollateralized.

Price oracles are critical infrastructure in DeFi because they feed external market data to smart contracts, determining collateral values, loan health and when automated liquidations should occur.

The root cause was not a faulty price feed but a misconfiguration in Aave’s CAPO risk oracle system, where outdated smart contract parameters created a temporary cap on the token’s exchange rate.

Decentralized finance (DeFi) protocols use automated logic to handle everything from collateral management to risk assessment. While this setup enables a truly open and permissionless financial system, it also means that minor technical issues can snowball into significant financial disruptions.

According to risk monitoring firm Chaos Labs, a market downturn on March 10, 2026, triggered approximately $27 million in liquidations for Aave borrowers, clearly illustrating this vulnerability. In a single 24-hour window, approximately $27 million in user positions were liquidated. Surprisingly, this was not caused by a massive market sell-off but by a brief 2.85% price discrepancy affecting wrapped staked ETH (wstETH) collateral.

This event serves as a stark reminder of how critical price oracles and
