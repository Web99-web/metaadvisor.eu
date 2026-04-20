---
title: "LayerZero krivi KelpDAO za $290M hack, sumnja pada na Lazarus grupu"
slug: "layerzero-krivi-kelpdao-290m-hack-lazarus"
date: 2026-04-20T12:00:00+02:00
category: "crypto"
translationKey: "478999bba611acd09744f72c4b1e4477"
source: "Metaadvisor (CoinDesk, TechCrunch)"
source_url: "https://metaadvisor.eu/"
author: "Metaadvisor.eu"
image_url: "/images/hack/Hack-KelpDao-vsLayerZero-Lazarus-group.png"
featured_image: "/images/hack/Hack-KelpDao-vsLayerZero-Lazarus-group.png"
image: "/images/hack/Hack-KelpDao-vsLayerZero-Lazarus-group.png"
thumbnail: "/images/hack/Hack-KelpDao-vsLayerZero-Lazarus-group.png"
image_alt: "Kelp DAO hack, LayerZero i Lazarus grupa"
image_credit: "Metaadvisor.eu"
tags: ["crypto", "defi", "kelpdao", "layerzero", "lazarus", "hack", "security", "blockchain", "web3", "rpc", "ddos"]
summary: "Napad vrijedan 290 milijuna dolara na Kelp DAO otkriva sofisticirani exploit infrastrukture, uz optužbe na račun Lazarus grupe i raspravu o odgovornosti između LayerZero i Kelp sustava."
---

*Slika je simbolična.*

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Ostvari Bitget bonus do 6200 USDT — registriraj se ovdje
  </a>
</p>

# Kelp DAO hack od $290M: LayerZero krivi konfiguraciju, sumnja pada na Lazarus grupu

Jedan od najvećih kripto napada u 2026. godini, vrijedan oko 290 milijuna dolara, otkriva novu razinu sofisticiranosti u DeFi svijetu — ali i otvara pitanje odgovornosti između infrastrukture i samih protokola.

Napad na Kelp DAO nije bio klasičan exploit pametnog ugovora. Umjesto toga, radilo se o koordiniranom napadu na više razina sustava, uz potencijalnu povezanost s poznatim državnim hakerskim grupama.

## Kako je napad izveden

Prema analizi LayerZero tima, napadači nisu ciljali kod, već infrastrukturu.

Meta su bili RPC čvorovi (Remote Procedure Call — serveri koji omogućuju komunikaciju s blockchainom), koje koristi LayerZero verifier za potvrdu cross-chain transakcija.

Napadači su kompromitirali dva ključna RPC čvora i zamijenili njihov softver zlonamjernom verzijom.

Posebnost ovog napada:

* kompromitirani čvorovi slali su lažne podatke samo verifieru
* ostali sustavi dobivali su točne informacije

👉 sustav je bio “selektivno prevaren”

{{< support1 >}}

## DDoS i manipulacija sustava

Kako bi uklonili dodatne sigurnosne provjere, napadači su pokrenuli DDoS napad (Distributed Denial of Service — preopterećenje sustava) na vanjske RPC čvorove.

Time su prisilili sustav da se osloni na kompromitirane izvore.

Rezultat:

👉 verifier prihvaća lažnu transakciju
👉 most (bridge) oslobađa sredstva
👉 116,500 rsETH završava kod napadača

Nakon toga, zlonamjerni softver briše sam sebe i uklanja tragove.

## Problem konfiguracije

LayerZero tvrdi da je napad bio moguć zbog načina na koji je Kelp DAO konfigurirao svoj sustav.

Korišten je single-verifier model bez višestrukih provjera.

To znači:

* jedan sustav kao ključna točka
* nedostatak redundancije
* veća ranjivost na ciljane napade

S druge strane, Kelp DAO osporava dio odgovornosti.

{{< support1 >}}

## Lazarus i TraderTraitor

Napad se preliminarno povezuje s Lazarus Group i njegovom podskupinom TraderTraitor.

Ove grupe godinama ciljaju kripto projekte zbog:

* visoke likvidnosti
* globalne dostupnosti
* slabije regulacije

Procjene pokazuju:

* više od 2 milijarde dolara ukradeno prošle godine
* oko 6 milijardi dolara ukupno od 2017.

## Zašto se uvijek spominje Sjeverna Koreja

U velikim kripto napadima Lazarus se često navodi kao glavni osumnjičeni.

No važno je naglasiti:

* atribucije su često preliminarne
* temelje se na obrascima, ne dokazima
* ne moraju biti konačne

👉 “North Korea” često postaje standardni narativ

{{< support2 >}}

## Što ovaj napad znači za DeFi

Napadi se razvijaju.

Više nije dovoljno štititi pametne ugovore.

Meta su sada:

* infrastruktura
* komunikacijski slojevi
* validacijski mehanizmi

To znači da sigurnost mora pokriti cijeli sustav.

## Zaključak

Kelp DAO hack pokazuje koliko su moderni kripto sustavi kompleksni i ranjivi.

Napad nije bio slučajan — bio je precizno planiran i izveden kroz više slojeva.

Bez obzira na stvarnog napadača, poruka je jasna:

👉 sigurnost infrastrukture postaje ključna za budućnost Web3-a

---

## Naš osvrt (Metaadvisor):

* napadi se sele s koda na infrastrukturu
* konfiguracija postaje kritična sigurnosna točka
* Lazarus ostaje glavni narativ, ali ne uvijek potvrđen
* cross-chain sustavi su posebno rizični
* Web3 i dalje ovisi o centraliziranim komponentama

---

<p style="font-size:12px; color:#777;">
Odricanje od odgovornosti: Ovaj sadržaj služi isključivo u informativne svrhe i ne predstavlja financijski ili investicijski savjet.
</p>
