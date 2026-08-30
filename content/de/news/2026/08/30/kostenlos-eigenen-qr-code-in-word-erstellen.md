---
title: "So erstellen Sie kostenlos Ihren eigenen QR-Code direkt in Word"
slug: "kostenlos-eigenen-qr-code-in-word-erstellen"
date: 2026-08-30T12:30:00+02:00
category: "Tech"
translationKey: "how-to-create-your-own-qr-code-in-microsoft-word-2026-08-30"
source: "Microsoft, Metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/metaadvisor1.png"
featured_image: "/images/metaadvisor1.png"
image: "/images/metaadvisor1.png"
thumbnail: "/images/metaadvisor1.png"
image_alt: "So erstellen Sie kostenlos Ihren eigenen QR-Code direkt in Microsoft Word"
image_credit: "Metaadvisor.eu"
tags: ["Microsoft Word", "QR Code", "QR-Code erstellen", "Microsoft", "Word Tipps", "Word Tricks", "Technologie", "digitale Tools", "DISPLAYBARCODE", "Ctrl F9", "Barcode", "Produktivität", "Office"]
description: "Microsoft Word kann kostenlos einen QR-Code erstellen, ganz ohne zusätzliches Programm oder Online-QR-Generator. Dafür genügt die integrierte DISPLAYBARCODE-Funktion."
summary: "Für einen einfachen QR-Code brauchen Sie keine externe Website. Microsoft Word verfügt über die integrierte DISPLAYBARCODE-Funktion, mit der sich Links, Texte und andere Daten direkt im Dokument in einen QR-Code umwandeln lassen."
---

# Wussten Sie, dass Sie kostenlos Ihren eigenen QR-Code direkt in Microsoft Word erstellen können?

Für die Erstellung eines QR-Codes ist nicht immer ein zusätzliches Programm oder ein Online-QR-Generator erforderlich. **Microsoft Word verfügt über eine integrierte Funktion, mit der sich eine Webadresse, Text oder andere Daten direkt innerhalb eines Dokuments in einen QR-Code umwandeln lassen.**

Die Funktion heißt **DISPLAYBARCODE**. Sobald Sie den richtigen Befehl kennen, dauert der gesamte Vorgang nur wenige Sekunden.

Das kann besonders praktisch für Dokumente, Angebote, Flyer, Anleitungen, Präsentationen oder andere Inhalte sein, bei denen Nutzer mit einem einzigen Scan auf eine Website weitergeleitet werden sollen.

## So erstellen Sie einen QR-Code in Word

Öffnen Sie Microsoft Word und klicken Sie an die Stelle im Dokument, an der der QR-Code erscheinen soll.

Drücken Sie anschließend:

**Ctrl + F9**

Word fügt spezielle Feldklammern ein:

`{ }`

Wichtig ist, dass Sie diese Klammern nicht manuell über die Tastatur eingeben. Mit **Ctrl + F9** erzeugt Word ein spezielles Feld, in dem anschließend der Befehl ausgeführt werden kann.

Innerhalb dieser Klammern wird nun der DISPLAYBARCODE-Befehl eingegeben.

Beispiel für die Website Metaadvisor.eu:

`{ DISPLAYBARCODE "https://metaadvisor.eu" QR \s 100 }`

Markieren Sie anschließend das Feld und drücken Sie **F9**.

Word sollte den Befehl nun in einen QR-Code umwandeln. Falls der QR-Code nicht automatisch erscheint, drücken Sie erneut **F9**, diesmal ohne die Ctrl-Taste.

![So erstellen Sie einen QR-Code in Microsoft Word](/images/informative/how-to-make-qr-code1.png)

## Was bedeutet DISPLAYBARCODE?

DISPLAYBARCODE ist ein Word-Befehl zur Erzeugung verschiedener Barcode-Typen.

Im Beispiel:

`{ DISPLAYBARCODE "https://metaadvisor.eu" QR \s 100 }`

steht der Teil:

`"https://metaadvisor.eu"`

für den Inhalt, der im QR-Code gespeichert wird.

Die Angabe:

`QR`

weist Word an, einen QR-Code zu erstellen.

Der Teil:

`\s 100`

bestimmt dessen Größe.

Die Zahl lässt sich verändern. Ein höherer Wert erzeugt einen größeren QR-Code, ein niedrigerer Wert verkleinert die Darstellung.

{{< support1 >}}

## Ein QR-Code kann mehr als nur einen Weblink enthalten

QR-Codes werden meistens mit Websites verbunden, doch eine URL ist nicht die einzige Art von Inhalt, die darin gespeichert werden kann.

Auch normaler Text kann direkt in einem QR-Code hinterlegt werden.

Zum Beispiel:

`{ DISPLAYBARCODE "Grüße aus Hamburg" QR \s 100 }`

Auch ein deutscher Telefonnummern-Link ist möglich:

`{ DISPLAYBARCODE "tel:+491701234567" QR \s 100 }`

Oder eine E-Mail-Adresse:

`{ DISPLAYBARCODE "mailto:info@example.de" QR \s 100 }`

Wie das Smartphone nach dem Scannen reagiert, hängt vom gespeicherten Inhalt ab. Enthält der QR-Code eine Webadresse, bietet das Gerät normalerweise an, die Website zu öffnen. Bei reinem Text zeigen manche Smartphones den Text direkt an, während andere ihn möglicherweise automatisch als Suchanfrage an eine Suchmaschine weitergeben.

## Wie viel Text passt in einen QR-Code?

Ein QR-Code kann wesentlich mehr Daten enthalten als nur eine kurze URL. Mit zunehmender Textmenge wird der Code allerdings immer dichter.

Das lässt sich auch in Word sehr schnell beobachten.

Ein QR-Code, der lediglich einen kurzen Link enthält, besteht aus vergleichsweise wenigen schwarzen und weißen Feldern. Werden dagegen mehrere Sätze gespeichert, muss Word ein deutlich komplexeres Muster erzeugen.

Das Ergebnis kann ein QR-Code sein, der einen großen Teil der Seite einnimmt.

Die Darstellung lässt sich verkleinern, indem der Wert von `\s` geändert wird, beispielsweise von:

`\s 100`

auf:

`\s 50`

oder noch kleiner.

Ein physisch kleiner QR-Code mit sehr vielen gespeicherten Daten kann allerdings schwieriger zu scannen sein, insbesondere bei schlechter Druckqualität oder wenn er sehr klein auf einem Bildschirm dargestellt wird.

Für längere Inhalte ist es deshalb meist sinnvoller, im QR-Code lediglich den Link zu einer Website zu speichern, statt einen ganzen Artikel direkt in den Code einzubetten.

{{< support2 >}}

## So prüfen Sie, ob der QR-Code funktioniert

Der einfachste Test benötigt keine zusätzliche App.

Richten Sie einfach die Kamera Ihres Smartphones auf den QR-Code.

Enthält der QR-Code einen Weblink, sollte auf dem Bildschirm eine anklickbare Adresse erscheinen.

Das Beispiel aus diesem Artikel führt zu:

`https://metaadvisor.eu`

Bei einzelnen Smartphones kann es vorkommen, dass die verlinkte Seite nach dem Scannen nur kurz geöffnet wird oder der Browser anschließend wieder zur zuvor geöffneten Seite zurückkehrt.

Falls das passiert, tippen Sie direkt nach dem Laden auf die geöffnete Seite oder scannen Sie den QR-Code erneut. Das bedeutet nicht automatisch, dass der QR-Code fehlerhaft ist. Es kann auch daran liegen, wie die Kamera oder der Browser das Scan-Ergebnis verarbeitet.

## Warum hat ein QR-Code nur drei große Quadrate?

Beim ersten Blick auf einen QR-Code kann es so wirken, als würde unten rechts ein großes Quadrat fehlen.

Das ist völlig normal.

Ein standardmäßiger QR-Code besitzt drei große Positionsmarkierungen:

* oben links
* oben rechts
* unten links

Ein viertes großes Quadrat unten rechts ist nicht erforderlich.

Diese Markierungen helfen dem Smartphone dabei, die Ausrichtung des QR-Codes zu erkennen, unabhängig davon, aus welchem Winkel er gescannt wird.

Deshalb sieht ein korrekt erzeugter QR-Code häufig so aus, als würde in einer Ecke etwas fehlen, obwohl genau dieses Muster vorgesehen ist.

## Word kann einen einfachen Online-QR-Generator ersetzen

Für fortgeschrittene QR-Codes gibt es spezialisierte Dienste, die beispielsweise Farben, Logos, Scan-Tracking, dynamische Links oder andere Zusatzfunktionen anbieten.

Für einen einfachen QR-Code, der zu einer Website führt oder einen kurzen Text enthält, kann die integrierte Word-Funktion jedoch vollkommen ausreichen.

Ein weiterer Vorteil: Daten müssen nicht auf einer unbekannten externen Website eingegeben werden, nur um daraus ein QR-Bild zu erzeugen.

Wer ohnehin in Word arbeitet, benötigt im Grunde nur wenige Schritte:

**Ctrl + F9 → DISPLAYBARCODE → F9 → QR-Code.**

Das ist eine jener Word-Funktionen, die seit Jahren im Programm vorhanden sind, von vielen Nutzern aber vermutlich nie entdeckt werden.

## Unser Blick darauf

* **Das Interessanteste an dieser Funktion ist nicht der QR-Code selbst, sondern dass für einen einfachen QR-Code kein zusätzlicher Online-Dienst benötigt wird.**
* **Ein Word-QR-Code kann einen Weblink, Text, eine E-Mail-Adresse oder Telefonnummer enthalten**, wobei das Verhalten nach dem Scannen davon abhängt, wie das Smartphone den Inhalt interpretiert.
* **Je mehr Text im QR-Code gespeichert wird, desto komplexer und dichter wird das Muster.** Deshalb ist es nicht immer sinnvoll, große Textmengen direkt darin unterzubringen.
* **Für Webartikel und andere längere Inhalte ist es in der Regel besser, lediglich die URL im QR-Code zu speichern.**
* **Wenn es so aussieht, als würde unten rechts ein großes Quadrat fehlen, ist das normal.** Ein Standard-QR-Code verwendet drei große Positionsmarkierungen.
* **DISPLAYBARCODE zeigt gut, wie viele praktische Word-Funktionen fast unsichtbar bleiben, bis jemand zufällig den richtigen Befehl entdeckt.**

**Folgen Sie Metaadvisor.eu für weitere praktische Tech-Tipps, AI-Tools, digitale Tricks, Sicherheitsthemen und Ideen, wie sich bereits vorhandene Programme und Tools besser nutzen lassen.**

**Disclaimer:** Dieser Artikel dient ausschließlich Informations- und Bildungszwecken. Die Verfügbarkeit einzelner Funktionen und deren Darstellung können von der verwendeten Microsoft-Word-Version, dem Betriebssystem und den Geräteeinstellungen abhängen. Bevor Sie einen QR-Code in wichtigen Dokumenten verwenden, sollten Sie ihn auf mehreren Geräten testen und prüfen, ob er tatsächlich zum erwarteten Inhalt führt.

<small style="color:#999; font-size:0.8em;">In Zusammenarbeit mit AI.</small>
