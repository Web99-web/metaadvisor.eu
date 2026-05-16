---
title: "THORChain Opens Refund Portal After $10M Hack"
date: 2026-05-16T09:47:44Z
category: "ai"
translationKey: "59bc6419b5914336927f965685320d91"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/thorchain-confirms-10m-exploit-rolls-out-recovery-portal-for-affected-users?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://s3-images.ctmedia.io/media/article-covers/lawsuit-litigation-court-1.jpg"
tags: ["ai"]
_build:
  publishResources: false
  render: never
  list: never
---

THORChain has launched a recovery portal following a $10 million exploit, allowing affected users across four chains to revoke malicious approvals and claim refunds.

THORChain has confirmed a $10 million exploit and launched a recovery portal, giving affected users a self-custodial path to revoke malicious token approvals and submit refund claims backed by a treasury-provisioned refund pool of equal size.

In a Saturday post on X, THORChain Foundation introduced the recovery portal, saying that “affected users are now able to check what they will be paid as compensation following the exploit.”

The portal, citing a PeckShield post-mortem, claims that the attack was detected at 02:14 UTC on May 11, when node operators flagged anomalous outbound transactions. Trading and outbound signing were paused within eight minutes. In total, attackers drained 36.75 BTC, worth around $3 million, and approximately $7 million in tokens across BNB Chain, Ethereum and Base, hitting 12,847 wallets across four chains.

THORChain’s recovery portal. Source: THORChain

Affected users have 21 days to submit claims. The refund window closes on June 4, after which any unclaimed allocation rolls over to the protocol’s insurance fund.

Related: Russia-linked crypto exchange Grinex halts trading after $14M hack

In an incident update, THORChain said the leading theory is that the attacker exploited a vulnerability in the GG20 threshold signature scheme (TSS) implementation, which allowed sensitive vault key material to leak gradually. By accumulating enough of this leaked data over time, the attacker was able to reconstruct the vault’s private key and authorize unauthorized outbound transactions.

The protocol also noted that a newly churned node entered the network several days before the attack
