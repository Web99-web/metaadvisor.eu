---
title: "Glamsterdam 20.8.: Ethereum changes gas rules"
slug: "glamsterdam-20-8-ethereum-changes-gas-rules"
date: 2026-08-18T22:46:00+02:00
category: "Crypto"
translationKey: "ethereum-glamsterdam-gas-rules-2026-08-18"
source: "Ethereum Foundation, Ethereum Improvement Proposals, Forkcast, Cointelegraph"
author: "Metaadvisor.eu"
image_url: "/images/eth4.jpg"
featured_image: "/images/eth4.jpg"
image: "/images/eth4.jpg"
thumbnail: "/images/eth4.jpg"
image_alt: "Ethereum Glamsterdam upgrade on August 20, 2026 and changes to gas rules"
image_credit: "Metaadvisor.eu – symbolic image"
tags: ["Ethereum", "Glamsterdam", "ETH", "gas", "EIP-8037", "wallet", "Ethereum wallet", "blockchain", "crypto"]
description: "The Glamsterdam fork on Ethereum's public Platåberget testnet is scheduled for August 20, while the Ethereum Foundation warns developers that new gas changes may require adjustments to wallets, indexers and gas estimators."
summary: "The Ethereum Foundation is urging developers to test wallets, indexers and gas estimators before Glamsterdam. The fork on the public Platåberget testnet is scheduled for August 20 and includes a new model for pricing the creation of permanent blockchain state."
---

*Symbolic image.*

# Glamsterdam 20.8.: Ethereum changes gas rules

Ethereum is approaching the next testing phase of the upcoming Glamsterdam upgrade. The Glamsterdam fork on the public Platåberget testnet is scheduled for August 20, 2026, while the Ethereum Foundation is warning developers that changes to the gas model could expose problems in wallets, indexers and gas-estimation tools that still rely on older assumptions.

Platåberget launched on August 13 as a longer-running public testnet where developers can test their applications before Glamsterdam moves into later testing stages and potentially reaches mainnet.

## Some wallets and gas estimators need adjustments

The Ethereum Foundation is specifically warning about tools that rely on hardcoded assumptions about maximum gas limits or the way gas is calculated.

The Glamsterdam changes affect a broad part of Ethereum infrastructure because they may impact wallets, indexers and gas estimators. Developers are therefore being encouraged to use Platåberget to identify assumptions in their software that may no longer remain valid.

This does not mean Ethereum wallets will suddenly stop working for users on August 20. The August 20 date refers to the Glamsterdam fork on the Platåberget testnet. The purpose of this testing phase is precisely to identify problems before the upgrade is later activated on mainnet.

## Ethereum introduces new costs for state creation

One of the more important changes is EIP-8037, which changes the cost of operations that create new permanent state on the Ethereum network.

EIP-8037 introduces a cost per newly created byte of state and separates state gas more clearly from the regular gas model. The goal is to prevent higher block gas limits from automatically causing uncontrolled growth in the amount of data Ethereum nodes must store permanently.

Ethereum developers have said EIP-8037 targets average state growth of roughly 120 GiB per year at a reference block gas limit of 150 million gas units.

{{< support1 >}}

## Why does this matter?

Ethereum has been trying for years to increase Layer 1 capacity. But higher throughput also means greater pressure on infrastructure.

If a higher gas limit allows significantly more permanent state to be created in each block, the database that nodes must maintain can grow too quickly. Glamsterdam therefore does not simply increase capacity; it also reprices certain operations so that their cost better reflects the resources they consume.

In other words, Ethereum wants to allow more throughput without making the blockchain increasingly difficult to maintain over the long term.

## Glamsterdam is much more than a gas change

The gas-model change is only one part of a much larger upgrade.

Glamsterdam also includes enshrined proposer-builder separation, known as ePBS, Block-Level Access Lists and other changes to the Ethereum protocol. Over recent months, Ethereum developers have been testing these components in parallel while preparing the network for significantly higher gas limits.

At an Ethereum core developer interoperability event earlier this year, a 200 million block gas limit was discussed as a credible possible post-Glamsterdam target, provided the new optimisations and rules make such an increase safe.

{{< support2 >}}

## What does this mean for ordinary ETH users?

For most users, the key point is simply that the wallets, exchanges and applications they use should be updated before Glamsterdam eventually reaches Ethereum mainnet.

The current warning is aimed primarily at developers. Platåberget gives them an opportunity to find places where software still assumes the old gas rules and make the necessary adjustments.

August 20 is therefore not the date when Ethereum changes for every user. It is an important date in the testing process for Glamsterdam.

## Our view

* The Glamsterdam fork on August 20 applies to the public Platåberget testnet, not Ethereum mainnet.
* The Ethereum Foundation is openly warning that the changes may expose problems in wallets, indexers and gas estimators that rely on outdated assumptions.
* EIP-8037 introduces more precise pricing for the creation of permanent state so that higher gas limits do not lead to uncontrolled database growth.
* Glamsterdam is a broader upgrade that also includes ePBS, Block-Level Access Lists and other changes aimed at scaling Ethereum Layer 1.
* For ordinary users, there is currently no reason to panic — that is exactly why Ethereum is testing the changes before any potential mainnet activation.

**Disclaimer:** This article is for informational purposes only and does not constitute investment advice. The Glamsterdam fork on August 20, 2026 applies to the Platåberget testnet. The date of Glamsterdam activation on Ethereum mainnet is separate from this testnet fork and may be determined later in the development and testing process.

*In collaboration with AI.*
