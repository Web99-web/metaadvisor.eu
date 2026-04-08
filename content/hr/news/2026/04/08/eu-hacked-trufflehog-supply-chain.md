---
title: "EU hakirana kroz sigurnosni alat: kako je jedan download otvorio vrata napadu"
slug: "eu-hack-trufflehog-supply-chain-napad"
date: 2026-04-08T16:30:00+01:00
category: "tech"
translationKey: "8e4c1f2a9b6d4c7ea1f0935bd2c4a8e1"
author: "Metaadvisor.eu"
source: "TechCrunch, CERT-EU analiza"
source_url: "https://techcrunch.com/2026/04/03/europes-cyber-agency-blames-hacking-gangs-for-massive-data-breach-and-leak/"
image_url: "/images/news/EU-hacked-TruffleHog.png"
featured_image: "/images/news/EU-hacked-TruffleHog.png"
image: "/images/news/EU-hacked-TruffleHog.png"
thumbnail: "/images/news/EU-hacked-TruffleHog.png"
image_alt: "EU hack i TruffleHog sigurnosni alat"
image_credit: "Ilustracija"
tags: ["eu","cybersecurity","hack","data breach","trufflehog","aws","cloud","security","supply chain","tehnologija","ai","infrastruktura"]
summary: "Europska komisija kompromitirana je kroz supply chain napad putem sigurnosnog alata, što je omogućilo krađu podataka i otvorilo pitanja o sigurnosti digitalne infrastrukture EU."
---

*Slika je simbolična.*

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Ostvari Bitget bonus do 6200 USDT — registriraj se ovdje
  </a>
</p>

# EU hakirana kroz vlastiti sustav — kada sigurnosni alat postane ulazna točka

Europska unija našla se u središtu ozbiljnog sigurnosnog incidenta nakon što je potvrđeno da su sustavi European Commission kompromitirani kroz napad na cloud infrastrukturu. Prema informacijama CERT-EU, napad nije bio klasičan proboj izvana, nego sofisticirana operacija koja je iskoristila povjerenje sustava u vlastite alate.

Napadači su uspjeli pristupiti i izvući oko 92 GB kompresiranih podataka, uključujući osobne podatke, email komunikaciju i tehničke informacije. No ono što ovaj slučaj čini posebno zabrinjavajućim nije samo količina podataka — nego način na koji su do njih došli.

## Napad nije probio sustav — ušao je kroz njega

Umjesto klasičnog napada na infrastrukturu, napadači su iskoristili kompromitirani softver koji je Europska komisija sama preuzela i koristila. Riječ je o tzv. supply chain napadu, gdje se kompromitira alat kojem sustav već vjeruje.

Takav pristup je posebno opasan jer ne aktivira standardne sigurnosne mehanizme. Sustav ne vidi prijetnju jer ona dolazi iz legitimnog izvora. U ovom slučaju, kompromitirani alat omogućio je napadačima pristup ključnim dijelovima infrastrukture, uključujući cloud okruženje na Amazon Web Services.

{{< support1 >}}

## Pet dana bez detekcije

Napad nije odmah otkriven. Procjenjuje se da su napadači imali pristup sustavu nekoliko dana prije nego što je incident identificiran i zaustavljen. Tijekom tog vremena mogli su analizirati sustav, preuzeti podatke i pripremiti ih za distribuciju.

Ovaj vremenski okvir otvara ozbiljno pitanje: koliko su zapravo sigurni sustavi koji se smatraju “visoko zaštićenima”, ako napad može ostati neprimijećen danima?

## Tko stoji iza napada — i zašto je slučaj neobičan

Prema informacijama CERT-EU, napad se povezuje s hakerskom grupom TeamPCP, koja je identificirana kao ključni akter u kompromitaciji sustava.

Dodatnu složenost donosi činjenica da se u istom incidentu pojavljuje i druga grupa — ShinyHunters, poznata po objavljivanju ukradenih podataka. Prema dostupnim informacijama, dio podataka koji je ukraden u ranijoj fazi kasnije je distribuiran upravo kroz takve kanale.

Takva podjela uloga pokazuje koliko su moderni cyber napadi organizirani — jedan akter ulazi u sustav, drugi monetizira ili distribuira podatke.

{{< support2 >}}

## Pokušaj širenja napada unutar sustava

Nakon inicijalnog pristupa, napadači nisu stali. Pokušali su proširiti pristup unutar sustava, tražeći dodatne ulaze i osjetljive podatke. Taj proces naziva se “lateral movement”.

To znači da napadači, jednom kada uđu u sustav, pokušavaju pronaći dodatne ključeve, pristupe i veze prema drugim dijelovima infrastrukture. Cilj nije samo krađa podataka — nego kontrola.

Iako nema potvrde da su u potpunosti uspjeli proširiti napad, sama činjenica da su to pokušali pokazuje dubinu kompromitacije.

## Što je TruffleHog — i zašto je važan u ovom napadu

Jedan od alata koji se spominje u analizama ovog incidenta je TruffleHog — alat koji je dizajniran za pronalaženje osjetljivih podataka poput API ključeva, lozinki i pristupnih tokena.

Takvi alati koriste se kako bi sigurnosni timovi otkrili ranjivosti prije nego što ih netko iskoristi. No u ovom slučaju dolazi do obrata: isti alat koji služi za zaštitu može se koristiti i za napad.

Napadači su, prema analizama, koristili slične metode kako bi pronašli dodatne pristupne podatke unutar sustava i proširili svoj pristup. To pokazuje koliko je tanka granica između obrane i napada u modernim sustavima.

{{< support2 >}}

## Što je zapravo ukradeno — i zašto je to ozbiljnije nego što izgleda

Ukradeni podaci ne uključuju samo osnovne informacije poput imena i emailova. Radi se o kombinaciji komunikacije, dokumenata i tehničkih podataka koji mogu otkriti strukturu sustava.

Posebno zabrinjava mogućnost kompromitacije sigurnosnih ključeva za autentifikaciju emailova. Ako su takvi podaci zaista ukradeni, postoji mogućnost slanja lažnih poruka koje izgledaju kao službena komunikacija EU.

Drugim riječima — ovo nije samo curenje podataka, nego potencijalna prijetnja cijelom komunikacijskom sustavu.

## Jesu li građani pogođeni

Za većinu građana koji samo koriste EU web stranice nema dokaza o izravnom utjecaju. Međutim, osobe koje su bile u komunikaciji s EU institucijama mogu biti izložene riziku.

Osim toga, postoji povećan rizik od phishing napada u kojima se napadači predstavljaju kao legitimne institucije koristeći ukradene podatke.

## Veći problem od jednog incidenta

Ovaj slučaj pokazuje da sigurnost više nije pitanje jednog sustava ili jednog sigurnosnog sloja. Radi se o cijelom ekosustavu u kojem svaka komponenta može postati ulazna točka.

Kako sustavi postaju složeniji, tako raste i broj potencijalnih ranjivosti. Povjerenje u alate postaje jednako važno kao i sigurnost same infrastrukture.

## Što to znači za budućnost

Sigurnost više nije pitanje “jesmo li zaštićeni”, nego “koliko je siguran svaki dio sustava koji koristimo”. U ovom slučaju, najslabija karika nije bio server — nego alat.

## Naš osvrt (Metaadvisor):

* Supply chain napadi postaju jedna od najvećih prijetnji modernim sustavima
* Povjerenje u sigurnosne alate postaje kritična točka
* Granica između obrane i napada sve je tanja
* Kompleksnost sustava povećava rizik
* Ključno pitanje: kome zapravo vjerujemo unutar digitalne infrastrukture?

<span style="font-size:12px; color:#777;">
Odricanje od odgovornosti: Ovaj sadržaj služi isključivo u informativne svrhe i ne predstavlja financijski ili investicijski savjet.
</span>
