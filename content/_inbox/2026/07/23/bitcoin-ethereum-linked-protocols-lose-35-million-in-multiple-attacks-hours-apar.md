---
title: "Bitcoin, Ethereum-linked protocols lose $35 million in multiple attacks hours apart"
date: 2026-07-23T06:38:18Z
category: "crypto"
translationKey: "9335ad855f79e070ca5c0a2244adf7db"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/07/23/bitcoin-ethereum-linked-protocols-lose-usd35-million-in-multiple-attacks-hours-apart"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Fd4b2490f30fa58bdb6ed0c1a89ed37ee02479a66-3407x2556.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

Crypto's bridges and cross-chain protocols are having a brutal day, capping an already punishing year .

At least three were drained in quick succession over a 6-hour period, for a combined total exceeding $35 million, according to blockchain data analyzed by CoinDesk and reported by security firms BlockAid and PeckShield.

The run of attacks shares a common thread that underscores the need to audit off-chain components, such as private keys, not just smart contract code.

None broke the underlying cryptography â€” each was either a logic flaw, where the code ran as written, but the rules still let money out, or a compromised key that handed an attacker control it should never have had.

The perpetuals exchange AFX lost about $24.15 million from a bridge it runs on Arbitrum. The Verus-Ethereum bridge was drained of $7.54 million, its second hack this year through the same flaw. And BÂ², a Bitcoin scaling network, lost $3.86 million from its token staking contract.

The most damning was blockchain network Verus. Blockaid detected an exploit on the Verus-Ethereum bridge early Thursday that drained about $7.54 million in ether, tokenized bitcoin and a spread of stablecoins.

ðŸš¨ Blockaid detected a @VerusCoin Ethereum Bridge exploit on Ethereum. An attacker used the bridge import path to trigger unbacked Ethereum-side payouts, draining ~$7.54M in ETH, tBTC, USDC, USDT, EURC, MKR, and scrvUSD from bridge reserves. More details in ðŸ§µ

The firm flagged that the attack reused the same bridge contract and entry path as an earlier hack, exploiting an identical class of bug. CoinDesk reported that earlier incident, an $11.5 million loss , in May.

A bridge is a blockchain-based tool that enables assets to move between two networks that otherwise cannot interact. It holds real
