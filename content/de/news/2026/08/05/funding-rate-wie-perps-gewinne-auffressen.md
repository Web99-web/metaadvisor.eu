---
title: "Funding Rate: Wie Perps Gewinne auffressen"
slug: "funding-rate-wie-perps-gewinne-auffressen"
date: 2026-08-05T06:00:00+02:00
category: "crypto"
translationKey: "funding-rate-kako-perpsi-pojedu-dobit-2026-08-05"
source: "Hyperliquid, Binance und öffentlich zugängliche Dokumentation zu Perpetual-Futures-Kontrakten"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/informative/Funding-cost-perps.png"
featured_image: "/images/informative/Funding-cost-perps.png"
image: "/images/informative/Funding-cost-perps.png"
thumbnail: "/images/informative/Funding-cost-perps.png"
image_alt: "Funding Rate als versteckte Kosten beim Handel mit Perpetual-Futures-Kontrakten"
image_credit: "Metaadvisor.eu – Symbolbild"
tags: ["Funding Rate", "Perpetual Futures", "Perps", "Krypto-Handel", "Hebel", "Long-Position", "Short-Position", "Handelsgebühren", "Hyperliquid", "Binance", "Derivate", "Margin-Handel", "Liquidation", "Krypto-Risiko", "Risikomanagement"]
description: "Funding Rates können Gewinne aus Perpetual-Futures-Positionen schrittweise verringern, insbesondere bei langer Haltedauer, höherem Hebel und hohen Sätzen."
summary: "Perpetual-Futures-Kontrakte haben kein Ablaufdatum, können aber nicht kostenlos unbegrenzt gehalten werden. Funding wird regelmäßig auf den gesamten Positionswert berechnet und kann den endgültigen Gewinn deutlich reduzieren."
---

*Das Bild ist symbolisch.*

# Funding Rate: Wie Perps Gewinne auffressen

Perpetual-Futures-Kontrakte, häufig als Perps bezeichnet, gehören zu den beliebtesten Möglichkeiten, Kryptowährungen zu handeln. Sie ermöglichen Long- oder Short-Positionen mit Hebel, haben kein Ablaufdatum und bieten häufig hohe Liquidität sowie vergleichsweise niedrige Handelsgebühren.

Es gibt jedoch einen Kostenfaktor, den Händler leicht übersehen: die Funding Rate.

Eine Position kann über Tage oder Wochen geöffnet bleiben, der Kurs kann sich sogar in die erwartete Richtung bewegen, und dennoch kann ein Teil des Gewinns durch regelmäßige Funding-Zahlungen nach und nach verschwinden.

## Was sind Perpetual Futures?

Ein klassischer Futures-Kontrakt besitzt ein Ablaufdatum. Ein Perpetual Future hat keines. Händler können ihre Position daher theoretisch unbegrenzt halten, solange ausreichend Margin vorhanden ist und die Position nicht liquidiert wird.

Mit Perps können Händler auf steigende oder fallende Kurse setzen, ohne den Token tatsächlich zu kaufen:

* Eine Long-Position gewinnt, wenn der Kurs steigt.
* Eine Short-Position gewinnt, wenn der Kurs fällt.
* Der Hebel vergrößert die Position im Verhältnis zum hinterlegten Kapital.

Händler schätzen Perps wegen ihrer Liquidität, vergleichsweise niedriger Gebühren und der großen Marktexponierung, die mit einer kleinen Menge an Sicherheiten erreicht werden kann.

Das langfristige Halten einer Position kann jedoch zusätzliche Kosten verursachen, die aus der Gebühr für die Eröffnung des Trades allein nicht ersichtlich sind.

## Warum gibt es eine Funding Rate?

Da Perpetual Futures kein Ablaufdatum besitzen, wird ein Mechanismus benötigt, der ihren Preis möglichst nahe am tatsächlichen Spotpreis der Kryptowährung hält.

Die Funding Rate führt deshalb zu regelmäßigen Zahlungen zwischen Händlern mit Long- und Short-Positionen.

Wenn zu viele Händler long gehen wollen, kann der Perp-Preis über den Spotpreis steigen. Dann ist die Funding Rate üblicherweise positiv:

**Long-Positionen zahlen an Short-Positionen.**

Wenn dagegen Short-Positionen überwiegen, kann die Funding Rate negativ werden:

**Short-Positionen zahlen an Long-Positionen.**

Das Geld geht normalerweise nicht an die Börse, sondern wird zwischen den beiden Marktseiten übertragen. Funding schafft damit einen Anreiz, Positionen auf der weniger beliebten Seite zu eröffnen, und hilft, den Perp-Preis näher an den Spotpreis zu bringen.

{{< support1 >}}

## Funding wird auf die gesamte Position berechnet

Einer der wichtigsten Punkte ist, dass Funding nicht nur auf das Kapital berechnet wird, das der Händler als Margin hinterlegt hat.

Es wird auf den vollständigen Wert der offenen Position berechnet.

Hinterlegt ein Händler zehn Dollar und eröffnet mit einem vierfachen Hebel eine Position im Wert von 40 Dollar, wird das Funding auf 40 Dollar berechnet.

Bei einer Funding Rate von 0,05 Prozent ergeben sich beispielsweise folgende Zahlungen:

* Eine Position von 10 Dollar zahlt 0,005 Dollar.
* Eine Position von 40 Dollar zahlt 0,02 Dollar.
* Eine Position von 10.000 Dollar zahlt 5 Dollar.

Eine einzelne Zahlung kann unbedeutend wirken. Sie wiederholt sich jedoch, solange die Position geöffnet bleibt und der Händler sich auf der Marktseite befindet, die Funding bezahlt.

## Wie kann Funding Gewinne auffressen?

Nehmen wir eine Position im Wert von 1.000 Dollar an, die über mehrere Tage einen nicht realisierten Gewinn von 20 Dollar erzielt.

Zahlt der Händler im selben Zeitraum drei Dollar Funding sowie Gebühren für die Eröffnung und Schließung der Position und zusätzlich Spread oder Slippage, fällt sein tatsächlicher Gewinn geringer aus als der Betrag, den er in der einfachen Kursanzeige gesehen hat.

Bei sehr hohen Funding Rates kann ein Händler die Marktrichtung sogar richtig vorhersehen und trotzdem nur einen sehr kleinen Gewinn oder einen Verlust erzielen.

Funding ist besonders wichtig bei Positionen, die über Tage oder Wochen gehalten werden. Bei einem Trade von wenigen Minuten hat eine einzelne Funding-Periode möglicherweise kaum Einfluss. Bei langer Haltedauer summieren sich jedoch auch kleine Beträge.

{{< support2 >}}

## Wie funktioniert Funding auf Hyperliquid?

Hyperliquid berechnet Funding stündlich.

Die Zahlung basiert auf der Positionsgröße, dem Oracle-Preis und der aktuellen Funding Rate. Die offizielle Dokumentation nennt zudem eine Obergrenze von vier Prozent pro Stunde.

Das bedeutet nicht, dass Funding gewöhnlich vier Prozent beträgt. Es bedeutet, dass es unter extremen Marktbedingungen deutlich stärker steigen kann, als Händler erwarten.

Funding unterscheidet sich von Token zu Token und kann sich schnell verändern. Zu einem bestimmten Zeitpunkt kann Hyperliquid teurer als eine andere Plattform sein, später günstiger oder sogar eine Funding Rate mit umgekehrtem Vorzeichen aufweisen.

Deshalb reicht es nicht, Funding nur beim Öffnen der Position zu prüfen. Die Rate kann sich verändern, während der Trade weiterhin geöffnet ist.

## Kleine Beträge bedeuten nicht, dass Funding unwichtig ist

Bei Positionen im Wert von nur wenigen Dollar ist der absolute Funding-Betrag normalerweise sehr gering.

Pro Abrechnung kann es sich lediglich um einen Bruchteil eines Cents handeln. Eine solche Position wird wahrscheinlich nicht allein wegen des Fundings einen erheblichen Verlust erleiden.

Kleine Positionen eignen sich dennoch gut zum Lernen, weil sie deutlich zeigen:

* wann Long an Short zahlt
* wann eine Short-Position Funding erhält
* wie der Hebel den Positionswert vergrößert
* warum nicht realisierter P&L nicht dem endgültigen Gewinn entspricht
* wie sich regelmäßige Kosten im Laufe der Zeit ansammeln

Bei kleinen Positionen können Handelsgebühren, Spread und ein ausbleibender erwarteter Kursschritt häufig ein größeres Problem darstellen als das Funding selbst.

{{< support1 >}}

## Funding kann auch Einnahmen bringen

Funding ist nicht immer ein Kostenfaktor.

Ein Händler auf der Seite, die Funding erhält, kann regelmäßige Zahlungen bekommen, solange die Position geöffnet bleibt.

Einige professionelle Händler verwenden deshalb Strategien, die auf das Sammeln von Funding abzielen und gleichzeitig die Exponierung gegenüber Kursbewegungen reduzieren.

Eine hohe positive Funding Rate ist jedoch nicht automatisch ein Grund, eine Short-Position zu eröffnen. Ebenso ist eine hohe negative Funding Rate nicht automatisch ein Long-Signal.

Der Markt kann viel länger stark steigen oder fallen, als ein Händler zahlungsfähig bleiben kann. Der mögliche Funding-Ertrag kann dann im Vergleich zum Verlust aus der Position oder einer Liquidation unbedeutend sein.

## Stündliches, achtstündiges und jährliches Funding sind nicht dasselbe

Besonders gefährlich ist es, die Zahlen zweier Plattformen direkt zu vergleichen, wenn eine stündliches Funding, eine andere eine Acht-Stunden-Rate und eine dritte eine jährliche Hochrechnung anzeigt.

Eine Rate von 0,01 Prozent pro Stunde ist nicht dasselbe wie 0,01 Prozent alle acht Stunden.

Auch eine jährliche Hochrechnung ist kein garantierter Kostenbetrag für das kommende Jahr. Sie zeigt lediglich, wie hoch das Funding wäre, wenn die aktuelle Rate unverändert bliebe, was in der Praxis nur selten geschieht.

Vor einem Vergleich müssen sämtliche Raten auf denselben Zeitraum umgerechnet werden.

{{< support2 >}}

## Was sollte vor dem Öffnen eines Perps geprüft werden?

Vor dem Öffnen einer Position sollte ein Händler prüfen:

* Ist die Funding Rate positiv oder negativ?
* Zahlt die Long- oder die Short-Seite?
* Wie häufig wird Funding berechnet?
* Bezieht sich die angezeigte Rate auf eine Stunde, acht Stunden oder eine jährliche Hochrechnung?
* Wie hoch ist der vollständige Positionswert?
* Wie lange soll die Position gehalten werden?
* Wie stark schwankte Funding in den vergangenen Stunden oder Tagen?

Auch bei einer bereits offenen Position sollten die bisherigen Funding-Zahlungen kontrolliert werden. Ein nicht realisierter Gewinn kann gut aussehen, doch das endgültige Ergebnis berücksichtigt zusätzlich Funding, Handelsgebühren und die Kosten der Positionsschließung.

## Perps haben kein Ablaufdatum, aber laufende Kosten

Perpetual Futures wirken einfach: Händler wählen Long oder Short, stellen den Hebel ein und beobachten den Kurs.

Die tatsächlichen Kosten beschränken sich jedoch nicht auf die geringe Gebühr für die Eröffnung und Schließung einer Position.

Bei einem kurzen Trade und einer kleinen Position kann die Funding Rate nahezu unbemerkt bleiben. Bei hohem Hebel, beliebten Altcoins und langer Haltedauer kann sie jedoch erheblich werden.

Entscheidend ist zu verstehen, dass Funding auf den gesamten Positionswert berechnet wird, nicht immer dieselbe Marktseite zahlt und sich die Rate während eines laufenden Trades verändern kann.

Perps haben kein Ablaufdatum. Das bedeutet aber nicht, dass sie kostenlos unbegrenzt gehalten werden können.

## Unsere Einschätzung

* Perpetual-Futures-Kontrakte besitzen kein Ablaufdatum.
* Die Funding Rate hilft, den Perp-Preis nahe am Spotpreis zu halten.
* Bei positiver Funding Rate zahlen Long-Positionen üblicherweise an Short-Positionen.
* Bei negativer Funding Rate zahlen Short-Positionen üblicherweise an Long-Positionen.
* Funding wird auf den vollständigen Positionswert und nicht nur auf die hinterlegte Margin berechnet.
* Der Hebel vergrößert deshalb auch den Betrag, auf den Funding berechnet wird.
* Kleine regelmäßige Zahlungen können sich bei langer Haltedauer erheblich summieren.
* Die Funding Rate kann sich verändern, während eine Position geöffnet ist.
* Hyperliquid berechnet Funding stündlich.
* Funding kann ein Kostenfaktor oder eine Einnahme für die empfangende Marktseite sein.
* Eine hohe Funding Rate allein ist kein ausreichendes Signal für eine Long- oder Short-Position.
* Stündliche, achtstündige und jährliche Raten dürfen nicht ohne Umrechnung miteinander verglichen werden.
* Der nicht realisierte P&L zeigt nicht unbedingt den endgültigen Gewinn nach sämtlichen Kosten.

**Disclaimer:** Dieser Artikel dient ausschließlich Informations- und Bildungszwecken und stellt keine Finanz- oder Anlageberatung dar. Der Handel mit Derivaten und der Einsatz von Hebeln sind mit einem hohen Verlustrisiko verbunden.

In Zusammenarbeit mit KI.
