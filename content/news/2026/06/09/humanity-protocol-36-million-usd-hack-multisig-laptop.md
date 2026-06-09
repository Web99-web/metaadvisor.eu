---
title: "Humanity Protocol $36M hack: how a multisig ended up on one laptop"
slug: "humanity-protocol-36-million-usd-hack-multisig-laptop"
date: 2026-06-09T12:00:00+02:00
category: "crypto"
translationKey: "humanity-protocol-hack-multisig-laptop-2026-06-09"
source: "CoinDesk, Metaadvisor.eu"
source_url: "https://metaadvisor.eu/"
author: "Metaadvisor.eu"
image_url: "/images/hack/Humanity-protocol-hack-36M.png"
featured_image: "/images/hack/Humanity-protocol-hack-36M.png"
image: "/images/hack/Humanity-protocol-hack-36M.png"
thumbnail: "/images/hack/Humanity-protocol-hack-36M.png"
image_alt: "Humanity Protocol hack 36M exploit symbolic image"
image_credit: "MetaAdvisor.eu"
tags: ["Humanity Protocol", "H token", "crypto hack", "private key", "private keys", "multisig", "multisignature wallet", "bridge exploit", "BNB Chain", "Ethereum", "DeFi", "crypto security", "token crash", "zero knowledge", "digital identity", "biometrics", "Worldcoin", "crypto theft", "blockchain", "Web3 security", "crypto bridge", "token minting"]
summary: "Humanity Protocol suffered a serious security incident after private keys were compromised, while its H token crashed more than 80%. The case shows that a multisig is not real protection if key signatures are poorly secured or end up on the same compromised device."
---

*The image is symbolic.*

# Humanity Protocol after the hack: when a multisig ends up on one laptop

Humanity Protocol, a project positioning itself as a decentralized identity solution, has become the center of one of those incidents that quickly turn a technology story into a question of trust. Its H token crashed by more than 80% after attackers compromised private keys connected to the project and drained tens of millions of dollars in value.

Initial estimates pointed to more than $32 million in lost funds, while later explanations of the incident suggested a figure closer to $36 million. The number matters, but the story behind it matters even more: this does not appear to have been caused by a highly complex smart contract bug. It appears to have come from a much more basic security failure — keys that were supposed to be separated ended up, at least partly, on a compromised device.

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Claim a Bitget bonus of up to 6200 USDT — register here
  </a>
</p>

## Why was the H token crash so severe?

Humanity Protocol uses palm-scan biometrics and zero-knowledge cryptography to allow users to prove they are real people without directly revealing personal data. In theory, this is a highly relevant idea. In a world of AI bots, fake profiles, automated accounts and digital fraud, proving that a real human stands behind an account is becoming increasingly important.

That is exactly why this incident is so uncomfortable. When a project built around trust in digital identity suffers a private-key security incident, the damage is not only financial. It directly affects the project’s reputation. If users are supposed to trust a system that proves identity, they must first be able to trust that the project can protect its own keys.

The H token fell from around $0.67 to roughly $0.13 and at one point touched about $0.05. That means the intraday decline was close to 90%. Such crashes are not unusual in crypto when the market senses that the problem has not yet been contained, especially if the attacker continues selling stolen tokens or if additional selling pressure may follow.

{{< support1 >}}

According to available information, the attacker emptied several wallets connected to the project, sold stolen H tokens for ether and additionally minted 100 million H tokens on BNB Chain. That is especially dangerous because it does not only mean that someone stole existing assets. It also means additional tokens could be created, increasing pressure on the market.

## What does it mean that the multisig was compromised?

The central part of the story concerns a multisig, or multisignature wallet. In theory, a multisig is a security mechanism designed to prevent one person or one device from being able to control funds or change important system settings alone. Instead of one private key, several separate signatures are required to approve an action.

It is important to understand that multisig does not automatically mean all keys are required. If there are six keys, the system may be configured so that three out of six signatures are enough, four out of six are enough, or some other combination is required. If the threshold is set at three out of six, an attacker does not need all six keys. Getting three keys is enough to cross the approval threshold.

In this case, the problem was not only that someone obtained private keys. The problem was that keys that were supposed to be organizationally and physically separated apparently became accessible through one compromised laptop. That defeats the purpose of a multisig. From the outside, the system may look decentralized, but if enough keys are stored in one place, the risk becomes centralized again.

{{< support1 >}}

Humanity Protocol explained that the incident began with the compromise of an employee’s laptop. That device reportedly held keys connected to the project’s bridges — tools that allow H tokens and other connected tokens to move between different blockchains. Bridges are already frequent targets because they connect multiple networks, multiple contracts and often large amounts of liquidity.

## How could the attacker take control?

According to the project’s explanation, the attacker obtained three of six keys controlling the bridge’s admin account on Ethereum. Those three keys were enough to cross the approval threshold. After that, the attacker could transfer ownership to their own wallet, replace the bridge code with a malicious version and drain a large amount of H tokens in a single transaction.

This detail matters because it shows the difference between security design on paper and real operational security. On paper, a multisig can look like serious protection. In practice, if keys are backed up incorrectly, if multiple signatures become accessible through one device, or if the setup process is not controlled strictly enough, the multisig becomes much weaker than investors may assume.

Humanity Protocol founder Terence Kwok said the team had originally set up the multisig across several people, as such a system should work. However, the suspicion is that some keys were accidentally backed up to a compromised device during setup. That means the formal problem was not necessarily the idea of a multisig itself, but how it was implemented and stored in practice.

{{< support2 >}}

For ordinary users, this may sound technical, but the idea is simple. A multisig is like a safe that opens with several keys. If those keys are held by different people, in different places and on secure devices, the risk is lower. If enough keys are copied to one laptop, the attacker no longer needs to attack the whole team. Compromising one device may be enough.

## The bigger lesson for the crypto sector

This case fits a broader trend in which major crypto losses increasingly come not from sophisticated code bugs, but from compromised keys, poor access management and weak internal procedures. That means security can no longer be reduced to smart contract audits alone. Serious operational security is also required.

For projects managing bridges, treasury funds, admin functions or the ability to mint new tokens, key management must be treated as seriously as the code itself. Hardware wallets, separated devices, clear backup rules, custodian or MPC solutions and strict internal controls are no longer optional extras. They are basic security infrastructure.

The ability to mint new tokens is especially sensitive. If an attacker gains admin control and can create additional tokens, the damage does not stop at the theft of existing funds. Additional minting can damage confidence in the project’s tokenomics, increase selling pressure and trigger a panic reaction across the market.

For investors and users, this is a reminder that it is not enough to ask what a project does, how modern the narrative sounds or who supports it. They should also ask who holds the keys, where those keys are stored, what the multisig threshold is, who can change the bridge, who can mint tokens and what happens if one employee loses or compromises a laptop. Metaadvisor sees this as one of the key practical questions that ordinary crypto users often never get to see in marketing materials.

{{< support2 >}}

## Our view (Metaadvisor)

- Humanity Protocol built its story around digital identity and proving humanness, but this incident shows that trust begins long before the user-facing product — with the project’s basic security architecture.

- The biggest problem is not only the token crash, but the fact that a multisig, which is supposed to reduce risk, appears to have been weakened by poor key-management practices.

- This is a strong example of why investors should not look only at narrative, backers, technology and marketing. Operational security is less visible, but it can be decisive.

- If a project uses bridges, admin keys and the ability to mint tokens, it needs extremely strict procedures. Otherwise, one compromised laptop can become enough for a multimillion-dollar collapse.

- This is not only a story about Humanity Protocol. It is a warning for the entire crypto sector: decentralization means little if the most important keys are concentrated, poorly backed up or insufficiently protected.

<p style="font-size:0.85em; color:#777; line-height:1.5; margin-top:28px;">
Disclaimer: This content is for informational purposes only and does not constitute financial or investment advice.
</p>
```
