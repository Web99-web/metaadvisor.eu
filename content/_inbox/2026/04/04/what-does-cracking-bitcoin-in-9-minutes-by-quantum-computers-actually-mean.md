---
title: "What does 'cracking' bitcoin in 9 minutes by quantum computers actually mean"
date: 2026-04-04T02:30:00Z
category: "crypto"
translationKey: "d1c1779f193c9ada65bbcea234583c31"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/03/31/what-does-cracking-bitcoin-in-9-minutes-by-quantum-computers-actually-mean"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F708aa3823548823e0c5fe35094db98ba9ba7a078-1500x997.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

Google's Quantum AI team said earlier this week that a future quantum computer could derive a bitcoin private key from a public key in roughly nine minutes. The number ricocheted across social media and spooked markets.

But, what does it actually mean in practice?

Let's start with how bitcoin transactions work. When you send bitcoin, your wallet signs the transaction with a private key, a secret number that proves you own the coins.

That signature also reveals your public key, a shareable address, which gets broadcast to the network and sits in a waiting area called the mempool until a miner includes it in a block. On average, that confirmation takes about 10 minutes.

Your private key and public key are linked by a math problem called the elliptic curve discrete logarithm problem. Classical computers can't reverse that math in any useful timeframe, while a sufficiently powerful future quantum computer running an algorithm called Shor's could.

Here's where the nine minutes part comes in. Google's paper found that a quantum computer could be "primed" in advance by pre-computing the parts of the attack that don't depend on any specific public key.

Once your public key appears in the mempool, the machine only needs about nine minutes to finish the job and derive your private key. Bitcoin's average confirmation time is 10 minutes. That gives the attacker a roughly 41% chance of deriving your key and redirecting your funds before the original transaction confirms.

Think of it like a thief spending hours building a universal safe-cracking machine (pre-computation). The machine works for any safe, but each time a new safe appears, it only needs a few final adjustments — and that last step is what takes about nine minutes.

That's the mempool attack. It's alarming but
