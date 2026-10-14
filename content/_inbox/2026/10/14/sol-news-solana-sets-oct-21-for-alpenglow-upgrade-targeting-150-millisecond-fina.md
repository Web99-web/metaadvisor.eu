---
title: "SOL news: Solana sets Oct. 21 for Alpenglow upgrade targeting 150-millisecond finality"
date: 2026-10-14T04:11:16Z
category: "crypto"
translationKey: "057b854c68327a213517b76149f8932b"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/10/14/solana-sets-oct-21-for-alpenglow-upgrade-targeting-150-millisecond-finality"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F54c0f3b41e62df4cdf774aab4c7d68c64e5e976c-1920x1080.png%3Fw%3D1920%26h%3D1080%26auto%3Dformat&w=1200&q=75"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

Solana has scheduled Oct. 21 for Alpenglow, a major upgrade aimed at making transactions irreversible in roughly 150 milliseconds by changing how the computers running the network agree on payments.

The updated timetable published by the Solana Foundation sets a date for replacing TowerBFT, the voting system Solana has used since its launch in 2020. The 150-millisecond figure remains a target, with actual performance depending on network conditions.

This matters as a Solana payment can already appear successful almost immediately. But Alpenglow aims to offer a stronger guarantee that it cannot be undone almost as quickly.

A merchant waiting for that assurance before accepting a payment, or a bridge before releasing funds on another blockchain, could act sooner.

As of today, validators, the computers that check transactions and help secure Solana, submit their votes as transactions recorded on the blockchain. Alpenglow will let them exchange votes directly and combine enough approvals into a certificate that finalizes a block after one or two voting rounds.

That could produce an odd result on activation day, however. Solana’s transaction count may fall sharply because validator votes disappear from blocks, even if people keep trading and making payments at the previous pace.

Read More: Solana’s 150-millisecond settlement upgrade reaches second public test network

Validators must also prepare for the switch. Operators need software built on Agave 4.3.0. Firedancer and Frankendancer, alternative programs used to run validators, will not support the initial migration, so their operators will need to switch temporarily.

Removing vote transactions also changes what validators pay. Their current voting charges of roughly 1 SOL per epoch will disappear, replaced by a
