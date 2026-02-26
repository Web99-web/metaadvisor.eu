---
title: "Ethereum news: Vitalik Buterin unveils roadmap to counter quantum computing threat"
date: 2026-02-26T18:14:20Z
category: "crypto"
translationKey: "6b7c1a7e73e154041b693baf5cfe8439"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/02/26/vitalik-buterin-unveils-ethereum-roadmap-to-counter-quantum-computing-threat"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Faf0ec5cb6450fadeb2b2eef1a3aa4339e46911ed-3840x2160.png%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

Ethereum co-founder Vitalik Buterin outlined a roadmap on Thursday to protect the blockchain from the long-term risks posed by quantum computers — a move that comes shortly after the Ethereum Foundation established a dedicated post-quantum research team to study the issue.

Although practical quantum computers capable of breaking modern cryptography do not yet exist, they could one day crack the digital signatures and cryptographic systems that secure Ethereum.

In a post on X , Buterin identified four key areas of vulnerability: validator signatures used in consensus, Ethereum’s data availability system, everyday wallet signatures, and certain zero-knowledge proofs used by applications and layer-2 networks.

A big part of the plan involves changing how Ethereum’s validators sign and confirm blocks. Right now, they use a type of digital signature called BLS. In a world with powerful quantum computers, those signatures could eventually be broken. Buterin suggests switching to “hash-based” signatures, which are considered much safer against quantum attacks.

Another area that would need updating is how Ethereum checks and stores large batches of transaction data. The system it uses today relies on a cryptographic tool called KZG commitments. Replacing that with a quantum-safe alternative is possible, Buterin said, but it would require significant behind-the-scenes engineering work and could make some parts of the system more complicated.

For everyday users, the proposed fix revolves around a planned upgrade called EIP-8141 . In simple terms, this upgrade would make Ethereum wallets more flexible. Today, most wallets rely on one standard type of digital signature to approve transactions. EIP-8141 would allow accounts to switch to different types of signatures in the
