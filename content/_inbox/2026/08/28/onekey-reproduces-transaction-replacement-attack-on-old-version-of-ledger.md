---
title: "OneKey Reproduces Transaction Replacement Attack on Old Version of Ledger"
date: 2026-08-28T08:21:16Z
category: "news"
translationKey: "b0056002e1d9959ab667bfed1047630c"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/onekey-transaction-replacement-attack-old-version-ledger?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://s3-images.ctmedia.io/media/article-covers/magnifier-coin-bitcoin-search22.png"
tags: []
_build:
  publishResources: false
  render: never
  list: never
---

OneKey said it reproduced an exploit against an older version of the Ledger app in its lab environment, which Ledger fixed in its Ethereum app 1.22.2, with no user funds lost.

The in-house security team at open-source wallet provider OneKey said it successfully reproduced an exploit targeting an outdated version of Ledger’s on-device Ethereum application in a test environment.

OneKey founder and CEO Yishi Wang said they executed a “transaction replacement attack” against Ledger Ethereum app 1.22.1 by exploiting a previously patched vulnerability that lets attackers overwrite the transaction waiting to be signed while the user is still reviewing the legitimate transaction.

Ledger said exploiting the vulnerability required control over communications between the device and its host, such as through malware, compromised wallet software or a hostile webpage. Ledger added app-level safeguards with Ethereum app 1.22.2 released on Aug. 13, before fixing the underlying issue in Secure SDK 26.6.1 on Aug. 21.

“No Ledger user was hacked. What’s described here is a lab reproduction of a vulnerability in an outdated version of the Ethereum app,” Ledger wrote in a Thursday X post .

The security test follows the Coldcard exploit in July, when attackers exploited a firmware bug introduced in March 2021 that weakened seed randomness on some Coldcard wallets, leaving the resulting private keys vulnerable to brute-force attacks.

Ledger had previously said its devices were not affected by the Coldcard vulnerability because recovery phrases are generated using a certified source of randomness built into the device’s security chip.

The vulnerability reproduced by OneKey is unrelated to seed generation and instead affects how transactions are handled during the signing
