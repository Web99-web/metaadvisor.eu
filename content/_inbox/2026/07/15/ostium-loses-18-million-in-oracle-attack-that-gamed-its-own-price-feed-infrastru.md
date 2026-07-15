---
title: "Ostium loses $18 million in oracle attack that gamed its own price-feed infrastructure"
date: 2026-07-15T15:27:43Z
category: "news"
translationKey: "242fdc58587dbb2729425cbfba274cdb"
source: "CoinDesk"
source_url: "https://www.coindesk.com/business/2026/07/15/ostium-suffers-usd18-million-exploit-as-oracle-attack-wave-continues-to-hit-defi"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F03e2d9be0c65442154bdff629a58c6496d145707-1280x717.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: []
_build:
  publishResources: false
  render: never
  list: never
---

An attacker drained approximately $18 million in USDC from Ostium's liquidity vault on Arbitrum in an oracle manipulation exploit detected by blockchain security firm Blockaid , onchain data shows .

According to Blockaid's alert, the attacker leveraged a registered PriceUpKeep forwarder, a component of Ostium's automated infrastructure, to submit oracle price reports with future-dated timestamps. The manipulated reports created the appearance of profitable trades, which triggered an $18 million USDC payout from the vault.

Ostium is a decentralized perpetuals exchange on Arbitrum that allows users to trade real-world assets including commodities, forex, and equity indices, with up to 200x leverage, settling in USDC.

Ostium uses a custom price-feed system to track real-world asset prices, with a third-party automation network called Gelato responsible for pushing those prices onchain at the right moments. A smart contract called PriceUpKeep sits at the center of that process, acting as the trigger that writes the latest price data to the blockchain whenever a trade needs to be executed.

The attack is consistent with a pattern of oracle and keeper-system exploits seen across DeFi in recent years, the most recent of which saw $6 million drained from Summer.fi last week. The exploit involves attackers gaining access to privileged roles and manipulate the timing or content of price data to extract funds from liquidity pools.

Ostium had raised $27.8 million in total funding, including a $24 million Series A co-led by General Catalyst and Jump Crypto in late 2025, and had processed over $50 billion in cumulative trading volume.

CEX trading volumes rose for the first time in five months in June, with spot climbing 15.3% to $1.11T and RWA perpetual volumes surging to a
