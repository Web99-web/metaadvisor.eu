---
title: "Coldcard-Angriff über 89 Millionen traf 4.585 Bitcoin-Wallets"
slug: "coldcard-angriff-89-millionen-4585-bitcoin-wallets"
date: 2026-08-02T12:00:00+02:00
category: "crypto"
translationKey: "coldcard-napad-89-milijuna-4585-bitcoin-novcanika-2026-08-02"
source: "Galaxy Research, Coinkite, CoinDesk, Cointelegraph und CryptoQuant"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/hack/Coldcard-hack-89M.png"
featured_image: "/images/hack/Coldcard-hack-89M.png"
image: "/images/hack/Coldcard-hack-89M.png"
thumbnail: "/images/hack/Coldcard-hack-89M.png"
image_alt: "Der Coldcard-Angriff weitete sich auf 4.585 Bitcoin-Wallets aus und verursachte Verluste von fast 89 Millionen Dollar"
image_credit: "Metaadvisor.eu – Symbolbild"
tags: ["Coldcard", "Bitcoin", "Bitcoin-Wallet", "Hardware-Wallet", "Krypto-Hack", "Cybersicherheit", "Seed-Phrase", "privater Schlüssel", "Coldcard Mk3", "Coldcard Mk4", "Bitcoin-Diebstahl", "Self-Custody", "Coinkite", "Galaxy Research", "Krypto-Sicherheit"]
description: "Der Coldcard-Angriff weitete sich auf 4.585 Bitcoin-Wallets aus. Die geschätzten Verluste stiegen auf 1.367 BTC beziehungsweise fast 89 Millionen Dollar."
summary: "Der Angriff auf anfällige Seeds, die mit bestimmten Coldcard-Firmwareversionen erzeugt wurden, setzte sich in mehreren Wellen fort. Die Angreifer zielen inzwischen auch auf kleinere Wallets und verteilen die gestohlenen Bitcoin auf mehr Zieladressen."
---

*Das Bild ist symbolisch.*

# Coldcard-Angriff über 89 Millionen traf 4.585 Bitcoin-Wallets

Der Angriff im Zusammenhang mit anfälligen Seeds, die mit bestimmten Coldcard-Firmwareversionen erzeugt wurden, ist längst nicht mehr auf die erste Welle beschränkt, in der fast 1.200 Bitcoin-Adressen innerhalb von nur 41 Minuten geleert wurden.

Nach neuen Schätzungen von Galaxy Research wurden in drei bislang identifizierten Angriffswellen insgesamt 4.585 Adressen geleert. Dabei wurden rund 1.367 BTC im Wert von fast 89 Millionen Dollar gestohlen.

Die jüngste Welle zeigt, dass der Angreifer nicht mehr nur größere Beträge ins Visier nimmt. Inzwischen werden systematisch auch Wallets mit einem Wert von nur wenigen Tausend Dollar angegriffen.

Der Angriff setzte sich fast drei Tage nach den ersten großen Transaktionen fort, während die Methode zur Verschiebung der gestohlenen Mittel komplexer und schwerer nachzuverfolgen wurde.

## Dritte Welle traf weitere 1.912 Adressen

In der dritten identifizierten Angriffswelle wurden rund 208 BTC von 1.912 Adressen gestohlen.

Der durchschnittliche Betrag pro betroffener Adresse liegt nun bei etwas mehr als 0,1 BTC. Das ist deutlich weniger als in der ersten Welle, als innerhalb von 41 Minuten rund 1.083 BTC von 1.196 Adressen abgezogen wurden, also nahezu ein Bitcoin pro Adresse.

Der sinkende Durchschnittsbetrag deutet darauf hin, dass die größten und profitabelsten Wallets aus dem anfälligen Schlüsselraum möglicherweise bereits geleert wurden. Der Angreifer geht nun zu kleineren Beträgen über, die dennoch wirtschaftlich interessant sein können.

Das ist besonders besorgniserregend für Nutzer, die möglicherweise glaubten, wegen eines relativ kleinen Guthabens auf ihrem Wallet kein attraktives Ziel zu sein.

## Der Angreifer hat seine Taktik geändert

Die ersten beiden Angriffswellen waren vergleichsweise leicht miteinander zu verbinden, weil die gestohlenen Bitcoin auf eine kleinere Zahl gemeinsamer Adressen flossen.

In der dritten Welle werden die Mittel von einzelnen betroffenen Adressen an separate Zieladressen gesendet. Gleichzeitig werden die Transaktionen gebündelt, im Durchschnitt etwa sechs Opfer pro Sweep.

Die Mittel wurden in Pay-to-Witness-Script-Hash-Ausgänge verschoben, die komplexere Bedingungen wie Multisignatur oder Zeitsperren unterstützen können. In früheren Wellen wurden häufiger einfachere, mit einem einzelnen Schlüssel verbundene Ausgänge verwendet.

In der neuen Welle überprüfte der Angreifer nur den Standard-Derivationspfad, also den üblichen Zweig des Schlüsselbaums, den ein Wallet normalerweise zuerst kontrolliert.

{{< support1 >}}

## Derselbe Angreifer oder mehrere unabhängige Betreiber?

Die veränderte Vorgehensweise könnte bedeuten, dass derselbe Angreifer sein System angepasst hat, nachdem seine ersten Adressen öffentlich identifiziert worden waren.

Ebenso ist möglich, dass ein zweiter Angreifer unabhängig denselben anfälligen Schlüsselraum durchsucht.

Die Blockchain allein kann nicht zeigen, ob alle drei Wellen miteinander koordiniert waren. Galaxy Research geht davon aus, dass jede einzelne Welle wahrscheinlich von jeweils einem Betreiber durchgeführt wurde, verbindet bislang aber nicht alle drei Wellen mit derselben Person oder Gruppe.

Die jüngste Taktikänderung zeigt jedoch, dass die Personen hinter der Ausnutzung der Schwachstelle öffentliche Analysen verfolgen und ihr Vorgehen beim Verschieben der gestohlenen Mittel anpassen.

## Wie ist der Diebstahl ohne Zugriff auf das Gerät möglich?

Das Problem entstand nicht dadurch, dass Angreifer Coldcard-Geräte physisch stahlen, sich mit ihnen verbanden oder Seed-Phrasen der Nutzer über das Internet abfingen.

Die Schwachstelle lag in der Erzeugung der Zufallsdaten, die zur Erstellung des Seeds benötigt werden.

Eine Änderung während einer Firmware-Migration im März 2021 führte dazu, dass die Seed-Erzeugung in bestimmten Versionen einen softwarebasierten Zufallszahlengenerator statt einer dafür vorgesehenen Hardwarequelle nutzte.

Bei betroffenen Mk2- und Mk3-Geräten könnte der effektiv durchsuchbare Raum nach einer vorläufigen Einschätzung des Herstellers nur etwa 40 Bit umfasst haben, statt des erwarteten Sicherheitsniveaus.

Spätere Modelle wie Mk4, Q und Mk5 verfügten über zusätzliche Entropie aus Sicherheitselementen. Der Hersteller schätzte jedoch, dass bestimmte Seeds nur ungefähr 72 Bit Entropie erreicht haben könnten, weiterhin weniger als die vorgesehenen 128 Bit.

{{< support2 >}}

## Der private Schlüssel kann offline rekonstruiert werden

Die geringere Entropie begrenzte die Zahl möglicher Seeds, die die anfällige Firmware erzeugen konnte.

Ein Angreifer mit ausreichender Rechenleistung und Kenntnis der Schwachstelle kann dadurch mögliche Seeds offline rekonstruieren, daraus private Schlüssel ableiten und prüfen, ob sich auf den zugehörigen Bitcoin-Adressen Guthaben befinden.

Der Angreifer muss das Coldcard-Gerät daher nicht berühren, den PIN des Nutzers nicht kennen und auch keine physische Kopie der Seed-Phrase besitzen.

Das Gerät kann die ganze Zeit ausgeschaltet und vom Internet getrennt bleiben, während die Mittel dennoch gefährdet sind, weil sich der Angriff nicht gegen die Kommunikation mit dem Gerät richtet.

Angegriffen wird der vorhersehbare Raum möglicher privater Schlüssel.

## Ein Firmware-Update rettet keinen alten Seed

Coinkite veröffentlichte korrigierte Firmwareversionen für die betroffenen Modelle und warnte Nutzer davor, einen neuen Seed zu erzeugen, bevor das passende Update installiert wurde.

Ein Firmware-Update kann jedoch keinen Seed reparieren, der bereits mit einer anfälligen Version erzeugt wurde.

Nutzer müssen:

* die korrigierte Firmware installieren
* einen vollständig neuen Seed erzeugen
* die neue Sicherung sorgfältig notieren und überprüfen
* die neue Adresse auf dem Gerätedisplay kontrollieren
* zunächst eine kleine Testtransaktion senden
* erst nach erfolgreicher Prüfung die restlichen Mittel verschieben

Coinkite warnt Nutzer davor, bei der Migration zu überstürzen, weil Fehler beim Abschreiben des Seeds, bei der Adressprüfung oder beim Senden der Mittel ein zusätzliches und unmittelbareres Verlustrisiko schaffen können.

{{< support1 >}}

## Welche Modelle und Versionen können betroffen sein?

Nach dem Sicherheitshinweis des Herstellers betrifft das Problem Seeds, die auf Mk2- und Mk3-Geräten mit Firmwareversionen von 4.0.1 bis 4.1.9 erzeugt wurden.

Betroffen sein können auch Seeds, die auf Mk4-, Mk5- und Q-Geräten vor der Veröffentlichung der korrigierten Firmwareversionen für das jeweilige Modell und den jeweiligen Release-Zweig erzeugt wurden.

Zu den vom Hersteller genannten korrigierten Versionen gehören:

* Mk2 und Mk3: Version 4.2.0 oder neuer
* Mk4 und Mk5 Standard: Version 5.6.0 oder neuer
* Q Standard: Version 1.5.0Q oder neuer
* Mk4 und Mk5 Edge: Version 6.6.0X oder neuer
* Q Edge: Version 6.6.0QX oder neuer

TAPSIGNER, OPENDIME und SATSCARD sind nicht betroffen, da sie andere Codebasen verwenden.

Nutzer sollten nicht davon ausgehen, sicher zu sein, nur weil sie ihr Gerät nach der Warnung aktualisiert haben. Entscheidend ist, mit welcher Firmwareversion der bestehende Seed ursprünglich erzeugt wurde.

## Würfelwürfe und eine starke Passphrase können das Risiko senken

Coinkite erklärt, dass ein Seed möglicherweise nicht allein durch diese RNG-Schwachstelle gefährdet ist, wenn der Nutzer bei der ursprünglichen Seed-Erzeugung mindestens 50 faire, unabhängige und private Würfelwürfe hinzugefügt hat.

Diese manuell hinzugefügte Entropie vergrößert den Raum möglicher Seeds, den ein Angreifer durchsuchen müsste.

Auch eine starke und einzigartige BIP-39-Passphrase schafft eine zusätzliche Hürde.

Eine kurze, gewöhnliche, wiederverwendete oder vorhersehbare Passphrase bietet jedoch keinen ausreichenden Schutz. Die Passphrase ist außerdem nicht dasselbe wie der PIN, mit dem das Coldcard-Gerät entsperrt wird.

Selbst Nutzern mit einer starken Passphrase wird die Migration zu einem vollständig neuen Seed empfohlen, weil die Passphrase nur die unmittelbare Gefährdung reduziert. Sie repariert nicht den anfälligen Seed, aus dem die Adressen abgeleitet wurden.

{{< support2 >}}

## Nutzer schicken Bitcoin zurück an Börsen

Der Vorfall führte zu einem Verhalten, das dem nach dem Zusammenbruch von FTX beobachteten Muster entgegengesetzt ist.

Nach dem Kollaps der zentralisierten Börse zogen Nutzer Kryptowährungen massenhaft auf private Wallets und Hardware-Geräte ab.

Nun schicken einige Bitcoin-Besitzer ihre Mittel zurück an Börsen, weil sie diese vorübergehend als sicherer ansehen als möglicherweise betroffene Coldcard-Adressen.

Daten von CryptoQuant zeigten einen starken Anstieg kleinerer Bitcoin-Transfers und Einzahlungen auf Börsen. Ein Teil dieser Transaktionen könnte von Nutzern stammen, die ihre Mittel auf neue, sicher erzeugte Wallets verschieben, während andere sie vorübergehend an zentralisierte Plattformen senden.

Das bedeutet nicht, dass zentralisierte Börsen grundsätzlich sicherer sind als Self-Custody.

Der Vorfall zeigt, dass Sicherheit nicht nur davon abhängt, ob ein privater Schlüssel offline gespeichert wird, sondern auch davon, ob der Seed, aus dem der Schlüssel entstand, mit ausreichend hochwertiger Zufälligkeit erzeugt wurde.

## Wo befinden sich die gestohlenen Bitcoin jetzt?

Nach den bisherigen Blockchain-Analysen befindet sich der größte Teil der gestohlenen Bitcoin weiterhin im Bitcoin-Netzwerk auf Adressen, die von den Angreifern kontrolliert werden.

In den ersten Wellen wurde ein Teil der Mittel auf eine kleinere Zahl von Adressen konsolidiert.

In der dritten Welle wurden die Mittel auf eine größere Zahl separater Zieladressen verteilt. Dadurch ist es schwieriger, sie als einen einzigen großen Saldo darzustellen und eindeutig mit den früheren Wellen zu verbinden.

Es gibt keine Bestätigung dafür, dass die gestohlenen BTC direkt an eine identifizierte zentralisierte Börse geschickt, in Fiatgeld umgewandelt oder gegen ETH getauscht und anschließend über Tornado Cash bewegt wurden.

Native Bitcoin können nicht direkt durch Tornado Cash geschickt werden, weil das Protokoll nicht auf dem Bitcoin-Netzwerk funktioniert. Der Angreifer müsste BTC zunächst in einen Vermögenswert auf einer unterstützten EVM-Blockchain umwandeln. Dabei würden zusätzliche Blockchain-Spuren und potenzielle Stellen für Identifizierung oder Einfrieren der Mittel entstehen.

{{< support1 >}}

## Ein Air-Gap schützt nicht vor einem schwachen Seed

Coldcard-Geräte sind dafür bekannt, ohne direkte Internetverbindung verwendet werden zu können.

Ein Air-Gap kann das Risiko von Angriffen während der Kommunikation, der Verbindung mit einem Computer und der Signierung von Transaktionen reduzieren.

Er kann Mittel jedoch nicht schützen, wenn der private Schlüssel aus einem vorhersehbaren Seed abgeleitet wurde.

In diesem Fall kann das Gerät vollständig offline bleiben, während der Angreifer dennoch auf die Mittel zugreift, weil er nicht das Gerät selbst angreift. Stattdessen durchsucht er den begrenzten Satz von Schlüsseln, den die anfällige Firmware erzeugt haben könnte.

Das macht den Vorfall zu einer wichtigen Warnung für die gesamte Hardware-Wallet-Branche.

Sicherheit hängt nicht nur vom physischen Schutz des Geräts, von Sicherheitselementen, einem PIN und einem Air-Gap ab. Die Grundlage bleibt eine hochwertige und tatsächlich unvorhersehbare Entropie bei der Erzeugung des privaten Schlüssels.

## Der Angriff weitete sich auf kleinere Wallets aus

Der Coldcard-Vorfall entwickelte sich von einem einzigen schnellen Angriff zu einer mehrtägigen und systematischen Leerung Tausender Bitcoin-Adressen.

Die bislang identifizierten Verluste stiegen auf rund 1.367 BTC, fast 89 Millionen Dollar und 4.585 betroffene Adressen.

Die dritte Welle zeigt, dass die Angreifer nicht mehr nur große Wallets ins Visier nehmen. Während die größten Beträge bereits abgezogen werden, setzt sich die Suche bei Adressen mit kleineren Guthaben fort.

Nutzer sollten daher nicht davon ausgehen, sicher zu sein, nur weil sich auf einer möglicherweise anfälligen Adresse kein großer Bitcoin-Betrag befindet.

Der wichtigste Schritt besteht nicht nur darin, die Firmware zu aktualisieren, sondern auf einem korrigierten Gerät einen vollständig neuen Seed zu erzeugen und die Mittel auf Adressen zu übertragen, die aus diesem neuen Seed abgeleitet wurden.

## Unsere Einschätzung

* Der Coldcard-Angriff weitete sich auf mindestens 4.585 Bitcoin-Adressen aus.
* Die geschätzten Verluste stiegen auf rund 1.367 BTC beziehungsweise fast 89 Millionen Dollar.
* Die dritte Welle traf weitere 1.912 Adressen und entwendete rund 208 BTC.
* Die Angreifer zielen inzwischen auch auf kleinere Wallets mit deutlich geringeren durchschnittlichen Guthaben.
* Die Verwendung separater Zieladressen und die Bündelung von Opfern erschweren die Nachverfolgung.
* Es ist nicht bestätigt, ob dieselbe Person oder Gruppe hinter allen drei Wellen steht.
* Der Angriff erfordert weder physischen Zugriff auf das Coldcard-Gerät noch Kenntnis des PINs.
* Die reduzierte Entropie ermöglichte die Offline-Suche nach möglichen Seeds und privaten Schlüsseln.
* Ein Firmware-Update verhindert die Erzeugung neuer anfälliger Seeds, repariert aber keinen bereits bestehenden Seed.
* Betroffene Nutzer müssen auf korrigierter Firmware einen neuen Seed erzeugen und ihre Mittel verschieben.
* Eine starke BIP-39-Passphrase und manuell hinzugefügte Entropie können das Risiko verringern, ändern aber nicht die offizielle Empfehlung zur Migration.
* Der größte Teil der gestohlenen Bitcoin befindet sich nach bisherigen Analysen weiterhin im Bitcoin-Netzwerk.
* Gestohlene native BTC können nicht direkt durch Tornado Cash geschickt werden.
* Ein Air-Gapped-Wallet ist nicht sicher, wenn der Seed, aus dem die privaten Schlüssel abgeleitet wurden, vorhersehbar war.
* Die endgültigen Zahlen könnten weiter steigen, da die Blockchain-Analyse fortgesetzt wird.

**Disclaimer:** Dieser Artikel dient ausschließlich Informations- und Bildungszwecken und stellt keine Finanz-, Anlage- oder Sicherheitsberatung dar. Nutzer, die betroffen sein könnten, sollten den offiziellen Sicherheitshinweis des Herstellers sorgfältig prüfen und ihre Seed-Phrase oder Passphrase niemals auf Webseiten, in Formularen oder auf nicht vertrauenswürdigen Geräten eingeben.

In Zusammenarbeit mit KI.
