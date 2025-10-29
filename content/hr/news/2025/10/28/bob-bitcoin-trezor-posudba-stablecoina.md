---
title: "BOB: posudba stablecoina uz zadržavanje kontrole nad BTC-om (rollup na Bitcoinu)"
slug: "bob-bitcoin-trezor-posudba-stablecoina"
date: 2025-10-28T14:30:00Z
category: "defi"
translationKey: "7f3a6a02-b7f5-4d2c-9d3b-1c34dfbb13b0"
source: "CoinDesk"
source_url: ""
author: "CoinDesk"
analysis_by: "Metaadvisor.eu"
image_url: "/images/bob-bitcoin-vault-stablecoin.png"
featured_image: "/images/bob-bitcoin-vault-stablecoin.png"
image: "/images/bob-bitcoin-vault-stablecoin.png"
thumbnail: "/images/bob-bitcoin-vault-stablecoin.png"
image_alt: "BOB Bitcoin Vault — posudba stablecoina uz zadržavanje kontrole nad BTC-om"
image_credit: "Ilustracija — Metaadvisor.eu (simbolična slika)"
tags: ["BOB","Build on Bitcoin","Bitcoin","BTC","stablecoin","DeFi","vault","rollup","layer-2","self-custody","crypto lending","kolateral","likvidacija","TVL"]
summary: "BOB (Build on Bitcoin) donosi posudbu stablecoina uz kolateralizirani BTC bez predaje ključeva — kao rollup rješenje koje DeFi funkcionalnosti veže na Bitcoin sigurnost."
---

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="/go/mexc" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Trguj BTC-om na MEXC
  </a>
</p>

**Sažetak (što je novo)**  
Projekt **BOB (Build on Bitcoin)** predstavlja **Bitcoin Vault Liquidation Engine** — mehanizam koji omogućava vlasnicima Bitcoina da **posude stablecoine** uz BTC kao kolateral, a pritom **ne predaju kontrolu nad privatnim ključevima** (*self-custody*). U slučaju jačeg pada cijene BTC-a, sustav može **automatski likvidirati** dio kolaterala kako bi pokrio dug.

---

## Što je BOB?
**BOB = Build on Bitcoin.** To je **open-source protokol** čiji je cilj donijeti **DeFi mehanizme na Bitcoin ekosustav**. Za razliku od centraliziranih kompanija, BOB razvija **BOB tim / zajednica developera** (*BOB Builders*), često uz podršku partnerstava i VC fondova.

---

## 🔑 Kako se to radi?
Bitcoin nema izvorne pametne ugovore kao Ethereum, pa BOB koristi **layer-2 / sidechain / rollup** pristupe.

- **“Bitcoin rollup”**: omogućuje pokretanje pametnih ugovora i DeFi funkcionalnosti, dok se sigurnost **“sidri” u Bitcoin mreži** (npr. periodičkim upisima stanja/kripto-dokaza).  
- Tako nastaju **DeFi aplikacije povezane s Bitcoinom** (posudbe, vydavanje stablecoina, vaultovi) **bez mijenjanja core Bitcoin protokola**.

**Pojmovi ukratko:**  
- **Layer-2 (L2)** — dodatni sloj iznad osnovnog lanca za više funkcionalnosti/propusnosti.  
- **Rollup** — grupira transakcije off-chain i zapisuje sažetke na bazni lanac radi sigurnosti.

---

## Tko stoji iza?
Iza BOB-a stoji **BOB tim (BOB Builders)** koji objavljuje **aplikaciju, dokumentaciju i kod**. Model je blizak **open-source protokolu uz (moguću) foundation** organizaciju — slično širem Ethereum ekosustavu.

---

## Kako “Bitcoin Vault” funkcionira (visoka razina)
1) **Depozit BTC-a** u pametni ugovor (vault) povezan s BOB-om.  
2) **Posudba stablecoina** (npr. USDC/USDT ili nativno podržanih tokena) prema LTV pravilima.  
3) **Praćenje kolaterala**: pad cijene može pokrenuti **djelomičnu likvidaciju** radi održavanja zdravlja zajma.  
4) **Self-custody**: korisnik **zadržava privatne ključeve**, bez predaje imovine trećoj strani.

> Implementacijski detalji (LTV omjeri, vrste stablecoina, pragovi likvidacije, orakli) ovise o verziji protokola i mogu se mijenjati.

---

## Kako pristupiti BOB-u
Protokol je dostupan kroz **službenu aplikaciju i dokumentaciju** koje objavljuje tim BOB Builders; sav kod je **otvoren (open-source)** i dostupan zajednici. U praksi, korisnik se spaja **walletom**, koristi **bridge** za prijenos BTC-a u BOB rollup, te u aplikaciji otvara **vault** i posuđuje stablecoine.  
Trenutno se navodi oko **275 milijuna USD zaključane vrijednosti (TVL)**, što sugerira vidljivu trakciju i korištenje.

> Napomena: uvijek samostalno provjerite da koristite **službene kanale** aplikacije/dokumentacije. Ne koristimo vanjske linkove u tekstu upravo kako bismo izbjegli rizik od krivih adresa i scamova.

---

## Zašto je ovo značajno
- **Self-custody po defaultu**: filozofija “Not your keys, not your coins” ostaje očuvana.  
- **DeFi na Bitcoinu**: širi spektar financijskih usluga povezanih uz najveću kriptovalutu.  
- **Likvidnost bez prodaje BTC-a**: vlasnici dobivaju stabilne kovanice, a zadržavaju dugoročnu BTC poziciju.

---

## Šira slika i rizici
- Potencijal za **novi val DeFi aplikacija na Bitcoinu** i za privlačenje konzervativnijih ulagača.  
- **Rizici**: volatilnost BTC-a, logika **likvidacija**, ovisnost o **oraklima**, pametno-ugovorni rizici, te **regulatorni tretman** (kreditni proizvod vs. softverski protokol).  
- Prije korištenja, proučite **dokumentaciju**, parametre (LTV, kamate), te sigurnosne revizije.

---

### Naš osvrt (Metaadvisor)
- BOB pristup je u skladu s **Bitcoin ethosom**: zadržavanje ključeva i minimiziranje povjerenja.  
- **Rollup na Bitcoinu** mogao bi ubrzati “DeFi na BTC-u” i smanjiti ovisnost o alt-lancima za financijalizaciju BTC-a.  
- Ključno će biti: **robustan dizajn likvidacija**, transparentni orakli i **kvalitetne sigurnosne revizije** koda.

---

*Disclaimer: Ovaj sadržaj je informativan i ne predstavlja investicijski savjet. Prije korištenja bilo kojeg protokola samostalno provjerite službene kanale, tehničku dokumentaciju i regulatorne rizike.*
