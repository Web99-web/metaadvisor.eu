---
title: "Bitcoin’s quantum problem gets a recovery tool, but not for Satoshi’s 1.1 million BTC"
date: 2026-07-19T10:00:00Z
category: "crypto"
translationKey: "b4892874810f6ddcbd9cc5548f840217"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/07/19/bitcoin-s-quantum-problem-gets-a-recovery-tool-but-not-for-satoshi-s-1-1-million-coin"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Fa0a7940835c9275731c2adf69015343cc4a850ac-1024x683.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

The proposal to freeze bitcoin's quantum-vulnerable coins has always carried an asterisk.

BIP-361 , published in April by Jameson Lopp and five co-authors, would block new deposits to vulnerable addresses after three years and freeze whatever remained after five, stranding coins in more than a third of bitcoin's supply, including the roughly 1.1 million BTC attributed to pseudonymous creator Satoshi Nakamoto.

A later step of that plan promised a recovery path using zero-knowledge proofs, a technology that lets someone prove to another person that they know a fact without ever revealing it.

Quantum research outfit Project Eleven says it has now built exactly that, and made it fast enough to use.

Q-Day is a theoretical point at which a quantum computer could derive a private key from a public key, allowing an attacker to sign transactions from any address whose public key has ever been exposed.

More than 34% of all bitcoin sits in that category, according to BIP-361. After Q-Day, a signature would prove nothing because the attacker can produce one as easily as the owner. The chain cannot tell them apart.

Bitcoin signatures rely on elliptic curve cryptography, a system in which a private key generates a public key through math that runs only one way. Anyone can check the public key, but nobody can work backward to the private one. However, Shor’s algorithm, a quantum method published in 1994 for problems that ordinary computers cannot crack, can be fed a public key and return the private key that generated it.

Hashing is a different kind of problem. A hash scrambles an input into a fixed-length fingerprint and cannot be run backward, and the best quantum attack on it, called Grover's algorithm, only halves the exponent rather than collapsing it, taking a 256-bit
