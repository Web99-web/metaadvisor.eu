---
title: "Fast 1.200 Coldcard-Wallets in 41 Minuten geleert"
slug: "fast-1200-coldcard-wallets-in-41-minuten-geleert"
date: 2026-08-01T12:00:00+02:00
category: "crypto"
translationKey: "gotovo-1200-coldcard-walleta-ispraznjeno-u-41-minuti-2026-08-01"
source: "CoinDesk, Galaxy Research, Coinkite, Block Bitcoin Engineering and Security und CZ"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/Crypto-alert.png"
featured_image: "/images/Crypto-alert.png"
image: "/images/Crypto-alert.png"
thumbnail: "/images/Crypto-alert.png"
image_alt: "Krypto-Sicherheitswarnung nach dem Diebstahl von Bitcoin aus Coldcard-Wallets"
image_credit: "Metaadvisor.eu – Symbolbild"
tags: ["Coldcard", "Coinkite", "Bitcoin", "Hardware-Wallet", "Cold Wallet", "Bitcoin-Diebstahl", "Seed-Phrase", "privater Schlüssel", "Sicherheitslücke", "Firmware", "Krypto-Sicherheit", "Galaxy Research", "Changpeng Zhao", "CZ", "Cybersicherheit"]
description: "Mehr als 1.000 BTC im Wert von rund 70 Millionen Dollar wurden von fast 1.200 Adressen gestohlen, die mit anfälligen Coldcard-Wallets verbunden waren."
summary: "Ein Angreifer bewegte in nur 41 Minuten 1.082,65 BTC von 1.196 Adressen, nachdem eine Sicherheitslücke die Rekonstruktion unzureichend zufällig erzeugter Schlüssel ermöglicht hatte."
---

# Fast 1.200 Coldcard-Wallets in 41 Minuten geleert

Mehr als 1.000 Bitcoin im damaligen Wert von rund 70 Millionen Dollar wurden in nur 41 Minuten von fast 1.200 Adressen gestohlen. Besonders beunruhigend ist die Methode des Angriffs: Der Angreifer musste weder die Geräte stehlen noch sie mit dem Internet verbinden oder die Seed-Phrases der Nutzer durch Phishing erlangen.

Das Problem lag in bestimmten Firmware-Versionen für COLDCARD-Hardware-Wallets. Aufgrund eines Fehlers erzeugten einige Geräte Schlüssel, die nicht ausreichend zufällig und dadurch besser vorhersagbar waren. Der Angreifer konnte versuchen, diese Schlüssel auf seinen eigenen Computern zu rekonstruieren.

*Das Bild ist symbolisch.*

## Was ist COLDCARD?

COLDCARD ist kein allgemeiner Begriff für alle Cold Wallets oder Hardware-Wallets. Es handelt sich um eine konkrete Marke von Bitcoin-Hardware-Wallets des kanadischen Unternehmens Coinkite.

Ähnliche Geräte werden unter anderen Markennamen angeboten, darunter Ledger und Trezor. Dieser Vorfall betrifft jedoch bestimmte Modelle und Firmware-Versionen von COLDCARD.

Bitcoin wird dabei nicht physisch auf dem Gerät gespeichert. Der Bestand ist auf der Blockchain verzeichnet, während das Gerät die geheimen Schlüssel erzeugt und verwahrt, mit denen der Eigentümer eine Transaktion signieren und Bitcoin übertragen kann.

## Wie konnte Bitcoin ohne Zugriff auf das Gerät gestohlen werden?

Wenn ein Wallet erstmals eingerichtet wird, muss das Gerät eine vollständig zufällige Seed-Phrase erzeugen. Aus ihr werden mathematisch die privaten Schlüssel und Bitcoin-Adressen abgeleitet.

Eine solche Seed-Phrase sollte praktisch unmöglich zu erraten sein. Bei den betroffenen COLDCARD-Geräten führte jedoch ein Firmware-Fehler dazu, dass der vorgesehene Hardware-Zufallszahlengenerator nicht verwendet wurde.

Stattdessen wurde ein schwächerer Softwaremechanismus aktiviert, der sich auf technische Daten des Geräts und Werte seiner internen Uhr stützte. Der Raum möglicher Kombinationen war dadurch deutlich kleiner als vorgesehen.

{{< support1 >}}

Vereinfacht gesagt sollte das Gerät einen vollständig unvorhersehbaren Schlüssel erzeugen. Aufgrund des Fehlers wählte es den Schlüssel jedoch nach einem Muster aus, das leichter rekonstruiert werden konnte.

Das ist vergleichbar mit einem Tresor, dessen Hersteller eine einzigartige und unvorhersehbare Kombination verspricht, sie aufgrund eines Fehlers aber aus der Seriennummer und dem Herstellungszeitpunkt zusammensetzt. Ein Dieb muss den Tresor weder sehen noch berühren. Er kann mögliche Kombinationen auf seinem eigenen Computer ausprobieren, bis er die passende findet.

## Der Angreifer konnte nach anfälligen Adressen suchen

Der Angreifer konnte mögliche Seed-Phrases automatisiert erzeugen, daraus die zugehörigen Bitcoin-Adressen berechnen und auf der öffentlichen Blockchain prüfen, ob sich auf diesen Adressen Guthaben befand.

Sobald er eine Übereinstimmung fand, konnte er aus derselben Seed-Phrase den privaten Schlüssel ableiten und eine Transaktion signieren. Das Bitcoin-Netzwerk akzeptiert eine solche Transaktion als gültig, weil sie mit dem passenden Schlüssel signiert wurde.

Der Angreifer hat mit großer Wahrscheinlichkeit nicht jede einzelne Adresse manuell geprüft und geleert. Der Angriff musste durch ein Programm automatisiert worden sein, das mögliche Schlüssel suchte, Adressen verglich und Transaktionen vorbereitete.

Bisher gibt es keine Beweise dafür, dass bei dem Angriff künstliche Intelligenz eingesetzt wurde. KI könnte bei der Analyse des Codes oder bei der Entwicklung der Werkzeuge geholfen haben, doch für einen solchen Angriff reicht auch ein automatisiertes Skript aus.

## 1.082,65 BTC gestohlen

Nach einer Analyse von Galaxy Research wurden am 30. Juli zwischen 01:10 und 01:51 Uhr UTC insgesamt 1.196 Bitcoin-Adressen geleert.

In sechs Blöcken wurden 1.082,65 BTC bewegt, die zu diesem Zeitpunkt rund 70 Millionen Dollar wert waren. Dazwischen wurden drei Blöcke ohne zugehörige Transaktionen registriert. Das deutet darauf hin, dass die Transaktionen in vorab vorbereiteten Gruppen gesendet wurden.

Erste Schätzungen gingen von rund 594 BTC und etwa 500 Wallets aus. Eine spätere Analyse entdeckte weitere mit dem Angriff verbundene Adressen, wodurch sich der geschätzte Betrag nahezu verdoppelte.

Die gestohlenen Bitcoin sollen sich auf vier Adressen befinden und nach den zuletzt verfügbaren Informationen noch nicht weiterbewegt worden sein.

{{< support2 >}}

## Welche COLDCARD-Geräte sind betroffen?

Coinkite teilte mit, dass Seed-Phrases betroffen sind, die auf dem Modell Mk3 mit Firmware-Versionen von 4.0.1 bis 4.1.9 erzeugt wurden.

Das Problem betrifft außerdem Seed-Phrases, die auf den Modellen Mk4 und Mk5 vor der Standardversion 5.6.0 oder der Edge-Version 6.6.0X sowie auf dem Modell Q vor der Standardversion 1.5.0Q oder der Edge-Version 6.6.0QX erzeugt wurden.

Bei den neueren Modellen ist das Risikoniveau nicht identisch mit dem der Mk3-Geräte. Coinkite stuft das Problem dennoch weiterhin als ernst ein.

TAPSIGNER, OPENDIME und SATSCARD sind nicht betroffen, da sie einen anderen Programmcode verwenden.

## Ein Firmware-Update allein reicht nicht aus

Coinkite bestätigte die Sicherheitslücke, entschuldigte sich bei den Nutzern und veröffentlichte korrigierte Firmware-Versionen.

Ein Update allein kann jedoch keine Seed-Phrase reparieren, die bereits mit einer anfälligen Version erzeugt wurde. Das Problem liegt nicht nur im Gerät, sondern in dem Schlüssel, den das Gerät bereits erstellt hat.

Betroffene Nutzer müssen eine sichere Firmware-Version installieren, eine vollständig neue Seed-Phrase erzeugen und ihre Mittel auf neue Bitcoin-Adressen übertragen. Die alte Seed-Phrase bleibt anfällig, selbst wenn sie später in ein anderes Hardware- oder Software-Wallet importiert wird.

Coinkite nennt eine mögliche Ausnahme für Nutzer, die bei der Erstellung ihrer Seed-Phrase mindestens 50 unabhängige und geheime Würfelwürfe hinzugefügt haben. Diese zusätzliche Zufallsquelle könnte trotz des Firmware-Fehlers eine ausreichend starke Seed-Phrase erzeugt haben.

{{< support2 >}}

## CZ empfiehlt die Verteilung der Mittel

Binance-Gründer Changpeng Zhao, bekannt als CZ, warnte nach dem Vorfall, dass selbst Hardware-Wallets mit langer Geschichte schwerwiegende Fehler enthalten können.

Er schlug Nutzern vor, größere Beträge auf mehrere Wallets zu verteilen, damit eine einzige Sicherheitslücke nicht sämtliche Mittel gefährdet.

Dieser Ansatz bringt jedoch ebenfalls neue Risiken mit sich. Nutzer müssen mehrere Geräte, Seed-Phrases und Sicherungskopien korrekt verwahren. Eine größere Zahl von Wallets erhöht zugleich die Wahrscheinlichkeit menschlicher Fehler.

## Ein Hardware-Wallet ist kein magischer Schutz

Der Vorfall zeigt, dass ein Hardware-Wallet vollständig offline bleiben kann und die Mittel dennoch gefährdet sein können, wenn der geheime Schlüssel von Anfang an fehlerhaft erzeugt wurde.

Die Nutzer verloren ihre Bitcoin nicht zwangsläufig, weil sie jemandem ihre Seed-Phrase verrieten, eine gefälschte Anwendung installierten oder das Gerät mit einer bösartigen Website verbanden. Sie verloren die Mittel, weil das Gerät einen Schlüssel erzeugte, der rekonstruiert werden konnte.

Ein Hardware-Wallet kann das Diebstahlrisiko weiterhin erheblich reduzieren. Seine Sicherheit hängt jedoch von der Qualität des Geräts, der Firmware und der Methode ab, mit der die wichtigste geheime Information des gesamten Wallets erzeugt wird: die Seed-Phrase.

## Unsere Einschätzung

* COLDCARD ist eine konkrete Marke von Bitcoin-Hardware-Wallets und kein allgemeiner Begriff für alle Cold Wallets.
* Der Angriff betrifft nicht sämtliche Hersteller von Hardware-Wallets.
* Innerhalb von nur 41 Minuten wurden von 1.196 Adressen insgesamt 1.082,65 BTC bewegt.
* Der Wert der gestohlenen Bitcoin lag damals bei rund 70 Millionen Dollar.
* Der Angreifer musste nicht physisch auf die Geräte zugreifen.
* Die Sicherheitslücke führte zur Erzeugung unzureichend zufälliger Seed-Phrases.
* Mögliche Seed-Phrases und die dazugehörigen Adressen konnten automatisiert geprüft werden.
* Es gibt keine Beweise dafür, dass bei dem Angriff künstliche Intelligenz eingesetzt wurde.
* Coinkite veröffentlichte Sicherheitsupdates und entschuldigte sich bei den Nutzern.
* Ein Firmware-Update repariert keine Seed-Phrase, die bereits mit einer anfälligen Version erzeugt wurde.
* Betroffene Nutzer müssen eine neue Seed-Phrase erstellen und ihre Mittel auf neue Adressen übertragen.
* CZ empfahl, größere Beträge auf mehrere Wallets zu verteilen, doch auch das bringt zusätzliche Risiken mit sich.
* Ein Hardware-Wallet bietet starken Schutz, kann aber nicht sicherer sein als die Methode, mit der sein Schlüssel erzeugt wurde.

**Disclaimer:** Dieser Artikel dient ausschließlich Informations- und Bildungszwecken und stellt keine Rechts-, Finanz-, Anlage- oder Sicherheitsberatung dar. Die Informationen beruhen auf öffentlich zugänglichen Quellen, und nicht alle Angaben wurden zwingend unabhängig bestätigt.

In Zusammenarbeit mit KI.
