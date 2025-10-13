---
title: "Centralizirane (CEX) vs. decentralizirane (DEX) mjenjačnice: likvidacije i zašto svi gledaju u Hyperliquid"
slug: "centralizirane-cex-vs-decentralizirane-dex-mjenjacnice-likvidacije-i-hyperliquid"
date: 2025-10-12T12:00:00Z
category: "crypto"
translationKey: "f837cbfa-b3f7-4497-9cb7-c87abef87220"
source: "Metaadvisor.eu"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/cex-vs-dex.png"
featured_image: "/images/cex-vs-dex.png"
image: "/images/cex-vs-dex.png"
thumbnail: "/images/cex-vs-dex.png"
image_alt: "CEX vs DEX mjenjačnice"
image_credit: "Slika je simbolična."
tags: ["CEX", "DEX", "mjenjačnice", "likvidacije", "Hyperliquid", "transparentnost", "kripto", "perps", "whales", "KYC", "self-custody", "cijene"]
summary: "Centralizirane mjenjačnice dominiraju volumenom, ali skrivaju detalje likvidacija. Decentralizirane nude potpunu on-chain transparentnost, zbog čega je Hyperliquid pod povećalom nakon nedavnih masovnih likvidacija."
---

## Centralizirane mjenjačnice (CEX)
Centralizirane mjenjačnice poput **Binance, Coinbase, Kraken, Bybit, Bitget, KuCoin, OKX, Huobi, Crypto.com, Bitstamp, MEXC** i drugih čine većinu volumena u kriptu.  
One nude:  
- ✅ jednostavan onboarding (KYC, fiat uplate karticom ili bankom)  
- ✅ veliku likvidnost i duboke order bookove  
- ✅ brze transakcije unutar vlastitog sustava  

Ali nose i ozbiljne **probleme**:  
- ❌ **središnji autoritet**: tvrtka kontrolira depozite i knjige naloga  
- ❌ **netransparentnost**: korisnici ne vide tko je točno likvidiran, koliko i kada  
- ❌ **prikazivanje samo neto razlike**: u teoriji (i praksi) CEX može objaviti samo agregat — npr. *“danas je likvidirano $2,3B”*, bez otkrivanja da je jedan whale zaradio ogroman iznos dok su tisuće manjih tradera ostale izbrisane  
- ❌ povijesni rizici: **FTX, Mt.Gox** pokazuju kako centralizacija i manjak uvida mogu završiti kolapsom  
- ❌ **mogućnost zamrzavanja računa**: burza može blokirati sredstva ili pristup računu bez detaljnog objašnjenja, često zbog regulatornih zahtjeva, sigurnosnih provjera ili vlastite procjene rizika  

Drugim riječima: na **Binanceu ili Coinbaseu moglo je biti i puno više likvidacija nego što je javno prikazano**. Ti vidiš samo **brojke koje oni objave**, ne i sve detalje.

---

## Decentralizirane mjenjačnice (DEX)
Decentralizirane mjenjačnice poput **Uniswap, PancakeSwap, dYdX, GMX, Hyperliquid, Jupiter, 1inch, Curve, Balancer, SushiSwap** rade direktno na blockchainu.  
One donose:  
- ✅ **potpunu on-chain transparentnost** — svaka transakcija, swap i likvidacija je zabilježena na lancu  
- ✅ **bez centralnog skrbnika**: korisnik drži vlastite ključeve i sredstva  
- ✅ **otvorene knjige**: može se pratiti tko je otvorio short/long, kada i za koliko  

Rizici postoje:  
- ❌ manja likvidnost i plići order bookovi  
- ❌ veća kompleksnost (walleti, gas, bridgevi)  
- ❌ nema centralne korisničke podrške  
- ❌ **gubitak pristupa**: ako izgubite seed frazu ili privatni ključ, sredstva su trajno izgubljena — nema “reset lozinke” niti korisničke podrške  

Ali prednost je ogromna: **vidi se sve**. Ako whale izgubi 400 milijuna USD, svi to mogu provjeriti na blockchainu.

---

## Identitet i kontrola računa
- **CEX = “račun na svoje ime”.** Registriraš se s osobnim podacima i dokumentima (KYC), burza drži tvoje coine i može ih blokirati po potrebi.  
- **DEX = “tvoj wallet, tvoja pravila”.** Nema centralnog računa ni obveznog KYC-a: sve se odvija kroz wallet, sredstva su pod tvojom kontrolom i nema oporavka ako izgubiš ključeve.  

---

## Zašto Hyperliquid?
**Hyperliquid** je decentralizirana burza koja nudi i **spot trgovanje** i **perpetual futures (perps)**.  
- 🔍 Prikazuje **svaku poziciju, short i long, s detaljima javne on-chain adrese walleta** (ne imena korisnika).  
- 📊 Analitičari mogu pratiti whale adrese i njihove poteze.  
- ⚠️ Nakon nedavnog pada, Hyperliquid je otkrio da je jedan whale otvorio short od **~$400M** neposredno prije pada Bitcoina — podatak koji na CEX-u nikada ne bi bio javno vidljiv.  

---

## Razlike u cijenama
Cijene na CEX i DEX burzama mogu biti različite — ponekad minimalno (par dolara), a ponekad drastično, ovisno o likvidnosti i o tome tko “stoji iza knjige”.  
Primjer:  
- Na **Binanceu** se BTC držao na **115.000 USD**, jer su market makeri branili cijenu.  
- U isto vrijeme na **Hyperliquidu** je cijena pala na **113.500 USD**, jer order book nije imao istu dubinu i nitko nije “stajao” iza zida ponuda.  
Razlike se kasnije izravnaju arbitrage botovima, ali u trenutku krize ili whale poteza mogu biti ogromne.

---

## Što pokazuju (i ne pokazuju) grafike i on-chain trag
U **danima i satima nakon sloma** svi analiziraju pomake: **koji su kitovi**, **koliko su zaradili** i **što sada rade**. Jedan trader je primijetio da je netko tko je **zaradio ~$160M shortanjem BTC & ETH** tijekom najvećeg pada, **poslao 100 BTC na Kraken**. Evo kako to uklopiti u sliku CEX vs DEX:

- **Što se vidi (DEX/on-chain):**  
  Na DEX-u i blockchain alatima vidi se svaki potez — uključujući i ovakav **transfer 100 BTC na Kraken**.  
  → Naš raniji osvrt: **OG whale — 3600 BTC short na Hyperliquidu** (poveznica: https://metaadvisor.eu/news/og-whale-3600btc-short-hyperliquid/).  

- **Što se ne vidi (CEX/off-chain):**  
  Ako isti akter pređe na CEX, javnost dobiva samo agregirane podatke, dok stvarni detalji ostaju sakriveni.  

- **Zašto je to važno:**  
  **DEX = provjera, CEX = povjerenje.** On-chain podaci su provjerljivi, dok CEX daje samo svoj izvještaj.

---

## Popis glavnih CEX i DEX mjenjačnica

**Centralizirane (CEX):**  
- Binance  
- Coinbase  
- Kraken  
- Bybit  
- Bitget  
- KuCoin  
- OKX  
- Huobi  
- Crypto.com  
- Bitstamp  
- **MEXC**  

**Decentralizirane (DEX):**  
- Uniswap  
- PancakeSwap  
- Curve  
- SushiSwap  
- 1inch  
- Balancer  
- GMX  
- dYdX  
- Hyperliquid  
- Jupiter  

---

### Naš osvrt (Metaadvisor)
- **CEX = udobnost, ali ne i potpuna transparentnost.** Burza može prikazati samo agregirane brojke i neto razlike.  
- **DEX = potpuna otvorenost.** Svaka transakcija i likvidacija vidljiva je na blockchainu.  
- **Hyperliquid** pokazuje koliko whaleovi stvarno pomiču tržište i zašto on-chain alati postaju ključni za praćenje pravih igrača.  
- **Cijene na DEX-u i CEX-u nisu uvijek iste.** To je podsjetnik da prava tržišna cijena ne ovisi o PR izvještaju burze, već o stvarnoj dubini knjige naloga.  
- **Ključno pitanje:** Hoće li budućnost pripasti **transparentnim DEX-ovima** ili će CEX-ovi morati otvoriti svoje podatke da bi zadržali povjerenje?

<p style="text-align:center; margin:20px 0;">
  <a href="/go/mexc" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:white; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:600; display:inline-block;">
     👉 Trguj kriptom na MEXC
  </a>
</p>
