---
title: "Bitcoin cold-wallet attack spreads to 4,500 addresses as losses near $89 million"
date: 2026-08-01T20:10:54Z
category: "crypto"
translationKey: "bf1974b3b531bd35f0d1cddc1826a6df"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/08/02/bitcoin-cold-wallet-attack-spreads-to-4-500-addresses-as-losses-near-usd89-million"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F6c28c3dcd5461d3803d6e6200f1da0686dde993f-1920x1082.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

The attacker working through Coldcard-generated keys is now emptying wallets worth a few thousand dollars each.

Galaxy Research flagged a third wave of sweeps early Sunday, roughly 208 bitcoin drained from 1,912 addresses between Friday midday and Saturday morning UTC.

That is just over a tenth of a bitcoin per victim. The July 30 opening wave averaged close to a full coin, 1,083 bitcoin from 1,196 addresses in 41 minutes.

Observed losses across all three waves now total 1,367 bitcoin, nearly $89 million, from 4,585 addresses.

Wave three sends each victim’s coins to its own destination rather than the handful of shared collector addresses that made the first two easy to map, and parks them in pay-to-witness-script-hash outputs, a format that can carry multisignature or timelock conditions, instead of the plain single-key outputs used before.

It batched an average of six victims into each sweep where wave one took exactly one at a time, and it scanned only the default derivation path, the standard branch of the key tree a wallet checks first, instead of testing several branches per seed.

That is either the same operator rebuilding after being enumerated in public or a second one grinding the same vulnerable key space independently, and the chain does not distinguish them.

Galaxy said it is confident each wave is internally one operator, and will not link the three.

The flaw traces to a March 2021 firmware build that routed seed generation to a predictable software randomiser instead of the chip’s hardware one, leaving a bounded set of possible keys that anyone with the disclosure and enough compute can reproduce offline, without ever touching a device.

But the sweeping has not stopped almost three days later, and the falling average haul says the profitable end
