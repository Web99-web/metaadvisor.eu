---
title: "Hackers Returned BTC as Promised: Liquid Hack of 4,000 BTC"
slug: "hackers-returned-btc-liquid-hack-4000-btc"
date: 2026-09-08T10:00:00+02:00
category: "Crypto"
translationKey: "liquid-white-hat-hackers-return-bitcoin-2026-09-08"
source: "Liquid Network, Blockstream, SideSwap, Bitquery, The Block, Metaadvisor.eu"
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
featured_image: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
image: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
thumbnail: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
image_alt: "White-hat hackers withdrew 4,000 BTC from Liquid Network and returned 3,400 BTC after the patch"
image_credit: "Metaadvisor.eu"
tags: ["Liquid Network", "Bitcoin", "crypto", "hackers", "white-hat hackers", "Blockstream", "SideSwap", "Elements", "blockchain", "OP_RETURN", "security", "cybersecurity", "L-BTC", "Bitcoin sidechain", "crypto security"]
description: "Actors calling themselves white-hat hackers withdrew nearly 4,000 BTC from Liquid Network, told Blockstream to fix the bug first and returned 3,400 BTC after the patch."
summary: "Liquid Network lost nearly 4,000 BTC after a bug in Elements was exploited. The actors promised through messages written directly into the Bitcoin blockchain to return most of the funds after the vulnerability was fixed — and then returned 3,400 BTC."
---

*Image is symbolic.*

# "White-Hat" Hackers Withdrew 4,000 BTC from Liquid, Said "Fix the Bug First" — Then Returned 3,400 BTC

**One of the most unusual crypto security incidents of the year took an even more unusual turn: actors calling themselves white-hat hackers withdrew nearly 4,000 BTC from Liquid Network, worth around $320 million at the time, told Blockstream they would return most of it once the vulnerability was fixed — and then actually returned 3,400 BTC.** Even more remarkably, much of the negotiation did not take place by email, Telegram or private chat, but through messages written directly into the Bitcoin blockchain.

The incident affected **Liquid Network**, a Bitcoin sidechain that uses the open-source Elements software. According to information published so far, the problem did not arise because someone stole the Liquid Federation's private keys or compromised SideSwap's Peg-out Authorization Key. A bug associated with Elements apparently made it possible to create L-BTC without corresponding real Bitcoin backing, after which those tokens passed through the peg-out process and the federation released real BTC.

## Nearly 4,000 BTC Left Through a Transaction That Looked Legitimate

The incident began on September 6 when around **4,000 L-BTC were sent to SideSwap's peg-out service**. SideSwap said its system processed the transaction as a normal customer order: the L-BTC were burned using a valid peg-out authorization, after which the Liquid Federation paid approximately **3,996 BTC** to the user's Bitcoin address.

SideSwap says its PAK was not compromised. According to the information currently available, the problem originated earlier in the Elements software on which Liquid runs, allowing L-BTC without real backing to reach the point where they could be redeemed for actual Bitcoin.

The federation wallet held approximately **4,200 BTC before the incident**, meaning the withdrawal removed around 95% of its Bitcoin reserve. Liquid subsequently disabled bridge nodes and asked exchanges to halt L-BTC deposits and withdrawals. The Bitcoin mainnet itself was not compromised.

## The First Message in the Blockchain: "We Are Whitehats"

A few hours after the withdrawal, something happened that completely changed the tone of the incident. On **September 6 at 18:30 UTC**, the address holding nearly 4,000 BTC sent a new Bitcoin transaction. Its OP_RETURN output contained a message.

**Hexadecimal record in the blockchain:**

**`776520617265207768697465686174732e20636f6e74616374207573206f6e20636861696e`**

**“We are white-hat hackers. Contact us on-chain.” (original: “we are whitehats. contact us on chain”)**

It is important to understand how anyone noticed this message among millions of Bitcoin transactions in the first place. Nobody was searching the entire blockchain for interesting sentences. After nearly 4,000 BTC had been withdrawn, the address where the funds landed was already under intense scrutiny by Blockstream, security teams and blockchain analysts. Any new transaction from that address could automatically trigger an alert.

An OP_RETURN output is also easy for software to identify because it uses a dedicated opcode in Bitcoin Script. When an analytics tool or block explorer sees that OP_RETURN contains data that can be decoded as text, it can immediately convert the hexadecimal record into a readable message. In other words, the hackers did not throw a message into an endless ocean of blockchain data and hope someone would stumble across it. They sent it from the exact address everyone was already watching.

That makes their phrase **“contact us on chain”** even more interesting. In effect, they were saying: **“We know you are watching this wallet — talk to us here.”**

This is the actual computer representation of the sentence. In the Bitcoin blockchain, letters are stored as bytes that can be displayed in hexadecimal form. For example, `77` represents the letter `w`, while `65` represents `e`, so the beginning `7765` decodes to the word `we`.

A Bitcoin block explorer can automatically convert that hexadecimal content back into readable text. A user opening the transaction can therefore see the OP_RETURN data and read the message left by the actors.

Even more unusually, this was not simply a comment stored somewhere beside the transaction. **The message itself became part of Bitcoin's permanent blockchain record.**

{{< support1 >}}

## Blockstream Replies — Also Through Bitcoin

Blockstream accepted their method of communication. About an hour later, on **September 6 at 19:31 UTC**, a new Bitcoin transaction was sent from an address associated with Blockstream containing an OP_RETURN message.

**Hexadecimal record in the blockchain:**

**`506c6561736520636f6e7461637420736563757269747940626c6f636b73747265616d2e636f6d`**

**“Please contact security@blockstream.com.” (original: “Please contact security@blockstream.com”)**

Blockstream therefore responded in the same way — with a message embedded inside a Bitcoin transaction. Instead of immediately moving the conversation to email or another private platform, the first response remained permanently recorded in the blockchain.

Blockstream later sent a PGP-signed encrypted message as well. The signature could be checked against Blockstream's publicly available security key, making it possible to verify that the communication really came from Blockstream's security side.

But the white-hat side continued the conversation on-chain.

## "Sending Most Back — Is This the Right Address?"

On **September 7 at 02:20 UTC**, the actors sent another transaction. This time, the message contained the full Liquid Federation wallet address to which they intended to return the Bitcoin.

**Hexadecimal record in the blockchain:**

**`73656e64696e67206d6f7374206261636b20746f2062633171646c6c6436616e746d76347875673234326564383371376b3472717735306377666e733338737a783471753266346a77617878737568777878722c2069732074686174206f6b`**

**“Sending most back to bc1qdlld6antmv4xug242ed83q7k4rqw50cwfns38szx4qu2f4jwaxxsuhwxxr, is that OK?” (original: “sending most back to bc1qdlld6antmv4xug242ed83q7k4rqw50cwfns38szx4qu2f4jwaxxsuhwxxr, is that ok”)**

This may have been the first moment when it became clear that their initial claim of being white-hat hackers might not have been merely an attempt to buy time. **They did not just say they would return the money — they provided the address to which they planned to return most of the nearly 4,000 BTC and asked Blockstream whether it was correct.**

Blockstream replied **“Yes, thank you.”**

But before the actual return, an even more important message followed.

## "Please Fix the Bug First"

On **September 7 at 03:30 UTC**, the white-hat side sent a third publicly readable message. It effectively explained why they would not return the Bitcoin immediately.

**Hexadecimal record of the publicly readable part of the message in the blockchain:**

**`506c656173652066697820746865206275672066697273742e2054686520636861696e20697320756e646572207269736b206174206c617465737420636f6d6d6974207269676874206e6f772e204d616b652073757265206576657279206e6f646520697320706174636865642e205468656e2077652077696c6c207472616e7366657220746865206d6f6e6579206261636b20736166656c7920616674657220636f6e6669726d696e6720746865206669782e`**

**“Please fix the bug first. The chain is under risk at latest commit right now. Make sure every node is patched. Then we will transfer the money back safely after confirming the fix.”**

After this publicly readable text, the same OP_RETURN record also contained a **PGP-encrypted technical section** intended for Blockstream. The public could see the encrypted data but could not read its contents without the private key. According to researchers who analyzed the blockchain, that section contained technical information about the vulnerability.

The message was clear: **do not simply confirm the address and take the Bitcoin back — first make sure the same vulnerability no longer exists.**

{{< support2 >}}

## Blockstream Says the Bridge Nodes Are Patched

After working on the security issue, Blockstream sent a signed on-chain message confirming that the problem affecting the bridge nodes had been patched.

**Hexadecimal record in the blockchain:**

**`427269646765206e6f6465732061726520706174636865642c207361666520746f2072657475726e207468652066756e64732e`**

**“Bridge nodes are patched, safe to return the funds.”**

That satisfied the condition the actors had written into the Bitcoin blockchain only hours earlier.

Then came the decisive turn: **they did what they said they would do.**

On **September 7 at 16:09 UTC**, a transaction was confirmed in Bitcoin block 965,950 that returned **exactly 3,400 BTC to the Liquid Federation address**.

## They Promised to Return Most of It — and Returned 3,400 BTC

The return is especially remarkable because of the sequence of events. The actors first wrote that they were white-hat hackers, then publicly asked whether the federation address was the correct destination for returning most of the money, and afterward refused to send the BTC immediately until the vulnerability had been fixed.

Blockstream confirmed that the bridge nodes had been patched. The **3,400 BTC transaction** followed.

In other words, the key sentence of the entire story — **“Then we will transfer the money back safely after confirming the fix”** — did not remain merely a message in the blockchain. After the fix was confirmed, the actors returned roughly 85% of the funds.

Around **598.5 BTC** remained on their address, worth approximately $47 million at the time.

## Around 600 BTC Were Not Returned

The status of the remaining nearly 600 BTC is still unresolved. There has been speculation that the amount could represent some form of bug bounty — a reward for discovering a critical vulnerability — but there is no publicly confirmed agreement showing that Blockstream accepted a bounty of that size.

The nearly 600 BTC represent around 15% of the total amount that remained under the actors' control after the incident. It would therefore be inaccurate to say that all of the Bitcoin was returned.

A more precise description is that they **promised to return "most" of the funds — and that is exactly what they returned**.

Even the word **“most”** in their second on-chain message became significant afterward. They did not write that they would return everything. They wrote **“sending most back.”**

## Were They Really White-Hat Hackers?

Their own description of themselves as white-hat hackers does not automatically mean they should be classified that way legally or from a security perspective. There is no public information showing that they had permission from Blockstream or the Liquid Federation to test the system in this way before exploiting the vulnerability.

A typical white-hat process would involve finding a vulnerability and reporting it to the company through a security disclosure or bug bounty program — not first taking control of nearly $320 million.

On the other hand, their behavior after the exploit also did not resemble a typical crypto theft. They did not immediately attempt to hide the funds through a chain of wallets or other networks. They remained visible on the blockchain, publicly contacted Blockstream, supplied technical information, demanded that the vulnerability be patched and then returned 3,400 BTC.

That is exactly what makes the incident so unusual. **They called themselves white-hat hackers, but their final classification may also depend on what happens to the remaining 598.5 BTC.**

## What Does a Conversation on the Bitcoin Blockchain Actually Look Like?

Bitcoin is not a chat application, but OP_RETURN allows a small amount of arbitrary data to be written into a transaction. Once that transaction is confirmed, the data becomes part of the blockchain.

So what a user sees in an explorer as:

**“we are whitehats. contact us on chain”**

looks like this in hexadecimal form:

**`776520617265207768697465686174732e20636f6e74616374207573206f6e20636861696e`**

The explorer simply takes the stored bytes and, when they represent text, decodes them back into characters that humans can read.

More importantly, each such message is contained inside a **real Bitcoin transaction**. In this case, the address sending the white-hat messages was the same address controlling the withdrawn Bitcoin. The blockchain does not prove who the people behind the wallet are, but it does confirm that the messages were sent by someone capable of signing transactions from the wallet holding the funds.

That makes this conversation much more than a screenshot or an anonymous post on the internet.

## The $320 Million Negotiation Took Place in Public

Perhaps the most interesting part of the incident is not even the exploit itself, but the way the problem was handled afterward. The white-hat side and Blockstream effectively conducted part of a negotiation involving hundreds of millions of dollars worth of Bitcoin in front of the entire world.

The messages, their timestamps and the addresses that sent them remained recorded in the blockchain. The public could follow the actors first seeking contact, then announcing that they would return most of the funds, later demanding that the vulnerability be fixed and finally actually returning 3,400 BTC.

There was no conventional private negotiation channel that was only described to the public afterward. **The most important parts of the conversation were written directly into Bitcoin itself.**

## What Is Liquid Network and Why Was the Bug So Dangerous?

Liquid is a Bitcoin sidechain developed by **Blockstream**, designed for faster Bitcoin transfers and the issuance of different types of digital assets. Its L-BTC is supposed to be backed by real Bitcoin locked within the federation system.

A user can lock BTC and receive a corresponding amount of L-BTC on Liquid. When the user wants to return to the Bitcoin mainnet, the L-BTC is removed from circulation through the peg-out process and the federation system releases the corresponding real Bitcoin.

That is precisely why this bug was so critical. If L-BTC can be created without actually being backed by Bitcoin and then redeemed through a normal peg-out for real BTC, one of the system's fundamental assumptions is undermined.

SideSwap says neither its own systems nor its PAK were compromised. According to the company, the source of the problem was a bug in **Elements**, the open-source software underlying Liquid.

## The Bitcoin Mainnet Was Not Hacked

The incident was not a hack of Bitcoin itself. Bitcoin consensus, Bitcoin nodes and users' private wallets were not compromised.

The problem occurred on the Liquid sidechain and within its mechanism for issuing and redeeming L-BTC. The Bitcoin mainnet simply executed validly signed transactions that were submitted to it.

Ironically, the Bitcoin blockchain then became the **public record of how the incident was resolved**. It preserved the hackers' messages, Blockstream's replies and the final transaction returning 3,400 BTC.

## Our Take

* **Actors calling themselves white-hat hackers exploited a vulnerability associated with the Elements software and withdrew approximately 4,000 BTC from the Liquid system.**
* On **September 6 at 18:30 UTC**, they wrote a message into the blockchain whose hexadecimal record begins with **`776520...`** and decodes to: **“we are whitehats. contact us on chain.”**
* On **September 7 at 02:20 UTC**, they wrote through another Bitcoin transaction that they were **sending most of the funds back** and asked Blockstream whether the federation address was correct.
* Just over an hour later came the key message: **“Please fix the bug first.”** They demanded that every node be patched before they returned the Bitcoin.
* The publicly readable portions of all three messages can be represented from the raw blockchain data as **hexadecimal strings**, while block explorers can decode them into ordinary text.
* After the patch, Blockstream said it was safe to return the funds.
* On **September 7 at 16:09 UTC**, the actors returned **3,400 BTC**, after the condition they had set was fulfilled.
* Approximately **598.5 BTC** remained on their address, with no publicly confirmed agreement that the amount represented a bug bounty.
* The Bitcoin mainnet itself **was not hacked**; the problem involved Liquid and Elements.
* The most unusual aspect of the entire incident is that **negotiations involving around $320 million worth of Bitcoin took place partly in public through messages permanently recorded in the Bitcoin blockchain**.
* They said they would return most of the funds after the bug was fixed — and **for 3,400 BTC, they kept their word**.

**Follow Metaadvisor.eu for more news on crypto, Bitcoin, blockchain, cybersecurity, digital assets, technology and financial markets.**

**Disclaimer:** This article is for informational purposes only and does not constitute financial, investment, legal, tax or security advice, nor a recommendation to use any particular crypto network, platform or service. Information about security incidents may change as new technical details and investigation results are published. Conduct your own research and verify current information through official sources before making financial decisions.

<small style="color:#999; font-size:0.8em;">In collaboration with AI.</small>
