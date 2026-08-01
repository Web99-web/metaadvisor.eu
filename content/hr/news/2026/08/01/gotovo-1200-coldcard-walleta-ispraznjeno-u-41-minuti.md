---
title: "Gotovo 1.200 Coldcard walleta ispražnjeno u 41 minuti"
slug: "gotovo-1200-coldcard-walleta-ispraznjeno-u-41-minuti"
date: 2026-08-01T12:00:00+02:00
category: "crypto"
translationKey: "gotovo-1200-coldcard-walleta-ispraznjeno-u-41-minuti-2026-08-01"
source: "CoinDesk, Galaxy Research, Coinkite, Block Bitcoin Engineering and Security i CZ"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/Crypto-alert.png"
featured_image: "/images/Crypto-alert.png"
image: "/images/Crypto-alert.png"
thumbnail: "/images/Crypto-alert.png"
image_alt: "Kripto sigurnosno upozorenje nakon krađe bitcoina iz Coldcard walleta"
image_credit: "Metaadvisor.eu – slika je simbolična"
tags: ["Coldcard", "Coinkite", "Bitcoin", "hardverski novčanik", "hladni novčanik", "krađa bitcoina", "seed fraza", "privatni ključ", "sigurnosni propust", "firmware", "kripto sigurnost", "Galaxy Research", "Changpeng Zhao", "CZ", "kibernetička sigurnost"]
description: "Više od 1.000 BTC-a vrijednog oko 70 milijuna dolara ukradeno je s gotovo 1.200 adresa povezanih s ranjivim Coldcard walletima."
summary: "Napadač je u samo 41 minuti premjestio 1.082,65 BTC-a s 1.196 adresa nakon što je sigurnosni propust omogućio rekonstruiranje nedovoljno nasumično generiranih ključeva."
---

# Gotovo 1.200 Coldcard walleta ispražnjeno u 41 minuti

Više od 1.000 bitcoina, tada vrijednih približno 70 milijuna dolara, ukradeno je s gotovo 1.200 adresa u samo 41 minuti. Posebno zabrinjava način napada: napadač nije morao ukrasti uređaje, povezati ih s internetom niti phishingom doći do seed fraza korisnika.

Problem je bio u određenim verzijama firmwarea za COLDCARD hardverske wallete. Zbog pogreške su neki uređaji stvarali nedovoljno nasumične, a time i predvidljivije ključeve koje je napadač mogao pokušati rekonstruirati na vlastitim računalima.

*Slika je simbolična.*

## Što je COLDCARD?

COLDCARD nije naziv za sve hladne ili hardverske wallete. Riječ je o konkretnom brendu Bitcoin hardverskih novčanika koje proizvodi kanadska kompanija Coinkite.

Slični uređaji postoje pod drugim imenima, poput Ledgera i Trezora, ali ovaj incident odnosi se na određene modele i verzije COLDCARD-a.

Bitcoin pritom nije fizički spremljen u uređaju. Stanje sredstava zapisano je na blockchainu, dok uređaj stvara i čuva tajne ključeve kojima vlasnik može potpisati transakciju i premjestiti bitcoin.

## Kako je bitcoin ukraden bez pristupa uređaju?

Kada se wallet prvi put postavlja, uređaj mora stvoriti potpuno nasumičnu seed frazu. Iz nje se matematičkim putem izvode privatni ključevi i Bitcoin adrese.

Takvu seed frazu trebalo bi biti praktički nemoguće pogoditi. Međutim, kod pogođenih COLDCARD uređaja greška u firmwareu uzrokovala je da se ne koristi predviđeni hardverski generator slučajnih brojeva.

Umjesto njega aktiviran je slabiji softverski mehanizam koji se oslanjao na tehničke podatke uređaja i vrijednosti njegova internog sata. Prostor mogućih kombinacija zbog toga je bio znatno manji nego što je trebao biti.

{{< support1 >}}

Najjednostavnije rečeno, uređaj je trebao stvoriti potpuno nepredvidljiv ključ, ali ga je zbog pogreške birao prema obrascu koji je bilo lakše rekonstruirati.

To je kao sef kojem proizvođač obećava jedinstvenu i nepredvidljivu šifru, ali je zbog pogreške sastavlja iz serijskog broja i vremena proizvodnje. Lopov ne mora vidjeti ni dodirnuti sef. Moguće šifre može isprobavati na vlastitom računalu dok ne pronađe onu koja odgovara određenom sefu.

## Napadač je mogao tražiti ranjive adrese

Napadač je mogao automatski stvarati moguće seedove, iz njih izračunavati pripadajuće Bitcoin adrese i na javnom blockchainu provjeravati nalaze li se na tim adresama sredstva.

Kada bi pronašao podudaranje, iz istog seeda mogao je izvesti privatni ključ i potpisati transakciju. Bitcoin mreža takvu transakciju prihvaća kao valjanu jer je potpisana odgovarajućim ključem.

Napadač gotovo sigurno nije ručno provjeravao i praznio svaku adresu. Napad je morao biti automatiziran programom koji je pronalazio moguće ključeve, uspoređivao adrese i pripremao transakcije.

Za sada nema dokaza da je u napadu korištena umjetna inteligencija. AI je mogao pomoći pri analizi koda ili razvoju alata, ali za ovakav napad dovoljna je i automatizirana skripta.

## Ukradeno 1.082,65 BTC-a

Prema analizi Galaxy Researcha, između 1:10 i 1:51 sati po UTC-u 30. srpnja ispražnjeno je ukupno 1.196 Bitcoin adresa.

U šest blokova premješteno je 1.082,65 BTC-a, tada vrijednog približno 70 milijuna dolara. Između njih zabilježena su tri bloka bez povezanih transakcija, što sugerira da su transakcije slane u unaprijed pripremljenim skupinama.

Prve procjene govorile su o približno 594 BTC-a i oko 500 walleta. Kasnija analiza otkrila je dodatne adrese povezane s napadom, pa se procijenjeni iznos gotovo udvostručio.

Ukradeni bitcoin navodno se nalazi na četiri adrese i prema posljednjim dostupnim podacima još nije dalje premješten.

{{< support2 >}}

## Koji su COLDCARD uređaji pogođeni?

Coinkite je objavio da su pogođeni seedovi generirani na modelu Mk3 s firmwareom od verzije 4.0.1 do 4.1.9.

Problem se odnosi i na seedove generirane na modelima Mk4 i Mk5 prije standardne verzije 5.6.0 ili Edge verzije 6.6.0X te na modelu Q prije standardne verzije 1.5.0Q ili Edge verzije 6.6.0QX.

Kod novijih modela razina rizika nije jednaka kao kod Mk3 uređaja, ali Coinkite problem i dalje smatra ozbiljnim.

TAPSIGNER, OPENDIME i SATSCARD nisu pogođeni jer koriste drukčiji programski kod.

## Nadogradnja firmwarea nije dovoljna

Coinkite je priznao sigurnosni propust, ispričao se korisnicima i objavio popravljene verzije firmwarea.

Međutim, sama nadogradnja ne može popraviti seed koji je ranije generiran na ranjivoj verziji. Problem nije samo u uređaju, nego u ključu koji je uređaj već stvorio.

Pogođeni korisnik mora instalirati sigurnu verziju firmwarea, generirati potpuno novi seed i sredstva premjestiti na nove Bitcoin adrese. Stari seed ostaje ranjiv čak i ako se poslije unese u drugi hardverski ili softverski wallet.

Coinkite navodi iznimku za korisnike koji su pri stvaranju seeda dodali najmanje 50 neovisnih i tajnih bacanja kocke. Takav dodatni izvor slučajnosti mogao je proizvesti dovoljno snažan seed unatoč pogrešci u firmwareu.

{{< support2 >}}

## CZ savjetuje raspodjelu sredstava

Osnivač Binancea Changpeng Zhao, poznat kao CZ, nakon incidenta upozorio je da čak i hardverski walleti s dugom poviješću mogu sadržavati ozbiljne pogreške.

Korisnicima je predložio raspodjelu većih iznosa na nekoliko walleta kako jedan sigurnosni propust ne bi ugrozio sva njihova sredstva.

Takav pristup ipak donosi i nove rizike. Korisnik mora pravilno čuvati više uređaja, seed fraza i sigurnosnih kopija, a veći broj walleta povećava mogućnost ljudske pogreške.

## Hardware wallet nije čarobna zaštita

Ovaj incident pokazuje da hardverski wallet može ostati potpuno offline, a sredstva ipak mogu biti ugrožena ako je tajni ključ od početka loše generiran.

Korisnici nisu nužno izgubili bitcoin zato što su nekome otkrili seed frazu, instalirali lažnu aplikaciju ili povezali uređaj sa zlonamjernom stranicom. Izgubili su ga jer je uređaj stvorio ključ koji je bilo moguće rekonstruirati.

Hardware wallet i dalje može znatno smanjiti rizik od krađe, ali njegova sigurnost ovisi o kvaliteti uređaja, firmwarea i načina na koji stvara najvažniju tajnu cijelog walleta — seed frazu.

## Naš osvrt

* COLDCARD je konkretan brend Bitcoin hardverskog walleta, a ne naziv za sve hladne wallete.
* Napad se ne odnosi na sve proizvođače hardverskih walleta.
* U samo 41 minuti s 1.196 adresa premješteno je 1.082,65 BTC-a.
* Vrijednost ukradenog bitcoina tada je iznosila približno 70 milijuna dolara.
* Napadač nije morao fizički pristupiti uređajima.
* Sigurnosni propust uzrokovao je stvaranje nedovoljno nasumičnih seedova.
* Mogući seedovi i pripadajuće adrese mogli su se provjeravati automatiziranim programom.
* Nema dokaza da je u napadu korištena umjetna inteligencija.
* Coinkite je objavio sigurnosne nadogradnje i ispričao se korisnicima.
* Nadogradnja firmwarea ne popravlja seed koji je već generiran na ranjivoj verziji.
* Pogođeni korisnici moraju stvoriti novi seed i premjestiti sredstva na nove adrese.
* CZ je predložio raspodjelu većih iznosa na više walleta, ali i to donosi dodatne rizike.
* Hardware wallet pruža snažnu zaštitu, ali ne može biti sigurniji od načina na koji je stvoren njegov ključ.

**Disclaimer:** Članak je informativnog i edukativnog karaktera te ne predstavlja pravni, financijski, investicijski ili sigurnosni savjet. Informacije se temelje na javno dostupnim izvorima i nisu svi navodi nužno neovisno potvrđeni.

U suradnji s AI-jem.
