---
title: "Address copied — and $50 million lost: the biggest crypto mistake of the year"
slug: "address-poisoning-copied-address-50-million-dollars-lost"
date: 2025-12-20T12:00:00
category: "crypto"
translationKey: "address_poisoning_50m_loss_20122025"
source: "Cointelegraph, CoinDesk"
source_url: "cointelegraph.com, coindesk.com"
author: "Metaadvisor.eu"
image_url: "/images/Lost-50-mil-usd.png"
featured_image: "/images/Lost-50-mil-usd.png"
image: "/images/Lost-50-mil-usd.png"
thumbnail: "/images/Lost-50-mil-usd.png"
image_alt: "Address poisoning scam and loss of 50 million dollars after copying a crypto address"
image_credit: "MetaAdvisor illustration"
tags:
  - bitcoin
  - crypto
  - security
  - scam
  - address poisoning
  - usdt
  - ethereum
  - wallet
  - on-chain
  - tornado cash
  - cybercrime
summary: "A single copied crypto address was enough to lose nearly $50 million in USDT. This case shows how address poisoning attacks exploit human behavior rather than blockchain vulnerabilities."
---

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter"
     target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Unlock a Bitget bonus of up to 6200 USDT — start trading
  </a>
</p>

In one of the most expensive individual crypto incidents of the year, a user **lost nearly $50 million in USDT** after falling victim to a sophisticated *address poisoning* scam. There was no wallet hack, no private key theft, and no blockchain failure. Everything happened within what most users consider “normal” wallet usage — which is precisely what makes this case so dangerous.

This was an attack targeting **human behavior**, not technology.

## What exactly happened?

According to on-chain data, the victim first withdrew a large amount of **USDT (Tether)** from an exchange. As a safety measure, a **small test transfer (0.005 USDT)** was sent to what was believed to be the correct address. The test transaction succeeded.

Before the main transfer, however, attackers managed to **poison the wallet’s transaction history**. A **fake address** appeared in the history that looked almost identical to the real destination — sharing the same first three and last four characters.

When the user later copied the address from the transaction history, they unknowingly copied **the attacker’s address** and sent **approximately 49,999,950 USDT**. The transaction was technically valid — and irreversible.

The test transfer did not help because:
- the test was sent to a previously saved address  
- the main transfer was sent to an address **copied from transaction history**

Two addresses. One mistake. A massive loss.

## What is an address poisoning scam?

*Address poisoning* is a scam technique that does not break cryptography or compromise the blockchain. Instead, attackers **mass-generate wallet addresses** until they find ones that closely resemble real target addresses — identical beginnings and endings, but different middle characters.

They then send **minimal “dust” transactions** to potential victims. Wallets record these transactions normally, without warnings. When users later copy an address from their “recent” list, they may unknowingly copy **the wrong address**.

This attack:
- requires no malware  
- requires no phishing links  
- leaves no technical error  

Everything occurs within standard wallet user interfaces.

## Rapid conversion and laundering of funds

After receiving nearly **$50 million in USDT**, the attacker quickly moved the funds through several steps:

- USDT was converted into **DAI**, a decentralized stablecoin  
- DAI was then swapped for approximately **16,690 ETH**  
- Almost the entire amount (**around 16,680 ETH**) was sent through **Tornado Cash**

This process effectively obscured the origin of the funds and made recovery extremely difficult. While Tornado Cash no longer operates as a traditional project with a public frontend, its **smart contracts still exist on-chain** and can be called directly — something criminals continue to exploit.

### [Tornado Cash: Roman Storm, Lazarus and the most controversial crypto court case of the decade](https://metaadvisor.eu/news/tornado-cash-roman-storm-lazarus-crypto-court-case/)

## Why this scam matters

This case highlights a harsh reality: today’s biggest crypto risks are **no longer technical**, but **operational**. Instead of smart contract bugs, attackers increasingly exploit:

- human error  
- poor wallet UX  
- the habit of copying addresses without full verification  

Such attacks can result in **losses worth tens of millions of dollars**, even for experienced users.

## How to protect yourself

**Never copy wallet addresses from transaction history — use an address book, ENS or domain-based addresses, and always verify the middle of the address, not just the beginning and end.**

<p style="font-size:0.85em; color:#6b7280; margin-top:18px;">
<strong>Disclaimer:</strong> This content is provided for informational purposes only and does not constitute financial advice. Cryptocurrency markets are volatile and risky; always conduct your own research before making financial decisions.
</p>
