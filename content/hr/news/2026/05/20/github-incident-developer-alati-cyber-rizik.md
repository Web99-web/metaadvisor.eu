---
title: "GitHub incident upozorava: novi cyber rizik počinje u alatima koje developeri koriste svaki dan"
slug: "github-incident-developer-alati-cyber-rizik"
date: 2026-05-20T10:00:00+02:00
category: "tech"
translationKey: "github-developer-tools-security-2026-05-20"
source: "Metaadvisor (GitHub, BleepingComputer, Times of India)"
source_url: "https://metaadvisor.eu/"
author: "Metaadvisor.eu"
image_url: "/images/GitHub.png"
featured_image: "/images/GitHub.png"
image: "/images/GitHub.png"
thumbnail: "/images/GitHub.png"
image_alt: "GitHub i developer alati kao nova meta cyber napada"
image_credit: "Metaadvisor.eu"
tags: ["github", "cyber sigurnost", "cybersecurity", "developer alati", "visual studio code", "vs code", "zlonamjerna ekstenzija", "supply chain", "software supply chain", "open source", "repozitoriji", "interni repozitoriji", "api ključevi", "tokeni", "secrets", "devops", "programeri", "sigurnost softvera", "malware", "tech", "tehnologija"]
summary: "GitHub incident pokazuje da se cyber napadi sve više sele prema developer okruženju: editorima, ekstenzijama, tokenima, lokalnim konfiguracijama i alatima koje programeri koriste svaki dan. Iako zasad nema javnih dokaza da su pogođeni korisnički repozitoriji, slučaj otvara važno pitanje povjerenja u software supply chain."
---

<p style="font-size:13px; opacity:0.75;">
Slika je simbolična.
</p>

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Ostvari Bitget bonus do 6200 USDT — registriraj se ovdje
  </a>
</p>

# GitHub incident upozorava: novi cyber rizik počinje u alatima koje developeri koriste svaki dan

GitHub je ponovno pokazao koliko je digitalni svijet osjetljiv na mjesta koja obični korisnici gotovo nikada ne vide. Prema javno dostupnim informacijama, incident se odnosi na neovlašteni pristup GitHubovim internim repozitorijima, nakon što je kompromitiran uređaj jednog zaposlenika preko zlonamjerne ekstenzije za **Visual Studio Code**, poznatiji kao **VS Code**. VS Code je popularan alat za pisanje i uređivanje koda, odnosno razvojno okruženje koje developeri svakodnevno koriste za rad na aplikacijama, web stranicama, servisima i automatizacijama.

GitHub zasad navodi da nema dokaza o utjecaju na korisničke repozitorije, organizacije ili enterprise račune. To je važna razlika, jer incident nije predstavljen kao proboj u privatne projekte korisnika, nego kao pristup internim GitHub repozitorijima. Ipak, sama metoda napada puno je važnija od jedne izolirane vijesti. Ako se napad može dogoditi preko alata koji developer koristi svaki dan, onda sigurnosni problem više ne počinje tek na serveru, nego puno ranije — na računalu osobe koja piše i objavljuje kod.

{{< support1 >}}

## GitHub više nije samo mjesto za kod

Za većinu ljudi GitHub je nevidljiva platforma. Ne koriste ga svakodnevno, ne otvaraju repozitorije i ne razmišljaju o tome gdje se zapravo razvija softver koji pokreće aplikacije, web trgovine, AI alate, crypto projekte, bankarske integracije, cloud servise i tisuće startup proizvoda. Ali za tehnološki svijet GitHub je jedno od ključnih mjesta digitalne infrastrukture.

Ondje se ne nalazi samo “kod”. U repozitorijima se često nalaze skripte, dokumentacija, testni alati, konfiguracije, automatizacije, deployment procesi, reference na API-je, interni nazivi sustava i tragovi o tome kako neka platforma funkcionira. Čak i kada napadač ne dođe izravno do korisničkih podataka, interni repozitoriji mogu mu pomoći da bolje razumije arhitekturu sustava i pripremi sljedeći napad.

Zato je važno da se ova priča ne promatra samo kao još jedan “hakerski incident”. Ovo je priča o povjerenju u cijeli **software supply chain**, odnosno lanac razvoja i isporuke softvera. Taj lanac uključuje developere, njihove uređaje, alate za pisanje koda, ekstenzije, repozitorije, pakete, API ključeve, cloud servise i automatizirane sustave koji kod pretvaraju u aplikacije koje korisnici na kraju vide.

## Zašto su VS Code ekstenzije postale zanimljiva meta?

VS Code ekstenzije developerima olakšavaju rad. One mogu pomagati u formatiranju koda, povezivanju s GitHubom, radu s bazama podataka, provjeri grešaka, pisanju dokumentacije, integraciji s AI asistentima ili upravljanju cloud servisima. Problem je u tome što takve ekstenzije često rade vrlo blizu osjetljivog radnog okruženja.

Ako napadač uspije podmetnuti zlonamjernu ekstenziju, potencijalno može pokušati čitati lokalne konfiguracije, pristupne tokene, privatne repozitorije, session podatke, API ključeve ili druge osjetljive informacije. Drugim riječima, ne mora nužno prvo napasti samu platformu. Može napasti alat koji developer koristi za pristup toj platformi.

{{< support2 >}}

To je velika promjena u odnosu na stariji način razmišljanja o cyber sigurnosti. Nekada se najviše govorilo o lozinkama, phishing emailovima, nezaštićenim serverima i virusima na običnim računalima. Danas se sve više govori o developer endpointu — računalu osobe koja ima pristup kodu, repozitorijima, internim sustavima i automatizacijama. Ako je taj uređaj kompromitiran, napadač može dobiti ulaz u sustav kroz vrata koja izgledaju potpuno legitimno.

## Problem nisu samo veliki sustavi, nego svakodnevne navike

Najopasniji dio ovakvih napada jest to što mogu izgledati sasvim normalno. Developer instalira ekstenziju, alat radi, editor se otvara, repozitoriji su dostupni, a napad se možda događa u pozadini. To je razlog zašto se sve više pažnje posvećuje provjeri ekstenzija, dependencyja, open-source paketa i svih dodataka koji ulaze u razvojno okruženje.

U malim timovima i startupima takva provjera često ne postoji ili je vrlo površna. Ljudi žele brzo raditi, instalirati alat koji im štedi vrijeme i nastaviti s projektom. Ali upravo tu nastaje rizik. Jedan pogrešan dodatak može biti dovoljan da napadač dođe do tokena, repozitorija ili internih informacija.

Za crypto projekte ovaj problem ima još veću težinu. U crypto svijetu kod često izravno upravlja novcem, walletima, smart contractima, exchange integracijama i API ključevima. Ako napadač dođe do pogrešnog tokena ili deploy skripte, šteta može biti ogromna. U teoriji se crypto često opisuje kao decentraliziran, ali razvojna infrastruktura mnogih projekata i dalje je vrlo centralizirana: GitHub, VS Code, npm paketi, cloud servisi i CI/CD alati ostaju ključne točke povjerenja.

## Open source nije problem, ali sigurnosna kultura mora biti jača

Važno je naglasiti da ovaj incident ne znači da je open source problem. Otvoreni kod je jedan od temelja interneta. On omogućuje učenje, provjeru, transparentnost, brži razvoj i suradnju među developerima iz cijelog svijeta. Problem nastaje kada se otvorenost kombinira s prevelikim povjerenjem u alate koji nisu dovoljno provjereni.

Moderna sigurnost više ne može stati na rečenici “imamo jaku lozinku”. Potrebno je znati tko ima pristup repozitorijima, koliko dugo vrijede tokeni, gdje se čuvaju API ključevi, koje ekstenzije smiju biti instalirane, kako se rotiraju secret-i i kako se prati neuobičajena aktivnost. Posebno je važno da se osjetljive vrijednosti ne ostavljaju u kodu, komentarima, starim konfiguracijama ili testnim datotekama.

GitHub incident zato treba gledati kao upozorenje cijeloj industriji. Ako se kompromitira developer alat, napad može početi prije nego što kod uopće dođe do repozitorija. Ako se kompromitira uređaj osobe s pristupom internim sustavima, napadač ne mora probijati “glavni zid” izvana. Može se pojaviti iznutra, kroz legitimni pristup koji je zlorabljen.

## Novi cyber rizik je tiši i bliži nego što se čini

Za obične korisnike sve ovo može zvučati tehnički i daleko. Ali posljedice nisu daleke. Aplikacije koje koristimo, fintech servisi, AI alati, web trgovine, crypto platforme i poslovni sustavi nastaju upravo u takvim developerskim okruženjima. Ako se kompromitira lanac razvoja, problem se kasnije može pojaviti kao ukradeni podaci, kompromitirana aplikacija, zlonamjerna nadogradnja ili supply-chain napad koji pogađa mnogo širi krug korisnika.

Zato pitanje nije samo “je li GitHub siguran?”. Pravo pitanje je koliko modernog interneta ovisi o alatima koje developeri svakodnevno instaliraju i koriste gotovo automatski. GitHub, VS Code, ekstenzije, repozitoriji i automatizirani deployment sustavi više nisu sporedni tehnički detalji. Oni su temelj digitalne ekonomije.

Ovaj incident ne treba pretvarati u paniku, ali ga ne treba ni podcijeniti. GitHub navodi da zasad nema dokaza o utjecaju na korisničke repozitorije, što je važna i umirujuća informacija. No činjenica da se napad veže uz zlonamjernu developer ekstenziju pokazuje gdje se cyber rizik sve više seli: prema ljudima, alatima i svakodnevnim radnim navikama onih koji grade internet.

## Naš osvrt (Metaadvisor)

* **GitHub incident pokazuje da napad više ne mora početi na serveru**, nego može početi u developer alatu koji se koristi svaki dan.
* **VS Code ekstenzije i slični dodaci postaju ozbiljna sigurnosna tema**, jer mogu imati pristup vrlo osjetljivom radnom okruženju.
* **Software supply chain više nije tema samo za velike korporacije**, nego i za male timove, startupove, crypto projekte i AI developere.
* **Crypto projekti posebno trebaju paziti na tokene, API ključeve, deploy skripte i repozitorije**, jer pogreška u razvojnom okruženju može imati financijske posljedice.
* **Open source ostaje važan i koristan**, ali mora ići zajedno s boljom sigurnosnom disciplinom, provjerom alata i redovitom rotacijom osjetljivih pristupa.

<p style="font-size:12px; opacity:0.7; margin-top:30px;">
Odricanje od odgovornosti: Ovaj sadržaj služi isključivo u informativne svrhe i ne predstavlja financijski ili investicijski savjet.
</p>
