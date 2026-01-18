---
title: "Čuli ste za gas fee u kriptu, a ne znate što to znači? I zašto vam to nitko ne objasni"
slug: "sto-je-gas-fee-u-kriptu-i-zasto-nitko-ne-objasni"
date: 2026-01-18T06:30:00
category: "crypto"
translationKey: "gas_fee_crypto_explained_20260118"
source: ""
source_url: ""
author: "MetaAdvisor.eu"
image_url: "/images/Gas-fee-in-crypto.png"
featured_image: "/images/Gas-fee-in-crypto.png"
image: "/images/Gas-fee-in-crypto.png"
thumbnail: "/images/Gas-fee-in-crypto.png"
image_alt: "Gas fee u kriptu kao simbol troška blockchain transakcija"
image_credit: "MetaAdvisor / simbolična ilustracija"
summary: "Gas fee je jedan od glavnih razloga zašto se ljudi u kriptu boje kliknuti pogrešan gumb. Objašnjavamo što je gas fee, kada se plaća, u čemu se plaća i gdje ga točno moraš imati — wallet po wallet, bez tehničkog žargona."
tags: ["crypto","kripto","gas-fee","blockchain","metamask","phantom","trust-wallet","ledger","ethereum","solana","defi","edukacija"]
---

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Ostvari Bitget bonus do 6200 USDT — registriraj se ovdje
  </a>
</p>

<p style="font-size:0.85em; color:#666; margin-top:-6px;">
Slika je simbolična.
</p>

# Čuli ste za gas fee, ali nitko vam ne zna objasniti što je to

Jedan od najvećih izvora zbunjenosti u kriptu je **gas fee**. To je pojam koji se stalno spominje, ali se rijetko objašnjava ljudskim jezikom, unaprijed i na jednom mjestu. Rezultat je da se korisnici boje kliknuti “Confirm”, ne znaju zašto transakcija ne prolazi ili zašto im “fali nešto”, iako imaju sredstva.

To nije zato što su ljudi neuki.  
To je zato što je sustav dizajniran tako da **ne objašnjava vlastita pravila**.

## Što je gas fee (najjednostavnije moguće)

**Gas fee** je **naknada za izvršenje transakcije na blockchainu**.

Drugim riječima:
- blockchain ne radi besplatno  
- netko mora obraditi tvoju transakciju  
- gas fee je cijena tog rada  

👉 Gas **nije porez**, **nije provizija burze** i **nije kazna**.  
👉 To je **gorivo mreže**.

Ako nemaš gorivo → transakcija se **ne može izvršiti**.

## Kada se gas fee plaća

Gas fee se plaća **SVAKI PUT kada radiš nešto izravno na blockchainu (on-chain)**.

### Primjeri kada se **PLAĆA gas**:
- slanje kripta iz walleta u wallet  
- swap (zamjena) tokena na decentraliziranim burzama (DEX)  
- bridge (prebacivanje tokena s jednog blockchaina na drugi)  
- mintanje NFT-a  
- stake / unstake  
- odobravanje pametnog ugovora (“approve”)  
- povlačenje sredstava iz DeFi protokola  

### Primjeri kada se **NE PLAĆA gas**:
- trgovanje unutar centralizirane burze  
- kupnja ili prodaja bez povlačenja u wallet  
- interno prebacivanje sredstava unutar burze  

📌 Čim izađeš iz burze → na blockchain → **gas je obavezan**.

## U čemu se gas fee plaća (najčešća zamka)

Gas se **uvijek plaća u native coinu blockchaina**, a ne u tokenu koji šalješ.

Primjeri:
- Ethereum → gas se plaća u **ETH**  
- Solana → gas se plaća u **SOL**  
- BNB Chain → gas se plaća u **BNB**  
- Polygon → gas se plaća u **MATIC**  
- Avalanche → gas se plaća u **AVAX**  
- Arbitrum → gas se plaća u **ETH**  
- Optimism → gas se plaća u **ETH**  
- Base → gas se plaća u **ETH**

👉 Ako imaš token, ali **nemaš native coin** → transakcija **ne ide**.

Zato ljudi često vide poruku:
> “Insufficient funds for gas”

## Gdje točno moraš imati gas — wallet po wallet

Ovo je dio koji gotovo nitko ne objašnjava jasno, a upravo tu nastaje najveća zbunjenost. **Gas ne plaća aplikacija, nego blockchain**, a wallet je samo sučelje.

### 🦊 MetaMask — najčešći izvor panike

MetaMask se koristi za:
- Ethereum  
- Arbitrum  
- Optimism  
- Base  
- BNB Chain  
- Polygon  
- Avalanche  

Gas moraš imati u **native coinu tog chaina**:
- **ETH** → Ethereum, Arbitrum, Optimism, Base  
- **BNB** → BNB Chain  
- **MATIC** → Polygon  
- **AVAX** → Avalanche  

📌 Ako imaš USDT ili USDC, ali **nemaš ovaj coin**, transakcija ne ide.  
📌 MetaMask **ne posuđuje gas** i **ne upozorava jasno unaprijed**.

### 🟣 Phantom — jednostavniji, ali ista pravila

Phantom se koristi primarno za **Solanu**.

- Gas se plaća u **SOL**  
- Naknade su male, ali **SOL moraš imati**

Ako imaš SPL token, ali nemaš SOL → **ne možeš ništa napraviti**.

### 🔵 Trust Wallet — fleksibilan, ali opasan za početnike

Trust Wallet radi s više chainova:
- Ethereum  
- BNB Chain  
- Polygon  
- Avalanche  
- i drugima  

Problem je što moraš:
- znati **na kojem si chainu**
- imati **odgovarajući native coin**

Aplikacija to rijetko objašnjava jasno.

### 🔐 Ledger — česta zabluda

Ledger **ne plaća gas umjesto tebe**.  
On samo **potpisuje transakciju**.

Ako Ledger koristiš preko MetaMaska ili Trust Walleta, vrijede **ista pravila** kao za te wallete.

## Najčešće greške (i zašto se stalno događaju)

❌ Imaš USDT, ali nemaš ETH za gas  
❌ Imaš ETH, ali na pogrešnom chainu  
❌ Imaš token na L2, ali nemaš ETH za L2 gas  
❌ Ne znaš da i “approve” troši gas  
❌ Ne znaš da gas cijena ovisi o gužvi na mreži  

To nisu početničke greške.  
To su **loše dizajnirana pravila bez objašnjenja**.

## Zašto je ovo ogroman UX problem

U tradicionalnim financijama:
- ne moraš znati kako banka obrađuje uplatu  
- ne zanima te infrastruktura  
- naknada je jasna unaprijed  

U kriptu se od korisnika očekuje da:
- razumije infrastrukturu  
- zna razliku između chainova  
- zna u kojem coinu plaća gas  

I to se smatra normalnim.

## Zaključak

Gas fee nije problem sam po sebi.  
Problem je što se od korisnika očekuje da **razumije sustav koji mu nitko nije objasnio**.

Ako kripto želi masovno usvajanje:
- gas mora postati **nevidljiv**
- ili barem **jasno objašnjen unaprijed**

Dok se to ne dogodi, strah od MetaMaska i pogrešnog klika ostat će realnost, a ne iznimka.

---

## Naš osvrt (MetaAdvisor):
- Gas fee je tehnički nužan, ali korisnički loše objašnjen.
- Strah od pogrešnog klika nije slabost korisnika, nego loš UX.
- Kripto mora sakriti kompleksnost, a ne je prebacivati na ljude.
- Edukacija mora biti dio proizvoda, a ne naknadna obveza.

<p style="font-size:0.8em; color:#777; margin-top:24px;">
<strong>Odricanje od odgovornosti:</strong> Ovaj sadržaj služi isključivo u informativne i edukativne svrhe te ne predstavlja financijski savjet, preporuku za ulaganje ili poziv na kupnju ili prodaju financijskih instrumenata. Ulaganje u kriptovalute nosi visok rizik i svatko donosi odluke na vlastitu odgovornost.
</p>
