---
title: "Bitcoin quantum proposal offers Satoshi Nakamoto a way to prove control without moving BTC"
date: 2026-05-02T06:24:06Z
category: "crypto"
translationKey: "207f7e67f667e7307833078ba7ed3219"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/05/02/new-bitcoin-quantum-proposal-offers-satoshi-nakamoto-a-way-to-prove-control-without-moving-btc"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F5ac794a198da68fdb1b6a9d4e19c2e947f99454c-1920x1080.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

Bitcoin's quantum computing concerns have always had a Satoshi problem inside it.

Millions of bitcoin sitting in old wallets with exposed public keys could be vulnerable to theft if powerful enough quantum computers arrive . That includes the roughly 1.1 million bitcoin attributed to pseudonymous creator Satoshi Nakamoto, currently worth around $84 billion.

The obvious defense is a soft fork (or an upgrade to existing network rules) that eventually stops allowing spends from those legacy address types, forcing holders to move into quantum-safe formats before attackers can derive their private keys.

Prominent developer Jameson Lopp and five other developers proposed exactly that in mid-April through BIP-361 , which would phase out quantum-vulnerable addresses on a five-year timeline and freeze any coins that fail to migrate.

That proposal created a different problem, however. Satoshi, and every other long-dormant holder, would have to wake up publicly or risk losing access to their assets.

Dan Robinson, a general partner at Paradigm, published a proposal Friday for a way around that trade-off that revolves around the concept of Provable Address-Control Timestamps, or PACTs.

The core idea is not to move coins but timestamp proof of ownership at a specific date and reveal nothing to the public until the owners of those wallets actually need to spend.

A holder generates a random salt, which is a piece of secret data used to make a cryptographic commitment unique and unguessable, and uses BIP-322, a standard for signing messages from a Bitcoin address without spending from it, to produce a proof of ownership.

The salt and proof are bundled together into an onchain commitment and timestamp it through OpenTimestamps, a free service that anchors data onto the Bitcoin
