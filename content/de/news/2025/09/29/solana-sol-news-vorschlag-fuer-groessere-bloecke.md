---
title: "Solana (SOL) — Vorschlag für größere Blöcke nach Alpenglow"
slug: "solana-sol-news-vorschlag-fuer-groessere-bloecke"
date: 2025-09-29T16:15:40Z
category: "crypto"
translationKey: "solana-bigger-blocks-simd-0370"

author: "CoinDesk"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2025/09/29/firedancer-devs-from-jump-crypto-pushes-solana-toward-bigger-blocks"
image_url: "/images/solana-sol.png"
featured_image: "/images/solana-sol.png"
image: "/images/solana-sol.png"
thumbnail: "/images/solana-sol.png"
image_alt: "Solana Logo & Netzwerk – Vorschlag für größere Blöcke"
image_credit: "Metaadvisor.eu"

tags:
  - solana
  - SOL
  - Firedancer
  - SIMD-0370
  - Alpenglow
  - throughput
  - validators
  - defi
  - fees
  - scaling

summary: "Firedancer (Jump Crypto) schlägt mit SIMD-0370 vor, das Block-Limit für Compute-Units nach dem Alpenglow-Upgrade zu entfernen. Ziel: höhere Durchsatzspitzen – bei diskutierten Risiken wie Zentralisierung und längerer Propagation."
---

> **Hinweis:** Symbolisches Bild.

## Was steht im Vorschlag?
Das Firedancer-Team hat **SIMD-0370** eingereicht: das **Block-Limit für Compute-Units (CU)** auf Solana (derzeit ~**60 Mio. CU**) soll **entfallen** – **nach** dem **Alpenglow**-Upgrade. Block-Producer dürften dann **größere Blöcke** bauen, abhängig von der Leistungsfähigkeit ihrer Validatoren.

Zuvor gab es nur den Vorstoß, das Limit auf **100 Mio. CU** zu erhöhen; jetzt steht **Entfernung** des Cap im Raum.

## Warum überhaupt?
- **Mehr Transaktionen bei Peaks** (Token-Launches, DeFi-Spikes) → weniger **failed trades** und Staus.  
- **Flexibilität pro Validator:** schnellere Maschinen können mehr Last schultern.

## Mögliche Risiken
- **Propagation & Latenz:** größere Blöcke brauchen länger → **mehr Forks/Orphans**, höhere Varianz.  
- **Hardware-Wettrüsten:** Vorteil für starke Server → **Zentralisierungsdruck**.  
- **MEV-Dynamik:** größere Batch-Fenster können **Arb/Sandwich** begünstigen.  
- **Gebühren:** bei echter Nachfrage steigen Median-Fees auch mit größeren Blöcken.

## Stimmen aus dem Ökosystem
Befürworter erwarten bessere **Burst-Capacity**;  
**Anatoly Yakovenko** hält dagegen: **Blöcke sind oft nicht voll**, der Endnutzer-Effekt könnte begrenzt sein, solange Nachfrage nicht nachhaltig anzieht.

## Nächste Schritte
Der Vorschlag befindet sich in der **Diskussion**. Bei Annahme dürfte die Aktivierung **nach Alpenglow** erfolgen; Details (Soft-Limits, Telemetrie) werden wahrscheinlich iterativ getuned.

---

## Unser Fazit (Metaadvisor)
- **Strategisch passend** zu Solanas Anspruch: **hoher Durchsatz + kurze Slots**. Ohne bessere **Propagation** und **Konsistenz** bringt Cap-Removal aber wenig. Firedancer adressiert genau das.  
- **Empfehlung:** **Soft-Limits & Telemetrie** (z. B. 95-Perzentil der Propagation), automatische Drosselung bei Netzstau.  
- **Bull-Case:** weniger **failed tx** in der Spitze → **besseres UX**, mehr Volumen, mehr Gebühren.  
- **Risiko:** höherer Mindest-Hardware-Footprint. Klare **Mindest-Specs** und Netzwerk-Optimierungen sind essenziell.

*Informationsinhalt. Keine Anlageberatung.*
