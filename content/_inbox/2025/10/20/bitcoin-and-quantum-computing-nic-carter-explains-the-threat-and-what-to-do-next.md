---
title: "Bitcoin and Quantum Computing: Nic Carter Explains the Threat and What To Do Next"
date: 2025-10-20T15:17:43Z
category: "crypto"
translationKey: "d1adab2f0b8af85d41f5fef732fbe1c3"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2025/10/20/quantum-computing-is-biggest-risk-to-bitcoin-says-coin-metrics-co-founder"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Fcc06c4c652f423950a5aaefa52e4c4580148298a-1920x1080.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

Nic Carter says quantum computing is the biggest long-term risk to bitcoin’s core cryptography and urges developers to treat it with urgency, not as science fiction.

In an essay published Monday, the Coin Metrics cofounder explains in plain language how bitcoin’s keys work and why quantum matters. Carter writes that users start with a secret number (a private key) and derive a public key with elliptic-curve math on the secp256k1 curve, the basis for ECDSA and Schnorr signatures.

He describes that transformation as deliberately one way: easy to compute forward, infeasible to reverse under classical assumptions. “Bitcoin’s entire cryptographic premise is ‘there exists a one-way function that’s easy to compute in one direction, and infeasible to invert,’” he writes.

To build intuition, Carter likens the system to a giant number scrambler. Going from private to public is efficient for honest users, he says, because they can use a shortcut known as “double and add” to reach a result quickly. He adds there is no comparable shortcut in the opposite direction.

For non-specialists, he offers a deck-shuffle analogy: you can repeat the same sequence of shuffles to reach an identical final order, but an observer cannot look at the shuffled deck and infer how many shuffles were used.

Carter argues the concern is that a sufficiently powerful quantum computer could erode that asymmetry by making progress on the discrete logarithm problem that underpins bitcoin’s signatures. In his telling, routine network behavior also raises exposure: when coins are spent, a public key is revealed on-chain.

He says that is safe today because converting a revealed public key back to the private key is not practical, but quantum advances could change that calculus, especially if addresses are
