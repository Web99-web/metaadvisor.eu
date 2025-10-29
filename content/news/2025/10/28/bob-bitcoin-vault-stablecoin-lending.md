---
title: "BOB: borrow stablecoins without losing control of your BTC (Bitcoin rollup)"
slug: "bob-bitcoin-vault-stablecoin-lending"
date: 2025-10-28T14:30:00Z
category: "defi"
translationKey: "7f3a6a02-b7f5-4d2c-9d3b-1c34dfbb13b0"
source: "CoinDesk"
source_url: ""
author: "CoinDesk"
analysis_by: "Metaadvisor.eu"
image_url: "/images/bob-bitcoin-vault-stablecoin.png"
featured_image: "/images/bob-bitcoin-vault-stablecoin.png"
image: "/images/bob-bitcoin-vault-stablecoin.png"
thumbnail: "/images/bob-bitcoin-vault-stablecoin.png"
image_alt: "BOB Bitcoin Vault — borrow stablecoins while keeping BTC self-custody"
image_credit: "Illustration — Metaadvisor.eu (symbolic image)"
tags: ["BOB","Build on Bitcoin","Bitcoin","BTC","stablecoin","DeFi","vault","rollup","layer-2","self-custody","crypto lending","collateral","liquidation","TVL"]
summary: "BOB (Build on Bitcoin) enables BTC-collateralized stablecoin borrowing without surrendering keys — a rollup approach that anchors DeFi functionality to Bitcoin security."
---

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="/go/mexc" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Trade BTC on MEXC
  </a>
</p>

**Summary (what’s new)**  
**BOB (Build on Bitcoin)** introduces the **Bitcoin Vault Liquidation Engine** — a mechanism that lets BTC holders **borrow stablecoins** against BTC as collateral while **keeping control of their private keys** (*self-custody*). If BTC drops sharply, part of the collateral can be **automatically liquidated** to protect the loan.

---

## What is BOB?
**BOB = Build on Bitcoin.** It’s an **open-source protocol** bringing **DeFi mechanics to the Bitcoin ecosystem**. Unlike centralized firms, BOB is built by the **BOB team / developer community** (*BOB Builders*), often with partners and VC support.

---

## 🔑 How it works
Because Bitcoin lacks native smart contracts like Ethereum, BOB uses **layer-2 / sidechain / rollup** approaches.

- A **“Bitcoin rollup”** runs smart contracts and DeFi on a separate execution layer while regularly **anchoring security** back to Bitcoin (e.g., via state commitments).  
- This enables **Bitcoin-connected DeFi apps** (lending, stablecoin issuance, vaults) **without** modifying the Bitcoin core protocol.

**Key terms:**  
- **Layer-2 (L2)** — an additional layer that increases functionality/throughput.  
- **Rollup** — batches transactions off-chain and commits verified summaries onto the base chain.

---

## Who is behind it?
The **BOB team (BOB Builders)** publishes the **app, docs, and code**. The model resembles **open-source protocol + (potential) foundation**, similar to parts of the Ethereum ecosystem.

---

## How the “Bitcoin Vault” operates (high level)
1) **Deposit BTC** into a BOB-connected smart contract (vault).  
2) **Borrow stablecoins** (e.g., USDC/USDT or natively supported tokens) under LTV rules.  
3) **Collateral monitoring**: sharp price declines can trigger **partial liquidations**.  
4) **Self-custody**: users **retain their keys**, no third-party custodian required.

> Implementation details (LTV ratios, stablecoin types, liquidation thresholds, oracles) depend on the protocol version and may evolve.

---

## How to access BOB
The protocol is available via an **official app and documentation** published by the BOB team; all code is **open source**. In practice, users connect a **wallet**, use a **bridge** to move BTC into the BOB rollup, open a **vault** in the app, and borrow stablecoins.  
Current communications cite roughly **$275M in Total Value Locked (TVL)** — indicating notable traction.

> Note: Always verify you are using **official channels**. We intentionally avoid external links in-article to reduce the risk of misdirects or scams.

---

## Why it matters
- **Self-custody by default**: the “Not your keys, not your coins” principle is preserved.  
- **DeFi on Bitcoin**: broader financial primitives around the largest crypto asset.  
- **Liquidity without selling BTC**: borrow stables while keeping a long BTC position.

---

## Bigger picture & risks
- Potential for a **new wave of Bitcoin-based DeFi** and appeal to more conservative holders.  
- **Risks**: BTC volatility, **liquidation design**, **oracle dependencies**, smart-contract risk, and **regulatory treatment** (credit product vs. software protocol).  
- Before use, review **docs, parameters (LTV, rates)**, and security audits.

---

### Our take (Metaadvisor)
- The approach aligns with the **Bitcoin ethos**: keep keys, minimize trust.  
- A **Bitcoin rollup** could accelerate “DeFi on BTC” and reduce reliance on alt-chains for BTC financialization.  
- Success hinges on **robust liquidation logic**, transparent oracles, and **high-quality code audits**.

---

*Disclaimer: This content is for informational purposes only and does not constitute investment advice. Always verify official channels, technical documentation, and regulatory risks before using any protocol.*
