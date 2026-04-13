---
title: "Attacker mints $1 billion Polkadot tokens on Ethereum, steals just $250,000"
date: 2026-04-13T07:16:58Z
category: "crypto"
translationKey: "7996d920ec1a06e455bfcc5c9a0cbaf0"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/04/13/attacker-mints-usd1-billion-polkadot-tokens-on-ethereum-ends-up-stealing-just-usd250-000"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F5844591d4fc53908b4ecc1fda0511af88a269620-6024x4024.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

Crypto hacks are nothing new, but cases where attackers take big risks and walk away with peanuts aren't common. That rare scenario played out on Sunday.

An attacker exploited a vulnerability in Hyperbridge's cross-chain gateway that connects different blockchains, minting 1 billion Polkadot tokens ($1.19 billion) on Ethereum and dumping them for approximately $237,000 worth of ether.

The exploit adds to a growing list of bridge vulnerabilities in 2026. Last month saw a $270 million Drift Protocol drain on Solana, while a social engineering attack, rather than a code exploit, similarly involved compromised infrastructure.

The Sunday exploit targeted the bridge contract, not Polkadot's core network. Polkadot's native token DOT was unaffected. The vulnerability sat in how Hyperbridge's EthereumHost contract validates incoming cross-chain messages before passing them to the TokenGateway.

Bridges, which help move coins from one blockchain to another, remain the weakest link in cross-chain architecture because they hold admin-level control over token contracts on destination chains, meaning a single validation failure can grant an attacker the ability to mint unlimited supply.

On-chain traces show that the attacker submitted a forged message via dispatchIncoming, which was routed to TokenGateway.onAccept.

The request receipts check, which should have verified the message against a valid cross-chain state commitment from Polkadot, stored an all-zeros commitment value, suggesting the proof validation was either absent or circumventable for this specific call path. The gateway processed the message as legitimate.

The accepted message executed changeAdmin on the bridged Polkadot token contract, transferring admin rights to the attacker's address. With admin control, the
