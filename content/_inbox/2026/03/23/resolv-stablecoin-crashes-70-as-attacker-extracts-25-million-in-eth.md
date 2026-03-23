---
title: "Resolv stablecoin crashes 70% as attacker extracts $25 million in ETH"
date: 2026-03-23T06:23:23Z
category: "crypto"
translationKey: "bb8eae9ad806e77e3c909062e5c5c723"
source: "CoinDesk"
source_url: "https://www.coindesk.com/markets/2026/03/23/resolv-stablecoin-drops-70-after-usd80-million-exploit-after-attacker-mints-usr"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Fa11ce5a4637c2f80d5f2476b76faed42c93fa03b-3403x1914.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

A stablecoin is supposed to be worth a dollar. Resolv's USR is worth 27 cents and the math to fix it doesn't work.

An attacker exploited a flaw in Resolv's USR stablecoin minting contract around 2:21 a.m. UTC on Sunday, creating approximately 80 million unbacked tokens across two transactions and extracting roughly $25 million, according to multiple blockchain security firms and onchain data.

The attacker then swapped the minted USR for USDC and USDT across decentralized exchanges, converted the proceeds to ETH, and now holds 11,409 ETH worth about $23.7 million plus $1.1 million in wrapped USR in a separate wallet.

USR, a dollar-pegged stablecoin that uses a delta-neutral hedging strategy backed by ETH and BTC, crashed to $0.025 on its most liquid Curve Finance pool within 17 minutes of the first mint, according to DEX Screener.

It later recovered to around $0.85 but has not restored its peg. As of Monday morning it was trading at $0.27, down 72% on the week.

This notice is issued on behalf of Resolv Digital Assets Ltd. in relation to the Resolv protocol. Earlier today, a malicious actor gained unauthorized access to Resolv infrastructure through compromised private key, resulting in the minting of approximately $80M of…

The root cause was worse than Resolv's initial statement suggested. The team described the incident as a "compromised private key" and "targeted infrastructure compromise."

But onchain analysts found the real problem was structural. The SERVICE_ROLE, a privileged account that completes swap requests in the minting contract, was controlled by a single externally owned account rather than a multisig. The contract lacked oracle checks, amount validation, and maximum mint limits.

The attacker deposited 100,000 USDC and received 50 million USR in
