---
title: "Ein Hardware-Wallet kann offline und trotzdem anfällig sein"
slug: "hardware-wallet-kann-offline-und-trotzdem-anfaellig-sein"
date: 2026-08-06T06:00:00+02:00
category: "crypto"
translationKey: "hardware-wallet-offline-ipak-ranjiv-2026-08-06"
source: "Öffentlich zugängliche Dokumentation von Hardware-Wallet-Herstellern und Sicherheitshinweise"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/informative/Hardware-wallet-risks.png"
featured_image: "/images/informative/Hardware-wallet-risks.png"
image: "/images/informative/Hardware-wallet-risks.png"
thumbnail: "/images/informative/Hardware-wallet-risks.png"
image_alt: "Ein Hardware-Wallet kann offline bleiben und dennoch durch einen schwachen Seed, anfällige Firmware oder menschliche Fehler gefährdet sein"
image_credit: "Metaadvisor.eu – Symbolbild"
tags: ["Hardware-Wallet", "Krypto-Sicherheit", "Offline-Wallet", "Air-Gapped-Wallet", "Seed-Phrase", "privater Schlüssel", "Firmware", "Self-Custody", "Passphrase", "PIN", "Multisig", "Phishing", "Krypto-Wallet", "Sicherheitskopie", "Risikomanagement"]
description: "Ein Hardware-Wallet kann das Risiko eines Fernangriffs deutlich reduzieren. Offline- und Air-Gapped-Betrieb schützen jedoch nicht vor schwachen Seeds, anfälliger Firmware und menschlichen Fehlern."
summary: "Ein privater Schlüssel kann vollständig offline bleiben, während die Mittel dennoch gefährdet sind. Die Sicherheit eines Hardware-Wallets hängt von der Seed-Erzeugung, der Firmware, der Transaktionsprüfung, dem Schutz der Sicherheitskopie und dem Verhalten des Nutzers ab."
---

*Das Bild ist symbolisch.*

# Ein Hardware-Wallet kann offline und trotzdem anfällig sein

Ein Hardware-Wallet gilt häufig als eine der sichersten Möglichkeiten zur Aufbewahrung von Kryptowährungen, weil die privaten Schlüssel außerhalb eines mit dem Internet verbundenen Computers oder Mobiltelefons bleiben. Einige Geräte können vollständig air-gapped verwendet werden, ohne USB-Verbindung und ohne direkte Internetkommunikation. Transaktionen werden dabei über eine Speicherkarte, einen QR-Code oder einen anderen getrennten Kanal übertragen.

Ein solcher Aufbau verringert die Möglichkeit eines Fernangriffs erheblich, beseitigt jedoch nicht alle Risiken. Ein Offline-Gerät kann anfällig sein, wenn der Seed vorhersehbar erzeugt wurde, die Firmware einen schwerwiegenden Fehler enthält, das Display falsche Informationen anzeigt oder die Sicherheitskopie unzureichend geschützt ist.

Jüngste Sicherheitsvorfälle haben gezeigt, wie wichtig diese Unterscheidung ist. Ein Gerät kann dauerhaft vom Internet getrennt bleiben und die Mittel können dennoch gefährdet sein, wenn die privaten Schlüssel aus einem Seed mit unzureichender Zufälligkeit entstanden sind.

## Was bedeutet es tatsächlich, wenn ein Wallet offline ist?

Wenn ein Hardware-Wallet als offline bezeichnet wird, bedeutet das normalerweise, dass der private Schlüssel das Gerät nicht verlässt und das Gerät nicht dauerhaft mit dem Internet verbunden ist. Der Nutzer erstellt auf einem Computer oder Smartphone eine unsignierte Transaktion, überträgt sie auf das Hardware-Wallet, überprüft die Angaben auf dessen Display und bestätigt die Signatur physisch.

Die signierte Transaktion wird anschließend an ein mit dem Internet verbundenes Gerät zurückgegeben und an die Blockchain gesendet. Im Idealfall kann selbst ein infizierter Computer den privaten Schlüssel nicht direkt aus dem Hardware-Wallet auslesen.

Der Computer kann dennoch versuchen, die Empfängeradresse zu verändern, falsche Angaben darzustellen oder den Nutzer dazu zu bringen, etwas anderes zu signieren als ursprünglich beabsichtigt. Ein Hardware-Wallet beseitigt daher nicht die Notwendigkeit, eine Transaktion zu prüfen. Es trennt lediglich den privaten Schlüssel vom Gerät, das dem Internet ausgesetzt ist.

## Ein Air-Gap reduziert das Risiko, beseitigt es aber nicht

Ein Air-Gapped-Wallet besitzt keine direkte Datenverbindung zu einem Computer oder zum Internet. Anstelle einer gewöhnlichen USB-Verbindung kann es QR-Codes, eine microSD-Karte, eine Kamera oder eine andere getrennte Übertragungsmethode verwenden.

Dadurch sinkt die Wahrscheinlichkeit, dass Schadsoftware auf dem Computer direkt mit dem Wallet kommuniziert oder eine Schwachstelle im Kommunikationsprotokoll ausnutzt. Ein Air-Gap schützt jedoch nur vor bestimmten Angriffstypen.

Er schützt nicht vor einem schwach erzeugten Seed, kompromittierter Firmware, einem physisch manipulierten Gerät, einer falsch dargestellten Adresse auf dem Display, dem Diebstahl der Seed-Phrase oder einer schädlichen Transaktion, die der Nutzer selbst bestätigt.

Offline bedeutet deshalb nicht automatisch vollständig sicher. Es bedeutet lediglich, dass ein wichtiger Angriffsweg deutlich eingeschränkt ist.

{{< support1 >}}

## Das größte Problem kann vor der ersten Transaktion entstehen

Die Sicherheit jedes Krypto-Wallets beginnt im Moment der Seed-Erzeugung. Die Seed-Phrase ist die Grundlage, aus der private Schlüssel und Adressen abgeleitet werden. Ist der Seed ausreichend zufällig, kann ein Angreifer ihn durch das Durchsuchen möglicher Kombinationen praktisch nicht erraten.

Problematisch wird es, wenn ein Gerät einen fehlerhaften oder vorhersehbaren Zufallszahlengenerator verwendet. Dann kann die Zahl möglicher Seeds erheblich kleiner sein, als der Nutzer erwartet.

Der Angreifer muss das Gerät in diesem Fall weder hacken noch stehlen oder mit dem Internet verbinden. Er kann auf seinem eigenen Computer mögliche Seeds erzeugen, daraus private Schlüssel ableiten und prüfen, ob die zugehörigen Blockchain-Adressen Guthaben enthalten.

Findet er eine Übereinstimmung, kann er eine Transaktion signieren, ohne jemals mit dem ursprünglichen Hardware-Wallet zu kommunizieren. Das Gerät des Opfers kann die ganze Zeit in einem Tresor liegen. War der Seed vorhersehbar, können die Mittel dennoch gestohlen werden.

## Die Firmware gehört zum Sicherheitsmodell

Ein Hardware-Wallet ist nicht nur ein physisches Gerät. Seine Sicherheit hängt auch von der Firmware ab, also der Software, die die Erzeugung von Schlüsseln, die Anzeige von Adressen, die Signierung von Transaktionen und die Kommunikation mit anderen Geräten steuert.

Ein Fehler in der Firmware kann die Entropiequelle schwächen, einen Betrag oder eine Adresse falsch darstellen, eine fehlerhafte Verarbeitung von Transaktionen ermöglichen oder einen physischen beziehungsweise entfernten Angriff begünstigen.

Deshalb ist es wichtig, Firmware nur aus offiziellen Quellen zu beziehen und, wenn der Hersteller dies ermöglicht, die digitale Signatur zu überprüfen.

Selbst die neueste Firmware kann jedoch nicht immer korrigieren, was zuvor geschehen ist. Wurde ein bestehender Seed mit einer anfälligen Version erzeugt, kann ein späteres Update die Erstellung neuer schwacher Seeds verhindern, dem alten Seed aber keine verlorene Entropie nachträglich hinzufügen.

In einer solchen Situation muss auf dem korrigierten Gerät ein vollständig neuer Seed erzeugt und das Guthaben auf neue Adressen verschoben werden.

{{< support2 >}}

## Das Display des Geräts ist wichtiger als die Anzeige am Computer

Einer der wichtigsten Vorteile eines Hardware-Wallets ist die Möglichkeit, eine Transaktion unabhängig auf dem eigenen Display des Geräts zu überprüfen.

Der Computer kann eine Adresse anzeigen, während Schadsoftware im Hintergrund eine andere vorbereitet. Deshalb sollte sich der Nutzer nicht ausschließlich auf die Informationen in der Anwendung auf dem Computer oder Smartphone verlassen.

Vor der Bestätigung sollten auf dem Display des Wallets die Empfängeradresse, der Betrag, das Netzwerk, die Gebühr und die Art der Transaktion geprüft werden. Bei DeFi-Anwendungen und Token sollte zusätzlich kontrolliert werden, ob einem Smart Contract eine Berechtigung zum Ausgeben von Mitteln erteilt wird.

Zeigt das Gerät nicht genügend Informationen an, kann der Nutzer eine Transaktion signieren, deren tatsächliche Wirkung er nicht versteht. Das ist besonders gefährlich bei komplexeren Smart-Contract-Aktionen, bei denen eine einzige Signatur eine unbegrenzte Token-Freigabe oder dauerhafte Kontrolle über das Wallet ermöglichen kann.

## Ein Hardware-Wallet weiß nicht, was der Nutzer beabsichtigt

Ein Hardware-Wallet kann prüfen, ob eine Transaktion technisch korrekt mit dem privaten Schlüssel signiert wurde. Es kann jedoch nicht immer erkennen, ob sie dem tatsächlichen Willen des Nutzers entspricht.

Bestätigt der Besitzer eine gefälschte Adresse, einen schädlichen Smart Contract, eine unbegrenzte Token-Freigabe oder eine betrügerische Nachricht, kann das Gerät alles technisch korrekt signieren.

In einer solchen Situation wurde der private Schlüssel nicht gestohlen, die Firmware ist möglicherweise nicht anfällig und der Air-Gap funktioniert einwandfrei. Die Mittel können dennoch verloren gehen, weil der Nutzer die schädliche Handlung selbst genehmigt hat.

Deshalb bleiben Phishing und die Manipulation des Nutzers selbst für Besitzer von Hardware-Wallets eine ernsthafte Bedrohung.

{{< support1 >}}

## Die Seed-Phrase bleibt der wichtigste Angriffspunkt

Selbst das hochwertigste Gerät kann keinen Seed schützen, den der Nutzer fotografiert, in einer Cloud gespeichert, per E-Mail verschickt oder auf einer gefälschten Webseite eingegeben hat.

Wer die Seed-Phrase besitzt, kann das Wallet in der Regel auf einem anderen Gerät wiederherstellen und die Mittel übernehmen. Deshalb sollte ein Seed weder fotografiert noch in einer gewöhnlichen Textdatei gespeichert, per Nachricht oder E-Mail verschickt oder in ein Online-Formular eingegeben werden.

Besonders gefährlich sind gefälschte Webseiten und angebliche Support-Mitarbeiter, die zur „Überprüfung des Wallets“ die Eingabe der Seed-Phrase verlangen. Ein legitimer Herstellersupport sollte niemals nach der vollständigen Seed-Phrase fragen.

Auch die Sicherheitskopie muss vor Feuer, Wasser, Diebstahl und versehentlicher Zerstörung geschützt werden. Eine Papierkopie ist einfach zu verwenden, aber physisch empfindlich. Eine Metallkopie kann widerstandsfähiger sein, muss jedoch ebenfalls verborgen und nur für eine berechtigte Person zugänglich aufbewahrt werden.

## PIN und Passphrase sind nicht dasselbe

Die PIN schützt den Zugang zum physischen Gerät. Wird ein Hardware-Wallet gestohlen, erschwert sie dem Täter den Zugriff und die Signierung von Transaktionen.

Eine Passphrase erfüllt eine andere Funktion. Zusammen mit dem grundlegenden Seed erzeugt sie ein zusätzliches Wallet. Gelangt ein Angreifer an die Seed-Phrase, kennt aber eine starke und einzigartige Passphrase nicht, kann er die in diesem zusätzlichen Wallet gespeicherten Mittel möglicherweise nicht finden.

Eine Passphrase erhöht jedoch auch die Verantwortung des Nutzers. Wird sie vergessen oder falsch notiert, können die Mittel nicht wiederhergestellt werden. Jede abweichende Zeichenfolge kann ein vollständig anderes, gültiges, aber leeres Wallet öffnen.

Eine kurze und vorhersehbare Passphrase kann außerdem durch automatisierte Versuche erraten werden. Deshalb ist sie nur sinnvoll, wenn sie ausreichend stark und sicher aufbewahrt wird.

{{< support2 >}}

## Das Risiko beginnt bereits beim Kauf des Geräts

Ein Hardware-Wallet sollte direkt beim Hersteller oder bei einem vertrauenswürdigen autorisierten Händler gekauft werden. Ein über eine unbekannte Anzeige oder einen Wiederverkäufer erworbenes Gerät kann geöffnet, manipuliert, durch eine Kopie ersetzt oder bereits vorkonfiguriert worden sein.

Besonders gefährlich ist ein Gerät, das mit einer bereits ausgedruckten Seed-Phrase geliefert wird. Den echten Seed sollte der Nutzer selbst auf dem Gerät erzeugen, nachdem die Verpackung geprüft und die offizielle Firmware installiert wurde.

Eine vorbereitete Seed-Karte kann bedeuten, dass jemand bereits eine Kopie der privaten Schlüssel besitzt und lediglich darauf wartet, dass der Nutzer Geld einzahlt.

Der Nutzer sollte außerdem prüfen, ob die Verpackung unbeschädigt erscheint, ob das Gerät von der offiziellen Anwendung erkannt wird und ob der Hersteller ein Verfahren zur Überprüfung der Geräteauthentizität bereitstellt.

## Physische Sicherheit bleibt wichtig

Nicht alle Angriffe erfolgen digital. Jemand kann versuchen, das Gerät zu stehlen, eine Papier- oder Metallkopie des Seeds zu finden, die PIN mit einer Kamera aufzuzeichnen oder das Wallet physisch auszutauschen.

Bei größeren Beträgen besteht zusätzlich das Risiko der Nötigung des Besitzers. Deshalb endet Sicherheit nicht bei den technischen Eigenschaften des Geräts.

Wichtig ist, wo der Seed aufbewahrt wird, ob andere Personen wissen, dass der Besitzer größere Mengen an Kryptowährungen hält, und ob ein Plan für Wiederherstellung, Vererbung oder Notfälle existiert.

Die Sicherheitskopie und das Gerät sollten nicht am selben Ort aufbewahrt werden, wenn ein einzelner Diebstahl, Brand oder Wasserschaden beide gleichzeitig zerstören könnte.

{{< support1 >}}

## Ein einziges Wallet ist nicht immer für alles geeignet

Der Nutzer kann den möglichen Schaden begrenzen, indem er nicht sämtliche Mittel unter einem einzigen Seed hält. Ein kleineres Hot Wallet kann für alltägliche Transaktionen, ein separates Wallet für DeFi und ein Hardware-Wallet für die langfristige Aufbewahrung verwendet werden.

Für größere Beträge können getrennte Wallets oder eine Multisig-Konfiguration eingesetzt werden, bei der ein einzelner Schlüssel nicht ausreicht, um Mittel zu übertragen.

Eine solche Trennung begrenzt die Folgen, wenn ein Wallet kompromittiert wird. Mehr Wallets bedeuten jedoch auch mehr Seeds, Sicherheitskopien, Adressen und Möglichkeiten für menschliche Fehler.

Das Sicherheitsmodell muss stark genug, aber zugleich so einfach sein, dass der Nutzer es korrekt verwalten kann.

## Multisig reduziert die Abhängigkeit von einem Schlüssel

Bei einem normalen Wallet kontrolliert ein Seed in der Regel alle Mittel. Bei einer Multisig-Konfiguration sind für eine Transaktion zwei oder mehr verschiedene Signaturen erforderlich.

In einem 2-von-3-Modell existieren drei Schlüssel, von denen beliebige zwei zum Senden der Mittel benötigt werden. Ist ein Hardware-Wallet anfällig oder wird ein Seed gestohlen, kann der Angreifer die Mittel dennoch nicht allein bewegen.

Multisig kann die Sicherheit erheblich erhöhen, bringt aber zusätzliche Komplexität mit sich. Die Schlüssel müssen getrennt aufbewahrt, die Konfigurationsdaten gesichert und der Wiederherstellungsprozess vollständig verstanden werden.

Für kleinere Beträge kann ein solches System unnötig kompliziert sein. Für Geschäftsreserven oder größere Summen kann es jedoch einen wichtigen zusätzlichen Schutz bieten.

{{< support2 >}}

## Sicherheit ist keine einzelne Funktion

Keine einzelne Bezeichnung kann die Sicherheit eines Hardware-Wallets garantieren. Es reicht nicht aus, dass ein Gerät offline, air-gapped, Open Source, Bitcoin-only oder mit einem Secure Element ausgestattet ist.

Jede dieser Eigenschaften löst nur einen Teil des Problems.

Die tatsächliche Sicherheit hängt von der gesamten Kette ab: der Herstellung des Geräts, der Bezugsquelle, der Qualität der Firmware, der Seed-Erzeugung, dem Schutz der Sicherheitskopie, der Kontrolle der Angaben auf dem Display, dem Signierungsverfahren, dem Verhalten des Nutzers und der Beobachtung offizieller Sicherheitshinweise des Herstellers.

Eine einzige schwerwiegende Schwachstelle kann das gesamte System gefährden.

Ein Hardware-Wallet kann ein wichtiger Bestandteil des Sicherheitsmodells sein, ersetzt aber nicht das Verständnis der Transaktion, die Kontrolle der Adresse und den sorgfältigen Umgang mit dem Seed.

## Was kann ein Nutzer praktisch tun?

Ein Nutzer sollte sein Hardware-Wallet aus einer vertrauenswürdigen Quelle beziehen, den Seed selbst erzeugen, offizielle Firmware installieren und vor jeder Transaktion Adresse und Betrag auf dem Display des Geräts überprüfen.

Bei größeren Überweisungen empfiehlt es sich, zunächst einen kleinen Testbetrag zu senden. Das Wallet für die langfristige Aufbewahrung sollte von jenem getrennt werden, das für DeFi-Anwendungen und alltägliche Transaktionen verwendet wird.

Wichtig ist außerdem, offizielle Sicherheitshinweise des Herstellers zu verfolgen und zu wissen, mit welcher Firmwareversion der bestehende Seed ursprünglich erzeugt wurde. Für größere Beträge können eine starke Passphrase oder Multisig in Betracht gezogen werden, jedoch nur, wenn der Nutzer den Wiederherstellungsprozess versteht.

Das sicherste Wallet ist nicht unbedingt jenes mit den meisten Funktionen, sondern jenes, dessen Sicherheitsmodell der Nutzer versteht und konsequent umsetzen kann.

## Unsere Einschätzung

* Ein Hardware-Wallet reduziert deutlich das Risiko, dass ein privater Schlüssel von einem mit dem Internet verbundenen Computer oder Smartphone gestohlen wird.
* Ein Air-Gapped-Betrieb schränkt die direkte Kommunikation mit einem infizierten Gerät zusätzlich ein.
* Offline-Betrieb ist keine Garantie für vollständige Sicherheit.
* Ein vorhersehbar erzeugter Seed kann ohne physischen Zugriff auf das Gerät rekonstruiert werden.
* Anfällige Firmware kann die Schlüsselerzeugung, die Transaktionsanzeige oder den Signierungsprozess gefährden.
* Ein späteres Firmware-Update kann einen bereits mit einer anfälligen Version erzeugten Seed nicht unbedingt reparieren.
* Das Display des Geräts dient der unabhängigen Überprüfung von Adresse, Betrag und Transaktionstyp.
* Ein Hardware-Wallet kann eine schädliche Aktion technisch korrekt signieren, wenn der Nutzer sie bestätigt.
* Die Seed-Phrase bleibt der empfindlichste Teil des gesamten Sicherheitssystems.
* Die PIN schützt den Zugang zum Gerät, während die Passphrase ein zusätzliches Wallet erzeugt.
* Ein aus einer nicht vertrauenswürdigen Quelle gekauftes Gerät kann manipuliert oder vorkonfiguriert sein.
* Mehrere getrennte Wallets können den möglichen Schaden begrenzen, erhöhen jedoch die operative Komplexität.
* Multisig reduziert die Abhängigkeit von einem einzelnen Gerät oder Seed, erfordert aber sorgfältige Planung.
* Die Sicherheit eines Hardware-Wallets hängt vom gesamten Prozess ab und nicht nur davon, ob das Gerät mit dem Internet verbunden ist.

**Disclaimer:** Dieser Artikel dient ausschließlich Informations- und Bildungszwecken und stellt keine Finanz-, Anlage- oder Sicherheitsberatung dar. Nutzer sollten die offizielle Dokumentation und die Sicherheitshinweise des Herstellers prüfen und ihre Seed-Phrase oder Passphrase niemals auf Webseiten, in Formularen oder auf nicht vertrauenswürdigen Geräten eingeben.

In Zusammenarbeit mit KI.
