---
title: "Trader Loses $2 Million From Malicious DEX incident"
date: 2026-07-07T05:58:11Z
category: "news"
translationKey: "7de9c4d08e8e629781c3d0db0b821828"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/trader-loses-2m-in-same-block-backrun-extraction-exploit?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://s3-images.ctmedia.io/media/article-covers/hi-how-to-assess-the-value-of-binance.jpg"
tags: []
_build:
  publishResources: false
  render: never
  list: never
---

One crypto trader noted the $2 million loss could have been prevented had the victim read the transaction route before signing the transaction.

A trader who swapped $2.01 million worth of Ether on a decentralized exchange has been left with just $14,500 worth of tokens after a router directed the order through a low-liquidity pool, allowing an Ethereum block builder to profit massively from a same-block arbitrage trade.

The trader swapped 1,126.44 of Ether (ETH) but only received 5,776 Lighter (LIT) tokens, in a “textbook case of same-block backrun extraction,” according to GoPlus Security.

“This was a real, highly imbalanced backrunner arbitrage, not a classic sandwich attack,” GoPlus Security said. Titan Builder was the biggest beneficiary, walking away with $1.8 million from the transaction, which took place on Monday at 1:59 am UTC.

The incident is a reminder of the risks posed by maximal extractable value (MEV) bots and liquidity routers on top of hackers and scammers, which continue to run rampant in the crypto industry.

To reduce the risk of such incidents, crypto trader Ruslan Khairullin said traders should read the transaction route before signing the transaction.

“This is what happens when you clicked confirm faster than you read the route. Painful lesson to see in a real time.”

The victim’s swap routed approximately 1,117 Ether into a low-liquidity AVAIL/WETH pool on Uniswap v3, causing the trade to execute at roughly 120 times higher than what AVAIL could later be sold for, GoPlus Security said.

After the trader received nearly 6.67 million AVAIL tokens at an inflated price, the router involved, 0x router, sold a small amount of externally sourced AVAIL into the same pool to extract about 1,072 WETH before paying out 1,018 ETH, worth $1.8 million,
