---
title: "iPhone, Zoom, IKEA, Salesforce: Hackerangriff über Optimizely"
slug: "iphone-zoom-ikea-salesforce-hackerangriff-optimizely"
date: "2026-11-17T08:00:00+01:00"
category: "technology"
translationKey: "optimizely-hackers-zoom-ikea-salesforce-iphone-2026-11-17"
source: "Optimizely Service Status; Report URI; Reuters; StepSecurity"
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
featured_image: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
image: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
thumbnail: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
image_alt: "Hackerangriff über Optimizely auf Websites von Zoom, IKEA und Salesforce mit versuchten Angriffen auf iPhones"
image_credit: "Metaadvisor.eu"
tags: ["Cybersecurity", "Optimizely", "Zoom", "IKEA", "Salesforce", "iPhone", "Apple", "Hacking", "Cryptocurrency", "Supply Chain Attack"]
description: "Manipulierte Optimizely-Skripte betrafen Websites von 178 Organisationen, darunter Zoom, IKEA und Salesforce. Angreifer zielten auf Krypto, Zahlungsdaten und iPhones."
summary: "Manipulierte Optimizely-Skripte betrafen Websites von 178 Organisationen, darunter Zoom, IKEA und Salesforce. Angreifer zielten auf Krypto, Zahlungsdaten und iPhones."
categories: ["technology"]
---

*Das Titelbild dient der Illustration.*

**Websites von mindestens 178 Organisationen, darunter Zoom, IKEA und Salesforce, waren am 16. November von einem groß angelegten Hackerangriff über die Plattform Optimizely betroffen. Angreifer schleusten schädlichen JavaScript-Code in reguläre Skripte zur Website-Optimierung ein. Dieser Code sollte unter anderem Kryptowährungsadressen austauschen, Zahlungsdaten aus Formularen abgreifen und Schwachstellen auf iPhones ausnutzen. Sicherheitsforscher bestätigten die Verbreitung des Codes und Hinweise auf einzelne Kryptodiebstähle. Wie viele Nutzer tatsächlich geschädigt wurden, ist jedoch noch unbekannt. Eine massenhafte erfolgreiche Infektion von iPhones wurde nicht nachgewiesen.**

## Wie konnten die Angreifer so viele bekannte Websites erreichen?

Die gemeinsame Verbindung war Optimizely, eine Plattform, mit der Unternehmen das Aussehen und die Funktionen ihrer Websites testen und optimieren. Solche Dienste laden eigenen Code in den Browser der Besucher. Wird ein Skript eines externen Anbieters manipuliert, können zahlreiche eigentlich vertrauenswürdige Websites gleichzeitig betroffen sein. Der Sicherheitsforscher Scott Helme von Report URI berichtete, sein Team habe 1.611 Optimizely-Skripte untersucht und in 188 davon, die 178 Organisationen zugeordnet wurden, Schadcode gefunden. Diese Zahl beschreibt die bestätigten Funde der Untersuchung und muss nicht den endgültigen Umfang des Vorfalls abbilden.

Auch CNN, BBC, HSBC, Equifax, GitLab und weitere bekannte Unternehmen tauchten in der Untersuchung auf. Dabei muss klar zwischen einem manipulierten Skript, das eine Website einbindet, und einem vollständigen Einbruch in die interne IT des jeweiligen Unternehmens unterschieden werden. Die bisher veröffentlichten Erkenntnisse belegen nicht, dass die Angreifer deren Kundendatenbanken, Geschäftssysteme oder Nutzerkonten übernommen haben.

## Was hat Optimizely bestätigt?

Optimizely bestätigte in einer offiziellen Sicherheitsmeldung, dass eine unbefugte Person eine Schwachstelle im Zusammenhang mit der Experimentation-Plattform ausgenutzt und schädlichen JavaScript-Code in bestimmte Kundenprojekte eingefügt hatte. Das Unternehmen erklärte, Maßnahmen zur Entfernung des Codes und zur Absicherung der betroffenen Systeme zu ergreifen. Laut Sicherheitsberichten waren bis zum Abend des 16. November viele der beobachteten schädlichen Skripte entfernt worden. Die Untersuchung des endgültigen Schadensumfangs war damit jedoch nicht abgeschlossen.

Der Vorfall verdeutlicht die besondere Gefahr eines sogenannten Lieferkettenangriffs (*Supply-Chain-Angriff*). Ein Besucher muss weder einen verdächtigen Link öffnen noch einen gefälschten Shop aufrufen. Schädlicher Code kann bereits beim Besuch einer bekannten Website ausgeführt werden, wenn diese einem kompromittierten externen Dienst vertraut.

{{< support1 >}}

## Kryptoadressen, Kartendaten und iPhones: dieselbe Kampagne

Nach Angaben der Forscher hatte der eingeschleuste Code mehrere Funktionen. Eine davon sollte kopierte Kryptowährungsadressen erkennen und durch Adressen der Angreifer ersetzen, sodass Nutzer eine Überweisung unbemerkt an den falschen Empfänger senden könnten. Eine weitere Funktion zielte auf Daten aus Zahlungsformularen. Die Ermittler beobachteten auch Zahlungseingänge auf einzelnen mit dem Angriff verbundenen Adressen. Daraus lässt sich aber noch keine endgültige Schadenssumme ableiten.

**Die Angriffsversuche gegen iPhones waren keine unabhängige, separate Geschichte.** Der analysierte Code enthielt einen Zweig, der Apple-Mobilgeräte und deren iOS-Version erkannte und daraufhin weitere Versuche zur Ausnutzung von Schwachstellen auslösen sollte. Technische Untersuchungen nennen in diesem Zusammenhang Coruna und DarkSword. Damit zielte dieselbe Operation je nach Gerät auf unterschiedliche Opfer und Methoden. Es bedeutet aber nicht, dass jedes iPhone beim Besuch einer betroffenen Website infiziert wurde. Eine verlässliche Zahl tatsächlich kompromittierter physischer Geräte liegt nicht vor.

## Was ist gesichert und was bleibt offen?

Gesichert ist, dass schädliche Skripte über die vertrauenswürdige Infrastruktur von Optimizely verteilt und teilweise auf bekannten Websites eingebunden wurden. Auch verschiedene Diebstahlversuche, darunter der Austausch von Kryptoadressen, wurden dokumentiert. Die Zahl von 178 Organisationen sagt jedoch nichts darüber aus, wie viele Menschen die Seiten während des Angriffs besuchten, wie viele Zahlungsvorgänge betroffen waren oder wie viele Geräte tatsächlich übernommen wurden.

Ebenso wenig lässt sich allen genannten Unternehmen derselbe Grad an Kompromittierung zuschreiben. Für jede Website kommt es darauf an, wann sie den manipulierten Code eingebunden hat, wie lange dieser aktiv war und welche Sicherheitsmaßnahmen griffen. Genauere Antworten müssen weitere technische Untersuchungen und Mitteilungen der jeweiligen Unternehmen liefern.

{{< support2 >}}

## Was können Nutzer und Website-Betreiber tun?

Wer am 16. November eine der genannten Websites besucht hat, muss nicht automatisch von gestohlenen Daten ausgehen. Dennoch ist es sinnvoll, Browser und Betriebssystem auf dem neuesten Stand zu halten. Beim Versand von Kryptowährungen sollte die vollständige Empfängeradresse unmittelbar vor der Bestätigung geprüft werden, besonders nach dem Kopieren und Einfügen. Bei unbekannten Kartenbelastungen oder verdächtigen Transaktionen sollten Betroffene ihre Bank oder die jeweilige Plattform unverzüglich kontaktieren.

Unternehmen, die Optimizely nutzen, sollten ihre eingebundenen Skripte, Berechtigungen und Sicherheitsprotokolle prüfen und die Hinweise des Dienstleisters befolgen. Beschränkungen für zulässige Skriptquellen, Änderungsüberwachung und zeitnahe Sicherheitsupdates können das Risiko ähnlicher Vorfälle reduzieren. Diese Vorsichtsmaßnahmen bedeuten nicht, dass jeder Besucher einer betroffenen Seite geschädigt wurde.

## Unsere Einschätzung (Metaadvisor)

* **Bekannte Marken erhöhen die Reichweite.** Zoom, IKEA und Salesforce gehörten zu den Organisationen mit betroffenen Skripten. Ein Einbruch in alle internen Systeme ist damit nicht bewiesen.
* **Optimizely war der gemeinsame Angriffsweg.** Die Angreifer missbrauchten das Vertrauen vieler Websites in extern eingebundenen Code.
* **iPhones waren Teil derselben Kampagne.** Die Skripte enthielten iOS-Angriffsversuche; eine massenhafte erfolgreiche Infektion ist nicht bestätigt.
* **Der Kryptobetrug hatte einen konkreten Mechanismus.** Durch den Austausch einer Empfängeradresse kann eine Zahlung unbemerkt umgeleitet werden.
* **178 bezeichnet Organisationen, nicht individuelle Opfer.** Die Zahl stammt aus der Untersuchung infizierter Skripte.
* **Der Gesamtschaden ist weiterhin unklar.** Bestätigte Codeverbreitung, beobachtete Diebstähle und ungeklärte Folgen müssen auseinandergehalten werden.

**Folgen Sie Metaadvisor.eu für weitere unabhängige Nachrichten und Analysen zu Technologie, künstlicher Intelligenz, Wirtschaft und digitaler Sicherheit.**

<small style="color:#757575; font-size:12px; font-weight:400; font-style:normal;">In collaboration with AI.</small>

**Hinweis:** Dieser Artikel basiert auf der offiziellen Sicherheitsmeldung von Optimizely, Recherchen von Report URI und Reuters-Berichten, die am 17. November 2026 verfügbar waren. Die genannte Zahl von Organisationen bezieht sich auf identifizierte manipulierte Skripte, nicht auf nachgewiesene Datendiebstähle bei allen betroffenen Unternehmen. Versuche, iPhone-Schwachstellen auszunutzen, sind kein Nachweis für erfolgreich kompromittierte Geräte. Der Inhalt dient ausschließlich der Information und ist keine individuelle Sicherheits-, Rechts- oder Finanzberatung.
