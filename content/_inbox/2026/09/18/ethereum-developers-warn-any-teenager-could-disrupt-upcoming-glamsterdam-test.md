---
title: "Ethereum developers warn ‘any teenager’ could disrupt upcoming Glamsterdam test"
date: 2026-09-18T05:23:29Z
category: "crypto"
translationKey: "12f025f9b2d31b11541d78f4ba5fb024"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/09/18/ethereum-confirms-glamsterdam-dates-but-warns-fake-builders-could-stall-the-chain"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Fc18c9af8ef94bcbc9a17fac89a01b83bfc76fd8f-5472x3648.jpg%3Frect%3D0%2C285%2C5472%2C3078%26w%3D1920%26h%3D1080%26auto%3Dformat&w=3840&q=75"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

A teenager with free test ether and a collection of disposable builder identities could repeatedly win Ethereum’s new block auctions and refuse to deliver the transactions, developers warned as they confirmed an Oct. 6 public test of the Glamsterdam upgrade.

The attack would not endanger mainnet funds. It targets Sepolia, where test ether has no meaningful cost, but could leave blocks without transaction payloads and derail the infrastructure testing needed before Glamsterdam reaches Ethereum itself.

Glamsterdam is Ethereum’s next major upgrade, designed to fit more activity into each block without overwhelming the computers that verify it. Together with changes to gas pricing, the upgrade is intended to support a block gas limit of about 200 million, creating room for more payments and trades before users begin bidding fees higher.

The upgrade moves the relationship between validators and specialized block builders into Ethereum’s protocol. Builders assemble transaction blocks and compete to supply them. Once a validator accepts the winning bid, the builder is expected to reveal the underlying transactions.

And that process becomes easy to abuse on a free test network. A malicious operator can submit bids far above every legitimate builder, win repeatedly and then withhold the promised payload.

“I can just spin up a thousand builders, rotate them, offer very high bids, and not produce payloads,” Ethereum consensus developer Potuz said during Thursday’s core developer call . “Any teenager can do this.”

Developers said existing safeguards typically fall back to locally built blocks only after several payloads go missing. Potuz added that clients also need to identify and reject individual builders so an attacker cannot return under a new identity and continue
