---
title: "Bitcoin BIP-361 Targets Quantum Security Threat"
date: 2026-04-15T04:36:51Z
category: "crypto"
translationKey: "e30608e0afb819a240058f41545f9f37"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/bitcoin-devs-and-researchers-propose-freezing-quantum-vulnerable-coins-bip-361?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://zoa.cointelegraph.com/pixel?postId=261607&regionId=1"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

The authors described it as a “private incentive to upgrade” because lost or frozen coins will make everyone else’s coins worth slightly more.

Cypherpunk Jameson Lopp and five co-authors from the Bitcoin quantum security space have proposed freezing quantum-vulnerable coins on the Bitcoin network, including Satoshi’s $74 billion stash, to prevent them from being stolen once quantum computers become available.

The move is the second part of a three-stage proposal under BIP-361 called the “Post Quantum Migration and Legacy Signature Sunset,” which was posted as a draft to GitHub on Tuesday.

It addresses a major risk to Bitcoin — the potential use of quantum computers to steal roughly 1.7 million BTC locked in early P2PK addresses, including Satoshi’s stash, which are not quantum-proof.

In the wrong hands, these coins could significantly undermine the value of the network.

BIP-361 builds on BIP-360, released in February , which proposed a soft fork for a new output type called pay-to-Merkle-root (P2MR). It works similarly to Bitcoin’s existing Taproot (P2TR) addresses but with the quantum-vulnerable key path removed.

While BIP-360 protects new coins going forward, it does not address the roughly 34% of the supply that remains vulnerable unless it is transferred to new addresses.

BIP-361 proposes that three years after activation, phase A of the proposal would prevent any new BTC from being sent to old-style addresses, with all users on quantum-resistant address types.

The second phase (B) would invalidate old-style signatures and any Bitcoin still sitting in vulnerable addresses becomes effectively frozen five years after activation.

Related: Bitcoin can be made quantum-safe without protocol upgrade: Researcher

Phase C provides a potential rescue mechanism using
