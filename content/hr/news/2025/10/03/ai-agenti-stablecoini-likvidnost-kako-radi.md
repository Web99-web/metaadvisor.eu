---
title: "AI agenti kao pokretači likvidnosti za stablecoine: kako će to praktično raditi"
slug: "ai-agenti-stablecoini-likvidnost-kako-radi"
date: 2025-10-04T08:30:00Z
category: "ai"
translationKey: "9f0f7a2a2f2b4c3f9a31d6f2a1b7e8c5"
source: "Cointelegraph (povod/intervju)"
source_url: "https://cointelegraph.com/news/ai-agents-liquidity-fragmented-stablecoin-paxos-labs"
author: "Metaadvisor.eu"
image_url: "/images/ai-agenti-stablecoini.png"
featured_image: "/images/ai-agenti-stablecoini.png"
image: "/images/ai-agenti-stablecoini.png"
thumbnail: "/images/ai-agenti-stablecoini.png"
image_alt: "AI agent i digitalni novčić — simbolično"
image_credit: "Metaadvisor.eu (simbolična grafika)"
tags:
  - ai
  - agenti
  - stablecoin
  - paxos
  - erc-4337
  - account-abstraction
  - paymasters
  - ap2
  - x402
  - ccip
  - cctp
  - interoperabilnost
  - tokenizacija
  - mikrotransakcije
  - e-trgovina
  - compliance
  - kyc
  - risk
  - web3
summary: "AI agenti mogu samostalno plaćati, prebacivati i arbitrirati stablecoine preko više mreža — uz account abstraction (ERC-4337), agent-native naplatu (AP2/x402) i cross-chain railove (CCTP/CCIP). Tako fragmentacija tržišta postaje prednost, a likvidnost brže teče prema najefikasnijim izdavateljima."
---

**Sažetak**  
Izjava Paxos Labsa da bi **AI agenti** mogli postati novi pokretači **likvidnosti stablecoina** dobiva sve više tehničke podloge: standardi za **agent-native plaćanja**, **smart accounti** bez plina (gasless) i **cross-chain** railovi za sigurno poravnanje.

## Kako to radi — end-to-end

1) **Agent + pametni novčanik (ERC-4337)**  
Agent upravlja **smart accountom** s pravilima (limiti, whitelist, session ključevi). **Paymasteri** omogućuju plaćanje naknada u **stablecoinu** ili sponzorirani gas.

2) **Nalog i naplata (AP2 / x402 / HTTP 402)**  
Trgovac izazove plaćanje (HTTP 402). Agent odgovara **mandatom** (kriptografski potpisana suglasnost) i izvršava uplatu u stablecoinu **bez ručnog klikanja** svake mikrotransakcije.

3) **Odabir coina i rute**  
Agent optimizira **ukupnu cijenu i latenciju**: koji stablecoin, koji lanac, koji paymaster/most. U igri su i jurisdikcijska pravila i likvidnost na burzama/DEX-ovima.

4) **Cross-chain pokretljivost (CCTP/CCIP)**  
Ako je ciljna aplikacija na drugom lancu, agent koristi **CCTP** (nativni burn-and-mint USDC) ili **CCIP** (sigurni cross-chain pozivi/poravnanje) — **bez klasičnog “bridganja”**.

5) **Poravnanje i revizija**  
Transakcije se bilježe **on-chain**, a metapodaci (mandat, referenca) služe za **revizijski trag**, povrate i usklađenost.

## Primjeri (konkretni tokovi)
- **E-commerce agent:** prima 402 zahtjev, plaća USDC-om preko x402; po potrebi “teleportira” novac CCTP-om na lanac trgovca.  
- **API/data agent:** mikroplaćanja po pozivu; automatski nadopunjuje depozit kad padne ispod praga.  
- **Treasury agent:** rotira između izdavatelja (USDC/PYUSD/…), koristi CCIP/CCTP za **just-in-time** rebalans.

## Ispod haube (tehničke karike)
- **Account abstraction (ERC-4337):** `UserOperation` bundleovi, ERC-20 gas, oporavak računa.  
- **AP2/x402 sloj:** zajednički jezik za **autonomne naplate**; stablecoini su nativno globalni i programabilni.  
- **CCTP/CCIP:** nativni mint/burn ili sigurni poravnalni kanali za **efikasno cross-chain kretanje**.

## Šira slika i implikacije
- **Kompresija naknada i natjecanje izdavatelja:** agenti trenutno preusmjeravaju promet tamo gdje je **najniža ukupna cijena + najbolji SLA**.  
- **Mikrotransakcije napokon imaju smisla:** gasless UX + standardizirani mandati.  
- **Compliance-by-design:** mandati + verifiable credentials + politike pristupa olakšavaju **KYC/AML**.  
- **Rizici:** zlouporaba mandata, mostovi kao točke rizika, “permission sprawl” — rješavati **limitima, rate-limitom i kratkim session ključevima**.

> **Napomena o slici:** Slika je simbolična.

---

### Naš osvrt (Metaadvisor):
- Agent-native plaćanja spajaju **UX bez trenja** i **cross-chain efikasnost** — to je ključ za realnu adopciju.  
- Pobjeđuju railovi i izdavatelji s **niže-ukupnim troškom** i **stabilnim vremenom poravnanja**.  
- Glavna prepreka je **povjerenje u mandate** (tko potpisuje, limiti, opoziv).  
- Kratkoročno očekujemo rast **mikroplaćanja** (API/sadržaj) i **treasury agenata** u poduzećima.
