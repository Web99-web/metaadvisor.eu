---
title: "BTC news: Bitcoin’s BIP 110 fork deadline nears with miner support at zero"
date: 2026-07-12T05:49:52Z
category: "crypto"
translationKey: "1712bdf6957ea035dbdebd4c18e24a4e"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/07/12/bitcoin-s-bip-110-fork-deadline-nears-with-miner-support-at-zero"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F61a9559ef27c28600826f6691b0424ccfd776182-1500x1000.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

An infamous proposal to purge non-financial data from the Bitcoin blockchain is heading toward a hard deadline in early August, and the initial support it has gathered from miners is less than 1% so far - a signal of outsized opposition despite the immense social chatter around the topic.

BIP-110 , formally titled the Reduced Data Temporary Soft Fork, is basically a fight over what Bitcoin block space is for.

Bitcoin transactions can carry money and extra data. An OP_RETURN section is the obvious “note field” for small bits of data within transactions, and data pushes are another route - where users can place larger chunks of raw data inside Bitcoin script or witness data. Ordinals, inscriptions and some token schemes use those paths to put images, text or token metadata onchain.

BIP-110 would temporarily tighten those paths for one year. It would cap OP_RETURN at the old small size, block most arbitrary data chunks above 256 bytes, and restrict some script formats used mainly for data storage.

Supporters say this keeps Bitcoin focused on payments and lowers node burden, but critics think it turns a policy fight into a consensus rule and tells users which transactions are “acceptable.”

Two of Bitcoin's most influential figures came out against it on Saturday. Strategy founder Michael Saylor posted that "there are 110 things more dangerous to Bitcoin than spam," arguing the proposal "turns a spam dispute into a consensus change that would invalidate some currently valid, fee-paying transactions." The precedent, he wrote, is the real danger.

There are 110 things more dangerous to Bitcoin than spam. BIP 110 turns a spam dispute into a consensus change that would invalidate some currently valid, fee-paying transactions. That precedent is the danger. We should save
