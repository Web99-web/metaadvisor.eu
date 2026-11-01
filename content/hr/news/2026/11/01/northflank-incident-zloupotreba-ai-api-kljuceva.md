---
title: "Northflank upozorava na zloupotrebu AI API ključeva"
slug: "northflank-incident-zloupotreba-ai-api-kljuceva"
date: "2026-11-01T07:00:00Z"
category: "ai"
translationKey: "northflank-security-incident-2026-11-01"
source: "Northflank status: Security incident, Wiz: Black October for AI Developer Platforms"
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/editorial/northflank-ai-api-key-alert.png"
featured_image: "/images/editorial/northflank-ai-api-key-alert.png"
image: "/images/editorial/northflank-ai-api-key-alert.png"
thumbnail: "/images/editorial/northflank-ai-api-key-alert.png"
image_alt: "Northflank - zloupotreba AI API ključeva"
image_credit: "Metaadvisor.eu"
tags: ["ai", "api", "cloud", "cybersecurity"]
description: "Northflank poziva na opoziv i rotaciju tajni nakon prijava neovlaštene upotrebe AI API ključeva. Zašto promjena lozinke nije dovoljna?"
summary: "Northflank poziva na opoziv i rotaciju tajni nakon prijava neovlaštene upotrebe AI API ključeva. Zašto promjena lozinke nije dovoljna?"
categories: ["ai"]
---

*Slika je ilustrativna.*

**Northflank, platforma koja razvojnim timovima pomaže pokretati aplikacije u oblaku, upozorava na neovlaštenu upotrebu pohranjenih AI API ključeva. Posljedica za korisnika može biti vrlo opipljiva: netko drugi koristi AI uslugu, a račun stiže njemu.**

Tvrtka je registrirana u Londonu, a vode je suosnivači Will Stewart i Frederik Brix. Njezine proizvode koriste razvojni i operativni timovi za postavljanje aplikacija, baza podataka i AI radnih opterećenja. Northflank pojednostavljuje upravljanje infrastrukturom, uključujući okruženja na AWS-u, Azureu i Google Cloudu. Ne treba ga poistovjećivati sa samim pružateljem AI modela.

## Cloud i API ključ, bez tehničkog žargona

Cloud, odnosno oblak, znači da aplikacija radi na udaljenim poslužiteljima umjesto na računalu vlasnika. Zamislite internetsku trgovinu s AI asistentom. Northflank može pomoći da ta aplikacija radi, dok se odgovori naručuju od zasebnog pružatelja AI-ja.

API ključ je digitalna pristupnica kojom se aplikacija predstavlja toj usluzi. Omogućuje joj slanje zahtjeva bez ručnog prijavljivanja čovjeka, unutar dodijeljenih ovlasti. Ako ključ dospije drugome, on može stvarati potrošnju na vlasnikovu računu. Mogući pristup podacima ovisi o dozvolama ključa i konkretnoj usluzi. To je objašnjenje rizika, ne tvrdnja da je u ovom incidentu potvrđeno curenje svih korisničkih podataka.
## Upozorenje obuhvaća sve varijable okruženja

Upozorenje od 30. listopada traži da korisnici sve varijable okruženja smatraju kompromitiranima. Northflank savjetuje opoziv starih vjerodajnica kod njihova izdavatelja, izradu novih i ažuriranje aplikacija. Tijekom 31. listopada proširena je dostupnost rotacije tajni za dodatke, a revizijski zapisi omogućeni su i besplatnim računima.

To je šire od promjene lozinke za prijavu na samu platformu. Varijable okruženja mogu sadržavati tajne kojima aplikacija pristupa drugim uslugama. Promjena jedne prijavne lozinke zato ne treba biti zamjena za popis vjerodajnica koje su bile pohranjene u pogođenom okruženju.

## API ključ povezuje pristup i račun za potrošnju

AI API ključ aplikaciji omogućuje pozivanje modela u okviru određenog računa. Ako ga koristi netko drugi, vlasnik mora odvojeno razmotriti pristup podacima, dozvole i troškove. Neuobičajena potrošnja nije sama po sebi dokaz kojim je putem ključ pribavljen, ali je važan signal za istragu.

Zato je korisno sačuvati vremenski označene zapise o korištenju i naplati prije nego što se promjene izgube među redovnim poslovima sanacije. Novi ključ treba imati samo dozvole koje aplikacija stvarno treba. Ograničenja potrošnje i upozorenja mogu pomoći pri ranom otkrivanju zloupotrebe, ali ne zamjenjuju opoziv kompromitirane vjerodajnice.

{{< support1 >}}

## Širi obrazac nije dokaz istog napadača

Wiz u izvještaju od 30. listopada opisuje širi val napada na razvojne AI platforme i zloupotrebu ukradenih vjerodajnica. Taj kontekst objašnjava zašto je pristup modelima privlačna meta. Ne dokazuje da je sve incidente uzrokovao isti propust niti da je ista skupina odgovorna za svaki slučaj.

Povezivanje po sličnim adresama ili obrascima treba ostati istraživački trag. Za konačnu atribuciju potrebno je više od vremenske blizine i sličnog cilja. Ni prijava zloupotrebe ključa ne znači da je provaljeno u infrastrukturu pružatelja samog AI modela.

## Naš osvrt (Metaadvisor)

* **Tajna u oblaku nije samo tehnička postavka.** Ona može predstavljati ovlast za pristup usluzi i stvaranje troška. Inventar tajni zato treba imati odgovornu osobu i postupak opoziva.
* **Rotacija mora završiti provjerom.** Spremanje novog ključa ne govori radi li aplikacija s njim i je li stari pristup doista ugašen. Te dvije provjere trebaju biti odvojene.
* **Oporavak ima operativnu cijenu.** Brza zamjena vjerodajnica može prekinuti integracije. Prioritete treba odrediti prema ovlastima i izloženosti, uz praćenje rada aplikacija.

Ovaj slučaj pokazuje zašto sigurnost AI primjene počinje i prije samog modela: u načinu pohrane, dijeljenja i povlačenja pristupa. Dostupnost usluge i završena istraga nisu isto, pa je za korisnike važna i provjerljiva obavijest o završetku sanacije.

Širi kontekst: [zašto ovisnost o cloud platformama ima posljedice za korisnike](/hr/news/globalni-cloud-outage-microsoft-azure-aws-google-cloud-cloudflare-akamai/). Riječ je o zasebnom ranijem događaju, ne o istom incidentu.

{{< support2 >}}

**Pratite Metaadvisor.eu za vijesti i analize o AI, tehnologiji i digitalnoj sigurnosti.**

<small style="color:#999; font-size:0.8em;">U suradnji s AI.</small>

**Disclaimer:** Tekst je informativan i nije financijski ili investicijski savjet. Stanje je provjereno 1. studenoga 2026.; posljednja tada vidljiva dopuna statusa nosi 31. listopada u 23:31 UTC. Status i nalazi mogu se promijeniti.
