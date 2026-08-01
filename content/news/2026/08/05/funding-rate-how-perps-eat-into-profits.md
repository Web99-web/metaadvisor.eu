---
title: "Funding Rate: How Perps Eat Into Profits"
slug: "funding-rate-how-perps-eat-into-profits"
date: 2026-08-05T06:00:00+02:00
category: "crypto"
translationKey: "funding-rate-kako-perpsi-pojedu-dobit-2026-08-05"
source: "Hyperliquid, Binance and publicly available documentation on perpetual futures contracts"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/informative/Funding-cost-perps.png"
featured_image: "/images/informative/Funding-cost-perps.png"
image: "/images/informative/Funding-cost-perps.png"
thumbnail: "/images/informative/Funding-cost-perps.png"
image_alt: "Funding rates as the hidden cost of trading perpetual futures contracts"
image_credit: "Metaadvisor.eu – image is symbolic"
tags: ["funding rate", "perpetual futures", "perps", "crypto trading", "leverage", "long position", "short position", "trading fees", "Hyperliquid", "Binance", "derivatives", "margin trading", "liquidation", "crypto risk", "risk management"]
description: "Funding rates can gradually reduce profits on perpetual futures positions, especially when trades are held for a long time, use higher leverage or face elevated rates."
summary: "Perpetual futures contracts do not expire, but they are not free to hold indefinitely. Funding is charged periodically on the full position value and can significantly reduce final profits."
---

*The image is symbolic.*

# Funding Rate: How Perps Eat Into Profits

Perpetual futures contracts, commonly known as perps, have become one of the most popular ways to trade cryptocurrencies. They allow traders to open leveraged long or short positions, have no expiry date and often provide deep liquidity with relatively low trading fees.

However, there is one cost traders can easily overlook: the funding rate.

A position may remain open for days or weeks, the price may even move in the expected direction, and part of the profit can still gradually disappear through recurring funding payments.

## What Are Perpetual Futures?

A traditional futures contract has an expiry date. A perpetual future does not, meaning a trader can theoretically keep a position open indefinitely as long as sufficient margin is available and the position is not liquidated.

Perps allow traders to speculate on rising or falling prices without actually buying the token:

* A long position profits when the price rises.
* A short position profits when the price falls.
* Leverage increases the position size relative to the collateral deposited.

Traders value perps for their liquidity, relatively low fees and the large market exposure they can obtain with a small amount of collateral.

However, holding a position for a long time can create additional costs that are not visible from the opening fee alone.

## Why Does the Funding Rate Exist?

Because perpetual futures do not expire, a mechanism is needed to keep their price close to the actual spot price of the cryptocurrency.

Funding rates therefore create recurring payments between traders holding long and short positions.

When too many traders want to go long, the perp price can rise above the spot price. Funding is then usually positive:

**Long positions pay short positions.**

When short positions dominate, funding may become negative:

**Short positions pay long positions.**

The money usually does not go to the exchange. It is transferred between the two sides of the market. Funding therefore encourages traders to take positions on the less popular side and helps keep the perp price closer to the spot price.

{{< support1 >}}

## Funding Is Calculated on the Full Position

One of the most important points is that funding is not calculated only on the money deposited as margin.

It is calculated on the full value of the open position.

If a trader deposits $10 and opens a $40 position using 4x leverage, funding is calculated on $40.

For example, with a funding rate of 0.05%:

* A $10 position pays $0.005.
* A $40 position pays $0.02.
* A $10,000 position pays $5.

A single payment may appear insignificant. However, it repeats for as long as the position remains open and the trader stays on the side that pays funding.

## How Can Funding Eat Into Profits?

Consider a position worth $1,000 that generates an unrealized profit of $20 over several days.

If the trader pays $3 in funding during the same period, along with fees for opening and closing the position and the cost of spread or slippage, the actual profit will be lower than the number shown in the basic price-movement display.

When funding is very high, a trader may even predict the market direction correctly and still end with only a very small profit or a loss.

Funding matters most for positions held for days or weeks. For a trade lasting only a few minutes, a single funding period may have little impact. Over longer periods, however, small payments accumulate.

{{< support2 >}}

## How Does Funding Work on Hyperliquid?

Hyperliquid calculates funding every hour.

The payment is based on the position size, the oracle price and the current funding rate. Its official documentation also states an upper limit of 4% per hour.

That does not mean funding is normally 4%. It means that under extreme market conditions, it can rise much higher than traders may expect.

Funding differs from token to token and can change quickly. At one moment, Hyperliquid may be more expensive than another platform, while later it may be cheaper or even show the opposite funding direction.

For that reason, checking funding only when opening the trade is not enough. The rate can change while the position remains open.

## Small Positions Do Not Make Funding Irrelevant

For positions worth only a few dollars, the absolute funding amount will usually be very small.

It may be only a fraction of a cent per settlement. Such a trade is unlikely to suffer a serious loss from funding alone.

Small positions can still be useful for learning because they clearly show:

* when longs pay shorts
* when shorts receive funding
* how leverage increases the position value
* why unrealized P&L is not the same as final profit
* how recurring costs accumulate over time

For small positions, trading fees, spread and the failure of the expected price move to occur may often be a bigger problem than funding itself.

{{< support1 >}}

## Funding Can Also Be Income

Funding is not always a cost.

A trader on the side receiving funding can collect recurring payments while the position remains open.

For that reason, some professional traders use strategies designed to collect funding while reducing their exposure to price movements.

However, a high positive funding rate is not automatically a reason to open a short position, just as a high negative funding rate is not automatically a long signal.

The market may continue rising or falling for much longer than the trader can remain solvent. Any possible funding income can then be insignificant compared with the loss on the position or a liquidation.

## Hourly, Eight-Hour and Annual Funding Are Not the Same

It is particularly dangerous to compare figures from two platforms directly when one shows hourly funding, another displays an eight-hour rate and a third provides an annualized estimate.

A rate of 0.01% per hour is not the same as 0.01% every eight hours.

An annualized estimate is also not a guaranteed cost for the coming year. It only shows what funding would amount to if the current rate remained unchanged, which rarely happens in practice.

Before comparing platforms, all rates must be converted to the same time period.

{{< support2 >}}

## What Should Be Checked Before Opening a Perp?

Before opening a position, traders should check:

* whether the funding rate is positive or negative
* whether the long or short side pays
* how often funding is calculated
* whether the displayed rate refers to one hour, eight hours or an annualized estimate
* the full value of the position
* how long the position is expected to remain open
* how volatile funding has been during the past several hours or days

Traders should also review funding payments already made on an open position. Unrealized profit may look attractive, but the final result also includes funding, trading fees and the cost of closing the position.

## Perps Have No Expiry, but They Have Ongoing Costs

Perpetual futures appear simple: choose long or short, set leverage and watch the price.

The actual cost, however, is not limited to the small fee charged when opening and closing a position.

Funding may be almost unnoticeable for a short trade and a small position, but it can become important with higher leverage, popular altcoins and long holding periods.

The key is to understand that funding is calculated on the full position, that the same side does not always pay and that the rate can change while the trade is open.

Perps have no expiry date, but that does not mean they can be held indefinitely at no cost.

## Our Take

* Perpetual futures contracts do not have an expiry date.
* Funding rates help keep perp prices close to spot prices.
* With positive funding, long positions usually pay short positions.
* With negative funding, short positions usually pay long positions.
* Funding is calculated on the full position value, not only on the deposited margin.
* Leverage therefore increases the amount on which funding is calculated.
* Small recurring payments can add up significantly over long holding periods.
* The funding rate can change while a position remains open.
* Hyperliquid calculates funding every hour.
* Funding can be a cost or income for the side receiving it.
* A high funding rate alone is not enough to justify a long or short position.
* Hourly, eight-hour and annual rates should not be compared without conversion.
* Unrealized P&L does not necessarily show the final profit after all costs.

**Disclaimer:** This article is for informational and educational purposes only and does not constitute financial or investment advice. Trading derivatives and using leverage involve a high risk of loss.

Created in collaboration with AI.
