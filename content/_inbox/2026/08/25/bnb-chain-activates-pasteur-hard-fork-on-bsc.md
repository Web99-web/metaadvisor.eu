---
title: "BNB Chain Activates Pasteur Hard Fork on BSC"
date: 2026-08-25T03:56:29Z
category: "ai"
translationKey: "d7104682d985ada6b59ef51ab9273e9b"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/bnb-chain-pasteur-hard-fork-bridge-security?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://s3-images.ctmedia.io/media/article-covers/hi-why-quantum-security-is-rising-on-layer-1-roadmaps-and-which-networks-are-preparing-first.jpg"
tags: ["ai"]
_build:
  publishResources: false
  render: never
  list: never
---

BNB Chain activates the Pasteur hard fork on BSC, closing bridge and validator security gaps while targeting greater transaction capacity.

BNB Smart Chain (BSC) activated its Pasteur hard fork on Tuesday, closing bridge verification and validator authorization gaps while introducing a new route intended to fit more transactions into each block.

In a Tuesday post, BNB Chain confirmed that Pasteur was live on the BSC mainnet. The team said the upgrade strengthens the network’s bridge, staking and governance security while giving blocks more capacity without changing its 450-millisecond block time.

The upgrade combines three BNB Evolution Proposals. BEP-682 rejects duplicate validator entries during cross-chain light-block verification, while BEP-695 tightens controls involving validator key rotation, slashing and governance voting. BEP-675 changes how specialist builders submit blocks to validators.

The upgrade prevents validators from being counted more than once in bridge approvals, removes authority from old validator keys and blocks restricted addresses from voting, while aiming to fit more transactions into blocks during busy periods.

Under BSC’s previous block-building route, a builder executed transactions before submitting a proposed block, and the validator executed them again before signing it. BNB Chain said the repeated work took time away from builders operating within the network’s block window, sometimes leaving blocks underfilled.

BEP-675 allows builders to submit blocks they have already executed. Validators check the proposed block against consensus rules, sign and broadcast it, then complete full execution verification afterward. Builders can also continue using the previous route, under which validators execute transactions before
