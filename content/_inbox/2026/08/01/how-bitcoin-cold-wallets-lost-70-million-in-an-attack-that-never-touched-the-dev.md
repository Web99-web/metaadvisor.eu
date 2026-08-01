---
title: "How bitcoin cold wallets lost $70 million in an attack that never touched the devices"
date: 2026-08-01T05:55:46Z
category: "crypto"
translationKey: "fc90b22b3e9438f8f018668fbdc4ecd1"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/08/01/how-bitcoin-cold-wallets-lost-usd70-million-in-an-attack-that-never-touched-the-devices"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Fee774b5ffc09b1ed7b4b987d689ad1a95db24aaa-1280x720.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

More than 1,000 bitcoin, worth about $70 million, was drained from 1,196 wallets in a 41-minute window on July 30, nearly double the amount reported when the theft first surfaced.

Galaxy Research mapped the full event on Friday, finding 1,082.65 BTC swept between 01:10 and 01:51 UTC across six blocks, with three intervening blocks containing nothing, which suggests the transactions were broadcast in batches rather than continuously.

The proceeds sit in four addresses and have not moved. Early reporting captured only one of those addresses, which is why the figure has grown.

The size of the attack is much smaller than some of the bigger attacks this year, but the mechanism is what makes this unusually — and why the attack is such a big deal.

Most crypto theft involves getting to something. An exchange is breached, a contract is tricked, a key is phished off a laptop. The defence has always been distance, which is precisely what a hardware wallet sells. Keep the key on a device that never connects to the internet and, theoretically, there is nothing for an attacker to touch.

When a wallet is created, the device is supposed to pick a number so large and so unpredictable that guessing it is impossible.

That number is the seed, and every address and private key derives from it by fixed public rules. Coldcard's firmware was meant to draw that number from a dedicated hardware randomness generator. An internal build setting told it to skip that generator, and a check in a supporting library tested only whether the setting existed rather than whether it was switched on.

Key generation fell through to a basic software substitute seeded from the chip's serial number and its clock registers. This serial number is fixed factory metadata, and clock values are timing state an
