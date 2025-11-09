---
title: "The impossibility of perfect fairness in transaction ordering"
date: 2025-11-09T15:00:00Z
category: "ai"
translationKey: "92066eddaf1ff964247a4827e882bac2"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/the-impossibility-of-perfect-fairness-in-transaction-ordering?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://images.cointelegraph.com/cdn-cgi/image/format=auto,onerror=redirect,quality=90,width=1434/https://s3.cointelegraph.com/uploads/2025-01/01942ae8-4c7a-7dd2-8050-a617b053ffb3"
tags: ["ai"]
_build:
  publishResources: false
  render: never
  list: never
---

Explore how the Condorcet paradox exposes the limits of perfect fairness in blockchain consensus.

For decades, research in distributed systems, especially in Byzantine consensus and state machine replication (SMR) , has focused on two main goals: consistency and liveness. Consistency means all nodes agree on the same sequence of transactions, while liveness ensures the system continues to add new ones. Still, these properties do not stop bad actors from changing the order of transactions after they are received.

In public blockchains, that gap in traditional consensus guarantees has become a serious problem. Validators , block builders or sequencers can exploit their privileged role in block ordering for financial gain, a practice known as maximal extractable value ( MEV ). This manipulation includes profitable frontrunning, backrunning and sandwiching of transactions. Because transaction execution order determines validity or profitability in DeFi applications, the integrity of transaction ordering is vital for maintaining fairness and trust.

To address this critical security gap, transaction order-fairness has been proposed as a third essential consensus property. Fair-ordering protocols ensure that the final order of transactions depends on external, objective factors, such as arrival times (or receiving order) and is resistant to adversarial reordering. By limiting how much power a block proposer has to reorder transactions, these protocols move blockchains closer to being transparent, predictable, and MEV-resistant.

The most intuitive and strongest notion of fairness is Receive-Order-Fairness (ROF) . Informally defined as “first received, first output,” ROF dictates that if a sufficient number of transactions (tx) arrive at a majority of nodes earlier than
