---
title: "Tokenizacija dionica DAT tvrtki: gdje nastaju rizici i kako ih dizajnirati"
slug: "tokenizacija-dionica-dat-rizici-dizajn"
date: 2025-10-04T17:30:56Z
category: "crypto"
translationKey: "ca4b27f6891175902dae6cb0c2618bfe"
source: "Cointelegraph"
source_url: ""
source_link: false
author: "Metaadvisor.eu"
image_url: "/images/DAT-digital-asset-treasuries.png"
featured_image: "/images/DAT-digital-asset-treasuries.png"
image: "/images/DAT-digital-asset-treasuries.png"
thumbnail: "/images/DAT-digital-asset-treasuries.png"
image_alt: "Digital Asset Treasuries (DAT) i tokenizirane dionice — simbolično"
image_credit: "Metaadvisor.eu (simbolična fotografija)"
tags:
  - crypto
  - dat
  - digital-asset-treasury
  - tokenizacija
  - tokenized-stocks
  - rwa
  - 24-7-trading
  - circuit-breaker
  - governance
  - pametni-ugovori
  - smart-contract-risk
  - multisig
  - timelock
  - pause
  - incident-response
  - transfer-agent
  - disclosure
  - likvidnost
  - timing-asimetrija
  - gap-risk
  - bank-run-dinamika
  - regulacija
  - usklađenost
  - volatilnost
summary: "Kad DAT tvrtke tokeniziraju dionice, na kripto trezor dodaje se novi sloj rizika: 24/7 on-chain trgovanje, pravna mapiranja i smart-contract rizici. Donosimo konkretne rizike i dizajnerske mjere."
---

**Sažetak**  
DAT (Digital Asset Treasury) kompanije drže značajnu kripto imovinu. Kad njihove dionice postanu **on-chain tokeni**, nastaje **asimetrija vremena** (24/7 tržišta vs. burzovno radno vrijeme), uz **smart-contract/operativne** rizike i **pravne** nedorečenosti (token ↔ registrirana dionica).

## Gdje nastaju rizici

1) **Asimetrija vremena (24/7 vs. radno vrijeme)**  
Šok izvan radnog vremena (hack, vijest) može srušiti **on-chain cijenu**, dok je off-chain dionica nelikvidna; otvaranje burze hvata **gap** i pojačava panično trgovanje.

2) **“Sloj na sloj” (synthetic on synthetic)**  
Ulagač je izložen trezorskoj kripto imovini **i** korporativnoj dionici, a tokenizacija dodaje **contract/custody** sloj: bugovi, ključevi, upgrade-i.

3) **Operativni/upgrade rizici**  
Greška u ugovoru, kompromitiran ključ ili nepravilna pauza mogu **zamrznuti/preraspodijeliti** tokene. Off-chain prava dioničara sporo se preslikavaju on-chain.

4) **Pravna mapiranja i evidencija prava**  
Token ≠ automatski pravno priznata dionica. Potrebna su jasna **1:1** mapiranja s **transfer-agent** evidencijom, prospektima i procedurama po jurisdikciji.

## Kako dizajnirati sigurniji okvir

- **Uskladiti režime trgovanja:** pauza on-chain dok je off-chain zatvoren **ili** sinkronizirani **circuit-breakeri/price-bandovi**.  
- **Pravna ekvivalencija 1:1:** token reprezentira prava dioničara; “**golden source**” registar + audit trail.  
- **Tehničke kontrole:** battle-tested ugovori, **multisig + timelock** za upgrade, jasna **pause** pravila i incident-runbook.  
- **Transparentnost trezora:** dnevni snapshoti, objave promjena ključeva/ugovora, jasne **disclosure** politike.  
- **Fazno za retail:** limiti i postepeno uvođenje likvidnosti dok kontrole ne sazru.

> **Napomena o slici:** Slika je simbolična.

---

### Naš osvrt (Metaadvisor):
- Tokenizirana equity **nije “free lunch”**: **asimetrija vremena** i tehnički sloj pojačavaju šokove upravo kod DAT izdavatelja.  
- I uz 24/7 burze trebat će **brže objave** i koordinirani **circuit-breakeri**.  
- Najbrži “win”: **transparentnost** i stroga **1:1** pravna ekvivalencija token↔dionica.  
- Ulagači neka procijene: kvalitetu trezora, prava iz tokena, mogućnost **pauze** i plan oporavka.
