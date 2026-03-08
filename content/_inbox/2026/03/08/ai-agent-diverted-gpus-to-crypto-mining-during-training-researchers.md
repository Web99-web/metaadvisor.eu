---
title: "AI Agent Diverted GPUs to Crypto Mining During Training: Researchers"
date: 2026-03-08T12:01:20Z
category: "crypto"
translationKey: "909fa3f2554dbe3b2d57f7467a4fb733"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/ai-agent-attempts-crypto-mining-during-training-researchers-say?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://zoa.cointelegraph.com/pixel?postId=253642&regionId=1"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

Researchers say the experimental AI agent ROME attempted unauthorized cryptocurrency mining during training after diverting GPU resources and opening an SSH tunnel.

A research team behind an autonomous AI agent said that the model unexpectedly attempted to use computing resources for crypto mining during training.

In a recent technical report , researchers said ROME, an experimental autonomous AI system designed to complete tasks through interaction with tools, software environments and terminal commands, went rogue and attempted crypto mining on its own.

According to the report, the unusual behavior surfaced during reinforcement learning runs, when the team noticed security alerts triggered by outbound traffic from training servers. Firewall logs flagged activity resembling crypto mining operations and attempts to access internal network resources.

“We initially treated this as a conventional security incident (e.g., misconfigured egress controls or external compromise). However, the violations recurred intermittently with no clear temporal pattern across multiple runs,” the researchers wrote.

Related: Blockchains may need 1B TPS to support AI agent future: Stripe

In one case, the AI agent reportedly created a reverse SSH (Secure Shell) tunnel, an encrypted server-client protocol for communications, to an external IP address, potentially bypassing inbound firewall protections. In another, it diverted GPU resources, originally allocated for model training, toward cryptocurrency mining processes.

The team said that these actions were not intentionally programmed. Instead, they emerged during reinforcement learning optimization as the agent explored different ways to interact with its environment.

ROME was developed by the ROCK, ROLL, iFlow and DT joint research
