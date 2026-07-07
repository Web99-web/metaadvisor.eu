---
title: "Trader loses $2M in DEX swap"
slug: "trader-loses-2m-dex-swap"
date: 2026-07-07T18:00:00+02:00
category: "crypto"
translationKey: "trader-loses-2m-dex-swap-bad-route-2026-07-07"
source: "Cointelegraph, GoPlus Security, Metaadvisor.eu"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/news/MIllions-lost.png"
featured_image: "/images/news/MIllions-lost.png"
image: "/images/news/MIllions-lost.png"
thumbnail: "/images/news/MIllions-lost.png"
image_credit: "Metaadvisor.eu"
tags: ["DEX swap", "DeFi risk", "MEV", "same-block backrun", "Titan Builder", "GoPlus Security", "Uniswap v3", "0x router", "slippage", "price impact", "crypto loss"]
summary: "A trader lost almost $2 million after a large ETH swap was routed through a pool with very low liquidity. The case shows why minimum received, slippage, price impact and the swap route are critical before signing any DEX transaction."
disclaimer: "This article is for informational purposes only and does not constitute financial, investment, legal or security advice."
draft: false
---

Image is symbolic.

# Trader loses $2 million in DEX swap: not a classic hack, but a catastrophic transaction route

A crypto trader lost almost the entire amount of around **$2 million** after trying to make a large Ether swap on a decentralized exchange. In the end, according to available reports, the trader was left with tokens worth only about **$14,500**.

At first glance, the story sounds like another crypto hack. But this case is more interesting than that. It was not simply a case of someone “stealing a wallet” or tricking a user with a fake link. The problem happened because the transaction was routed through a **pool with very low liquidity**, and other market participants immediately exploited the price difference.

In other words: the trader signed a swap that executed at a terrible price.

According to Cointelegraph and an analysis by GoPlus Security, the trader swapped **1,126.44 ETH**, worth around **$2.01 million**, but received only **5,776 Lighter (LIT) tokens**. GoPlus Security described the incident as a “textbook case” of **same-block backrun extraction**.

{{< support1 >}}

That means another actor was able to exploit, within the same Ethereum block, the imbalance created by this large and poorly routed transaction.

The biggest beneficiary was reportedly **Titan Builder**, which extracted around **$1.8 million** from the incident.

## What actually happened?

The trader wanted to make a large swap on a decentralized exchange. In such transactions, the user often does not go directly from one token to another. Instead, a DEX router finds a path through different tokens and liquidity pools.

In this case, the swap was reportedly routed through an **AVAIL/WETH pool on Uniswap v3**, which did not have enough liquidity for such a large order.

That is the key to the whole story.

If a pool is small and the order is huge, the price can move dramatically. It is like trying to exchange 2 million euros at a small currency kiosk instead of through a major bank. The kiosk does not have enough “depth” for that kind of transaction, so the exchange rate would become completely unfavorable.

According to GoPlus Security, part of the transaction went through a pool where the price was around **120 times higher** than the price at which the token could later be sold.

So the trader did not lose money because there was “no money in the pool” in the classic sense. The trader lost money because a large transaction went through a pool that could not normally absorb that volume.

## Not a classic sandwich attack

GoPlus Security stressed that this was not a classic **sandwich attack**.

In a sandwich attack, a bot usually sees a user’s transaction, buys before the user, lets the user push the price up, and then sells immediately afterward. The user is “sandwiched” between two bot transactions.

Here, the situation was different.

GoPlus Security described the case as a real, highly imbalanced **backrunner arbitrage**. That means the badly executed transaction itself created the opportunity, and another participant immediately exploited it within the same block.

That is why this case is so uncomfortable: the transaction may have technically executed “as signed,” but the result for the user was catastrophic.

## How could the trader have known something was wrong?

This is the most important and most interesting part of the story.

The trader did not have to manually know how much liquidity was available in every pool. They did not have to inspect every smart contract or calculate market depth themselves. But before signing the transaction, they could have checked several basic signals that a DEX interface, wallet or aggregator often shows before a user clicks **Confirm**.

The first and most important signal is **minimum received**.

This is the minimum amount of tokens the user will receive if the transaction executes. Before confirmation, the interface often says something like: “You will receive at least X tokens.”

If the trader had seen that ETH worth around **$2 million** would result in tokens worth only about **$14,500** after execution, that would have been an immediate warning not to sign the transaction.

The second signal is **slippage** or **price impact**.

In a normal swap, price impact should be relatively small. If the interface shows a huge price impact, for example 30, 80 or 99 percent, that means the transaction itself will strongly move the price because the pool does not have enough liquidity.

Simply put: the swap is too large for the pool it is passing through.

The third signal is the **transaction route**.

In an advanced view, it is often possible to see which tokens and pools the swap will pass through. A route might look like this:

ETH → WETH → AVAIL → LIT

or something similar.

If the trader had seen that a huge amount was going through a small or unusual AVAIL/WETH pool, they could have stopped and refused to sign the transaction.

## With $2 million, you do not just click Confirm

For a swap worth around **$2 million**, it is also important to compare the result across multiple DEXs and aggregators.

That kind of amount should not be sent with one quick click and no checking. The trader could have compared quotes on services such as 1inch, Matcha, CoW Swap or Uniswap. They could also have considered an OTC solution, especially when dealing with a large order and weaker liquidity.

If one router gives a significantly worse result than others, that is a major red flag.

There was also a simpler option: split the transaction into smaller parts. A large swap through a small pool can create extreme price impact. Smaller orders, a limit order or an OTC deal can often reduce the risk that the price moves in a completely unfavorable direction.

That is why this story is not only about hackers or MEV bots. It shows how dangerous it is to sign DEX transactions without checking the details.

The trader did not need to know in advance how much “money” was in the pool, but the consequences were likely visible through four things: **minimum received, price impact, slippage and the swap route**.

In short: the problem was not only that the pool was too small. The problem was that the transaction was signed even though the swap details could have shown that the result would be catastrophic.

{{< support2 >}}

## Why MEV and block builders matter

This incident again raises the issue of **MEV**, or maximal extractable value.

MEV refers to the additional value that validators, block builders or bots can extract from the way transactions are ordered, executed and arranged inside a blockchain block.

In practice, this means that someone who sees a large or poorly configured transaction can try to profit from price differences, arbitrage or the order of execution.

<a href="https://metaadvisor.eu/news/what-is-mev-trading-defi/" target="_blank" rel="noopener">
  <img src="/images/MEV-explained.png" alt="What Is MEV Trading and Why It Has Become One of DeFi’s Biggest Problems" style="max-width: 360px; width: 100%; height: auto; display: block; margin: 1rem 0;">
</a>

<a href="https://metaadvisor.eu/news/what-is-mev-trading-defi/" target="_blank" rel="noopener">What Is MEV Trading and Why It Has Become One of DeFi’s Biggest Problems</a>

In this case, Titan Builder was reportedly the biggest beneficiary of the opportunity created after the bad swap. That does not necessarily mean the user’s wallet was “hacked.” It means that market infrastructure exploited a transaction that had already been signed and sent.

For ordinary users, the difference may sound technical, but the consequence is very real: almost the entire $2 million amount disappeared through poor swap execution.

## What can users learn from this case?

The most important lesson is simple: with DEX transactions, it is not enough to look only at which token you are buying or selling. You also need to look at **how** the transaction is being executed.

Before signing, users should check:

- the minimum amount they will receive,
- slippage,
- price impact,
- the transaction route,
- liquidity in the pools,
- price differences across multiple DEXs or aggregators.

For small amounts, a mistake can be unpleasant. For large amounts, a mistake can be devastating.

DEXs give users more control, but that control comes with responsibility. A bank or centralized exchange often has more protective mechanisms, while a decentralized swap can execute exactly what the user signed, even if the result is extremely unfavorable.

That is exactly what makes this case important.

It is not only about one trader losing money. It is a warning that in decentralized finance, users must understand what they are signing.

## Our view

- This case matters because it shows that crypto risk does not come only from classic hackers, phishing links or fake tokens.
- Sometimes, a badly routed swap, a tiny liquidity pool and one click on **Confirm** are enough.
- The most interesting part of the story is not only the $2 million loss, but the fact that part of the risk was probably visible before the transaction was signed.
- **Minimum received**, **price impact**, **slippage** and the **swap route** are not minor technical details. They are warning signals that can show a transaction may end catastrophically.
- For small retail users, this is a warning not to sign transactions without reading the details.
- For larger traders, the message is even clearer: large orders should not be executed like ordinary quick swaps without checking liquidity, alternatives and protection against poor execution.
- Crypto often promises speed, freedom and open markets. But in DeFi, freedom also means the system will not always stop you.
- If you sign a bad transaction, the blockchain can execute it perfectly — even when the result is catastrophic for you.

**Disclaimer:** This article is for informational purposes only and does not constitute financial, investment, legal or security advice. Crypto and DeFi transactions carry high risk, and users are responsible for checking transactions before signing them.
