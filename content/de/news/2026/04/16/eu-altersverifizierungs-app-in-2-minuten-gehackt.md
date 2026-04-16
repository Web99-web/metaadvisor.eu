---
title: "EU-Altersverifizierungs-App in 2 Minuten gehackt: Sicherheitslücke von Security Consultant aufgedeckt"
slug: "eu-altersverifizierungs-app-in-2-minuten-gehackt"
date: 2026-04-16T10:00:00+02:00
category: "tech"
translationKey: "eu-age-verification-app-security-flaw-2026"
author: "Metaadvisor.eu"
source: "X (Twitter), öffentliche Beiträge"
source_url: "https://metaadvisor.eu/"
image_url: "/images/news/EU-age-verification-app-hacked.png"
featured_image: "/images/news/EU-age-verification-app-hacked.png"
image: "/images/news/EU-age-verification-app-hacked.png"
thumbnail: "/images/news/EU-age-verification-app-hacked.png"
image_alt: "EU age verification app security flaw bypass"
image_credit: "Metaadvisor Illustration"
tags: ["eu", "altersverifizierung", "sicherheit", "hacking", "privatsphäre", "digitale identität", "sicherheitslücke"]
summary: "Ein Sicherheitsberater zeigte, dass die EU-App zur Altersverifizierung aufgrund eines schwerwiegenden Designfehlers in weniger als zwei Minuten umgangen werden kann."
---

*Das Bild ist symbolisch.*

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Erhalte einen Bitget-Bonus von bis zu 6200 USDT — hier registrieren
  </a>
</p>

# EU-Altersverifizierungs-App in 2 Minuten gehackt: Sicherheitslücke von Security Consultant aufgedeckt

Die neue EU-App zur Altersverifizierung, die als Lösung zur Festlegung eines Standards für Sicherheit und Datenschutz präsentiert wurde, steht bereits unter ernsthaften Zweifel. Nur wenige Tage nach ihrer Vorstellung als „technisch bereit“ zeigte der Sicherheitsberater **Paul Moore, dass das System in weniger als zwei Minuten umgangen werden kann.**

## Wie die Schwachstelle funktioniert

<p style="text-align:center;">
  <img src="/images/news/EU-age-app-Paul-Moore-Security-Consultant.png" alt="EU age verification security flaw analysis" style="max-width:100%; border-radius:10px;" />
</p>

Während der Einrichtung fordert die App den Nutzer auf, eine PIN zu erstellen. Diese PIN wird anschließend „verschlüsselt“ und lokal auf dem Gerät im sogenannten shared_prefs-Verzeichnis gespeichert.

Auf den ersten Blick scheint dies eine Sicherheitsmaßnahme zu sein. Laut Analyse handelt es sich jedoch um ein schwerwiegendes Designproblem. Die PIN ist nicht kryptografisch mit der Identität des Nutzers bzw. mit dem „Vault“ verbunden, der die eigentlichen Identitätsdaten enthält.

Das bedeutet, dass das System die Verbindung zwischen Authentifizierung und Identität nicht tatsächlich überprüft.

{{< support1 >}}

## Umgehung in der Praxis

<p style="text-align:center;">
  <img src="/images/news/EU-age-app-Paul-Moore-Security-Consultant1.png" alt="EU age verification bypass method" style="max-width:100%; border-radius:10px;" />
</p>

Der Angriff erfordert keine fortgeschrittenen Tools oder komplexen Methoden. Es reicht aus, auf die lokale Konfigurationsdatei zuzugreifen und die Werte für die PIN (PinEnc und PinIV) zu entfernen.

Nach dem Neustart der App wird eine neue PIN gesetzt — die Anwendung behält jedoch weiterhin die alten Anmeldedaten des vorherigen Profils.

Das Ergebnis ist eine schwerwiegende Sicherheitslücke: Das System erlaubt die Nutzung einer bestehenden Identität ohne tatsächliche Überprüfung. Mit anderen Worten, die Anwendung kann in einen „gültigen“ Zustand versetzt werden, ohne dass die Identität erneut bestätigt wird.

## Weitere Sicherheitsprobleme

<p style="text-align:center;">
  <img src="/images/news/EU-age-app-Paul-Moore-Security-Consultant2.png" alt="EU age verification additional issues" style="max-width:100%; border-radius:10px;" />
</p>

Neben der grundlegenden Schwachstelle wurden weitere Probleme identifiziert, die die Sicherheit zusätzlich beeinträchtigen.

Die Begrenzung der Anzahl von Versuchen (Rate Limiting) ist als einfacher Zähler in derselben Konfigurationsdatei implementiert. Das bedeutet, dass er zurückgesetzt werden kann und Versuche unbegrenzt fortgesetzt werden können.

Ähnliches gilt für die biometrische Authentifizierung. Die Option „UseBiometricAuth“ ist lediglich ein boolescher Wert, der sich leicht ändern lässt — wodurch dieser Schritt vollständig übersprungen werden kann.

{{< support2 >}}

## Größerer Kontext: Sicherheit vs. Wahrnehmung

Dieser Fall wirft eine wichtigere Frage auf als nur die App selbst. Es geht um das Vertrauen in digitale Identitätssysteme, die zunehmend auf EU-Ebene eingeführt werden.

Die Anwendung wird als Open-Source-Lösung beworben, die höchste Datenschutzstandards erfüllt. Dieses Beispiel zeigt jedoch, dass Transparenz nicht automatisch Sicherheit bedeutet.

Wenn sich zentrale Sicherheitsmechanismen auf lokale Einstellungen stützen, die verändert werden können, wird das System anfällig — unabhängig davon, wie „sicher“ es formal erscheint.

## Fazit

Dies ist kein klassischer Hackerangriff, sondern ein Designfehler. Genau deshalb ist er potenziell gefährlicher — da er ohne fortgeschrittene technische Kenntnisse ausgenutzt werden kann.

Wenn ein System zur Identitätsprüfung in wenigen Minuten umgangen werden kann, stellt sich nicht mehr die Frage, wie fortschrittlich die Technologie ist, sondern wie zuverlässig sie tatsächlich ist.

---

### Unsere Einschätzung (Metaadvisor)

Dieser Fall zeigt deutlich, dass Sicherheit nicht aus Aussagen entsteht, sondern aus der Systemarchitektur. Systeme können „offiziell“, „reguliert“ und „open-source“ sein — doch wenn das grundlegende Design fehlerhaft ist, wird Sicherheit zur Illusion.

Noch wichtiger ist, dass es sich hier nicht um ein isoliertes Problem handelt. Es geht um die Richtung, in die sich digitale Identitäts- und Zugriffssysteme entwickeln.

Wenn solche Systeme auch nur kleinste Schwächen aufweisen, sind die Folgen nicht lokal, sondern systemisch.

Und vielleicht die wichtigste Erkenntnis: Die gefährlichsten Schwachstellen sind nicht die, die komplexe Angriffe erfordern, sondern die, die sich einfach ausnutzen lassen. In solchen Fällen ist die Frage nicht, ob es zu Missbrauch kommt — sondern wann.

---

<span style="font-size:0.9em; color:#777;">
Dieser Inhalt dient ausschließlich Informationszwecken und stellt keine finanzielle oder Anlageberatung dar.
</span>
