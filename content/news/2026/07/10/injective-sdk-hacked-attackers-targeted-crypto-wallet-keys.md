---
title: "Injective SDK Hacked: Attackers Targeted Crypto Wallet Keys"
slug: "injective-sdk-hacked-attackers-targeted-crypto-wallet-keys"
date: 2026-07-10T12:00:00+02:00
category: "crypto"
translationKey: "injective-sdk-npm-wallet-keys-2026-07-10"
source: "Cointelegraph, Socket, Aikido, OX Security, DefiLlama, CoinGecko, Metaadvisor.eu"
source_url: "https://cointelegraph.com/news/hackers-compromise-injective-npm-package-with-malware-to-steal-wallet-keys"
author: "Metaadvisor.eu"
image_url: "/images/hack/Injective-SDK-hacked.png"
featured_image: "/images/hack/Injective-SDK-hacked.png"
image: "/images/hack/Injective-SDK-hacked.png"
thumbnail: "/images/hack/Injective-SDK-hacked.png"
image_credit: "Metaadvisor.eu"
tags: ["Injective", "Injective SDK", "npm package", "supply chain attack", "crypto security", "wallet keys", "private keys", "seed phrase", "mnemonic phrase", "Web3 security", "DeFi security", "developer tools", "GitHub", "npm malware", "crypto wallet"]
summary: "The Injective npm package @injectivelabs/sdk-ts was compromised, and a malicious version targeted private keys and mnemonic phrases from crypto wallets. The incident was not an attack on the blockchain itself, but an example of a growing Web3 risk: attacks on the software supply chain."
disclaimer: "This article is for informational purposes only and does not constitute investment, technology, security or financial advice."
draft: false
---

The image is symbolic.

# Injective SDK Hacked: Attackers Targeted Crypto Wallet Keys

Injective has become part of a security story that shows how dangerous a software supply-chain attack can be. According to security researchers, the npm package **@injectivelabs/sdk-ts** was compromised. It is a TypeScript/JavaScript SDK used to develop applications connected to the Injective ecosystem.

The key point is this: this was not an attack on the blockchain itself. The attackers did not target the protocol’s cryptography or smart contracts. They targeted a developer tool trusted by applications. That is exactly why the incident matters. In Web3, a private key is not an ordinary password. If an attacker obtains a private key or seed phrase, they can take control of a wallet.

## What happened?

The malicious package version was **@injectivelabs/sdk-ts 1.20.21**. According to Socket, that version recorded private keys and mnemonic phrases, while the risk also spread through other packages in the Injective Labs npm scope that were connected to the malicious version.

Aikido reported that the compromised package had around **50,000 weekly downloads**, which explains why the incident quickly attracted attention from the security community. The malicious code was disguised as telemetry, meaning it looked like a harmless software component, while in the background it targeted the most sensitive wallet data.

This is a typical example of a supply-chain attack. Attackers do not need to break the blockchain itself to reach user assets. Sometimes it is enough to compromise a tool that developers use to build applications.

{{< support1 >}}

## Why is this serious?

In a classic attack, the user often has to click a suspicious link, download a fake app or enter a seed phrase on a phishing page. In a supply-chain attack, the danger comes from a direction the user may never see. An application can look legitimate, while malicious code arrives through a package pulled during development or the build process.

In this case, the malware targeted private keys and mnemonic phrases during wallet workflows. If such code ends up in an application that creates, loads or manages wallets, the risk becomes very real. The blockchain may function normally, smart contracts may be correct, and the user may still be exposed because of a compromised developer dependency.

That is why this story is bigger than one package. It shows that crypto security is not only about protocols and smart contracts. It is also about npm packages, GitHub accounts, dependency chains, lockfiles and CI/CD processes used to build applications.

## How wide was the impact?

According to Aikido, the malicious version was active for less than an hour before it was detected and replaced with a clean version. That is good news, but it does not remove the risk for everyone who pulled the package during that short window.

OX Security also noted that the incident may have affected a broader dependency chain, with **87 dependent packages** and more than **112,000 combined downloads** in the affected environment. In incidents like this, the question is not only how long the malicious version was publicly available. It also matters whether it ended up in a project, cache, lockfile or application that continued using it later.

That is why developers cannot check only direct package installations. They also need to review transitive dependencies, meaning packages that may have pulled the compromised version as a dependency.

{{< support1 >}}

## Market context: lower TVL and a weaker token

Injective is an interoperable layer-1 blockchain focused on DeFi applications. However, its ecosystem is much smaller today than it was at its peak. According to data cited by Cointelegraph, total value locked, or TVL, has fallen by about **88%**, from a peak of **$71 million** in mid-2024 to around **$8.2 million**.

A similar decline can be seen on the market side. INJ reached a peak of around **$52.62**, while it is now trading around **$4.8**. This does not mean that the security incident caused the decline in TVL or the token price. Those declines happened over a longer period. But the context matters: when an ecosystem is already much smaller than it was at its peak, security incidents raise additional questions about trust, developer activity and the quality of tools used in applications.

In other words, this is not a story about one hack crashing the market. It is a story about reputational risk in an ecosystem that is already dealing with much lower activity than it had two years ago.

## What should developers do?

Developers should check whether they use **@injectivelabs/sdk-ts 1.20.21** or any related package that may have pulled that version. Particular attention should be paid to **package.json**, lockfiles, builds, deployment pipelines and all Injective packages used in the project.

If the malicious version was used, simply updating the package may not be enough. Any private key or mnemonic phrase that may have passed through the compromised SDK should be treated as potentially compromised. In crypto, that kind of risk cannot really be “fixed.” If there is a real possibility that a seed phrase was exposed, funds should be moved to a new wallet with new keys.

That may sound strict, but the logic is simple: if someone may know the private key, that wallet is no longer safe.

{{< support2 >}}

## What does this mean for users?

Regular users do not need to panic just because they use Injective applications or follow the Injective ecosystem. The issue is not that every user is automatically at risk. The risk is connected to applications that may have used the compromised SDK in wallet workflows.

Users should follow security updates from the applications they use and be especially careful if an application asked them to enter, generate or restore a seed phrase. A seed phrase should not be entered into applications that are not trusted, should not be shared and should not be stored insecurely.

If there is any suspicion that a seed phrase may have been exposed, moving funds to a new wallet is the safer option. In crypto, waiting is often the most expensive choice.

## Why this story is bigger than Injective

This incident highlights a broader problem in Web3 security. Applications are no longer built completely from scratch. Developers use a large number of packages, libraries and dependencies. One compromised package can spread quickly through the entire chain.

In Web3, this risk is especially sensitive because applications often interact with wallets, transaction signing and assets that can be moved irreversibly. Attackers therefore do not always need to find a bug in a smart contract. Sometimes it is easier to compromise a developer account, an npm package or a build process.

That is the most important lesson of this incident: the weakest point does not have to be the blockchain. It can be the tool used to build blockchain applications.

{{< support2 >}}

## Our take

- This is not a story about a “hacked token,” but about a compromised developer package.
- The malicious version was **@injectivelabs/sdk-ts 1.20.21**.
- The malware targeted private keys and mnemonic phrases from crypto wallets.
- The biggest risk applies to developers, applications and users that may have used the compromised version in wallet workflows.
- The potential reach was serious because the package is used in developer environments, and part of the risk could spread through dependency chains.
- Injective’s TVL and INJ’s market price are far below their peaks, which gives the incident additional reputational context.
- That does not mean the incident caused the decline in TVL or the token price, but security issues carry more weight when an ecosystem already shows lower activity.
- The broader lesson is clear: in Web3 security, it is not enough to look only at blockchains and smart contracts. npm packages, GitHub accounts, dependency chains and the tools used to build applications matter too.

**Disclaimer:** This article is for informational purposes only and does not constitute investment, technology, security or financial advice.
