---
title: "Chainflip: Validator als Tresorwächter, 12,6 Millionen gestohlen?"
slug: "chainflip-validator-crypto-vault-heist-12-million-2026"
date: "2026-11-24T08:00:00+01:00"
category: "markets"
translationKey: "chainflip-validator-vault-exploit-2026-11-24"
source: "Chainflip Labs; Chainflip Incident Report; The Block"
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/hack/Chainflip-Crypto-Vault-Heist-by-validator.jpg"
featured_image: "/images/hack/Chainflip-Crypto-Vault-Heist-by-validator.jpg"
image: "/images/hack/Chainflip-Crypto-Vault-Heist-by-validator.jpg"
thumbnail: "/images/hack/Chainflip-Crypto-Vault-Heist-by-validator.jpg"
image_alt: "Illustration des Chainflip-Kryptotresors und des Angriffs auf die Validatoren"
image_credit: "Metaadvisor.eu"
tags: ["Chainflip", "Validator", "Crypto Vault", "Crypto Hack", "Bitcoin", "Ethereum", "Tornado Cash", "Blockchain Security"]
description: "Ein Chainflip-Validatorkandidat konnte offenbar Schlüsselanteile erbeuten und Krypto im Wert von 12,6 Millionen Dollar stehlen. Das Netzwerk verfolgt digitale Spuren."
summary: "Der Angreifer wurde nie aktiver Validator, konnte aber über die Netzwerksoftware Schlüsselanteile entwenden. Chainflip hat die Registrierung und einen Server zurückverfolgt."
categories: ["markets"]
---

*Das Titelbild ist eine Illustration.*

**Er meldete sich als Kandidat für eine Art digitalen Tresorwächter an, gehörte aber nie zu den aktiven Validatoren. Am nächsten Morgen verschwanden dennoch Kryptowährungen im Wert von rund 12,6 Millionen US-Dollar aus den Tresoren des Chainflip-Protokolls. Nun erklärt Chainflip, es habe die Tokenkäufe, die Registrierung und sogar den bei der Vorbereitung verwendeten Server zurückverfolgt. Der Angreifer könnte bereits vor dem Diebstahl Spuren hinterlassen haben.**

Am 20. November 2026 registrierte der unbekannte Angreifer ein Validator-Konto bei Chainflip. Dadurch wurde er kein aktiver Verantwortlicher für Kundengelder, erhielt aber die Möglichkeit, mit den Rechnern bestehender Validatoren über das Netzwerk zu kommunizieren. Nach dem vorläufigen Untersuchungsbericht vom 23. November nutzte er genau diesen Zugang, um einen Fehler in der Netzwerksoftware anzugreifen und Teile kryptografischer Schlüssel zu stehlen. Die späteren Abhebungen trugen gültige Signaturen, waren vom Chainflip-Protokoll jedoch niemals genehmigt worden.

## Tresorwächter, die keinen vollständigen Schlüssel besitzen

Ein Validator ist kein Mensch, der Geldscheine bewacht, sondern ein Rechner mit spezieller Software, der an der Arbeit eines Blockchain-Protokolls beteiligt ist. Bei Chainflip verwalten Validatoren gemeinsam die Berechtigung, Transaktionen aus Tresoren zu unterzeichnen, die für den Austausch von Kryptowährungen zwischen verschiedenen Blockchains benötigt werden. Ein einzelner Validator soll diese Gelder nicht allein bewegen können.

Das Prinzip lässt sich mit einem Tresor vergleichen, dessen Schlüssel auf mehrere Wächter verteilt ist. Erst eine ausreichende Zahl von Schlüsselanteilen erlaubt eine gültige Signatur. Das schützt vor einem einzelnen kompromittierten Teilnehmer. Werden aber genügend Anteile auf mehreren Rechnern gestohlen, kann ein Angreifer eine Transaktion unterschreiben, ohne die tatsächliche Zustimmung der Wächter einzuholen. **Nach dem bisherigen Untersuchungsstand wurde nicht die Kryptografie geknackt, sondern die Software angegriffen, die die Schlüsselanteile schützen sollte.**

## Registriert, aber nie aktiver Validator

Die Chronologie von Chainflip nennt den **20. November, 11:00:18 UTC**, als Zeitpunkt der Registrierung. Nur 79 Sekunden zuvor war das Konto mit dem Mindestbetrag von **20.500 FLIP-Token** finanziert worden. Um 11:07:06 UTC wurde eine Peer-to-Peer-Identität registriert. Das Konto gelangte nie in die aktive Validatorengruppe, doch bestehende Knoten akzeptierten Verbindungen, weil neue Kandidaten zur Vorbereitung ihrer Teilnahme mit dem Netzwerk kommunizieren können müssen.

Nach der vorläufigen Analyse wurde über diese Verbindung eine Schwachstelle bei der Speichersicherheit in einer externen Netzwerkbibliothek ausgenutzt. Der Angreifer konnte nach Darstellung von Chainflip Code auf Validatorrechnern ausführen und gespeicherte Schlüsselanteile extrahieren. Mit einer ausreichenden Zahl solcher Anteile wurden Unterschriften außerhalb des normalen Protokolls erstellt. Chainflip weist ausdrücklich darauf hin, dass noch nicht jeder technische Schritt abschließend bestätigt ist.

{{< support1 >}}

## Der erste Abfluss, ein übersehener Alarm und ein weiterer Zugriff

Am **21. November um 06:41:01 UTC** wurden **122,86137042 BTC** aus dem Bitcoin-Tresor entwendet. Acht Minuten später meldete eine automatische Überwachung einen ungewöhnlichen Vorgang. Da dieses System noch getestet wurde und zuvor Fehlalarme produziert hatte, löste die Warnung keine automatische Eskalation aus. Die Bitcoin wurden zwischenzeitlich an eine weitere Adresse weitergeleitet.

Um **07:10:59 UTC** folgte der Ethereum-Tresor: **520,2243399 ETH**, **3.249.631,41 USDC** und **758.141,33 USDT** wurden abgezogen. Die Stablecoins wurden in ETH getauscht; anschließend transferierte der Angreifer insgesamt **2.909 ETH** in Tornado Cash, einen Dienst, der die Nachverfolgung von Blockchain-Transaktionen erschwert. Erst um 07:41 UTC schlug ein Teammitglied Alarm. Bis 08:31 UTC wurden Swaps, Einzahlungen und Auszahlungen angehalten.

Trotz einer ersten Schlüsselrotation blieb der alte kompromittierte Schlüssel für einen Bitcoin-Tresor noch nutzbar. Um **11:24:18 UTC** wurden deshalb weitere **10,48288011 BTC** abgezogen. Insgesamt verlor Chainflip **133,34425053 BTC** sowie die genannten Ethereum-Vermögenswerte und Stablecoins. Der Gegenwert betrug zum Zeitpunkt des Angriffs ungefähr **12,6 Millionen US-Dollar**, nahezu das gesamte damalige Vermögen der betroffenen Tresore.

## Wie Chainflip dem Angreifer bereits folgte

Besonders bemerkenswert ist die öffentliche Botschaft von Chainflip Labs an den Angreifer. Das Unternehmen behauptet, mehrere Vorbereitungsschritte rekonstruiert zu haben: **die Finanzierung über Tornado Cash am 11. November, den Kauf von FLIP-Token, die Registrierung des Validator-Kontos am 20. November sowie den dafür verwendeten Server**. Außerdem seien identifizierende Metadaten zu Konten und genutzten Onlinediensten gesichert worden, die Strafverfolgungsbehörden bei der Feststellung der Identität helfen könnten.

Warum ist die Person dann nicht bereits bekannt? Ein Validator-Konto auf einer Blockchain erfordert nicht notwendigerweise einen amtlichen Namen oder Ausweis. Blockchain-Transaktionen hinterlassen aber nachvollziehbare Adressen und Zeitstempel; zusätzlich können Hostinganbieter Protokolle über Zahlungen oder Zugriffe besitzen. Ob diese Informationen tatsächlich auf eine Person zurückführen, muss erst geklärt werden. **Eine Identifizierung des Angreifers hat Chainflip öffentlich nicht bestätigt.**

Nach Angaben des Unternehmens sind die betroffenen Adressen bei großen Blockchain-Analysefirmen markiert und Abflüsse aus den verwendeten Tornado-Cash-Pools werden beobachtet. Das kann die Verwertung erschweren, garantiert aber weder die Aufklärung noch die Rückgabe des Geldes. Chainflip arbeitet eigenen Angaben zufolge mit Behörden und dem spezialisierten Unternehmen ZeroShadow zusammen.

## Zehn Prozent als Angebot für die Rückgabe

Chainflip Labs bot dem Angreifer an, **10% der entwendeten Vermögenswerte** zu behalten, falls er die übrigen **90%** zurückgibt. In der öffentlichen Nachricht wurden als Rückgabemengen **110,57523337 BTC** und **2.618,1 ETH** sowie Zieladressen angegeben. Eine rechtzeitige Rückgabe sollte von Chainflip Labs als freiwillige White-Hat-Rückführung betrachtet werden; das Unternehmen kündigte an, seine eigenen Anzeigen und Beschwerden zurückzuziehen.

Die Frist endete am **23. November um 18:38 UTC**. Chainflip warnte, dass die registrierten Adressen und die benutzten Dienste eine spätere Identifizierung erleichtern könnten. **In den geprüften offiziellen Mitteilungen ist weder eine Annahme des Angebots noch eine erfolgreiche Rückzahlung nach Ablauf der Frist bestätigt.** Auch der Rückzug einer Anzeige durch ein Unternehmen kann eine unabhängige strafrechtliche Untersuchung nicht automatisch verhindern.

{{< support2 >}}

## Was geschah mit dem Geld, und wann startet das Netzwerk wieder?

Laut dem am 23. November veröffentlichten Bericht lagen die gestohlenen Bitcoin zu diesem Zeitpunkt noch auf zwei identifizierten Adressen. Die Vermögenswerte aus dem Ethereum-Tresor waren in ETH getauscht und zu Tornado Cash transferiert worden. Diese Angaben beschreiben den Stand des Berichts, nicht zwangsläufig die spätere Bewegung der Gelder.

Am 21. November lieferte Chainflip eine gepatchte Softwareversion aus. Am 22. November erfolgte eine weitere Schlüsselrotation. Am **23. November um 11:31 UTC** liefen nach Angaben des Protokolls alle aktiven Validatoren mit der gepatchten Version. Dennoch blieben Swaps, Einzahlungen und Auszahlungen zum Zeitpunkt des Berichts gestoppt. Ein Termin für die Wiederaufnahme war nicht bestätigt. Freie Guthaben von Liquiditätsanbietern auf nicht betroffenen Netzwerken wurden vorsorglich teilweise zurückgesandt.

Für geschädigte Nutzer bleibt die Frage der Entschädigung offen. Chainflip ermittelt die individuellen Verluste und arbeitet an einem Wiederaufbauplan mit möglichen Finanzierungen und Anreizen für Liquiditätsanbieter. **Ein verbindlicher Entschädigungsplan mit Summen und Auszahlungsterminen wurde in den geprüften offiziellen Angaben nicht veröffentlicht.**

## Nicht der erste ernsthafte Vorfall

Bereits im September 2026 betraf ein gesonderter Exploit den Tron-Tresor von Chainflip. Dabei wurde eine andere Schwachstelle in der Verarbeitung von Transaktionsnachrichten ausgenutzt und ein Verlust von etwa **736.000 USDT** verursacht. Es gibt keinen Grund anzunehmen, dass dieselbe Person für beide Angriffe verantwortlich war. Die zwei Vorfälle werfen jedoch Fragen zur Prüfung externer Softwarekomponenten und zur Reaktionsgeschwindigkeit bei Sicherheitswarnungen auf.

## Unsere Einschätzung

- **Kein aktiver Validator:** Der Angreifer registrierte sich als Kandidat, wurde aber nie Teil der aktiven Gruppe. Die Aussage, ein bestätigter aktiver Validator habe gestohlen, wäre falsch.
- **Schlüsselanteile statt gebrochener Kryptografie:** Der vorläufige Befund deutet auf eine Schwachstelle in der Software hin, die die Schlüsselanteile speicherte.
- **Alarm ohne Eskalation:** Der erste Warnhinweis kam acht Minuten nach dem ersten Abfluss, führte jedoch nicht automatisch zur Alarmierung.
- **Spuren, aber kein Name:** Tokenkauf, Registrierung und genutzter Server können Ermittlungsansätze liefern; die Identität ist nicht bestätigt.
- **Zehn-Prozent-Angebot:** Der Ablauf der Rückgabefrist bedeutet nicht, dass eine erfolgreiche Rückführung nachgewiesen ist.
- **Patch ist keine Entschädigung:** Die technischen Schutzmaßnahmen ersetzen nicht die verlorenen Kundengelder.

**Das Paradoxe: Chainflip wollte verhindern, dass ein einzelner Wächter einen Tresor leeren kann. Nach den bisherigen Erkenntnissen musste der Angreifer nicht einmal zum Wächter werden. Er nutzte einen Fehler in der Kommunikation, sammelte Schlüsselanteile und erzeugte Signaturen, denen der Tresor vertraute.** Ausgerechnet die Spuren seiner Registrierung und Vorbereitung könnten ihn nun verraten. Ob die Ermittlungen zu einer Identität und zu einer Rückgabe des Geldes führen, bleibt offen.

**Folgen Sie Metaadvisor.eu für unabhängige Nachrichten und Analysen zu Kryptowährungen, KI, Technologie und Wirtschaft.**

<small style="color:#757575; font-size:12px; font-weight:400; font-style:normal;">In collaboration with AI.</small>

**Quellen:** Chainflip Labs, *Incident Report: Bitcoin and Ethereum Vault Exploit (Part 1)* (23.11.2026); Chainflip Labs, *Message from Chainflip Labs*; Chainflip Labs, *Getting Chainflip Back Up and Running* (15.09.2026); The Block (21.–22.11.2026).

**Hinweis:** Dieser Beitrag beruht auf den bis zum 24. November 2026 überprüften Veröffentlichungen. Die technische Ursache wird noch untersucht; Identität, Entschädigung und Ergebnis des Rückgabeangebots sind öffentlich nicht abschließend bestätigt. Keine Finanz- oder Anlageberatung.
