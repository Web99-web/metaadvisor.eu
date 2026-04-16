---
title: "EU aplikacija za provjeru dobi hakirana u 2 minute: sigurnosni propust otkriven od security consultanta"
slug: "eu-aplikacija-za-provjeru-dobi-hakirana-u-2-minute"
date: 2026-04-16T10:00:00+02:00
category: "tech"
translationKey: "eu-age-verification-app-security-flaw-2026"
author: "Metaadvisor.eu"
source: "X (Twitter), javne objave"
source_url: "https://metaadvisor.eu/"
image_url: "/images/news/EU-age-verification-app-hacked.png"
featured_image: "/images/news/EU-age-verification-app-hacked.png"
image: "/images/news/EU-age-verification-app-hacked.png"
thumbnail: "/images/news/EU-age-verification-app-hacked.png"
image_alt: "EU age verification app security flaw bypass"
image_credit: "Metaadvisor ilustracija"
tags: ["eu", "provjera dobi", "sigurnost", "hakiranje", "privatnost", "digitalni identitet", "sigurnosni propust"]
summary: "Sigurnosni konzultant pokazao je kako se EU aplikacija za provjeru dobi može zaobići u manje od dvije minute zbog ozbiljnog dizajnerskog propusta."
---

*Slika je simbolična.*

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Get a Bitget bonus up to 6200 USDT — register here
  </a>
</p>

# EU aplikacija za provjeru dobi hakirana u 2 minute: sigurnosni propust otkriven od security consultanta

Nova EU aplikacija za provjeru dobi, predstavljena kao rješenje koje bi trebalo postaviti standard za sigurnost i privatnost korisnika, već se našla pod ozbiljnim upitnikom. Samo nekoliko dana nakon što je predstavljena kao “tehnički spremna”, sigurnosni konzultant **Paul Moore pokazao je kako se sustav može zaobići u manje od dvije minute.**

## Kako funkcionira propust

<p style="text-align:center;">
  <img src="/images/news/EU-age-app-Paul-Moore-Security-Consultant.png" alt="EU age verification security flaw analysis" style="max-width:100%; border-radius:10px;" />
</p>

Tijekom inicijalnog postavljanja aplikacija od korisnika traži kreiranje PIN-a. Taj PIN se zatim “kriptira” i sprema lokalno na uređaj, u tzv. shared_prefs direktorij.

Na prvi pogled, to može djelovati kao sigurnosna mjera. No prema analizi, riječ je o ozbiljnom dizajnerskom problemu. PIN nije kriptografski povezan s identitetom korisnika, odnosno s “vaultom” koji sadrži stvarne identifikacijske podatke.

To znači da sustav zapravo ne provjerava vezu između autentifikacije i identiteta.

{{< support1 >}}

## Zaobilaženje u praksi

<p style="text-align:center;">
  <img src="/images/news/EU-age-app-Paul-Moore-Security-Consultant1.png" alt="EU age verification bypass method" style="max-width:100%; border-radius:10px;" />
</p>

Napad ne zahtijeva napredne alate niti kompleksne metode. Dovoljno je pristupiti lokalnom konfiguracijskom zapisu i ukloniti vrijednosti povezane s PIN-om (PinEnc i PinIV).

Nakon ponovnog pokretanja aplikacije, korisnik postavlja novi PIN — ali aplikacija i dalje zadržava stare vjerodajnice povezane s prethodnim profilom.

Rezultat je ozbiljan sigurnosni propust: sustav omogućuje da se postojeći identitet koristi bez stvarne provjere. Drugim riječima, aplikacija može biti dovedena u stanje “validno” bez da je identitet ponovno potvrđen.

## Dodatni sigurnosni problemi

<p style="text-align:center;">
  <img src="/images/news/EU-age-app-Paul-Moore-Security-Consultant2.png" alt="EU age verification additional issues" style="max-width:100%; border-radius:10px;" />
</p>

Osim osnovnog propusta, identificirani su i dodatni problemi koji dodatno kompromitiraju sigurnost sustava.

Ograničenje broja pokušaja (rate limiting) implementirano je kao običan brojač u istom konfiguracijskom fajlu. To znači da ga je moguće resetirati i nastaviti pokušaje bez ikakvog ograničenja.

Slično vrijedi i za biometrijsku autentifikaciju. Opcija za korištenje biometrije nalazi se kao jednostavna boolean vrijednost, što omogućuje njeno isključivanje bez stvarne provjere.

{{< support2 >}}

## Širi kontekst: sigurnost vs. percepcija

Ovaj slučaj otvara važnije pitanje od same aplikacije. Radi se o povjerenju u digitalne identifikacijske sustave koji se sve više uvode na razini Europske unije.

Aplikacija se promovira kao open-source rješenje koje poštuje najviše standarde privatnosti. Međutim, ovaj primjer pokazuje da transparentnost ne znači automatski i sigurnost.

Ako se ključni sigurnosni elementi oslanjaju na lokalne postavke koje je moguće mijenjati, tada sustav postaje ranjiv bez obzira na to koliko je formalno “siguran”.

## Zaključak

Ovo nije klasičan hakerski napad, nego dizajnerski propust. Upravo zato je potencijalno opasniji — jer ga je moguće iskoristiti bez naprednog tehničkog znanja.

Ako se sustav koji bi trebao potvrditi identitet može zaobići u nekoliko minuta, tada pitanje više nije koliko je tehnologija napredna, nego koliko je pouzdana.

---

### Naš osvrt (Metaadvisor)

Ovaj slučaj jasno pokazuje da sigurnost ne dolazi iz deklaracija, nego iz arhitekture sustava. Sustavi mogu biti “službeni”, “regulirani” i “open-source”, ali ako osnovni dizajn nije ispravan, sigurnost postaje iluzija.

Još važnije, ovdje se ne radi o izoliranom problemu jedne aplikacije. Radi se o smjeru u kojem se kreću digitalni identiteti i sustavi kontrole pristupa.

Ako takvi sustavi imaju i najmanju slabost, posljedice nisu lokalne — nego sustavne.

I možda najvažnije: najopasniji propusti nisu oni koji zahtijevaju kompleksne napade, nego oni koji se mogu iskoristiti jednostavno. U takvim slučajevima, pitanje nije hoće li doći do zlouporabe — nego kada.

---

<span style="font-size:0.9em; color:#777;">
Ovaj sadržaj je informativne prirode i ne predstavlja financijski ili investicijski savjet.
</span>
