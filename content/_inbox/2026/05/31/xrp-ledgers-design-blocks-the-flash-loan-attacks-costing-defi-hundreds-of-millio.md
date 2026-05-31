---
title: "XRP Ledger's design blocks the flash loan attacks costing DeFi hundreds of millions"
date: 2026-05-31T02:30:00Z
category: "news"
translationKey: "c7f6648f7c49376c9f51a0d801c8dc9d"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/05/29/xrp-ledger-s-new-proposal-blocks-the-flash-loan-attacks-costing-defi-hundreds-of-millions"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F92e1b9587d9046ddc71662c77ea0332e9f8a8771-3840x2160.png%3Fauto%3Dformat&w=3840&q=75"
tags: []
_build:
  publishResources: false
  render: never
  list: never
---

The two biggest DeFi exploits of the past two months have one thing in common. They used a tool that does not exist on the XRP Ledger.

Thorchain lost roughly $10.8 million on May 15 to a cross-chain attack that drained funds across Bitcoin, Ethereum, BSC, and Base. Drift Protocol, a Solana-based decentralized perpetual exchange, and KelpDAO, a liquid restaking protocol on Ethereum, together accounted for more than $600 million in losses through April alone.

Cross-chain bridges have lost over $2.8 billion to attacks since 2021, per Chainalysis. And a significant share of these exploits used some variant of the same mechanic: flash loans.

A flash loan is a smart contract feature that lets a trader borrow millions of dollars with no collateral, on the condition that the loan is repaid inside the same transaction. The legitimate use cases include arbitrage between exchanges, collateral swaps without unwinding positions, and liquidation bots that maintain solvency in lending markets.

The attack pattern is the same mechanic pointed in the wrong direction.

A borrower takes out the loan, uses the funds to manipulate an oracle or drain a poorly designed pool, profits from the manipulation, and repays the loan, all before the transaction settles. If any step fails, the whole sequence rolls back, so the attacker risks nothing but gas fees.

The XRP Ledger does not let this work. A draft amendment filed on the XRPL standards repository earlier this week, proposing concentrated liquidity and StableSwap-style pools for the chain's native automated market maker, included a single line in its Security Considerations section: "Flash loan attacks are structurally impossible. XRPL transactions are atomic without composable intra-transaction calls."

What that means is that XRPL
