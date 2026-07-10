---
title: "Injective SDK gehackt: Angreifer zielten auf Krypto-Wallet-Schlüssel"
slug: "injective-sdk-gehackt-angreifer-zielten-auf-krypto-wallet-schluessel"
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
tags: ["Injective", "Injective SDK", "npm Paket", "Supply-Chain-Angriff", "Krypto-Sicherheit", "Wallet-Schlüssel", "Private Keys", "Seed Phrase", "Mnemonic Phrase", "Web3-Sicherheit", "DeFi-Sicherheit", "Developer Tools", "GitHub", "npm Malware", "Krypto Wallet"]
summary: "Das Injective-npm-Paket @injectivelabs/sdk-ts wurde kompromittiert. Eine bösartige Version zielte auf Private Keys und Mnemonic Phrases von Krypto-Wallets. Der Vorfall ist kein Angriff auf die Blockchain selbst, sondern ein Beispiel für ein immer wichtigeres Risiko im Web3-Bereich: Angriffe auf die Software-Lieferkette."
disclaimer: "Dieser Artikel dient ausschließlich Informationszwecken und stellt keine Anlage-, Technologie-, Sicherheits- oder Finanzberatung dar."
draft: false
---

Das Bild ist symbolisch.

# Injective SDK gehackt: Angreifer zielten auf Krypto-Wallet-Schlüssel

Injective ist in eine Sicherheitsgeschichte geraten, die zeigt, wie gefährlich ein Angriff auf die Software-Lieferkette sein kann. Laut Sicherheitsforschern wurde das npm-Paket **@injectivelabs/sdk-ts** kompromittiert, ein TypeScript/JavaScript-SDK, das bei der Entwicklung von Anwendungen im Injective-Ökosystem verwendet wird.

Wichtig ist dabei die klare Einordnung: Dies war kein Angriff auf die Blockchain selbst. Die Angreifer zielten nicht auf die Kryptografie des Protokolls oder auf Smart Contracts, sondern auf ein Developer-Tool, dem Anwendungen vertrauen. Genau deshalb ist der Vorfall relevant. In der Web3-Welt ist ein Private Key kein gewöhnliches Passwort. Wenn ein Angreifer an einen Private Key oder eine Seed Phrase gelangt, kann er die Kontrolle über ein Wallet übernehmen.

## Was ist passiert?

Die bösartige Version des Pakets war **@injectivelabs/sdk-ts 1.20.21**. Laut Socket zeichnete diese Version Private Keys und Mnemonic Phrases auf, während sich das Risiko auch über andere Pakete im npm-Scope von Injective Labs ausbreiten konnte, die mit der bösartigen Version verbunden waren.

Aikido berichtet, dass das kompromittierte Paket etwa **50.000 wöchentliche Downloads** hatte. Das erklärt, warum der Vorfall schnell die Aufmerksamkeit der Sicherheitscommunity auf sich zog. Der bösartige Code war als Telemetrie getarnt, also als scheinbar harmloser Softwarebestandteil, zielte im Hintergrund jedoch auf die sensibelsten Wallet-Daten.

Das ist ein typisches Beispiel für einen Supply-Chain-Angriff. Angreifer müssen nicht die Blockchain selbst brechen, um an Nutzervermögen zu gelangen. Manchmal reicht es, ein Tool zu kompromittieren, das Entwickler für den Bau von Anwendungen verwenden.

{{< support1 >}}

## Warum ist das ernst?

Bei einem klassischen Angriff muss der Nutzer oft auf einen verdächtigen Link klicken, eine gefälschte App herunterladen oder seine Seed Phrase auf einer Phishing-Seite eingeben. Bei einem Supply-Chain-Angriff kommt die Gefahr aus einer Richtung, die der Nutzer gar nicht sieht. Eine Anwendung kann legitim wirken, während bösartiger Code über ein Paket eingeschleust wurde, das während der Entwicklung oder im Build-Prozess eingebunden wurde.

In diesem Fall zielte die Malware während des Wallet-Workflows auf Private Keys und Mnemonic Phrases. Wenn ein solcher Code in einer Anwendung landet, die Wallets erzeugt, lädt oder verwaltet, wird das Risiko sehr konkret. Die Blockchain kann normal funktionieren, Smart Contracts können korrekt sein, und der Nutzer kann trotzdem durch eine kompromittierte Developer-Abhängigkeit gefährdet sein.

Deshalb ist diese Geschichte größer als ein einzelnes Paket. Sie zeigt, dass Krypto-Sicherheit nicht nur aus Protokollen und Smart Contracts besteht. Man muss auch npm-Pakete, GitHub-Konten, Dependency-Ketten, Lockfiles und CI/CD-Prozesse betrachten, mit denen Anwendungen gebaut werden.

## Wie groß war die Reichweite?

Laut Aikido war die bösartige Version weniger als eine Stunde aktiv, bevor sie entdeckt und durch eine saubere Version ersetzt wurde. Das ist eine gute Nachricht, beseitigt aber nicht das Risiko für alle, die das Paket in diesem kurzen Zeitfenster gezogen haben.

OX Security weist zusätzlich darauf hin, dass der Vorfall eine breitere Dependency-Kette betroffen haben könnte, mit **87 abhängigen Paketen** und mehr als **112.000 kombinierten Downloads** im betroffenen Umfeld. Bei solchen Vorfällen ist nicht nur wichtig, wie lange die bösartige Version öffentlich verfügbar war. Wichtig ist auch, ob sie in einem Projekt, Cache, Lockfile oder einer Anwendung gelandet ist, die sie später weiterverwendet hat.

Deshalb können Entwickler nicht nur auf die direkte Installation des Pakets schauen. Sie müssen auch transitive Abhängigkeiten prüfen, also Pakete, die die kompromittierte Version als Dependency mitgezogen haben könnten.

{{< support1 >}}

## Marktkontext: geringerer TVL und schwächerer Token

Injective ist eine interoperable Layer-1-Blockchain, die auf DeFi-Anwendungen ausgerichtet ist. Das Ökosystem ist heute jedoch deutlich kleiner als auf seinem Höhepunkt. Laut den von Cointelegraph genannten Daten ist der Total Value Locked, also TVL, um etwa **88 %** gefallen, von einem Höchststand von **71 Millionen Dollar** Mitte 2024 auf rund **8,2 Millionen Dollar**.

Ein ähnlicher Rückgang ist auch auf der Marktseite zu sehen. INJ lag auf seinem Höchststand bei etwa **52,62 Dollar**, während der Token aktuell bei rund **4,8 Dollar** notiert. Das bedeutet nicht, dass dieser Sicherheitsvorfall den Rückgang des TVL oder des Tokenpreises verursacht hat. Diese Rückgänge haben sich über einen längeren Zeitraum entwickelt. Der Kontext ist aber wichtig: Wenn ein Ökosystem bereits deutlich kleiner ist als auf seinem Höhepunkt, werfen Sicherheitsvorfälle zusätzliche Fragen zu Vertrauen, Developer-Aktivität und der Qualität der verwendeten Tools auf.

Anders gesagt: Dies ist keine Geschichte darüber, dass ein einzelner Hack den Markt zum Einsturz gebracht hat. Es ist eine Geschichte über Reputationsrisiko in einem Ökosystem, das bereits mit deutlich geringerer Aktivität kämpft als noch vor zwei Jahren.

## Was sollten Entwickler tun?

Entwickler sollten prüfen, ob sie **@injectivelabs/sdk-ts 1.20.21** oder ein verbundenes Paket verwenden, das diese Version mitgezogen haben könnte. Besonders wichtig sind **package.json**, Lockfiles, Builds, Deployment-Pipelines und alle Injective-Pakete, die im Projekt eingesetzt wurden.

Wenn die bösartige Version verwendet wurde, reicht es nicht, nur das Paket zu aktualisieren. Jeder Private Key oder jede Mnemonic Phrase, die durch das kompromittierte SDK gelaufen sein könnte, sollte als potenziell kompromittiert behandelt werden. In Krypto lässt sich ein solches Risiko nicht einfach “reparieren”. Wenn eine reale Möglichkeit besteht, dass eine Seed Phrase offengelegt wurde, sollten Mittel auf ein neues Wallet mit neuen Schlüsseln übertragen werden.

Das klingt streng, folgt aber einer einfachen Logik: Wenn jemand möglicherweise den Private Key kennt, ist dieses Wallet nicht mehr sicher.

{{< support2 >}}

## Was bedeutet das für Nutzer?

Normale Nutzer müssen nicht allein deshalb in Panik geraten, weil sie Injective-Anwendungen verwenden oder das Injective-Ökosystem verfolgen. Das Problem besteht nicht darin, dass jeder Nutzer automatisch gefährdet ist. Das Risiko hängt mit Anwendungen zusammen, die das kompromittierte SDK möglicherweise in Wallet-Workflows verwendet haben.

Nutzer sollten die Sicherheitsmeldungen der Anwendungen verfolgen, die sie verwenden, und besonders vorsichtig sein, wenn eine Anwendung sie zur Eingabe, Erzeugung oder Wiederherstellung einer Seed Phrase aufgefordert hat. Eine Seed Phrase sollte nicht in Anwendungen eingegeben werden, denen man nicht vertraut, sie sollte nicht geteilt und nicht unsicher gespeichert werden.

Wenn der Verdacht besteht, dass eine Seed Phrase offengelegt wurde, ist es sicherer, Mittel auf ein neues Wallet zu übertragen. In Krypto ist Abwarten oft die teuerste Option.

## Warum ist diese Geschichte größer als Injective?

Dieser Vorfall zeigt ein breiteres Problem der Web3-Sicherheit. Anwendungen werden heute nicht mehr von Grund auf neu geschrieben. Entwickler verwenden eine große Zahl von Paketen, Bibliotheken und Abhängigkeiten. Ein kompromittiertes Paket kann sich schnell durch die gesamte Kette ausbreiten.

Im Web3-Bereich ist dieses Risiko besonders sensibel, weil Anwendungen häufig mit Wallets, Transaktionssignaturen und Vermögenswerten arbeiten, die unwiderruflich verschoben werden können. Angreifer müssen daher nicht immer einen Bug in einem Smart Contract finden. Manchmal ist es einfacher, ein Developer-Konto, ein npm-Paket oder einen Build-Prozess zu kompromittieren.

Das ist die wichtigste Lektion dieses Vorfalls: Die schwächste Stelle muss nicht die Blockchain sein. Sie kann auch das Tool sein, mit dem Blockchain-Anwendungen gebaut werden.

{{< support2 >}}

## Unser Fazit

- Dies ist keine Geschichte über einen “gehackten Token”, sondern über ein kompromittiertes Developer-Paket.
- Die bösartige Version war **@injectivelabs/sdk-ts 1.20.21**.
- Die Malware zielte auf Private Keys und Mnemonic Phrases von Krypto-Wallets.
- Das größte Risiko betrifft Entwickler, Anwendungen und Nutzer, die die kompromittierte Version in Wallet-Workflows verwendet haben könnten.
- Die potenzielle Reichweite war ernst, weil das Paket in Developer-Umgebungen genutzt wird und sich ein Teil des Risikos über Dependency-Ketten ausbreiten konnte.
- Der TVL von Injective und der Marktpreis von INJ liegen deutlich unter ihren Höchstständen, was dem Vorfall zusätzlichen reputationsbezogenen Kontext gibt.
- Das bedeutet nicht, dass der Vorfall den Rückgang von TVL oder Token verursacht hat, sondern dass Sicherheitsprobleme mehr Gewicht bekommen, wenn ein Ökosystem bereits weniger Aktivität zeigt.
- Die wichtigste Lektion ist größer: In der Web3-Sicherheit reicht es nicht, nur Blockchain und Smart Contracts zu betrachten. Man muss auch npm-Pakete, GitHub-Konten, Dependency-Ketten und die Tools prüfen, mit denen Anwendungen gebaut werden.

**Disclaimer:** Dieser Artikel dient ausschließlich Informationszwecken und stellt keine Anlage-, Technologie-, Sicherheits- oder Finanzberatung dar.
