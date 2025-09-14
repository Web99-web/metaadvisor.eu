---
title: "Što je L2 (layer-2) — i zašto vašoj tvrtki vjerojatno ne treba vlastiti Ethereum L2"
slug: "sto-je-l2-i-zasto-vjerojatno-ne-treba-vlastiti-ethereum-l2"
date: 2025-09-13T18:00:00Z
category: "news"
translationKey: "deb9039d3dd61126d44c252223bbf1ba"
source: "MetaAdvisor"
sources:
  - name: "CoinDesk (op-ed): Your Company Probably Doesn’t Need Its Own L2"
    url: "https://www.coindesk.com/opinion/2025/09/09/your-company-probably-doesn-t-need-its-own-l2"
    date: "2025-09-09"
image_url: "/images/eth.jpg"
image_alt: "Shema Ethereum L1 i L2 (rollup) — objašnjenje"
image_credit: "MetaAdvisor Library"
tags: ["ethereum", "layer2", "rollups", "objašnjenje"]
summary: "L2 je “drugi sloj” iznad Ethereuma: obrađuje transakcije izvan glavnog lanca i na L1 objavljuje dokaze — brže i jeftinije. Vlastiti L2 većini tvrtki ne donosi realnu korist."
our_take: "Kreni tamo gdje su korisnici i likvidnost; vlastiti L2 ima smisla tek kad metrike to jasno opravdaju."
---

**Ukratko: što je L2?**  
L2 (layer-2) je dodatni sloj nad Ethereumom (L1). Tamo se transakcije **grupiraju/izvršavaju**, a **dokazi** i/ili **sažeci podataka** objavljuju natrag na Ethereum kako bi se zadržala sigurnost glavnog lanca.  
- **Zašto postoji:** niže naknade, veća propusnost.  
- **Kako radi:** najčešće kao *rollup* — *optimistic* (osporiv) ili *zk* (kriptografski dokaz).  
- **Što dobivate:** brzinu i niže troškove uz sigurnosnu sidrenicu Ethereuma.

Sve više tvrtki razmišlja o “vlastitom L2-u”. Zvuči moćno, ali u praksi je često **skupa distrakcija**. Umjesto gradnje na zrelom L2-u, završite s malim, izoliranim otokom koji traži stalni **operativni tim** (sekvencer, monitoring, incidenti, nadogradnje), **mostove** i **MEV politiku** — uz reputacijske i pravne rizike.

**Zašto najčešće ne:** fragmentacija likvidnosti i korisnika, visoki TCO i operativni teret, rizici mostova/nadogradnji, te činjenica da postoje **snažne alternative** (zreli L2-ovi i “rollup-as-a-service”).

**Kada ima smisla?**  
Ako imate **veliku distribuciju** i **vrlo specifične zahtjeve** (privacy/compliance, performanse, monetizacija na razini protokola). Često je pametnije **početi kao app na postojećem L2-u** (ili kao L3) i **tek kasnije** izdvojiti vlastiti rollup kad to metrike traže.

**Checklist prije odluke:** korisnička korist vs. postojeći L2; izbor dokaza (optimistic/zk) i DA sloja; model sekvencera i mitigacija centralizacije; dizajn mostova; incident/rollback plan; monitoring i ritam nadogradnji.

## Naš osvrt
Budite **metrics-first**. Shipajte na provjerenom L2-u, validirajte potražnju i tek potom razmišljajte o vlastitom L2-u.
