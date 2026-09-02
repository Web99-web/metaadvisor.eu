---
title: "Dropbox-Hack über Lenovo ID kompromittierte 5.000 Konten"
slug: "dropbox-hack-lenovo-id-5000-konten-kompromittiert"
date: 2026-09-03T06:00:00+02:00
category: "Tech"
translationKey: "dropbox-lenovo-id-hack-5000-accounts-2026-09-02"
source: "Dropbox, Lenovo, Reuters, BleepingComputer"
author: "Metaadvisor.eu"
image_url: "/images/hack/Dropbox-Lenovo-hack.png"
featured_image: "/images/hack/Dropbox-Lenovo-hack.png"
image: "/images/hack/Dropbox-Lenovo-hack.png"
thumbnail: "/images/hack/Dropbox-Lenovo-hack.png"
image_alt: "Dropbox-Sicherheitsvorfall, bei dem über eine Schwachstelle in der Lenovo-ID-Integration rund 5.000 Nutzerkonten kompromittiert wurden"
image_credit: "Metaadvisor.eu"
tags: ["Dropbox", "Lenovo", "Lenovo ID", "Hackerangriff", "Cybersicherheit", "Sicherheit", "Datendiebstahl", "Nutzerkonten", "Cloud", "2FA", "Authentifizierung", "digitale Identität", "Sicherheitslücke", "Passwörter", "Datenschutz"]
description: "Dropbox bestätigte, dass rund 5.000 Nutzerkonten über eine Sicherheitslücke im Zusammenhang mit einer alten Lenovo-ID-Integration kompromittiert wurden. Die Angreifer benötigten dafür nicht einmal das Dropbox-Passwort."
summary: "Angreifer nutzten eine Schwachstelle bei der Lenovo-ID-E-Mail-Verifizierung, um sich als Besitzer fremder E-Mail-Adressen auszugeben und über eine alte Integration auf Dropbox-Konten zuzugreifen. Auf einem Teil der Konten wurden Dateien angesehen oder heruntergeladen."
---

*Das Bild dient nur zur Illustration.*

# Dropbox-Hack: Rund 5.000 Konten über Lenovo-ID-Schwachstelle kompromittiert

Dropbox hat einen Sicherheitsvorfall bestätigt, bei dem im August rund **5.000 Nutzerkonten kompromittiert** wurden. Auf einem Teil dieser Konten konnten Angreifer Dateien ansehen oder herunterladen. Besonders bemerkenswert ist die Angriffsmethode: **Die Hacker benötigten nicht das Dropbox-Passwort der Nutzer.**

Das Problem hing mit einer älteren Integration zwischen **Lenovo ID und Dropbox** zusammen. Angreifer konnten offenbar eine Schwachstelle bei der Überprüfung von E-Mail-Adressen auf der Lenovo-Seite ausnutzen und sich dadurch gegenüber Dropbox als legitime Kontoinhaber ausgeben.

## Wie konnte Lenovo ID ein fremdes Dropbox-Konto öffnen?

Dropbox erlaubte früher die Authentifizierung über Lenovo ID. Das Grundprinzip solcher Systeme ist einfach: Ein externer Dienst bestätigt die Identität eines Nutzers, und Dropbox vertraut dieser Bestätigung, ohne jedes Mal erneut das Dropbox-Passwort abzufragen.

Nach den veröffentlichten Informationen konnten Angreifer **eine Lenovo ID mit der E-Mail-Adresse einer anderen Person registrieren**. Wenn dieselbe Adresse mit einem bestehenden Dropbox-Konto verbunden war, konnte die alte Integration unter bestimmten Bedingungen Zugang zu diesem Konto ermöglichen.

Der Angreifer musste also weder das Passwort stehlen noch erraten. Es reichte aus, eine Schwachstelle in der Art auszunutzen, wie ein System dem anderen die Identität des Nutzers bestätigte.

## Rund 5.000 Konten waren betroffen

Die unbefugten Zugriffe wurden zwischen dem **4. und 21. August 2026** festgestellt. Nach Abschluss der ersten Untersuchung begann Dropbox damit, betroffene Nutzer zu informieren.

Rund **5.000 Konten** wurden kompromittiert. Bei weniger als einem Drittel davon konnten Angreifer tatsächlich Dateien ansehen oder herunterladen. Ein kompromittiertes Konto bedeutet also nicht automatisch, dass sämtliche gespeicherten Daten gestohlen wurden, wohl aber, dass ein unbefugter Zugriff möglich war.

Ein besonders wichtiger Punkt: Die betroffenen Konten **hatten keine aktivierte Zwei-Faktor-Authentifizierung von Dropbox**.

{{< support1 >}}

## Ein Lenovo-Laptop war dafür nicht notwendig

Der Vorfall bedeutet nicht, dass Lenovo-Laptops gehackt wurden oder dass der Besitz eines Lenovo-Geräts automatisch ein Risiko darstellte.

Noch bemerkenswerter ist, dass ein Nutzer **nicht einmal vorher eine Lenovo ID besitzen musste**. Genau darin lag die Schwachstelle: Ein Angreifer konnte unter Umständen eine neue Lenovo ID mit der E-Mail-Adresse des Opfers anlegen und anschließend die alte Verbindung zu Dropbox ausnutzen.

Es handelt sich deshalb vor allem um ein Problem der **digitalen Identität und des Vertrauens zwischen zwei Plattformen**, nicht um einen Angriff auf Lenovo-Hardware.

## Die Schwachstelle war nicht das Dropbox-Passwort

Seit Jahren werden Nutzer dazu angehalten, starke und einzigartige Passwörter zu verwenden, Phishing-Seiten zu vermeiden und Zugangsdaten niemals weiterzugeben. Dieser Vorfall zeigt jedoch, dass selbst ein sehr starkes Passwort nicht jedes Risiko beseitigt.

Wenn eine Plattform die Anmeldung über einen anderen Dienst erlaubt, hängt die Sicherheit des Kontos teilweise auch von diesem externen Identitätsanbieter ab. Bestätigt dieser fälschlicherweise, dass ein Angreifer Besitzer einer bestimmten E-Mail-Adresse ist, kann sich dieser Fehler auf den Dienst übertragen, der dieser Bestätigung vertraut.

In diesem Fall wurde **die Vertrauenskette zwischen Lenovo ID und Dropbox selbst zur Sicherheitslücke**.

{{< support2 >}}

## Dropbox änderte die Anmeldung

Nach der Entdeckung des Vorfalls setzte Dropbox aktive Sitzungen zurück, die über Lenovo ID authentifiziert worden waren, entfernte bestehende Verknüpfungen und änderte die Funktionsweise der Integration.

Eine Lenovo ID allein soll nun nicht mehr ausreichen, um auf ein bestehendes Dropbox-Konto zuzugreifen. Bei diesem Anmeldeweg wird zusätzlich das **Dropbox-Passwort** verlangt.

Betroffenen Nutzern wurde außerdem empfohlen, Passwörter zu ändern und die Zwei-Faktor-Authentifizierung zu aktivieren.

## Warum 2FA hier besonders wichtig ist

Bei aktivierter Zwei-Faktor-Authentifizierung reicht ein Passwort oder eine Identitätsbestätigung über einen anderen Dienst allein nicht aus. Für die Anmeldung ist eine zusätzliche Bestätigung notwendig, beispielsweise ein Code aus einer Authenticator-App.

Gerade deshalb ist die Information relevant, dass die kompromittierten Konten keinen Dropbox-2FA-Schutz aktiviert hatten. Der Angreifer konnte die Schwäche im ersten Authentifizierungsschritt ausnutzen, ohne anschließend an einer zweiten Sicherheitsbarriere zu scheitern.

Der Vorfall ist damit ein gutes Beispiel dafür, warum 2FA auch dann sinnvoll ist, wenn ein Nutzer ein starkes Passwort verwendet und niemals auf Phishing-Links klickt.

## Unsere Einschätzung

* **Rund 5.000 Dropbox-Konten wurden über eine Schwachstelle im Zusammenhang mit einer alten Lenovo-ID-Integration kompromittiert.**
* **Die Angreifer benötigten kein Dropbox-Passwort.** Entscheidend war die Art, wie Lenovo ID den Besitz einer E-Mail-Adresse bestätigen konnte.
* **Bei weniger als einem Drittel der betroffenen Konten wurden Dateien angesehen oder heruntergeladen.**
* **Der Besitz eines Lenovo-Laptops bedeutete nicht automatisch, dass ein Nutzer betroffen war**, und einige Opfer mussten vorher nicht einmal eine Lenovo ID besitzen.
* **Die betroffenen Dropbox-Konten hatten keinen aktivierten 2FA-Schutz**, was erneut zeigt, wie wichtig eine zusätzliche Authentifizierungsebene ist.
* **Die wichtigste Lehre geht über Dropbox und Lenovo hinaus.** Alte „Sign in with…“-Verbindungen und externe Identitätsdienste können Teil einer Sicherheitskette bleiben, lange nachdem Nutzer vergessen haben, dass diese Verbindung überhaupt existiert.
* **Kontosicherheit hängt deshalb nicht nur vom Passwort ab**, sondern auch von allen Diensten, denen im Laufe der Zeit erlaubt wurde, unsere digitale Identität zu bestätigen.

**Folgen Sie Metaadvisor.eu für weitere Wirtschafts- und Technologienachrichten, KI-Themen, Cybersicherheit, digitale Plattformen, praktische Tech-Tipps und Analysen zu Entwicklungen, die unsere digitale Sicherheit betreffen.**

**Disclaimer:** Dieser Artikel dient ausschließlich Informationszwecken. Die Informationen zum Dropbox- und Lenovo-Sicherheitsvorfall basieren auf öffentlich verfügbaren Aussagen der Unternehmen und Medienberichten zum Zeitpunkt der Veröffentlichung. Nutzer, die einen unbefugten Zugriff vermuten, sollten aktive Sitzungen und verbundene Apps prüfen, ihr Passwort ändern und die Zwei-Faktor-Authentifizierung aktivieren.

<small style="color:#999; font-size:0.8em;">In Zusammenarbeit mit KI.</small>
