---
title: "Adresse kopiert — und 50 Millionen Dollar verloren: der größte Krypto-Fehler des Jahres"
slug: "address-poisoning-adresse-kopiert-50-millionen-dollar-verloren"
date: 2025-12-20T12:00:00
category: "crypto"
translationKey: "address_poisoning_50m_loss_20122025"
source: "Cointelegraph, CoinDesk"
source_url: "cointelegraph.com, coindesk.com"
author: "Metaadvisor.eu"
image_url: "/images/Lost-50-mil-usd.png"
featured_image: "/images/Lost-50-mil-usd.png"
image: "/images/Lost-50-mil-usd.png"
thumbnail: "/images/Lost-50-mil-usd.png"
image_alt: "Address-Poisoning-Betrug und Verlust von 50 Millionen Dollar nach dem Kopieren einer Krypto-Adresse"
image_credit: "MetaAdvisor illustration"
tags:
  - bitcoin
  - krypto
  - sicherheit
  - betrug
  - address poisoning
  - usdt
  - ethereum
  - wallet
  - on-chain
  - tornado cash
  - cyberkriminalität
summary: "Eine falsch kopierte Krypto-Adresse reichte aus, um fast 50 Millionen USDT zu verlieren. Der Fall zeigt, wie Address-Poisoning-Angriffe menschliche Gewohnheiten ausnutzen – nicht Schwächen der Blockchain."
---

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter"
     target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Bitget-Bonus bis zu 6200 USDT sichern — jetzt traden
  </a>
</p>

In einem der teuersten individuellen Krypto-Vorfälle dieses Jahres verlor ein Nutzer **fast 50 Millionen USDT**, nachdem er Opfer eines ausgeklügelten *Address-Poisoning*-Betrugs geworden war. Es gab keinen Hack, keinen Diebstahl privater Schlüssel und keinen technischen Fehler der Blockchain. Alles geschah im Rahmen dessen, was viele als „normale“ Nutzung eines Krypto-Wallets betrachten — und genau das macht diesen Fall so gefährlich.

Es handelt sich um einen Angriff, der **menschliches Verhalten** ins Visier nimmt, nicht die Technologie.

## Was genau ist passiert?

Laut On-Chain-Daten zog das Opfer zunächst eine große Menge **USDT (Tether)** von einer Börse ab. Als Sicherheitsmaßnahme wurde **eine kleine Testüberweisung (0,005 USDT)** an eine Adresse gesendet, die als korrekt angesehen wurde. Diese Testtransaktion verlief erfolgreich.

Bevor jedoch der Hauptbetrag gesendet wurde, gelang es den Angreifern, den **Transaktionsverlauf des Wallets zu „vergiften“**. Im Verlauf erschien eine **gefälschte Adresse**, die der echten optisch nahezu identisch war — mit denselben ersten drei und letzten vier Zeichen.

Als der Nutzer später die Adresse aus dem Transaktionsverlauf kopierte, kopierte er unwissentlich **die Adresse des Angreifers** und überwies **rund 49.999.950 USDT**. Die Transaktion war technisch korrekt — und unwiderruflich.

Die Testüberweisung half nicht, da:
- der Test an eine zuvor gespeicherte Adresse ging  
- der Hauptbetrag an eine Adresse gesendet wurde, die **aus dem Transaktionsverlauf kopiert** wurde

Zwei Adressen. Ein Fehler. Ein massiver Verlust.

## Was ist ein Address-Poisoning-Betrug?

*Address Poisoning* ist eine Betrugsmethode, die weder Kryptografie bricht noch die Blockchain kompromittiert. Stattdessen generieren Angreifer **massiv neue Wallet-Adressen**, bis sie solche erhalten, die echten Zieladressen sehr ähnlich sehen — gleicher Anfang und gleiches Ende, aber ein anderer Mittelteil.

Anschließend senden sie **minimale „Dust“-Transaktionen** an potenzielle Opfer. Wallets zeigen diese Transaktionen regulär im Verlauf an, ohne Warnhinweis. Kopiert der Nutzer später eine Adresse aus der „Recent“-Liste, kopiert er möglicherweise **die falsche Adresse**.

Dieser Angriff:
- benötigt keine Malware  
- benötigt keine Phishing-Links  
- hinterlässt keinen technischen Fehler  

Alles passiert innerhalb der normalen Wallet-Bedienoberfläche.

## Blitzschnelle Umwandlung und Verschleierung der Gelder

Nachdem der Angreifer fast **50 Millionen USDT** erhalten hatte, wurden die Gelder rasch weitergeleitet:

- USDT wurde in **DAI**, einen dezentralen Stablecoin, getauscht  
- DAI wurde anschließend in etwa **16.690 ETH** umgewandelt  
- Fast der gesamte Betrag (**ca. 16.680 ETH**) wurde durch **Tornado Cash** geschickt

Auf diese Weise wurde die Herkunft der Gelder effektiv verschleiert und eine Rückverfolgung stark erschwert. Auch wenn Tornado Cash nicht mehr als klassisches Projekt mit öffentlichem Frontend existiert, sind seine **Smart Contracts weiterhin auf der Blockchain aktiv** und können direkt angesprochen werden — was Kriminelle weiterhin nutzen.

### [Tornado Cash: Roman Storm, Lazarus und der umstrittenste Krypto-Prozess des Jahrzehnts](https://metaadvisor.eu/de/news/tornado-cash-roman-storm-lazarus-krypto-prozess/)

## Warum dieser Betrug besonders relevant ist

Dieser Fall zeigt, dass die größten Risiken im Krypto-Bereich heute **nicht mehr technischer Natur**, sondern **operativ** sind. Statt Smart-Contract-Bugs dominieren Angriffe, die ausnutzen:

- menschliche Unachtsamkeit  
- schlechtes UX-Design von Wallets  
- die Gewohnheit, Adressen ohne vollständige Prüfung zu kopieren  

Solche Angriffe können **Verluste in zweistelliger Millionenhöhe** verursachen — selbst bei erfahrenen Nutzern.

## Wie man sich schützt

**Kopiere niemals Wallet-Adressen aus dem Transaktionsverlauf — nutze ein Adressbuch, ENS- bzw. Domain-Adressen und überprüfe immer den Mittelteil der Adresse, nicht nur Anfang und Ende.**

<p style="font-size:0.85em; color:#6b7280; margin-top:18px;">
<strong>Haftungsausschluss:</strong> Dieser Inhalt dient ausschließlich zu Informationszwecken und stellt keine Anlageberatung dar. Kryptowährungen sind volatil und risikobehaftet; triff finanzielle Entscheidungen nur auf Basis eigener Recherche.
</p>
