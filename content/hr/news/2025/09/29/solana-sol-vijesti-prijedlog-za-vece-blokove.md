---
title: "Solana (SOL) — prijedlog za veće blokove nakon Alpenglow nadogradnje"
slug: "solana-sol-vijesti-prijedlog-za-vece-blokove"
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
image_alt: "Solana logotip i mreža — prijedlog za veće blokove"
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

summary: "Firedancer tim (Jump Crypto) predložio je SIMD-0370: uklanjanje blokovskog ograničenja compute-unitsa nakon Alpenglow nadogradnje. Cilj je omogućiti veće blokove i veću propusnost — uz raspravu o rizicima centralizacije i propagacije."
---

> **Napomena:** Slika je simbolična.

## Što je predloženo
Firedancer dev tim (Jump Crypto) objavio je prijedlog **SIMD-0370** koji bi **ukinuo blokovsko ograničenje compute-unitsa (CU)** na Solani (trenutno ~**60 milijuna CU** po bloku). Ideja je da nakon **Alpenglow** nadogradnje **proizvođači blokova** mogu pakirati **veće blokove** ovisno o performansama validatora.

Podsjetnik: ranije je postojao prijedlog za **povećanje** limita na **100M CU**; ovaj korak ide dalje — **ukidanje** limita na razini bloka.

## Zašto to žele
- **Više transakcija u špici** (lansiranja tokena, DeFi “spikes”) → **manje neuspjelih swapova** i “mempool” gužvi.  
- **Fleksibilnost po validatoru:** brže konfiguracije mogu obraditi više posla bez čekanja na globalni “čep”.

## Potencijalni rizici (kratko i jasno)
- **Propagacija i latencija:** veći blokovi duže putuju mrežom → **više forkova/orphan-slotova** i moguće **povećanje kašnjenja**.  
- **Hardverska utrka:** validatori s jačim serverima imaju prednost → **centralizacijski pritisak**.  
- **MEV i tržišna mikrostruktura:** veće “batch” jedinice mogu povećati **sandwich/arb** prozore ako se mempool signali koncentriraju kod jačih čvorova.  
- **Korisničke naknade:** ako potražnja *zbilja* poraste, **medijan fee** može rasti bez obzira na veličinu bloka (kapacitet ≠ besplatne naknade).

## Što kažu ključni akteri
Dio zajednice podržava prijedlog kao **“burst capacity”** za evente s velikom potražnjom.  
**Anatoly Yakovenko** (osnivač) upozorava da **blokovi često nisu puni** te da učinak na korisnike možda neće biti dramatičan dok **stvarna potražnja** ne pogura naknade.

## Što dalje
Prijedlog je u **diskusijskoj fazi**. Ako bude prihvaćen, promjena bi se aktivirala **nakon Alpenglow nadogradnje**; detalji (granice po slotu, sigurnosne “guard-rail” postavke) vjerojatno će se kalibrirati u praksi.

---

## Naš osvrt (Metaadvisor)
- **Smjer je konzistentan** s vizijom Solane: **visoka propusnost + kratki slotovi** uz paralelni runtime. Uklanjanje CU-cap-a može imati smisla **ako** mreža dobije bolje **propagation** i **dosljednost** (što Firedancer upravo cilja).  
- **Ključ je u guard-railovima:** preporučili bismo **soft-limite po validatoru**, nadzor **propagation-time percentila** i automatsko “throttlanje” kad mreža uspori.  
- **Investitorski pogled:** ako se pokaže da veći blokovi smanjuju **failed tx** u špici bez rasta fork-ratea, to je **pozitivno** za DeFi i korisničko iskustvo → potencijalno više volumena i naknada.  
- **Rizik:** hardverska eskalacija može suziti set validatora. Transparentni **min-spec** i subvence/optimizacije (npr. QUIC tuning, better gossip) bit će važni.

*Informativni sadržaj. Nije financijski savjet.*
