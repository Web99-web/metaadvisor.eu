---
title: "LayerZero blames KelpDAO for $290M hack, Lazarus group suspected"
slug: "layerzero-kelpdao-290m-hack-lazarus"
date: 2026-04-20T12:00:00+02:00
category: "crypto"
translationKey: "478999bba611acd09744f72c4b1e4477"
source: "Metaadvisor (CoinDesk, TechCrunch)"
source_url: "https://metaadvisor.eu/"
author: "Metaadvisor.eu"
image_url: "/images/hack/Hack-KelpDao-vsLayerZero-Lazarus-group.png"
featured_image: "/images/hack/Hack-KelpDao-vsLayerZero-Lazarus-group.png"
image: "/images/hack/Hack-KelpDao-vsLayerZero-Lazarus-group.png"
thumbnail: "/images/hack/Hack-KelpDao-vsLayerZero-Lazarus-group.png"
image_alt: "Kelp DAO hack, LayerZero and Lazarus group"
image_credit: "Metaadvisor.eu"
tags: ["crypto", "defi", "kelpdao", "layerzero", "lazarus", "hack", "security", "blockchain", "web3", "rpc", "ddos"]
summary: "A $290M Kelp DAO exploit highlights a sophisticated infrastructure attack, with LayerZero blaming configuration issues and pointing to the Lazarus group."
---

*The image is symbolic.*

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Claim your Bitget bonus up to 6200 USDT
  </a>
</p>

# Kelp DAO $290M hack: LayerZero points to configuration, Lazarus suspected

One of the largest crypto attacks of 2026, worth around $290 million, reveals a new level of sophistication in DeFi — while raising questions about responsibility between infrastructure providers and protocols.

The attack on Kelp DAO was not a classic smart contract exploit. Instead, it was a coordinated multi-layer attack targeting the underlying infrastructure, with potential links to state-backed hacking groups.

## How the attack was executed

According to LayerZero’s analysis, attackers did not target code — they targeted infrastructure.

Specifically, they compromised RPC nodes (Remote Procedure Call — servers that allow interaction with the blockchain) used by the LayerZero verifier to validate cross-chain transactions.

Attackers took control of two critical RPC nodes and replaced their software with malicious versions.

What makes this attack particularly dangerous:

* compromised nodes sent false data only to the verifier
* all other systems continued receiving correct data

👉 the system was “selectively deceived”

{{< support1 >}}

## DDoS and system manipulation

To bypass additional verification layers, attackers launched a DDoS (Distributed Denial of Service — overwhelming systems with traffic) attack on external RPC nodes.

This forced the system to rely solely on the compromised nodes.

The result:

👉 the verifier accepted a fraudulent transaction
👉 the bridge released funds
👉 116,500 rsETH were transferred to attackers

After execution, the malicious software self-destructed, erasing traces.

## The configuration issue

LayerZero argues the exploit was made possible by Kelp DAO’s system configuration.

A single-verifier model was used, without multi-layer validation.

This means:

* one central point of trust
* lack of redundancy
* increased vulnerability to targeted attacks

Kelp DAO, however, disputes part of that responsibility.

{{< support1 >}}

## Lazarus and TraderTraitor

The attack has been preliminarily linked to the Lazarus Group and its subunit TraderTraitor.

These groups have long targeted crypto projects due to:

* high liquidity
* global accessibility
* weaker regulatory frameworks

Estimates suggest:

* over $2 billion stolen last year alone
* around $6 billion stolen since 2017

Metaadvisor notes that such patterns have become increasingly common in recent years.

## Why North Korea is often mentioned

In major crypto attacks, Lazarus is frequently cited as the main suspect.

Part of this is justified — due to its track record.

However:

* attributions are often preliminary
* they are based on patterns, not definitive proof
* they are not always final

👉 “North Korea” often becomes a default narrative in large-scale hacks

{{< support2 >}}

## What this means for DeFi

The nature of attacks is evolving.

It is no longer enough to secure smart contracts alone.

Attackers are now targeting:

* infrastructure layers
* communication channels
* validation systems

This means security must extend across the entire stack.

## Conclusion

The Kelp DAO exploit shows how complex and fragile modern crypto systems have become.

This was not a random attack — it was precise, coordinated, and multi-layered.

Regardless of who is ultimately responsible, one thing is clear:

👉 infrastructure security is becoming critical for the future of Web3

---

## Our take (Metaadvisor):

* attacks are shifting from code to infrastructure
* configuration is becoming a critical security factor
* Lazarus remains a dominant narrative, but not always confirmed
* cross-chain systems are especially vulnerable
* Web3 still depends on centralized components

---

<p style="font-size:12px; color:#777;">
This content is for informational purposes only and does not constitute financial or investment advice.
</p>
