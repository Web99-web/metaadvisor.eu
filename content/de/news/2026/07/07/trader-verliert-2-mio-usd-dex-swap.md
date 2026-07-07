---
title: "Trader verliert 2 Mio. USD bei DEX-Swap"
slug: "trader-verliert-2-mio-usd-dex-swap"
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
tags: ["DEX-Swap", "DeFi-Risiko", "MEV", "Same-Block-Backrun", "Titan Builder", "GoPlus Security", "Uniswap v3", "0x Router", "Slippage", "Price Impact", "Crypto-Verlust"]
summary: "Ein Trader verlor fast 2 Millionen US-Dollar, nachdem ein großer ETH-Swap durch einen Pool mit sehr geringer Liquidität geleitet wurde. Der Fall zeigt, warum Minimum Received, Slippage, Price Impact und die Swap-Route vor jeder DEX-Signatur entscheidend sind."
disclaimer: "Dieser Artikel dient ausschließlich Informationszwecken und stellt keine Finanz-, Anlage-, Rechts- oder Sicherheitsberatung dar."
draft: false
---

Bild ist symbolisch.

# Trader verliert 2 Millionen US-Dollar bei DEX-Swap: kein klassischer Hack, sondern eine katastrophale Transaktionsroute

Ein Crypto-Trader verlor fast den gesamten Betrag von rund **2 Millionen US-Dollar**, nachdem er auf einer dezentralen Börse einen großen Ether-Swap durchführen wollte. Am Ende blieb er laut verfügbaren Berichten mit Token im Wert von nur etwa **14.500 US-Dollar** zurück.

Auf den ersten Blick klingt die Geschichte wie ein weiterer Crypto-Hack. Doch dieser Fall ist interessanter. Es geht nicht darum, dass jemand einfach eine Wallet „gestohlen“ oder den Nutzer mit einem Fake-Link getäuscht hat. Das Problem entstand, weil die Transaktion durch einen **Pool mit sehr geringer Liquidität** lief und andere Marktteilnehmer den Preisunterschied sofort ausnutzten.

Mit anderen Worten: Der Trader signierte einen Swap, der zu einem katastrophalen Preis ausgeführt wurde.

Laut einem Bericht von Cointelegraph und einer Analyse von GoPlus Security tauschte der Trader **1.126,44 ETH** im Wert von rund **2,01 Millionen US-Dollar**, erhielt dafür aber nur **5.776 Lighter (LIT) Token**. GoPlus Security beschrieb den Vorfall als „textbook case“ einer sogenannten **Same-Block Backrun Extraction**.

{{< support1 >}}

Das bedeutet, dass innerhalb desselben Ethereum-Blocks ein anderer Akteur die Schieflage ausnutzen konnte, die durch diese große und schlecht geroutete Transaktion entstanden war.

Der größte Gewinner war Berichten zufolge **Titan Builder**, der aus dem gesamten Vorfall rund **1,8 Millionen US-Dollar** herausziehen konnte.

## Was ist eigentlich passiert?

Der Trader wollte einen großen Swap auf einer dezentralen Börse durchführen. Bei solchen Transaktionen geht der Nutzer oft nicht direkt von einem Token in einen anderen, sondern ein DEX-Router sucht einen Weg über verschiedene Token und Liquidity Pools.

In diesem Fall wurde der Swap Berichten zufolge durch einen **AVAIL/WETH-Pool auf Uniswap v3** geleitet, der nicht genügend Liquidität für einen so großen Auftrag hatte.

Das ist der Kern der ganzen Geschichte.

Wenn ein Pool klein ist und der Auftrag riesig, kann sich der Preis extrem verschieben. Es ist, als würde man versuchen, 2 Millionen Euro in einer kleinen Wechselstube statt über eine große Bank zu tauschen. Die Wechselstube hat nicht genug „Tiefe“ für eine solche Transaktion, also würde der Wechselkurs völlig ungünstig werden.

Laut GoPlus Security landete ein Teil der Transaktion in einem Pool, in dem der Preis etwa **120-mal höher** war als der Preis, zu dem der Token später verkauft werden konnte.

Der Trader verlor sein Geld also nicht, weil „kein Geld im Pool“ war, zumindest nicht im klassischen Sinn. Er verlor Geld, weil seine große Transaktion durch einen Pool lief, der dieses Volumen nicht normal aufnehmen konnte.

## Kein klassischer Sandwich Attack

GoPlus Security betont, dass es sich nicht um einen klassischen **Sandwich Attack** handelte.

Bei einem Sandwich-Angriff sieht ein Bot normalerweise die Transaktion eines Nutzers, kauft vor ihm, lässt den Nutzer den Preis nach oben treiben und verkauft direkt danach wieder. Der Nutzer steckt dann zwischen zwei Bot-Transaktionen „im Sandwich“.

Hier war die Situation anders.

GoPlus Security beschreibt den Fall als echte, stark unausgewogene **Backrunner-Arbitrage**. Das bedeutet, dass die schlecht ausgeführte Transaktion selbst die Gelegenheit geschaffen hat und ein anderer Teilnehmer sie sofort innerhalb desselben Blocks ausnutzte.

Genau deshalb ist dieser Fall so unangenehm: Die Transaktion wurde möglicherweise technisch genau so ausgeführt, wie sie signiert wurde, aber das Ergebnis war für den Nutzer katastrophal.

## Wie hätte der Trader erkennen können, dass etwas nicht stimmt?

Das ist der wichtigste und interessanteste Teil der ganzen Geschichte.

Der Trader musste nicht manuell wissen, wie viel Liquidität in jedem einzelnen Pool vorhanden war. Er musste nicht jeden Smart Contract selbst prüfen oder die Markttiefe berechnen. Aber vor der Signatur der Transaktion hätte er mehrere grundlegende Signale prüfen können, die ein DEX-Interface, eine Wallet oder ein Aggregator häufig anzeigt, bevor der Nutzer auf **Confirm** klickt.

Das erste und wichtigste Signal ist **Minimum Received**.

Das ist die Mindestmenge an Token, die der Nutzer erhält, wenn die Transaktion ausgeführt wird. Vor der Bestätigung steht oft etwas wie: „You will receive at least X tokens.“

Wenn der Trader gesehen hätte, dass er für ETH im Wert von rund **2 Millionen US-Dollar** Token erhält, die nach der Ausführung nur etwa **14.500 US-Dollar** wert sind, wäre das sofort ein Zeichen gewesen, die Transaktion nicht zu signieren.

Das zweite Signal ist **Slippage** oder **Price Impact**.

Bei einem normalen Swap sollte der Price Impact relativ klein sein. Wenn das Interface einen enormen Price Impact anzeigt, zum Beispiel 30, 80 oder 99 Prozent, bedeutet das, dass die Transaktion selbst den Preis stark verschieben wird, weil der Pool nicht genügend Liquidität hat.

Einfach gesagt: Der Swap ist zu groß für den Pool, durch den er läuft.

Das dritte Signal ist die **Transaktionsroute**.

In einer erweiterten Ansicht lässt sich oft sehen, über welche Token und Pools der Swap läuft. Eine Route kann zum Beispiel so aussehen:

ETH → WETH → AVAIL → LIT

oder ähnlich.

Wenn der Trader gesehen hätte, dass ein riesiger Betrag durch einen kleinen oder ungewöhnlichen AVAIL/WETH-Pool läuft, hätte er stoppen und die Transaktion nicht signieren können.

## Bei 2 Millionen US-Dollar klickt man nicht einfach auf Confirm

Bei einem Swap im Wert von rund **2 Millionen US-Dollar** ist es zusätzlich wichtig, das Ergebnis auf mehreren DEXs und Aggregatoren zu vergleichen.

Ein solcher Betrag sollte nicht mit einem schnellen Klick ohne Prüfung gesendet werden. Der Trader hätte das Angebot auf Diensten wie 1inch, Matcha, CoW Swap oder Uniswap vergleichen können. Er hätte auch eine OTC-Lösung in Betracht ziehen können, besonders wenn es um einen großen Auftrag und schwächere Liquidität geht.

Wenn ein Router ein deutlich schlechteres Ergebnis liefert als andere, ist das eine große rote Flagge.

Es gab auch eine einfachere Möglichkeit: die Transaktion in kleinere Teile aufzuteilen. Ein großer Swap durch einen kleinen Pool kann einen extremen Price Impact verursachen. Kleinere Orders, eine Limit Order oder ein OTC-Deal können oft das Risiko verringern, dass der Preis in eine völlig ungünstige Richtung läuft.

Deshalb geht es in dieser Geschichte nicht nur um Hacker oder MEV-Bots. Sie zeigt, wie gefährlich es ist, DEX-Transaktionen zu signieren, ohne die Details zu prüfen.

Der Trader musste nicht im Voraus wissen, wie viel „Geld“ im Pool lag, aber die Folgen davon hätten wahrscheinlich durch vier Dinge sichtbar sein können: **Minimum Received, Price Impact, Slippage und die Swap-Route**.

Kurz gesagt: Das Problem war nicht nur, dass der Pool zu klein war. Das Problem war, dass die Transaktion signiert wurde, obwohl die Swap-Details hätten zeigen können, dass das Ergebnis katastrophal wird.

{{< support2 >}}

## Warum sind MEV und Block Builder wichtig?

Dieser Vorfall öffnet erneut die Frage nach **MEV**, also Maximal Extractable Value.

MEV bezeichnet den zusätzlichen Wert, den Validatoren, Block Builder oder Bots aus der Art und Weise ziehen können, wie Transaktionen in einem Blockchain-Block sortiert, ausgeführt und angeordnet werden.

In der Praxis bedeutet das: Wer eine große oder schlecht konfigurierte Transaktion sieht, kann versuchen, aus Preisunterschieden, Arbitrage oder der Reihenfolge der Ausführung Profit zu ziehen.

<a href="https://metaadvisor.eu/de/news/was-ist-mev-trading-defi/" target="_blank" rel="noopener">
  <img src="/images/MEV-explained.png" alt="Was ist MEV-Trading und warum es zu einem der größten Probleme im DeFi geworden ist" style="max-width: 360px; width: 100%; height: auto; display: block; margin: 1rem 0;">
</a>

<a href="https://metaadvisor.eu/de/news/was-ist-mev-trading-defi/" target="_blank" rel="noopener">Was ist MEV-Trading und warum es zu einem der größten Probleme im DeFi geworden ist</a>

In diesem Fall war Titan Builder Berichten zufolge der größte Nutznießer der Gelegenheit, die nach dem schlechten Swap entstand. Das bedeutet nicht unbedingt, dass die Wallet des Nutzers „gehackt“ wurde. Es bedeutet, dass die Marktinfrastruktur eine Transaktion ausnutzte, die bereits signiert und gesendet worden war.

Für normale Nutzer klingt dieser Unterschied vielleicht technisch, aber die Folge ist sehr real: Fast der gesamte Betrag von 2 Millionen US-Dollar verschwand durch eine schlechte Swap-Ausführung.

## Was können Nutzer aus diesem Fall lernen?

Die wichtigste Lektion ist einfach: Bei DEX-Transaktionen reicht es nicht, nur darauf zu schauen, welchen Token man kauft oder verkauft. Man muss auch darauf achten, **wie** die Transaktion ausgeführt wird.

Vor der Signatur sollte man prüfen:

- den Mindestbetrag, den man erhält,
- Slippage,
- Price Impact,
- die Transaktionsroute,
- die Liquidität der Pools,
- den Preisunterschied zwischen mehreren DEXs oder Aggregatoren.

Bei kleinen Beträgen kann ein Fehler unangenehm sein. Bei großen Beträgen kann ein Fehler zerstörerisch sein.

DEXs geben Nutzern mehr Kontrolle, aber diese Kontrolle kommt mit Verantwortung. Eine Bank oder eine zentrale Börse hat oft mehr Schutzmechanismen, während ein dezentraler Swap genau das ausführen kann, was der Nutzer signiert hat, selbst wenn das Ergebnis extrem ungünstig ist.

Genau das macht diesen Fall so wichtig.

Es geht nicht nur um einen Trader, der Geld verloren hat. Es geht um eine Warnung, dass Nutzer in dezentralen Finanzen verstehen müssen, was sie signieren.

## Unser Fazit

- Dieser Fall ist wichtig, weil er zeigt, dass Crypto-Risiko nicht nur von klassischen Hackern, Phishing-Links oder Fake-Token kommt.
- Manchmal reichen ein schlecht gerouteter Swap, ein zu kleiner Liquidity Pool und ein Klick auf **Confirm**.
- Der interessanteste Teil der Geschichte ist nicht nur der Verlust von 2 Millionen US-Dollar, sondern die Tatsache, dass ein Teil des Risikos wahrscheinlich schon vor der Signatur sichtbar gewesen wäre.
- **Minimum Received**, **Price Impact**, **Slippage** und die **Swap-Route** sind kein technisches Kleingedrucktes. Das sind Signale, die zeigen können, dass eine Transaktion katastrophal enden wird.
- Für kleine Retail-Nutzer ist das eine Warnung, Transaktionen nicht zu signieren, ohne die Details zu lesen.
- Für größere Trader ist die Botschaft noch klarer: Große Orders sollten nicht wie ein gewöhnlicher schneller Swap ausgeführt werden, ohne Liquidität, Alternativen und Schutz vor schlechter Ausführung zu prüfen.
- Crypto verspricht oft Geschwindigkeit, Freiheit und offene Märkte. Aber im DeFi bedeutet Freiheit auch, dass das System nicht immer für einen stoppt.
- Wenn man eine schlechte Transaktion signiert, kann die Blockchain sie perfekt ausführen — selbst wenn das Ergebnis für einen selbst katastrophal ist.

**Disclaimer:** Dieser Artikel dient ausschließlich Informationszwecken und stellt keine Finanz-, Anlage-, Rechts- oder Sicherheitsberatung dar. Crypto- und DeFi-Transaktionen sind mit hohen Risiken verbunden, und Nutzer sind selbst dafür verantwortlich, Transaktionen vor der Signatur zu prüfen.
