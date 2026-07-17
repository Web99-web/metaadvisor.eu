---
title: "BTC news: Bitcoin’s anti-spam fight gets a 'DOG Mode' reply"
date: 2026-07-17T05:32:00Z
category: "crypto"
translationKey: "6034ca9c5311ccf23dcf183014a8cc77"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/07/17/bitcoin-s-anti-spam-fight-gets-a-dog-mode-reply"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Fca4073986b82e35a5d6bd80c2e88a27749ed87bf-1024x576.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

Five days after CoinDesk reported that a proposal to purge non-financial data from Bitcoin was approaching deadline with effectively zero miner backing, some developers in the community have a different plan that skips the vote entirely.

Leonidas, co-founder of the Runestone project and one of the most prominent figures in Bitcoin's Ordinals and Runes ecosystem, said Friday he is starting an open source Bitcoin client called DOG Mode.

It would lift two of the limits set by Bitcoin Core, the software that runs on the large majority of Bitcoin's nodes. One caps the largest transaction a node will pass along to its peers, while the other sets the smallest amount of bitcoin an output can hold.

Consensus rules define what makes a block valid, and breaking them splits a node off the network. Relay policy is separate and softer, as it governs what an individual node chooses to forward to its neighbours, and Core's version rejects transactions it deems "non-standard" even when they are perfectly valid under consensus.

Because almost every node runs Core, those defaults function as Bitcoin's rules in practice. A miner who receives such a transaction directly can still mine it, and the block stands. And because Core won't relay these transactions, anyone wanting one has to know a miner, and services like MARA's Slipstream exist to broker exactly that.

On the other hand, DOG Mode would raise the maximum standard transaction from 400,000 weight units to 3,900,000. A Bitcoin block holds four million weight units, so Core currently relays nothing larger than a tenth of a block, while DOG Mode would carry transactions filling nearly all of one.

It would also cut the dust limit, the floor below which an output is considered too small to bother relaying, from between 294 and 546
