---
title: "A week of AI coding cut a quantum-safe bitcoin transaction estimate from $320 to $66"
date: 2026-09-24T05:24:56Z
category: "crypto"
translationKey: "6cf0b23aadaddc38c0937242a467b41b"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/09/24/a-week-of-ai-coding-cut-a-quantum-safe-bitcoin-transaction-estimate-from-usd320-to-usd66"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F631d76c20667ca4a1c610d2007c676c073cc1346-6000x4000.jpg%3Frect%3D0%2C313%2C6000%2C3375%26w%3D1920%26h%3D1080%26auto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

A week of AI-assisted coding has brought the estimated GPU cost of preparing a quantum-resistant bitcoin transaction down to $66 from about $320, according to StarkWare, the company behind the research .

The earlier figure came from a transaction mined on Bitcoin in August . Preparing it took roughly 3,100 hours of computing time across a fleet of about 100 graphics processors. That $320 was the cost of the computing work done before the transaction reached Bitcoin, separate from the fee paid to put it on the blockchain.

StarkWare then opened the code to a competition. Participants, many working with AI coding tools, tried to make it search through possible solutions faster. The leaderboard shows a leading submission checking about 881 million candidates a second, against roughly 146 million for the starting code on the same benchmark graphics processor.

The work addresses a possible future threat to Bitcoin. A sufficiently powerful quantum computer could use a wallet’s exposed public key to work out its private key and steal the coins. StarkWare’s method adds a form of protection based on hashes, which are expected to withstand that attack. It fits within Bitcoin’s existing rules, so trying it did not require the network to approve an upgrade.

As such, the method is an emergency option for moving eligible coins if the quantum threat arrives before Bitcoin adopts a broader fix. Using it widely would be expensive at $320 of computing per transaction — and a lower bill could make the option more practical.

Read More: Quantum-safe bitcoin now possible without a soft fork, but costs $200 a pop, new research shows

The $66 figure remains an estimate drawn from a test of the computation. The improved code has not been shown preparing another transaction mined on
