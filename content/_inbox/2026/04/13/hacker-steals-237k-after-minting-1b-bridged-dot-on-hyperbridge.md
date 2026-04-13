---
title: "Hacker Steals $237K after Minting 1B Bridged DOT on Hyperbridge"
date: 2026-04-13T09:19:10Z
category: "news"
translationKey: "25fb0807a064de46ad4548072051fa4f"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/hacker-steals-237k-1b-bridged-dot-hyperbridge?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://zoa.cointelegraph.com/pixel?postId=261012&regionId=1"
tags: []
_build:
  publishResources: false
  render: never
  list: never
---

A Hyperbridge exploit let an attacker mint 1 billion bridged Polkadot tokens on Ethereum and cash out about $237,000, reviving debate over bridge security.

A hacker exploited the Polkadot-based cross-chain interoperability protocol Hyperbridge, netting about $237,000 and raising renewed security concerns about blockchain bridge infrastructure.

An attacker minted 1 billion bridged Polkadot ( DOT ) tokens in a single transaction on Hyperbridge, according to blockchain data shared by cybersecurity platform CertiK. The exploit only affected DOT on Ethereum that was bridged through Hyperbridge, while native DOT tokens and the wider Polkadot ecosystem remain unaffected, Polkadot noted in a Monday X post .

CertiK said the attacker managed to mint the tokens after “slipping through a forged message to change the admin of the Polkadot token contract on Ethereum.” Limited liquidity in the bridged DOT pool capped the proceeds at 108.2 Ether ( ETH ), worth around $237,000.

Hyperbridge paused operations after the attack while the team worked on an upgrade, with contributor Web3 Philosopher saying the initial diagnosis pointed to a malicious proof that fooled the protocol’s Merkle tree verifier.

The exploit is notable because Hyperbridge has marketed itself as a proof-based interoperability layer built to deliver “full node security” for crosschain bridges. The incident also follows Aethir’s disclosure last week that it had contained a separate bridge exploit and kept user losses below $90,000.

Cybersecurity research company Blocksec Falcon said the likely root cause of the exploit was a Merkle Mountain Range (MMR) proof replay vulnerability caused by missing proof-to-request binding, though the final root cause has not yet been confirmed by the protocol.

The native DOT token
