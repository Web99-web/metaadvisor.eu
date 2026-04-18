---
title: "How a quantum computer can be used to actually steal your bitcoin in '9 minutes'"
date: 2026-04-18T03:51:35Z
category: "crypto"
translationKey: "d26d2582f2cdd3a08f707667386dbee2"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/04/18/how-a-quantum-computer-can-be-used-to-actually-steal-your-bitcoin-in-9-minutes"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F701a2df2a038e65d0dd59a68d97e28340b9398e1-1080x1080.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

Part 1 of this series explained what quantum computers actually are. Not just faster versions of regular computers, but a fundamentally different kind of machine that exploits the weird rules of physics that only apply at the scale of atoms and particles.

But knowing how a quantum computer works does not tell you how it can be used to steal bitcoin by a bad actor. That requires understanding what it is actually attacking, how bitcoin's security is built, and exactly where the weakness sits.

This piece starts with bitcoin's encryption and works through to the nine-minute window it takes to break it, as identified by Google's recent quantum computing paper .

Bitcoin uses a system called elliptic curve cryptography to prove who owns what. Every wallet has two keys. A private key, which is a secret number, 256 digits long in binary, roughly as long as this sentence. A public key is derived from the private key by performing a mathematical operation on the specific curve called " secp256k1 ."

Think of it as a one-way map. Start at a known location on the curve that everyone agrees on, called the generator point G (as shown in the chart below). Take a private number of steps in a pattern defined by the curve's math. The number of steps is your private key. Where you end up on the curve is your public key (point K in the chart) . Anyone can verify that you ended up at that specific location. Nobody can figure out how many steps you took to get there.

Technically, this is written as K = k × G, where k is your private key and K is your public key. The "multiplication" is not regular multiplication but a geometric operation where you repeatedly add a point to itself along the curve. The result lands on a seemingly random spot that only your specific number k would
