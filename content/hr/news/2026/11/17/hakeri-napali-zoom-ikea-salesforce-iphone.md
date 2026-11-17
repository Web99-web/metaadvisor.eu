---
title: "iPhone, Zoom, IKEA, Salesforce: hakerski napad preko Optimizelyja"
slug: "hakeri-napali-zoom-ikea-salesforce-iphone"
date: "2026-11-17T08:00:00+01:00"
category: "technology"
translationKey: "optimizely-hackers-zoom-ikea-salesforce-iphone-2026-11-17"
source: "Optimizely Service Status; Report URI; Reuters; StepSecurity"
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
featured_image: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
image: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
thumbnail: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
image_alt: "Hakerski napad preko Optimizelyja na internetske stranice Zooma, IKEA-e i Salesforcea uz pokušaje napada na iPhone"
image_credit: "Metaadvisor.eu"
tags: ["Cybersecurity", "Optimizely", "Zoom", "IKEA", "Salesforce", "iPhone", "Apple", "Hacking", "Cryptocurrency", "Supply Chain Attack"]
description: "Zlonamjerne skripte preko Optimizelyja zahvatile su stranice 178 organizacija, uključujući Zoom, IKEA-u i Salesforce. Napadači su ciljali kripto novčanike, kartice i iPhonee."
summary: "Zlonamjerne skripte preko Optimizelyja zahvatile su stranice 178 organizacija, uključujući Zoom, IKEA-u i Salesforce. Napadači su ciljali kripto novčanike, kartice i iPhonee."
categories: ["technology"]
---

*Naslovna slika je ilustrativna.*

**Internetske stranice najmanje 178 organizacija, među njima Zooma, IKEA-e i Salesforcea, 16. studenoga našle su se u velikom hakerskom napadu izvedenom preko platforme Optimizely. Napadači su u legitimne skripte za optimizaciju web-stranica ubacili zlonamjerni JavaScript koji je posjetiteljima mogao pokušati zamijeniti adrese kripto novčanika, presresti podatke s obrazaca za plaćanje ili pokrenuti napad na ranjive iPhone uređaje. Sigurnosni istraživači potvrdili su distribuciju zlonamjernog koda i tragove kripto krađa, ali zasad nije poznato koliko je korisnika stvarno oštećeno niti je potvrđena masovna zaraza iPhonea.**

## Kako su napadači došli do toliko poznatih stranica?

Zajednička točka napada bio je Optimizely, platforma koju kompanije koriste za testiranje i prilagodbu izgleda te funkcioniranja web-stranica. Takvi servisi učitavaju vlastiti kod u preglednik posjetitelja, pa kompromitirana skripta vanjskog dobavljača može postati problem za velik broj potpuno različitih stranica. Istraživač Scott Helme iz servisa Report URI objavio je da je njegov tim pregledao 1.611 Optimizelyjevih skripti i u njih 188, povezanih sa 178 organizacija, pronašao zlonamjerni kod. Taj broj predstavlja potvrđeni uzorak istraživanja, a ne nužno konačan opseg incidenta.

Među organizacijama čije su skripte bile zahvaćene nalaze se i CNN, BBC, HSBC, Equifax, GitLab i druge poznate kompanije. Važno je pritom razlikovati kompromitiranu skriptu koju stranica učitava od potpunog proboja u internu infrastrukturu svake od tih kompanija. Dosad objavljeni nalazi ne dokazuju da su napadači preuzeli njihove korisničke baze, poslovne sustave ili račune.

## Što je potvrdio Optimizely?

Optimizely je u službenoj obavijesti potvrdio sigurnosni incident u kojem je neovlaštena osoba iskoristila ranjivost povezanu s njegovom platformom Experimentation i dodala zlonamjerni JavaScript u pojedine korisničke projekte. Kompanija je navela da poduzima mjere za uklanjanje koda i zaštitu pogođenih sustava. Prema sigurnosnim izvještajima, velik dio uočenih zlonamjernih skripti uklonjen je do večeri 16. studenoga, no istraga o konačnom opsegu napada time nije završena.

Ovaj slučaj pokazuje osobitu slabost takozvanog napada na lanac dobave (*supply-chain attack*). Posjetitelj ne mora otvoriti sumnjivu poveznicu ili lažnu trgovinu: štetan kod može mu biti isporučen dok pregledava inače vjerodostojnu internetsku stranicu, jer se ta stranica oslanja na kompromitiranog vanjskog pružatelja usluga.

{{< support1 >}}

## Kripto adrese, kartični podaci i iPhonei: ista kampanja

Prema analizi istraživača, ubačeni kod imao je više funkcija. Jedna je pokušavala prepoznati kopirane adrese kripto novčanika i zamijeniti ih adresama pod kontrolom napadača, tako da korisnik pri slanju sredstava nesvjesno uplati novac na pogrešno odredište. Druga je bila usmjerena na podatke unesene u obrasce za plaćanje. Istraživači su zabilježili i sredstva pristigla na neke adrese povezane s napadom, ali to nije konačna procjena financijske štete.

**Pokušaji napada na iPhone nisu zasebna, nepovezana vijest.** Analizirani kod sadržavao je i dio koji je provjeravao koristi li posjetitelj Appleov mobilni uređaj te pokušavao otvoriti dodatni lanac iskorištavanja ranjivosti, ovisno o verziji iOS-a. U tehničkim analizama spominju se alati Coruna i DarkSword. To znači da su napadači u istoj operaciji ciljali različite korisnike različitim metodama, ali ne i da je svaki iPhone koji je otvorio pogođenu stranicu bio zaražen. Javno dostupni nalazi ne potvrđuju broj uspješno kompromitiranih fizičkih iPhone uređaja.

## Što se zna, a što još nije potvrđeno?

Potvrđeno je da su se zlonamjerne skripte distribuirale preko pouzdane infrastrukture Optimizelyja i da su neke bile povezane s poznatim velikim web-odredištima. Potvrđeni su i različiti pokušaji krađe, uključujući zamjenu kripto adresa. Međutim, sam popis 178 organizacija ne govori koliko je ljudi posjetilo njihove stranice u vrijeme napada, koliko je plaćanja bilo izloženo niti koliko je uređaja stvarno preuzeto.

Ujedno ne postoji osnova da se svim navedenim kompanijama pripiše isti stupanj kompromitacije. Za pojedinu stranicu važno je kada je učitala zaraženi kod, koliko je dugo bio prisutan i koje su zaštitne mjere preglednika ili same stranice djelovale. To su pitanja na koja će odgovoriti naknadne tehničke analize i službene obavijesti.

{{< support2 >}}

## Što mogu učiniti korisnici i vlasnici web-stranica?

Korisnicima koji su 16. studenoga posjećivali neku od spomenutih stranica nema razloga automatski zaključiti da su im podaci ukradeni, ali je razumno ažurirati preglednik i operacijski sustav. Pri slanju kriptovaluta treba provjeriti cijelu adresu primatelja neposredno prije potvrde transakcije, osobito ako je kopirana i zalijepljena. Ako korisnik primijeti nepoznata kartična terećenja ili sumnjive transakcije, treba odmah kontaktirati banku odnosno odgovarajuću platformu.

Organizacije koje koriste Optimizely trebaju pregledati vlastite skripte, pristupe i sigurnosne zapise te slijediti upute pružatelja usluge. Ograničavanje izvora iz kojih web-stranica smije učitavati kod, nadzor promjena i pravodobne sigurnosne zakrpe mogu smanjiti rizik od ponavljanja sličnih incidenata. To nije dokaz da je svaki korisnik zahvaćene stranice pretrpio štetu, nego mjera opreza nakon potvrđene zlouporabe dobavljačke platforme.

## Naš osvrt (Metaadvisor)

* **Velika imena povećavaju doseg napada.** Zoom, IKEA i Salesforce bili su među organizacijama čije su skripte zahvaćene, no to ne dokazuje proboj u sve njihove interne sustave.
* **Optimizely je bio zajednička ulazna točka.** Napadači su iskoristili povjerenje koje brojne stranice daju vanjskom kodu za optimizaciju.
* **iPhone je bio dio iste operacije.** Skripte su uključivale pokušaje iskorištavanja iOS ranjivosti, ali masovna uspješna zaraza nije potvrđena.
* **Kripto prijevara imala je konkretan mehanizam.** Zamjena adrese primatelja može preusmjeriti uplatu bez vidljivog upozorenja korisniku.
* **Broj 178 nije broj žrtava.** Riječ je o organizacijama u čijim su skriptama istraživači otkrili zlonamjerni kod.
* **Konačna šteta ostaje nepoznata.** Treba razlikovati potvrđeno širenje koda, zabilježene krađe i još neutvrđene posljedice.

**Pratite Metaadvisor.eu za više neovisnih vijesti i analiza o tehnologiji, umjetnoj inteligenciji, poslovanju i digitalnoj sigurnosti.**

<small style="color:#757575; font-size:12px; font-weight:400; font-style:normal;">In collaboration with AI.</small>

**Napomena:** Članak se temelji na službenoj sigurnosnoj obavijesti Optimizelyja, istraživanju Report URI-ja i izvještaju Reutersa dostupnima 17. studenoga 2026. Navedeni broj organizacija odnosi se na identificirane zaražene skripte, a ne na dokazanu krađu podataka iz svih tih organizacija. Pokušaji iskorištavanja iPhone ranjivosti nisu isto što i potvrđena uspješna kompromitacija uređaja. Tekst je informativnog karaktera i ne predstavlja individualni sigurnosni, pravni ni financijski savjet.
