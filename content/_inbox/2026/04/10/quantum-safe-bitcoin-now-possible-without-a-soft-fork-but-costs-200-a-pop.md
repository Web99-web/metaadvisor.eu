---
title: "Quantum-safe bitcoin now possible without a soft fork, but costs $200 a pop"
date: 2026-04-10T03:54:27Z
category: "crypto"
translationKey: "1678ca2ed1398793452a3e3fd23a0eb7"
source: "CoinDesk"
source_url: "https://www.coindesk.com/markets/2026/04/10/quantum-safe-bitcoin-now-possible-without-a-soft-fork-but-costs-usd200-a-pop"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Fecfe1c9a91435e545a466715bbc0457d2e3a48f4-5105x3403.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

A StarkWare researcher has published what he says is the first method for making bitcoin transactions quantum-safe on the live network today, without any changes to the Bitcoin protocol. The scheme, however, costs up to $200 per transaction and is designed as an emergency measure rather than a permanent fix.

In a paper published this week , StarkWare researcher Avihu Levy introduced Quantum Safe Bitcoin, or QSB, a scheme that aims to enable quantum-resistant transactions without requiring changes to the Bitcoin protocol, by replacing signature-based security assumptions with hash-based proofs within its design.

The hash-based design survives the kind of quantum attack that would break today’s cryptography, but shifts the burden from consensus to computation, requiring heavy off-chain GPU work for every transaction.

Think of traditional digital signatures as a handwritten signature on a cheque, which proves you authorized a transaction using a secret key that others can cross check with a public key.

In Bitcoin, these digital signatures are called ECDSA signatures. They are secure against today’s computers, but a sufficiently powerful future quantum computer could, in theory, derive the secret key from a public key and potentially compromise funds.

QSB addresses that flaw by redesigning the system around a different kind of cryptography, involving hash-based proofs, which are more like a tamper-proof fingerprint, where instead of relying on signature alone, a unique mathematical digest of data is created. This is said to be extremely difficult to forge or reverse, even for powerful computers.

QSB works entirely within Bitcoin's existing consensus rules for legacy transactions. It requires no soft fork (software upgrade), no miner signaling, and no activation
