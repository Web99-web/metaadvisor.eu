---
title: "Injective NPM Package Hacked to Steal Crypto Wallet Keys"
date: 2026-07-10T03:07:47Z
category: "crypto"
translationKey: "cdcc85138ba4f94609d0557cdfcf2046"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/hackers-compromise-injective-npm-package-with-malware-to-steal-wallet-keys?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://s3-images.ctmedia.io/media/article-covers/hi-how-hong-kong-is-turning-tokenized-bonds-into-real-market-infrastructure.jpg"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

The incident is significant for developers and applications that handle Injective wallet workflows, Socket researchers said.

Hackers compromised a widely used Injective software package in a supply chain attack with malware designed to steal crypto wallet private keys, adding to a growing attack vector involving attackers using legitimate platforms to deliver malicious payloads.

Security firm Socket discovered on Thursday that a popular npm (node package manager) package with around 50,000 weekly downloads used for building on the Injective blockchain was maliciously modified to steal wallet private keys and seed phrases.

The large number of downloads makes the incident “significant for developers and applications that handle Injective wallet workflows,” Socket researchers said . The malicious code has since been removed.

The software supply chain attack is a relatively new attack vector in which hackers don’t target a blockchain’s cryptography or smart contracts directly, but instead compromise trusted developer tools used to build wallets, exchanges and apps.

Injective is an interoperable layer 1 designed for DeFi applications. Its usage has dwindled over the past two years, with total value locked shrinking by 88% to current levels of $8.2 million from its $71 million peak in mid-2024, according to DefiLlama.

Version 1.20.21 of the @injectivelabs/sdk-ts npm package was modified through a compromised developer GitHub account, with suspicious commits beginning June 8. It was also pinned across 17 other packages in the Injective Labs npm scope, “exposing users who may not have installed the SDK [software development kit] directly,” Socket said.

“The malicious release hooks wallet key-derivation functions, records private keys and mnemonics, and exfiltrates them
