---
title: "Skrivena sila iza skokova cijena Bitcoina i Ethera: dospijeće opcija (options expiry)"
slug: "skrivena-sila-iza-skokova-cijena-bitcoina-i-ethera-dospijece-opcija"
date: 2025-09-28T07:55:08Z
category: "crypto"
translationKey: "5e2a172f9c676672fff8bce8b9d5128a"

author: "Metaadvisor.eu"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/the-hidden-force-behind-bitcoin-and-ether-price-swings-options-expiry?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"

image_url: "/images/btc3.jpg"
featured_image: "/images/btc3.jpg"
image: "/images/btc3.jpg"
thumbnail: "/images/btc3.jpg"
image_alt: "BTC/ETH volatilnost i options expiry (simbolično)"
image_credit: "Metaadvisor.eu"

tags:
  - crypto
  - bitcoin
  - ethereum
  - options
  - options-expiry
  - opex
  - derivatives
  - open-interest
  - max-pain
  - gamma
  - dealers
  - hedging
  - volatility
  - skew
  - implied-volatility
  - perps
  - futures
  - funding
  - liquidity

summary: "Tjedna, mjesečna i kvartalna dospijeća opcija (OPEX) stvaraju valove ponude i potražnje koji mogu pomicati BTC/ETH cijene oko razina „max pain“. Objašnjavamo mehaniku, tipične obrasce i što pratiti u praksi."
---

> **Napomena:** Slika je simbolična.

## Uvod — zašto se cijene „odjednom” pomiču na iste razine
Ako primjećuješ da se **Bitcoin** i **Ether** krajem tjedna ili mjeseca često „prilijepe“ uz određene razine, vrlo vjerojatno gledaš **efekt dospijeća opcija (options expiry, OPEX)**. Na isteku se zatvaraju/poravnavaju tisuće ugovora s **koncentriranim open interestom** na nekolicini strikeova, pa **market makeri (dealeri)** i drugi sudionici moraju prilagođavati **hedging** — što može **privući** cijenu prema zoni gdje je zbirna vrijednost opcija **najmanja** (tzv. **max pain**), ili pak izazvati **naglo „otpuštanje opruge“** nakon isteka.

---

## Mehanika (bez žargona)
1. **Open interest** se gomila na najpopularnijim strikeovima (npr. 60k, 62k, 65k za BTC).  
2. Kako se bliži **expiry**, dealeri dinamički rade **delta/gamma hedging** da neutraliziraju rizik dok opcije gube vrijeme (theta).  
3. Hedging je **stvarna kupnja/prodaja** spota ili perpsa → to **pomiče cijenu**.  
4. Ako je OI velik i zbijen, cijena se lakše **stabilizira** oko **max pain** razine; ako je asimetričan, češće dobijemo **mini-squeeze**.  
5. **Nakon isteka** taj tehnički pritisak nestaje i cijena često **„prodiše“** u novom rasponu.

---

## Ilustrativni primjer (simbolični brojevi)
- U petak dospijeva **$3B BTC opcija**.  
- Najveći OI: **call 65k**, **put 60k** → izračun **max pain ≈ 62k**.  
- Dok je spot 63–64k, dealeri **prodaju** (da smanje deltu od callova); ako padne prenisko, **kupovat će** (da pokriju put deltu).  
- Rezultat: gravitacija oko **62k** do 16:00 UTC.  
- **Dan poslije**: hedging isparava → raspon i volatilnost se **premještaju**.

---

## „Max pain” — korisno, ali ne svemoguće
**Max pain** je razina gdje je **zbirna isplativost opcija minimalna**.  
- **Zašto često „radi“?** Jer **dealeri**, kao glavni prodavatelji opcija, hedgiranjem **guraju** tržište prema zoni najmanjeg rizika.  
- **Kada ne radi?** Kada **makro** (ETF tokovi, vijesti, velika likvidacija perpsa) **pregazi** OPEX signal ili je OI raspršen bez jasnog centra.

---

## BTC vs. ETH — isti princip, drukčija dinamika
- **BTC**: dublja likvidnost, često **čistiji** max-pain magnet na tjednim/mjesečnim istecima.  
- **ETH**: dodatno utječu **staking/DeFi** i cross-hedging na L2 perpsima, pa su **post-expiry** potezi ponekad **oštriji**.

---

## Kalendar za trejdere
- **Tjedni**: petkom (kratkoročni „magnet“).  
- **Mjesečni**: zadnji petak u mjesecu (veći OI, jači efekt).  
- **Kvartalni**: ožujak, lipanj, rujan, prosinac — često najizraženiji pomaci.

---

## Što pratiti (praktično)
- **Koncentracija OI po strikeovima** (koliko je „nagurano“ oko 1–2 razine).  
- **Put/Call omjer i skew** (nagib IV): sugeriraju pritisak i smjer rizika.  
- **Gamma exposure (GEX)**: pozitivna gamma → smiruje trzaje; negativna → pojačava ih.  
- **Funding & basis** (perps/futures): visoki pozitivni funding znači da **long strana plaća** → lakše spuštanje prema max painu.  
- **Kolizija s makro događajima**: FOMC, velike objave, unlockovi mogu **nadglasati** OPEX.

---

## Pojmovnik
- **Options expiry (OPEX)** — dospijeće opcija; dan kada ugovor prestaje vrijediti.  
- **Open Interest (OI)** — broj aktivnih (neporavnatih) ugovora.  
- **Max pain** — razina cijene na kojoj su kupci opcija (call+put) ukupno najviše „povrijeđeni“.  
- **Delta/Gamma hedging** — dinamičko pokriće portfelja kupnjom/prodajom spota/perpsa.  
- **Implied Volatility (IV)** — očekivana buduća volatilnost ugrađena u cijenu opcije.  
- **Skew** — razlika u IV između callova i putova (asimetrija straha/pohlepe).  
- **Funding** — periodična naknada između long/short strana na perpetualima.

---

## Naš osvrt (Metaadvisor)
- **OPEX je mehanika, ne magija.** Kod velikog i koncentriranog OI-a očekuj „magnetski“ efekt — osim ako makro ne promijeni igru.  
- **Greška retaila:** loviti „točan trenutak“ na sam dan isteka; često je bolje planirati **dan–dva prije** ili **dan poslije**.  
- **Za investitore:** OPEX je kratkoročni **šum**; dugoročne odluke ne oslanjaj na njega.  
- **Za trejdere:** kombiniraj **OI/GEX/funding** s kalendarom isteka i disciplinom u veličini pozicije.

*Informativni sadržaj. Nije financijski savjet.*
