---
title: "Mullenweg: WordPress und Tumblr — mein „größter Fehlschlag“ bisher"
slug: "mullenweg-wordpress-und-tumblr-groesster-fehlschlag-bisher"
date: 2025-10-20T16:21:50Z
category: "ai"
translationKey: "7dd70dc2c082c409ed8b7ae2672a12d9"
source: "TechCrunch"
source_url: "https://techcrunch.com/2025/10/20/automattic-ceo-calls-tumblr-his-biggest-failure-so-far/"
author: "TechCrunch"
analysis_by: "Metaadvisor.eu"
image_url: "/images/tumblr.png"
featured_image: "/images/tumblr.png"
image: "/images/tumblr.png"
thumbnail: "/images/tumblr.png"
image_alt: "Tumblr — Logo, illustrative Darstellung"
image_credit: "Symbolbild."
tags: ["tumblr", "wordpress", "automattic", "matt mullenweg", "migration", "wordpress backend", "fediverse", "activitypub", "open source", "cms", "technik", "restrukturierung", "monetarisierung", "saas", "cloud", "cdn", "seo", "id mapping"]
summary: "Automattic-CEO Matt Mullenweg nennt die Tumblr-Akquisition und die weiterhin getrennte Infrastruktur von WordPress seinen 'größten Fehlschlag'. Die massive Migration auf den WordPress-Back-End ist pausiert, bleibt aber strategisches Ziel."
---

Der WordPress-Mitgründer und Automattic-CEO **Matt Mullenweg** sagte offen, was Branchenkenner vermuten: Die Übernahme von **Tumblr** und das jahrelange Zögern, die Plattform vollständig auf die **WordPress-Infrastruktur** zu heben, seien sein „**größter Fehlschlag bisher**“. Ein Fehlschlag — aber **keine Kapitulation**. Die Vision bleibt: Tumblr auf das WordPress-Back-End bringen, Entwicklung vereinfachen, Kosten senken und Tumblr tiefer im **Fediverse** verankern. Der Plan ist derzeit **pausiert**: zu teuer, zu komplex für den aktuellen Zustand von Tumblr. Das strategische Ziel besteht fort.

## Warum der Plan jahrelang stockte
**Technische Schulden** und **verschiedene Tech-Stacks**: Tumblr und WordPress.com pflegten getrennte Systeme für Identität, Medien-Storage, Kommentare, Empfehlungen und Moderation. Das führt zu doppeltem Code, doppelten Teams und doppeltem Wartungsaufwand. Hinzu kommt die **Skalierung**: **Hunderte Millionen Blogs**, Milliarden von URLs, Slugs, Bildern, GIFs und Videos aus sehr unterschiedlichen Tumblr-Epochen.

Gleichzeitig ist die **Ökonomie hart**: Tumblr **verbraucht mehr, als es einnimmt**. Anzeigen und Abos decken die Betriebskosten nicht. Automattic musste **Kosten senken**, Personal in profitablere Linien (WordPress.com, WooCommerce, Jetpack) verlagern und die Migration so timen, dass sie gesunde Bereiche **nicht gefährdet**.

## Was ein WordPress-Back-End konkret brächte
- **Eine Plattform statt zwei**: gemeinsames Auth, Media, Billing, Anti-Spam, Security & Observability — weniger technische Schulden, schnellere Feature-Lieferung.  
- **Skalenvorteile**: geteilte Teams und Tools, besserer Einsatz von CDN, Caching und vereinheitlichtem Storage, niedrigere Stückkosten.  
- **Saubere Daten-Pipelines**: standardisierte APIs, stabile Schemata, leichteres A/B-Testing für beide Dienste.  
- **Pfad ins Fediverse**: mit konsolidiertem Kern lässt sich **ActivityPub** stabiler integrieren; Interoperabilität mit dezentralen sozialen Netzen wird einfacher.

## Größte technische Risiken
1. **ID-Mapping & permanente Redirects:** Jede Änderung an Permalinks/IDs braucht exakte Mapping-Tabellen, sonst leiden **SEO und Social-Signals**.  
2. **Medien-Migration & Deduplikation:** Tumblr ist medial schwergewichtig (v. a. GIFs). Erforderlich sind starkes **Caching**, **Deduplikation** und Cold-Storage für Altbestände.  
3. **Kommentare, Reblogs, Notes:** der „soziale Layer“ von Tumblr; die Semantik muss erhalten bleiben, damit die Community lebendig bleibt.  
4. **Moderation & Sicherheit:** schnelle Moderations-Workflows, Anti-Spam, Schutz vor bösartigen Kampagnen.  
5. **Datenschutz & Compliance:** **DSGVO**, Retention-Policies und Medienlizenzen vor Retro-Migration klären; klare Trennung privater/öffentlicher Signale.

<p style="text-align:center; margin:20px 0;">
  <a href="/go/mexc" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:white; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:600; display:inline-block;">
     👉 Krypto auf MEXC handeln
  </a>
</p>

## Realistischer operativer Plan (Phasen ohne Kürzung)
**Phase 0 — Kostenniveau stabilisieren**  
CDN standardisieren, aggressives Caching einführen, inaktive Medien archivieren, Duplikate reduzieren, Observability vereinheitlichen (Logs, Metriken, Tracing).

**Phase 1 — „Neu geht voraus“**  
Alle **neuen Posts** und Medien auf WordPress-Services schreiben; Altinhalte bleiben lesbar, aber wachsen nicht weiter auf dem alten Storage.

**Phase 2 — Vertikale Piloten**  
**Einen Inhaltstyp** migrieren (z. B. Text + Bilder ohne Video) für eine begrenzte Blog-Kohorte. **ID-Map** etablieren, Verluste/Performance messen (TTFB, CTR, Retention).

**Phase 3 — Horizontale Ausweitung**  
Weitere Formate (Video, GIF, Umfragen), **Comment-Bridge** einführen, Reblog/Like-Semantik bewahren. Ab hier **permanente Redirects** und kanonische URLs.

**Phase 4 — Sozialer Layer & Fediverse**  
Zunächst einseitiges Publishing nach ActivityPub, dann bidirektional (Follow, Replies) mit granularen Privacy-Settings und Spam-Schutz.

**Phase 5 — Long-Tail aufräumen**  
Deduplikation alter Medien, Edge-Cases schließen, Analytics & Reporting konsolidieren.

## Auswirkungen für Tumblr-Nutzer:innen
Im Ideal bleibt **Tumblr Tumblr**: derselbe Look & Feel, aber schneller und stabiler. Änderungen passieren „**unter der Haube**“: weniger Ausfälle, konsistentere Feeds. Für Creator bedeutet das **planbare Reichweite**, bessere Posting-Tools und intakte URLs bei Umstellungen.

## Auswirkungen auf das WordPress-Ökosystem
WordPress profitiert vom **Wissensrückfluss** aus Tumblr: kreative Formate, soziale Integrationen, schnellere Experimente. Gelingt die Migration, kann WordPress **soziale Features** optional anbieten, ohne seine CMS-Stärken zu verlieren. Für Partner (Agenturen, Publisher) ist das Signal: **einheitliche Infrastruktur**, langfristig tragfähig.

## Business-Dimension & Monetarisierung
Ohne Abbau technischer Schulden bleibt Monetarisierung limitiert. Ein konsolidiertes Back-End öffnet Wege zu **leichteren Abo-Modellen**, **weniger invasiver Werbung**, „Tip-Jar“-Spenden und Publisher-Partnerschaften. Der transparentere Kostenrahmen erleichtert **Budgetierung** und ROI-Steuerung.

## Risiken beim Status quo
- Dauerhafte **technische Schulden** und langfristig höhere Kosten.  
- Verzögerte Feature-Lieferung, langsamere Marken-Erholung.  
- Mögliches **Creator-Abwandern** zu schneller iterierenden Plattformen.

## Erfolgsmetriken
- **Stabilität & Performance:** TTFB, Error-Rate, Medien-Ladezeit.  
- **Content-Integrität:** Anteil korrekt gemappter URLs, null verlorene Kommentare/Reblogs.  
- **Ökonomie:** Kosten je 1.000 Medienaufrufe, Storage-Kosten/TB, Revenue-zu-Kosten-Quote pro Nutzer:in.  
- **Community:** aktive Creator, Retention, organisches Re-Engagement nach neuen Features.

---

**Unser Kommentar (Metaadvisor):**  
- ✅ Offenheit über den „größten Fehlschlag“ schafft Raum für **diszipliniertes Restrukturieren** statt Kosmetik.  
- ⚙️ **Migration ohne Verluste** erfordert kompromissloses ID-Mapping, kanonische URLs, permanente Redirects und Pilot-Tests.  
- 🧑‍⚖️ **Compliance** (DSGVO, Medienlizenzen, Retention) vor Retro-Migration abschließen — sonst verlagert sich Risiko nur.  
- 🌐 **Fediverse** als Bonus nach der Konsolidierung — Differenzierer, nicht Ablenkung.  
- 📈 Kurzfristig erwarten wir **Vorsicht** bei Tumblr-Investments; mittelfristig kann ein einheitliches Back-End Vertrauen bei Creators und Werbekunden zurückbringen.

---

**Quellen (ohne Links):** TechCrunch; WordCamp Canada 2025 (Town Hall).
