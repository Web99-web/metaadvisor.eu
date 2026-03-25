---
title: "Ethereum Foundation launches post-quantum security hub with more than 10 client teams"
date: 2026-03-25T15:33:22Z
category: "crypto"
translationKey: "c47aebbea862f6988caf257f74614bcf"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/03/25/ethereum-foundation-prepares-for-quantum-threat-with-new-cryptography-roadmap"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Fc357579ddef2051b405b9e89f8525dd02709081d-5760x3240.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

Ethereum isn't waiting for quantum computers to become a problem before figuring out how to survive them.

The Ethereum Foundation launched pq.ethereum.org on Wednesday, a dedicated resource hub for the protocol's post-quantum security effort. The site consolidates a roadmap, open-source repositories, specifications, research papers, EIPs, and a 14-question FAQ written by the EF's post-quantum team.

More than 10 client teams are already building and shipping devnets weekly through what the foundation calls PQ Interop, the foundation said in an X post earlier Wednesday.

Today, several teams at the EF are launching https://t.co/L9ZOUoRNNB , a dedicated resource for Ethereum's post-quantum security effort. What started with early STARK-based signature aggregation research in 2018 has grown into a coordinated, multi-team effort, all open source.…

The technical challenge is substantial. Quantum computers are widely believed to will eventually break the public-key cryptography that secures ownership, authentication, and consensus across Ethereum.

The EF's position is that a cryptographically relevant quantum computer isn't imminent, but migrating a decentralized global protocol takes years of coordination, engineering, and formal verification.

The migration touches every layer of the protocol.

At the execution layer, post-quantum signature verification through a vector math precompile would let users transition to quantum-safe authentication through account abstraction without a disruptive "flag day" where everyone has to upgrade simultaneously.

At the consensus layer, the current BLS validator signature scheme gets replaced with hash-based signatures called leanXMSS, with a minimal zk-based virtual machine handling aggregation to restore scalability since
