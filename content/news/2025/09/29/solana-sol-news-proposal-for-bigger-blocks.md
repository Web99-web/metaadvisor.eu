---
title: "Solana (SOL) — proposal to enable bigger blocks after Alpenglow"
slug: "solana-sol-news-proposal-for-bigger-blocks"
date: 2025-09-29T16:15:40Z
category: "crypto"
translationKey: "solana-bigger-blocks-simd-0370"

author: "CoinDesk"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2025/09/29/firedancer-devs-from-jump-crypto-pushes-solana-toward-bigger-blocks"
image_url: "/images/solana-sol.png"
featured_image: "/images/solana-sol.png"
image: "/images/solana-sol.png"
thumbnail: "/images/solana-sol.png"
image_alt: "Solana logo and network — bigger blocks proposal"
image_credit: "Metaadvisor.eu"

tags:
  - solana
  - SOL
  - Firedancer
  - SIMD-0370
  - Alpenglow
  - throughput
  - validators
  - defi
  - fees
  - scaling

summary: "Jump Crypto’s Firedancer team proposed SIMD-0370 to remove the per-block compute-unit cap after the Alpenglow upgrade. The goal is more throughput and burst capacity — with open questions around propagation, hardware pressure and fees."
---

> **Note:** Image is symbolic.

## What’s on the table
Firedancer developers submitted **SIMD-0370** to **remove the per-block compute-unit (CU) limit** on Solana (currently ~**60M CU** per block) **after** the **Alpenglow** upgrade. Block producers could then build **bigger blocks**, bounded by validator performance rather than a hard cap.

Previously, core devs floated raising the cap to **100M CU**; this proposal goes further — **cap removal**.

## Why it might help
- **Peak demand handling:** token launches/DeFi spikes process **more txs**, cut **failed trades**.  
- **Validator-level flexibility:** faster machines can utilize spare headroom instead of waiting on a global ceiling.

## Trade-offs and risks
- **Propagation/latency:** larger blocks take longer to gossip → **higher fork/orphan risk**, more variance.  
- **Hardware arms race:** favors high-end operators → **centralization pressure**.  
- **MEV dynamics:** larger batches may widen **arb/sandwich** windows.  
- **Fees reality:** sustained demand still pushes **median fees** up; capacity ≠ free tx.

## Voices in the thread
Supporters see meaningful **burst capacity**;  
**Anatoly Yakovenko** notes blocks aren’t consistently full today, so **end-user impact** may be limited without stronger demand.

## What’s next
The proposal is **under discussion**. If accepted, activation would follow **Alpenglow**; expect guard-rails (soft limits/telemetry) to be tuned iteratively.

---

## Our take (Metaadvisor)
- **Aligned with Solana’s thesis:** **high throughput + short slots**. Removing the cap only works if **propagation** and **consistency** improve (Firedancer’s focus).  
- **We’d like to see:** **soft caps**, network **telemetry-based throttling**, and clear **min-specs** to avoid validator squeeze.  
- **Bull case:** fewer **failed tx** during bursts → **better UX**, higher volumes/fees.  
- **Risk:** hardware escalation narrows validator set; network-level optimizations (QUIC tuning, gossip) remain critical.

*Informational content. Not financial advice.*
