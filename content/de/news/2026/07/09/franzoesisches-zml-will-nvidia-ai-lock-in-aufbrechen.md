---
title: "Französisches ZML will Nvidia AI Lock-in aufbrechen"
slug: "franzoesisches-zml-will-nvidia-ai-lock-in-aufbrechen"
date: 2026-07-09T08:00:00+02:00
category: "ai"
translationKey: "zml-france-nvidia-ai-lock-in-2026-07-08"
source: "TechCrunch, ZML, Metaadvisor.eu"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/companies/ZML-France.png"
featured_image: "/images/companies/ZML-France.png"
image: "/images/companies/ZML-France.png"
thumbnail: "/images/companies/ZML-France.png"
image_credit: "Metaadvisor.eu"
tags: ["ZML", "ZML LLMD", "französisches AI-Startup", "AI Inference", "LLM Inference Server", "Nvidia Lock-in", "CUDA", "Multi-Chip AI", "AI-Infrastruktur", "Open-Source LLM", "AI-Chips", "AMD GPU", "Google TPU", "Apple Metal", "Intel Arc"]
summary: "Das französische AI-Startup ZML hat ein kostenloses Inference-Tool veröffentlicht, das Open-Source-AI-Modelle schneller auf verschiedenen Chips ausführen soll, nicht nur auf Nvidia-GPUs. Für gewöhnliche Nutzer ist das kein neuer Chatbot, sondern Infrastruktur unter der Haube, die Profis helfen könnte, Kosten zu senken und die Abhängigkeit von einem einzigen Hardware-Ökosystem zu reduzieren."
disclaimer: "Dieser Artikel dient ausschließlich Informationszwecken und stellt keine Anlage-, Technologie- oder Geschäftsberatung dar."
draft: false
---

Bild ist symbolisch.

# Französisches ZML will Nvidia AI Lock-in aufbrechen: warum das kein neuer Chatbot ist, sondern Infrastruktur unter der Haube

Das französische AI-Startup **ZML** hat ein kostenloses Produkt veröffentlicht, das für Profis interessant sein könnte, die AI-Systeme, Cloud-Infrastruktur, große Chatbots und Anwendungen mit Open-Source-Sprachmodellen bauen. Für gewöhnliche Nutzer ist jedoch zuerst wichtig zu verstehen, was ZML **nicht** ist.

ZML ist kein neuer ChatGPT. Es ist kein neuer AI-Agent, der E-Mails beantwortet, Beiträge schreibt, Dokumente liest oder Kundensupport übernimmt. ZML ist kein Tool, das ein durchschnittlicher Nutzer öffnet, mit Gmail oder Google Sheets verbindet und sofort einen „AI-Mitarbeiter“ bekommt.

ZML ist etwas anderes: Infrastruktur unter der Haube. Es ist Software, die AI-Modellen helfen soll, schneller und effizienter auf verschiedenen Arten von Chips zu laufen, nicht nur auf Nvidia-GPUs.

Anders gesagt: ZML ist nicht das Restaurant, in dem der Nutzer ein fertiges Gericht bestellt. ZML ist Technologie für die Küche. Es hilft denjenigen, die AI-Systeme bauen, dasselbe „Gericht“ schneller, günstiger und auf verschiedenen Arten von Öfen zuzubereiten.

## Warum ist das überhaupt wichtig?

Heute sehen die meisten Menschen AI durch fertige Tools: ChatGPT, Claude, Gemini, Copilot, Sintra, Make, Zapier AI oder verschiedene „AI-Agenten“, die in sozialen Netzwerken beworben werden. Diese Tools wirken für den Nutzer einfach. Man gibt eine Frage ein, verbindet Dokumente, fügt E-Mail, CRM oder eine Website hinzu, und der Agent beginnt zu arbeiten.

Aber hinter dieser einfachen Oberfläche gibt es eine große technische Schicht, die der Nutzer nicht sieht. Wenn ein AI-Agent auf eine Anfrage antworten soll, passiert im Hintergrund eine ganze Kette: Die Anwendung nimmt die Frage entgegen, sendet sie an ein AI-Modell, das Modell wird auf einem Server ausgeführt, der Server nutzt bestimmte Chips, und die Antwort kommt zurück zum Nutzer.

Für gewöhnliche Nutzer ist das unsichtbar. Für Unternehmen, die eigene AI-Systeme bauen, ist es ein großes Problem. Sie müssen entscheiden, worauf sie das Modell laufen lassen, wie viel das kostet, wie schnell das System antworten muss, wie viel Energie es verbraucht und ob es auf **Nvidia**-Chips, **AMD**, **Google TPU**, **Apple Metal**, **Intel Arc** oder anderer Hardware laufen kann.

Hier kommt ZML ins Spiel.

{{< support1 >}}

## ZML versucht, das Problem der AI-„Adapter“ zu lösen

Eines der größten Probleme der AI-Infrastruktur ist, dass verschiedene Chips unterschiedliche Software-Ökosysteme haben. Nvidia ist nicht nur deshalb so dominant, weil das Unternehmen leistungsstarke Chips hat, sondern auch, weil es eine riesige Softwareschicht um diese Chips herum aufgebaut hat. Der bekannteste Teil dieses Ökosystems ist **CUDA**, das über Jahre für viele AI- und Rechenaufgaben fast zu einem Standard geworden ist.

Das erzeugt das, was oft **Vendor Lock-in** genannt wird. Wenn ein System für das Nvidia-Ökosystem gebaut wurde, ist es nicht immer einfach, es auf andere Hardware zu übertragen. Ein Unternehmen kann Zugang zu AMD-GPUs, Apple-Chips oder einem europäischen AI-Chip haben, aber wenn die Software nicht gut angepasst ist, können die Leistung schlecht oder die Entwicklung zu teuer sein.

ZML versucht, eine Schicht zu sein, die dieses Problem abschwächt. Das neue Produkt **ZML/LLMD** ist als Inference Server gedacht, der das Ausführen von Open-Source-Großsprachmodellen auf verschiedenen Arten von Chips ermöglicht. Laut TechCrunch zielt ZML auf Unterstützung für **Nvidia**, **AMD**, **Google TPU**, **Apple Metal**, **Intel Arc** und weitere Chips.

Einfach gesagt: ZML möchte, dass dasselbe AI-Modell auf mehreren verschiedenen „Motoren“ laufen kann, ohne dass Entwickler jedes Mal alles manuell von Grund auf anpassen müssen.

## Was ist Inference und warum wird sie immer wichtiger?

In der AI-Welt wird oft über das Training von Modellen gesprochen. Das ist die Phase, in der ein großes Modell mit riesigen Datenmengen gelernt wird. Das ist teuer, anspruchsvoll und normalerweise großen Akteuren vorbehalten.

Wenn ein Nutzer AI verwendet, passiert aber meistens etwas anderes: **Inference**. Das ist der Moment, in dem ein bereits trainiertes Modell eine Anfrage erhält und eine Antwort generiert. Wenn Sie einen Chatbot bitten, eine E-Mail zu schreiben, ein Gesetz zu erklären, ein Dokument zusammenzufassen oder Code zu generieren, nutzen Sie Inference.

Je stärker AI in immer mehr Anwendungen integriert wird, desto wichtiger wird Inference. Es reicht nicht mehr, ein gutes Modell zu haben. Man muss es schnell, zuverlässig und zu akzeptablen Kosten betreiben. Wenn Millionen von Nutzern ständig Anfragen senden, kostet jede Antwort Geld. Jeder Token verbraucht Rechenressourcen. Jede Sekunde Verzögerung stört den Nutzer.

Deshalb ist Infrastruktur zu einem zentralen Thema geworden. Wenn ein AI-Unternehmen dasselbe Modell schneller oder günstiger betreiben kann, kann das einen großen Unterschied machen.

{{< support1 >}}

## Für wen ist ZML gedacht?

ZML ist kein Tool für gewöhnliche Nutzer, die einen einfachen AI-Agenten für Arbeit, Marketing oder Verwaltung erstellen möchten. Wenn Sie fertige Tools wie Sintra, Make, Zapier, OpenAI Assistants oder einen No-Code-AI-Dienst nutzen, denken Sie normalerweise nicht über Chips nach. Die Plattform löst das für Sie.

ZML ist für ein anderes Publikum interessant: Programmierer, AI-Ingenieure, Cloud-Unternehmen, Startups, die AI-Produkte bauen, Firmen, die Modelle selbst hosten, und Organisationen, die nicht vollständig von einem einzigen Hardwareanbieter abhängig sein wollen.

Wenn jemand einen eigenen Chatbot von Anfang bis Ende baut, ein eigenes AI-Backend oder eine eigene Plattform zum Bereitstellen von Modellen, dann wird die Frage, „worauf das Modell ausgeführt wird“, sehr wichtig. ZML versucht, genau dieser Schicht des Marktes zu helfen.

Deshalb ist es wichtig, zwei Dinge nicht zu verwechseln. Fertige AI-Agenten sind Nutzerprodukte. ZML ist ein Infrastrukturwerkzeug.

Sintra ist wie ein fertiges Restaurant: Der Nutzer bestellt ein Gericht und muss nicht wissen, welche Art von Ofen in der Küche steht. ZML ist Technologie für diese Küche: Es hilft Profis, dasselbe Gericht schneller, günstiger und auf verschiedenen Arten von Ausrüstung zuzubereiten.

## Warum wird ständig Nvidia erwähnt?

Nvidia ist heute ein Symbol für AI-Infrastruktur. Die GPUs des Unternehmens treiben einen großen Teil der modernen AI-Welle an, und die Nachfrage nach ihnen ist durch große Modelle, Clouds und AI-Anwendungen explodiert. Doch die Dominanz von Nvidia bringt auch Probleme mit sich: hohe Preise, begrenzte Verfügbarkeit und Abhängigkeit von einem einzigen Ökosystem.

ZML bedeutet nicht, dass die Dominanz von Nvidia vorbei ist. Das wäre übertrieben. Nvidia hat weiterhin eine enorme technologische, marktbezogene und softwareseitige Position. Aber ZML passt in einen breiteren Trend: Immer mehr Unternehmen versuchen Wege zu finden, AI-Modelle auch auf anderen Chips zu betreiben.

Wenn diese Schicht besser wird, bekommt der Markt mehr Auswahl. Unternehmen könnten je nach Preis, Verfügbarkeit, Geschwindigkeit und Energieverbrauch eine Kombination aus Nvidia, AMD, Google, Apple, Intel oder spezialisierten AI-Chips nutzen.

Das muss für gewöhnliche Nutzer nicht sichtbar sein, kann aber die Preise und die Verfügbarkeit der AI-Tools beeinflussen, die sie verwenden.

{{< support2 >}}

## Der europäische Blickwinkel

Interessant ist auch, dass ZML aus Frankreich kommt. Europa liegt bei großen Plattformen und verbraucherorientierten AI-Produkten oft hinter den USA zurück, versucht aber, in Infrastruktur, Chips, Sicherheit und spezialisierten Technologieschichten Raum zu finden.

TechCrunch schreibt, dass eine solche Softwareschicht auch neuen AI-Chipmakern helfen könnte, von denen viele aus Europa stammen. Im Artikel werden **Axelera**, **Fractile**, **Kalray**, **OLIX**, **Q.ANT**, **SiPearl**, **SpiNNcloud** und **VSORA** erwähnt. Entscheidend ist nicht nur, woher diese Unternehmen kommen, sondern dass neue AI-Hardware nur schwer breit nutzbar werden kann, wenn es keine Software gibt, die sie mit Modellen, Anwendungen und realen Einsatzfällen verbindet.

Das ist eine wichtige Lektion: Ein Chip allein reicht nicht. Hardware ohne gute Software schafft es nur schwer in die tatsächliche Nutzung. Nvidia weiß das sehr gut. Der Erfolg des Unternehmens liegt nicht nur im Silizium, sondern auch im Software-Ökosystem, das über Jahre darum herum aufgebaut wurde.

Wenn Europa eine ernsthaftere Rolle in der AI-Infrastruktur spielen will, muss es sowohl Hardware als auch die Software entwickeln, die diese Hardware nützlich macht.

## Warum kann das trotzdem für gewöhnliche Menschen wichtig sein?

Auch wenn ZML kein Tool für gewöhnliche Nutzer ist, können die Folgen solcher Technologien breiter spürbar werden. Wenn AI-Modelle günstiger betrieben werden können, können mehr Unternehmen AI-Dienste anbieten. Wenn die Abhängigkeit von einem einzigen Hardwareanbieter sinkt, kann der Markt wettbewerbsfähiger werden. Wenn Inference schneller wird, können AI-Tools schneller und zugänglicher werden.

Ein gewöhnlicher Nutzer wird ZML/LLMD vielleicht nie installieren. Aber er kann eine Anwendung nutzen, die im Hintergrund eine solche oder ähnliche Infrastrukturschicht verwendet. So wie die meisten Menschen nicht wissen, welcher Server ihre Banking-App betreibt, aber sehr wohl merken, wenn die App langsam, teuer oder nicht verfügbar ist.

ZML ist deshalb eine Geschichte über den unsichtbaren Teil von AI. Nicht über den Chatbot, der dem Nutzer antwortet, sondern über die Schicht, die überhaupt ermöglicht, dass der Chatbot schnell, stabil und zu akzeptablen Kosten läuft.

{{< support2 >}}

## Unser Fazit

- ZML ist kein neuer Chatbot, AI-Agent oder Tool für gewöhnliche Nutzer.
- ZML ist Infrastruktur-Software für Profis, die AI-Modelle bauen, hosten oder optimieren.
- Ziel ist es, Open-Source-LLM-Modelle auf verschiedenen Chips laufen zu lassen, nicht nur auf Nvidia-GPUs.
- Das Hauptthema ist nicht „neue AI“, sondern die Reduzierung der Abhängigkeit von einem einzigen Hardware-Ökosystem.
- Für Nutzer fertiger AI-Tools ist diese Schicht größtenteils unsichtbar.
- Für Unternehmen, die AI-Systeme von Grund auf bauen, werden Inference, Geschwindigkeit, Kosten und Chip-Kompatibilität zu entscheidenden Problemen.
- Wenn Tools wie ZML erfolgreich sind, könnte der AI-Markt langfristig mehr Wettbewerb, niedrigere Kosten und weniger Abhängigkeit von Nvidia bekommen.
- Das ist eine Infrastrukturgeschichte, aber gerade solche Geschichten bestimmen oft, wie zugänglich, schnell und teuer AI am Ende wird.

**Disclaimer:** Dieser Artikel dient ausschließlich Informationszwecken und stellt keine Anlage-, Technologie- oder Geschäftsberatung dar.
