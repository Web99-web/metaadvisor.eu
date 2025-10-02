---
title: "Kako koristiti Google Gemini za istraživanje coina prije ulaganja"
slug: "kako-koristiti-google-gemini-za-istrazivanje-coina-prije-ulaganja"
date: 2025-10-02T11:11:23Z
category: "news"
translationKey: "15bed88f2c8685722b2d472e603c06a1"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/how-to-use-google-s-gemini-to-research-coins-before-you-invest?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
author: "Cointelegraph"
analysis_by: "Metaadvisor.eu"
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
summary: "Praktični workflow kako koristiti Google Gemini za brzu, a temeljitu provjeru coina prije ulaganja — konkretni prompti, izvori podataka, on-chain i fundamentalne checkliste te crvene zastavice."
---

**Gemini** može ubrzati tvoj **kripto due diligence**, ali ključ je tražiti **provjerljive izvore**, zadržati **kritički filter** i rezultate **ukrstiti s podacima** (CoinGecko, DeFiLlama, Token Terminal, GitHub…). U nastavku je **korak-po-korak** workflow i gotovi **prompti** (copy/paste) koje koristiš u Geminiju.

> **Napomena:** *Slika je simbolična.*

---

## 1) Brzi “project snapshot”
**Prompt:**  
> “Sažmi projekt **{COIN/PROJEKT}** u 6 rečenica: problem koji rješava, tržište, ključni modul/protokol, tim/financiranje, mreža/layer, status proizvoda (mainnet/testnet). Dodaj 3 najrelevantnija izvora (whitepaper, docs, GitHub).”

**Što gledati:** radni proizvod vs. roadmap, povezanost tima (LinkedIn/GitHub), jesu li navodi **referencirani** (ne marketinški blog).

---

## 2) Tokenomika i raspodjela
**Prompt:**  
> “Izvedi tablicu tokenomike za **{TOKEN}**: total/max/circulating supply, raspored otključavanja (mj.), alokacije (team, investitori, treasury), inflacija sada i projekcija. Navedi izvore.”

**Provjere:** veliki **unlockovi** u idućih 3–12 mj.; udio tima/investitora (≥30–40% = rizik); stvarni **utility** (fee/staking/governance/collateral).

---

## 3) Likvidnost i tržišni profil
**Prompt:**  
> “Nabroji burze/parove s najvećim volumenom za **{TOKEN}**, procijeni realnu likvidnost (order book depth 2%/5%), koncentraciju top walleta i dnevni on-chain promet. Izvori: CoinGecko/CMC, DEX screener, chain explorer.”

**Čeklista:** koncentracija (top10 >60% supplya?), **market-making** bez dubine, **mostovi/wrappanje** (dodatni smart-contract rizici).

---

## 4) On-chain zdravlje i usvajanje
**Prompt:**  
> “Daj 6-mjesečni trend: aktivni korisnici, broj transakcija, TVL (ako DeFi), prihodi protokola, fee burn/issuance za **{PROJEKT/TOKEN}**. Uključi graf i linkove na izvore (DeFiLlama, Token Terminal, Dune).”

**Tumačenje:** rast korisnika/TVL vs. hype, postojanje **cash-flowa** (naknade/spread/MEV), ovisnost o **poticajima**.

---

## 5) Tehnički rizici (kod i sigurnost)
**Prompt:**  
> “Analiziraj sigurnost **{PROJEKT}**: auditi i datum, kritične ranjivosti, open-source status, frekvencija commitova, broj contribora, otvoreni issuei. Izvori: GitHub, audit izvještaji, bug bounties.”

**Red flags:** bez audita / audit stariji od 12 mj.; **admin ključevi** bez multisiga; nizak broj recentnih commitova.

---

## 6) Regulatorni okvir i dostupnost
**Prompt:**  
> “Sažmi regulatorni rizik za **{TOKEN}** (US/EU/UK/HK): status security/commodity, KYC/AML, ograničenja listanja/custody, relevantni pravni događaji.”

**Napomena:** za retail u EU provjeri **MiCA** (whitepaper, marketing, stablecoini).

---

## 7) Portfeljna odluka — matrica
**Prompt:**  
> “Ocijeni (0–5) **{TOKEN}** po: tim, proizvod, tokenomika, likvidnost, on-chain usvajanje, prihodi, sigurnost, regulatorni rizik. Dodaj pondere i izračunaj score. Napiši bull & bear tezu i invalidation.”

**Primjena:** limit **veličine pozicije**, DCA umjesto all-in, **stop-loss** na razinama koje likvidnost podržava.

---

## 8) Brzi “ready-to-use” prompti
- “One-pager za {TOKEN} s linkovima na **whitepaper/docs/GitHub**.”  
- “Izvuci **vesting raspored** (datumi i količine); procijeni **prodajni pritisak** pri trenutačnoj likvidnosti.”  
- “Usporedi {TOKEN} s **{PEER1}** i **{PEER2}**: TVL, prihodi, aktivni korisnici, **FDV/TVL**, **P/S**; izvedi **relativnu valuaciju**.”  
- “Nabroji **3 najveća rizika** i **3 katalizatora** u sljedećih 90 dana (mainnet, airdrop, listanje, unlock).”

---

## Česte “crvene zastavice”
- Visoka **FDV** uz malu cirkulaciju (unlock tsunami).  
- **Ponzi-like** prinos bez realnog cash-flowa.  
- **Anonimni/pseudo-anonimni tim** bez tragova.  
- Ovisnost o jednom **mostu/oraklu**.  
- **Sponzorirane recenzije** bez neovisnih izvora.

---

> **Podsjetnik:** Gemini (kao i svaki LLM) može **hallucinirati**. Uvijek **klikni izvore** i provjeri brojke u **primarnim alatima** (CoinGecko/CMC, DeFiLlama, Token Terminal, Dune, explorers).

---

### Naš osvrt (Metaadvisor)

- **LLM kao copilot, ne orakul**: Vrijednost je u **ukrštanju s podacima** i **discipliniranom risk-managementu**.  
- **Prednost je u procesu**: standardizirani **prompti + checkliste** filtriraju šum i sprječavaju skupe greške (unlockovi, lažna likvidnost).  
- **Institucionalni trend**: tokenizirani podaci i on-chain izvještavanje postaju standard; **LLM + data izvori** daju najbolji omjer brzine i točnosti.  
- **Ograničenja**: bez provjere **realnog volumena** (order book depth) i **izvora**, i najbolji sažetak je samo — priča.
