---
title: "Kako koristiti Google Gemini za istraživanje coina prije ulaganja"
slug: "kako-koristiti-google-gemini-za-istrazivanje-coina-prije-ulaganja"
date: 2025-10-02T11:11:23Z
category: "news"
translationKey: "15bed88f2c8685722b2d472e603c06a1"
source: "Metaadvisor.eu"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/gemini-research-coins.png"
featured_image: "/images/gemini-research-coins.png"
image: "/images/gemini-research-coins.png"
thumbnail: "/images/gemini-research-coins.png"
image_alt: "Vodič: kako uz Google Gemini istražiti kripto prije ulaganja"
image_credit: "Metaadvisor.eu (simbolična slika)"
tags:
  - gemini
  - google
  - istrazivanje
  - due-diligence
  - fundamentalna-analiza
  - onchain
  - tokenomika
  - whitepaper
  - defi
  - risk
  - marketcap
  - likvidnost
  - coingecko
  - defillama
  - tokenterminal
  - github
  - prompt-engineering
  - portfolio
  - matrix
  - kripto-vodic
summary: "Praktični workflow kako koristiti Google Gemini za brzu, a temeljitu provjeru coina prije ulaganja — konkretni prompti, izvori podataka, on-chain i fundamentalne checkliste te crvene zastavice."
---

**Gemini** može ubrzati tvoj **kripto due diligence**, ali ključ je tražiti **provjerljive izvore**, zadržati **kritički filter** i rezultate **ukrstiti s podacima** (CoinGecko, DeFiLlama, Token Terminal, GitHub…). U nastavku je **korak-po-korak** workflow i gotovi **prompte** (copy/paste) za praktičan rad u Geminiju.

> **Napomena:** *Slika je simbolična.*

---

## 1) Brzi “project snapshot”
**Prompt:**  
> “Sažmi projekt **{COIN/PROJEKT}** u 6 rečenica: problem koji rješava, tržište, ključni modul/protokol, tim/financiranje, mreža/layer, status proizvoda (mainnet/testnet). Dodaj 3 najrelevantnija izvora (whitepaper, docs, GitHub).”

**Što gledati:** live proizvod vs. roadmap, provjerljive veze tima (LinkedIn/GitHub), **reference > marketing**.

---

## 2) Tokenomika i raspodjela
**Prompt:**  
> “Izvedi tablicu tokenomike za **{TOKEN}**: total/max/circulating supply, raspored otključavanja (mj.), alokacije (team, investitori, treasury, ekosustav), trenutačna i projekcija inflacije. Uključi izvore.”

**Provjere:** veliki **unlockovi** u idućih 3–12 mj.; visok udio tima/investitora (≥30–40% = rizik); postoji li **stvarni utility** (fee, staking, governance, collateral).

---

## 3) Likvidnost i tržišni profil
**Prompt:**  
> “Nabroji burze/parove s najvećim volumenom za **{TOKEN}**, procijeni realnu likvidnost (order book depth 2%/5%), koncentraciju top walleta i dnevni on-chain promet. Izvori: CoinGecko/CMC, DEX screener, chain explorer.”

**Čeklista:** koncentracija (top10 >60% supplya?), **market-making** bez dubine, rizici **mostova/wrappinga**.

---

## 4) On-chain zdravlje i usvajanje
**Prompt:**  
> “Daj 6-mjesečni trend: aktivni korisnici, broj transakcija, TVL (ako DeFi), prihodi protokola te fee burn/issuance za **{PROJEKT/TOKEN}**. Uključi graf i linkove (DeFiLlama, Token Terminal, Dune).”

**Tumačenje:** održiv **rast** vs. hype, **cash-flow** (naknade/spread/MEV), ovisnost o **poticajima**.

---

## 5) Tehnički rizici (kod i sigurnost)
**Prompt:**  
> “Analiziraj sigurnost **{PROJEKT}**: audit(i) i datum, kritične ranjivosti, open-source status, frekvencija commitova, broj contribora i otvoreni issuei. Izvori: GitHub, audit izvještaji, bug bounties.”

**Red flags:** bez audita / audit >12 mj.; **admin ključevi** bez multisiga; nizak broj recentnih commitova.

---

## 6) Regulatorni okvir i dostupnost
**Prompt:**  
> “Sažmi regulatorni/pravni rizik za **{TOKEN}** (US/EU/UK/HK): security vs. commodity, KYC/AML, ograničenja listanja/custody, relevantni pravni događaji.”

**Napomena:** za retail u EU provjeri **MiCA** (whitepaper, marketing, stablecoini).

---

## 7) Portfeljna odluka — matrica
**Prompt:**  
> “Ocijeni (0–5) **{TOKEN}** po: tim, proizvod, tokenomika, likvidnost, on-chain usvajanje, prihodi, sigurnost, regulatorni rizik. Predloži pondere, izračunaj score i napiši bull/bear tezu + invalidation.”

**Primjena:** limitiraj **veličinu pozicije**, koristi **DCA** umjesto all-in, postavi **stop-loss** na razinama koje likvidnost podržava.

---

## 8) Brzi „ready-to-use” prompti
- “One-pager za {TOKEN} s linkovima na **whitepaper/docs/GitHub**.”  
- “Izvuci **vesting raspored** (datumi/količine); procijeni **sell pressure** pri trenutačnoj likvidnosti.”  
- “Usporedi {TOKEN} s **{PEER1}** i **{PEER2}**: TVL, prihodi, aktivni korisnici, **FDV/TVL**, **P/S**; izvedi **relativnu valuaciju**.”  
- “Nabroji **3 najveća rizika** i **3 katalizatora** u sljedećih 90 dana (mainnet, airdrop, listanje, unlock).”

---

## Česte “crvene zastavice”
- Visoka **FDV** uz mali float (unlock tsunami).  
- **Ponzi-like** prinos bez stvarnog cash-flowa.  
- (Pseudo)anonimni tim bez tragova.  
- Ovisnost o jednom **mostu/oraklu**.  
- **Sponzorirane recenzije** bez neovisnih izvora.

---

> **Podsjetnik:** Kao i svaki LLM, Gemini može **hallucinirati**. Uvijek **otvori izvore** i provjeri brojke u **primarnim alatima** (CoinGecko/CMC, DeFiLlama, Token Terminal, Dune, explorers).

---

### Naš osvrt (Metaadvisor)

- **LLM kao copilot, ne orakul**: vrijednost dolazi iz **ukrštanja s podacima** i **discipliniranog risk-managementa**.  
- **Proces = edge**: standardizirani **prompti + checkliste** filtriraju šum i izbjegavaju skupe greške (unlockovi, lažna likvidnost).  
- **Institucionalni trend**: tokenizirani podaci i on-chain izvještavanje postaju standard; **LLM + data izvori** daju i brzinu i točnost.  
- **Ograničenja**: bez verifikacije **realnog volumena** (order-book depth) i **izvora**, i najbolji sažetak ostaje — priča.

---

### Disclaimer 
Ovaj sadržaj služi isključivo u **informativne i obrazovne svrhe** i **ne predstavlja investicijski savjet** niti ponudu za kupnju/prodaju financijskih instrumenata ili kriptoimovine. Trgovanje kriptoimovinom nosi **visok rizik gubitka**. Prije odluke, provedite **vlastito istraživanje (DYOR)** i, po potrebi, konzultirajte **neovisnog stručnjaka**.
