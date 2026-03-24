---
title: "Bitcoin's mining concentration just showed up in a rare 2-block reorg"
date: 2026-03-24T04:33:49Z
category: "crypto"
translationKey: "b9d6b8c3a4e0fdba79a7111785ee67e2"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/03/24/bitcoin-s-mining-concentration-just-showed-up-in-a-rare-2-block-reorg"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Fa944f5c40b9f1fece6ecb4c387377f37ae7134cc-1920x1080.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

Bitcoin's mining concentration problem just showed up on the blockchain itself, triggering a small “reorg.”

At the center of the story is Foundry USA, the largest bitcoin mining pool, representing a group of miners who combine their computing power to verify transactions, mine blocks, and split the rewards in BTC.

On the blockchain, there are many miners, and sometimes two or more find a block at nearly the same time. When that happens, the network temporarily has two competing versions of the blockchain. Eventually, the network reorganizes back into a single chain, depending on which version grows faster. This process is called a blockchain reorganization, or “reorg.”

That’s what happened on Monday: Foundry and AntPool both mined blocks at roughly the same time, causing a chain split. Foundry then produced several consecutive blocks, moving slightly faster than its competitors, and became the chain the network followed.

The result: the blockchain reorganized to Foundry’s version, and the blocks mined by AntPool and ViaBTC were orphaned or effectively erased from the ledger. Those miners earned nothing for the work they had done.

Think of it as two checkout lines opening at the same time in a busy store. At first, both lines are moving, but suddenly, one of the line starts clearing customers faster.  This leads everyone to shift to the faster line and the slower one gets abandoned.

The episode highlights the risks of mining concentration in Bitcoin and how controlling network power can translate directly into outsized influence and losses for rivals. When a single pool like Foundry can produce several blocks in a row, it can trigger a reorg, and orphan valid blocks from other miners.

We just had a rare-ish two block fork/reorg between Foundry and AntPool+ViaBTC.
