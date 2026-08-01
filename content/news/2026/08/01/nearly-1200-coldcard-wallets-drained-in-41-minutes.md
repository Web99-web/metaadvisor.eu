---
title: "Nearly 1,200 Coldcard Wallets Drained in 41 Minutes"
slug: "nearly-1200-coldcard-wallets-drained-in-41-minutes"
date: 2026-08-01T12:00:00+02:00
category: "crypto"
translationKey: "gotovo-1200-coldcard-walleta-ispraznjeno-u-41-minuti-2026-08-01"
source: "CoinDesk, Galaxy Research, Coinkite, Block Bitcoin Engineering and Security, and CZ"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/Crypto-alert.png"
featured_image: "/images/Crypto-alert.png"
image: "/images/Crypto-alert.png"
thumbnail: "/images/Crypto-alert.png"
image_alt: "Crypto security alert following the theft of bitcoin from Coldcard wallets"
image_credit: "Metaadvisor.eu – image is symbolic"
tags: ["Coldcard", "Coinkite", "Bitcoin", "hardware wallet", "cold wallet", "bitcoin theft", "seed phrase", "private key", "security flaw", "firmware", "crypto security", "Galaxy Research", "Changpeng Zhao", "CZ", "cybersecurity"]
description: "More than 1,000 BTC worth around $70 million was stolen from nearly 1,200 addresses linked to vulnerable Coldcard wallets."
summary: "An attacker moved 1,082.65 BTC from 1,196 addresses in just 41 minutes after a security flaw enabled the reconstruction of insufficiently random keys."
---

# Nearly 1,200 Coldcard Wallets Drained in 41 Minutes

More than 1,000 bitcoin, worth approximately $70 million at the time, was stolen from nearly 1,200 addresses in just 41 minutes. What makes the attack particularly alarming is the method: the attacker did not need to steal the devices, connect them to the internet or obtain users’ seed phrases through phishing.

The problem affected certain firmware versions used by COLDCARD hardware wallets. Because of a flaw, some devices generated keys that were not sufficiently random and were therefore more predictable. The attacker could then attempt to reconstruct those keys on their own computers.

*The image is symbolic.*

## What Is COLDCARD?

COLDCARD is not a general term for all cold wallets or hardware wallets. It is a specific brand of Bitcoin hardware wallet produced by the Canadian company Coinkite.

Similar devices are sold under other brand names, including Ledger and Trezor. This incident, however, concerns specific COLDCARD models and firmware versions.

Bitcoin is not physically stored on the device. The balance is recorded on the blockchain, while the device generates and stores the secret keys that allow the owner to sign a transaction and move the bitcoin.

## How Was Bitcoin Stolen Without Accessing the Device?

When a wallet is first set up, the device must generate a completely random seed phrase. Private keys and Bitcoin addresses are then mathematically derived from that phrase.

Such a seed phrase should be virtually impossible to guess. However, on affected COLDCARD devices, a firmware flaw caused the intended hardware random number generator not to be used.

A weaker software mechanism was activated instead. It relied on technical device data and values from the internal clock. As a result, the number of possible combinations was far smaller than intended.

{{< support1 >}}

Put simply, the device was supposed to create a completely unpredictable key. Because of the flaw, it selected the key according to a pattern that was easier to reconstruct.

It is similar to a safe whose manufacturer promises a unique and unpredictable combination, but due to an error creates that combination from the serial number and production time. A thief does not need to see or touch the safe. Possible combinations can be tested on a separate computer until the correct one is found.

## The Attacker Could Search for Vulnerable Addresses

The attacker could automatically generate possible seed phrases, calculate the corresponding Bitcoin addresses and check the public blockchain to see whether those addresses contained funds.

Once a match was found, the attacker could derive the private key from the same seed phrase and sign a transaction. The Bitcoin network accepts such a transaction as valid because it is signed with the correct key.

The attacker almost certainly did not check and drain each address manually. The operation had to be automated with a program that searched for possible keys, matched addresses and prepared transactions.

There is currently no evidence that artificial intelligence was used in the attack. AI may have helped with code analysis or tool development, but an automated script would have been sufficient to carry out an attack of this kind.

## 1,082.65 BTC Stolen

According to an analysis by Galaxy Research, a total of 1,196 Bitcoin addresses were drained between 01:10 and 01:51 UTC on July 30.

Across six blocks, 1,082.65 BTC was moved, worth approximately $70 million at the time. Three blocks without related transactions appeared between those groups, suggesting that the transactions were broadcast in pre-prepared batches.

Initial estimates referred to approximately 594 BTC and around 500 wallets. A later analysis identified additional addresses linked to the attack, nearly doubling the estimated amount.

The stolen bitcoin is reportedly sitting in four addresses and, according to the latest available information, has not yet been moved further.

{{< support2 >}}

## Which COLDCARD Devices Are Affected?

Coinkite said that seed phrases generated on the Mk3 model using firmware versions 4.0.1 through 4.1.9 are affected.

The problem also applies to seeds generated on Mk4 and Mk5 devices before standard firmware version 5.6.0 or Edge version 6.6.0X, as well as on the Q model before standard version 1.5.0Q or Edge version 6.6.0QX.

The level of risk is not identical across the newer models and the Mk3 devices. Coinkite nevertheless continues to treat the issue as serious.

TAPSIGNER, OPENDIME and SATSCARD are not affected because they use different code.

## A Firmware Update Alone Is Not Enough

Coinkite acknowledged the security flaw, apologized to users and released corrected firmware versions.

However, an update alone cannot repair a seed phrase that was already generated using a vulnerable version. The problem does not exist only in the device, but also in the key the device has already created.

Affected users must install a secure firmware version, generate a completely new seed phrase and move their funds to new Bitcoin addresses. The old seed remains vulnerable even if it is later imported into a different hardware or software wallet.

Coinkite identified a possible exception for users who added at least 50 independent and secret dice rolls when generating their seed phrase. That additional source of randomness may have produced a sufficiently strong seed despite the firmware flaw.

{{< support2 >}}

## CZ Recommends Splitting Funds Across Wallets

Binance founder Changpeng Zhao, known as CZ, warned after the incident that even hardware wallets with a long operating history can contain serious flaws.

He suggested that users split larger amounts across several wallets so that a single security failure cannot put all their funds at risk.

That approach creates additional risks of its own. Users must correctly secure multiple devices, seed phrases and backups, while a larger number of wallets also increases the possibility of human error.

## A Hardware Wallet Is Not Magical Protection

This incident shows that a hardware wallet can remain completely offline while the funds are still exposed if the secret key was generated incorrectly from the beginning.

Users did not necessarily lose their bitcoin because they revealed a seed phrase, installed a fake application or connected the device to a malicious website. They lost the funds because the device created a key that could be reconstructed.

A hardware wallet can still substantially reduce the risk of theft. However, its security depends on the quality of the device, its firmware and the method used to generate the most important secret in the entire wallet: the seed phrase.

## Our Take

* COLDCARD is a specific brand of Bitcoin hardware wallet, not a general term for all cold wallets.
* The attack does not affect every hardware wallet manufacturer.
* A total of 1,082.65 BTC was moved from 1,196 addresses in just 41 minutes.
* The stolen bitcoin was worth around $70 million at the time.
* The attacker did not need physical access to the devices.
* The security flaw caused insufficiently random seed phrases to be generated.
* Possible seed phrases and their corresponding addresses could be checked automatically.
* There is no evidence that artificial intelligence was used in the attack.
* Coinkite released security updates and apologized to users.
* A firmware update does not repair a seed phrase already generated on a vulnerable version.
* Affected users must create a new seed phrase and move their funds to new addresses.
* CZ suggested splitting larger amounts across several wallets, although that also creates additional risks.
* A hardware wallet can provide strong protection, but it cannot be more secure than the method used to generate its key.

**Disclaimer:** This article is for informational and educational purposes only and does not constitute legal, financial, investment or security advice. The information is based on publicly available sources, and not all claims have necessarily been independently verified.

Created in collaboration with AI.
