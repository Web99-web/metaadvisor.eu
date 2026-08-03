---
title: "Hardware wallet može biti offline i ipak ranjiv"
slug: "hardware-wallet-moze-biti-offline-i-ipak-ranjiv"
date: 2026-08-06T06:00:00+02:00
category: "crypto"
translationKey: "hardware-wallet-offline-ipak-ranjiv-2026-08-06"
source: "Javno dostupna dokumentacija proizvođača hardverskih novčanika i sigurnosna upozorenja"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/informative/Hardware-wallet-risks.png"
featured_image: "/images/informative/Hardware-wallet-risks.png"
image: "/images/informative/Hardware-wallet-risks.png"
thumbnail: "/images/informative/Hardware-wallet-risks.png"
image_alt: "Hardware wallet može ostati offline, ali ipak biti ranjiv zbog slabog seeda, firmwarea ili ljudske pogreške"
image_credit: "Metaadvisor.eu – slika je simbolična"
tags: ["hardware wallet", "kripto sigurnost", "offline wallet", "air-gapped wallet", "seed fraza", "privatni ključ", "firmware", "self-custody", "passphrase", "PIN", "multisig", "phishing", "kripto novčanik", "sigurnosna kopija", "upravljanje rizikom"]
description: "Hardware wallet može značajno smanjiti rizik udaljenog napada, ali offline i air-gapped način rada ne štite od slabog seeda, ranjivog firmwarea i ljudske pogreške."
summary: "Privatni ključ može ostati potpuno offline, a sredstva ipak biti ugrožena. Sigurnost hardverskog novčanika ovisi o generiranju seeda, firmwareu, provjeri transakcija, zaštiti sigurnosne kopije i ponašanju korisnika."
---

*Slika je simbolična.*

# Hardware wallet može biti offline i ipak ranjiv

Hardware wallet često se smatra jednim od najsigurnijih načina čuvanja kriptovaluta jer privatni ključevi ostaju izvan računala ili mobilnog telefona povezanog s internetom. Neki uređaji mogu se koristiti potpuno air-gapped, bez USB veze i bez izravne internetske komunikacije, pri čemu se transakcije prenose putem memorijske kartice, QR koda ili drugog odvojenog kanala.

Takav način rada znatno smanjuje mogućnost udaljenog napada, ali ne uklanja sve rizike. Offline uređaj može biti ranjiv ako je seed generiran predvidljivo, ako firmware sadrži ozbiljnu pogrešku, ako zaslon prikazuje netočne podatke ili ako je sigurnosna kopija loše zaštićena.

Nedavni sigurnosni incidenti pokazali su koliko je važna ta razlika. Uređaj može cijelo vrijeme ostati odvojen od interneta, a sredstva ipak mogu biti ugrožena ako su privatni ključevi nastali iz nedovoljno nasumičnog seeda.

## Što zapravo znači da je wallet offline?

Kada se za hardware wallet kaže da je offline, to obično znači da privatni ključ ne napušta uređaj i da uređaj nije stalno povezan s internetom. Korisnik na računalu ili mobitelu pripremi nepotpisanu transakciju, prenese je na hardware wallet, provjeri podatke na njegovu zaslonu i fizički potvrdi potpisivanje.

Potpisana transakcija zatim se vraća na uređaj povezan s internetom i šalje na blockchain. U idealnom slučaju čak ni zaraženo računalo ne može izravno izvući privatni ključ iz hardware walleta.

Ipak, računalo i dalje može pokušati promijeniti adresu primatelja, prikazati lažne podatke ili korisnika navesti da potpiše nešto drugo od onoga što je namjeravao poslati. Hardware wallet zato ne uklanja potrebu za provjerom transakcije, nego samo odvaja privatni ključ od uređaja koji je izložen internetu.

## Air gap smanjuje rizik, ali ga ne uklanja

Air-gapped wallet nema izravnu podatkovnu vezu s računalom ili internetom. Umjesto standardne USB komunikacije može koristiti QR kodove, microSD karticu, kameru ili drugi odvojeni način prijenosa podataka.

Time se smanjuje mogućnost da zlonamjerni program na računalu izravno komunicira s walletom ili iskoristi ranjivost u komunikacijskom protokolu. Međutim, air gap štiti samo od određenih vrsta napada.

Ne štiti od slabo generiranog seeda, kompromitiranog firmwarea, fizički preinačenog uređaja, pogrešnog prikaza adrese na zaslonu, krađe seed fraze ili zlonamjerne transakcije koju korisnik sam potvrdi.

Offline zato nije isto što i potpuno sigurno. To samo znači da je jedan važan kanal napada znatno ograničen.

{{< support1 >}}

## Najveći problem može nastati prije prve transakcije

Sigurnost svakog kripto novčanika počinje u trenutku stvaranja seeda. Seed fraza je temelj iz kojeg se izvode privatni ključevi i adrese. Ako je seed dovoljno nasumičan, napadač ga praktično ne može pogoditi pretraživanjem mogućih kombinacija.

Problem nastaje ako uređaj koristi neispravan ili predvidljiv generator slučajnih brojeva. Tada broj mogućih seedova može biti mnogo manji nego što korisnik očekuje.

Napadač u tom slučaju ne mora hakirati uređaj, ukrasti ga niti ga spojiti na internet. Može na vlastitom računalu generirati moguće seedove, iz njih izvoditi privatne ključeve i provjeravati postoje li sredstva na pripadajućim blockchain adresama.

Kada pronađe podudaranje, može potpisati transakciju bez ikakve komunikacije s originalnim hardware walletom. Uređaj žrtve može cijelo vrijeme biti zaključan u sefu, ali ako je seed bio predvidljiv, sredstva ipak mogu biti ukradena.

## Firmware je dio sigurnosnog modela

Hardware wallet nije samo fizički uređaj. Njegovu sigurnost određuje i firmware, odnosno softver koji upravlja generiranjem ključeva, prikazom adresa, potpisivanjem transakcija i komunikacijom s drugim uređajima.

Pogreška u firmwareu može oslabiti izvor entropije, pogrešno prikazati iznos ili adresu, dopustiti neispravno obrađivanje transakcije ili otvoriti mogućnost fizičkog i udaljenog napada.

Zato je važno firmware preuzimati samo sa službenih izvora i, kada proizvođač to omogućuje, provjeriti njegov digitalni potpis.

Ipak, čak ni najnoviji firmware ne može uvijek ispraviti ono što se dogodilo ranije. Ako je postojeći seed generiran na ranjivoj verziji, naknadno ažuriranje može spriječiti stvaranje novih slabih seedova, ali starom seedu ne može naknadno dodati izgubljenu entropiju.

U takvoj situaciji potrebno je generirati potpuno novi seed na ispravljenom uređaju i sredstva premjestiti na nove adrese.

{{< support2 >}}

## Zaslon uređaja važniji je od prikaza na računalu

Jedna od glavnih prednosti hardware walleta jest mogućnost neovisne provjere transakcije na vlastitom zaslonu uređaja.

Računalo može prikazivati jednu adresu, dok zlonamjerni program u pozadini priprema drugu. Zato korisnik ne bi trebao vjerovati samo informacijama prikazanim u aplikaciji na računalu ili mobitelu.

Prije potvrde potrebno je na zaslonu walleta provjeriti adresu primatelja, iznos, mrežu, naknadu i vrstu transakcije. Kod DeFi aplikacija i tokena treba provjeriti i daje li se smart contractu ovlast za trošenje sredstava.

Ako zaslon uređaja ne prikazuje dovoljno podataka, korisnik može potpisati transakciju čiji stvarni učinak ne razumije. To je posebno opasno kod složenijih smart contract radnji, gdje jedan potpis može odobriti neograničeno trošenje tokena ili trajnu ovlast nad walletom.

## Hardware wallet ne zna što korisnik želi

Hardware wallet može provjeriti je li transakcija tehnički ispravno potpisana privatnim ključem. Ne može uvijek znati odgovara li ona stvarnoj namjeri korisnika.

Ako vlasnik potvrdi lažnu adresu, zlonamjerni smart contract, neograničeni token approval ili prijevarnu poruku, uređaj može sve tehnički ispravno potpisati.

U takvoj situaciji privatni ključ nije ukraden, firmware možda nije ranjiv, a air gap može savršeno raditi. Sredstva se ipak mogu izgubiti zato što je korisnik odobrio zlonamjernu radnju.

Zbog toga phishing i manipulacija korisnikom ostaju ozbiljna prijetnja čak i vlasnicima hardware walleta.

{{< support1 >}}

## Seed fraza ostaje najvažnija točka napada

Ni najkvalitetniji uređaj ne može zaštititi seed koji je korisnik fotografirao, spremio u cloud, poslao e-mailom ili unio na lažnu web-stranicu.

Tko posjeduje seed frazu najčešće može obnoviti wallet na drugom uređaju i preuzeti sredstva. Zato se seed ne bi trebao fotografirati, spremati u običnu tekstualnu datoteku, slati porukom ili e-mailom niti unositi u online obrazac.

Posebno su opasne lažne stranice i navodna korisnička podrška koja traži „provjeru walleta” unosom seed fraze. Legitimna podrška proizvođača ne bi trebala tražiti kompletnu seed frazu.

Sigurnosna kopija također mora biti zaštićena od požara, vode, krađe i slučajnog uništenja. Papirnata kopija jednostavna je za korištenje, ali je fizički osjetljiva. Metalna kopija može biti otpornija, ali i dalje mora biti skrivena i dostupna samo ovlaštenoj osobi.

## PIN i passphrase nisu ista stvar

PIN štiti pristup fizičkom uređaju. Ako netko ukrade hardware wallet, PIN mu otežava pristup i potpisivanje transakcija.

Passphrase ima drugačiju ulogu. U kombinaciji s osnovnim seedom stvara dodatni wallet. Ako napadač dođe do seed fraze, ali ne zna snažan i jedinstven passphrase, možda neće moći pronaći sredstva spremljena u tom dodatnom walletu.

Međutim, passphrase povećava i odgovornost korisnika. Ako ga zaboravi ili pogrešno zapiše, sredstva se ne mogu vratiti. Svaka drugačija kombinacija znakova može otvoriti potpuno drugi, valjani, ali prazan wallet.

Kratak i predvidljiv passphrase također može biti pogođen automatiziranim pokušajima. Zato passphrase ima smisla samo ako je dovoljno snažan i sigurno pohranjen.

{{< support2 >}}

## Rizik počinje i pri kupnji uređaja

Hardware wallet trebalo bi kupovati izravno od proizvođača ili provjerenog ovlaštenog prodavatelja. Uređaj kupljen preko nepoznatog oglasa ili preprodavača može biti otvoren, preinačen, zamijenjen kopijom ili unaprijed konfiguriran.

Posebno je opasno ako dolazi s već ispisanom seed frazom. Pravi seed korisnik treba generirati sam na uređaju nakon provjere pakiranja i instaliranja službenog firmwarea.

Unaprijed pripremljena seed kartica može značiti da netko već posjeduje kopiju privatnih ključeva i samo čeka da korisnik uplati sredstva.

Korisnik također treba provjeriti izgleda li pakiranje neoštećeno, prepoznaje li uređaj službena aplikacija i prikazuje li proizvođač postupak provjere autentičnosti uređaja.

## Fizička sigurnost i dalje je važna

Nisu svi napadi digitalni. Netko može pokušati ukrasti uređaj, pronaći papirnatu ili metalnu kopiju seeda, snimiti PIN kamerom ili fizički zamijeniti wallet.

Kod većih iznosa postoji i rizik prisile vlasnika. Zbog toga sigurnost ne završava tehničkim značajkama uređaja.

Važno je gdje se čuva seed, zna li netko da vlasnik posjeduje veći iznos kriptovaluta i postoji li plan za oporavak, nasljeđivanje ili izvanredne situacije.

Sigurnosna kopija i uređaj ne bi se trebali čuvati na istom mjestu ako bi jedna krađa, požar ili poplava mogli uništiti oboje.

{{< support1 >}}

## Jedan wallet nije uvijek najbolji za sve

Korisnik može smanjiti štetu tako da sva sredstva ne drži pod jednim seedom. Manji hot wallet može koristiti za svakodnevne transakcije, poseban wallet za DeFi, a hardware wallet za dugoročno čuvanje.

Za veće iznose mogu se koristiti odvojeni walleti ili multisig postava u kojoj za slanje sredstava nije dovoljan samo jedan ključ.

Takva podjela smanjuje posljedice kompromitiranja jednog walleta. Međutim, više walleta znači i više seedova, sigurnosnih kopija, adresa i prilika za ljudsku pogrešku.

Sigurnosni model mora biti dovoljno snažan, ali i dovoljno jednostavan da ga korisnik može pravilno održavati.

## Multisig smanjuje ovisnost o jednom ključu

Kod standardnog walleta jedan seed najčešće kontrolira sva sredstva. Kod multisig postave za transakciju su potrebna dva ili više različitih potpisa.

U modelu 2-od-3 postoje tri ključa, ali su za slanje sredstava potrebna bilo koja dva. Ako je jedan hardware wallet ranjiv ili jedan seed ukraden, napadač još uvijek ne može samostalno premjestiti sredstva.

Multisig može značajno povećati sigurnost, ali donosi dodatnu složenost. Ključevi se moraju čuvati odvojeno, potrebno je sačuvati podatke o konfiguraciji i dobro razumjeti postupak oporavka.

Za manje iznose takav sustav može biti nepotrebno složen, ali za poslovne rezerve ili veće iznose može pružiti važnu dodatnu zaštitu.

{{< support2 >}}

## Sigurnost nije jedna značajka

Nijedna pojedinačna oznaka ne može jamčiti sigurnost hardware walleta. Nije dovoljno samo to što je uređaj offline, air-gapped, open-source, Bitcoin-only ili opremljen secure elementom.

Svaka od tih značajki rješava samo dio problema.

Stvarna sigurnost ovisi o cijelom lancu: načinu proizvodnje uređaja, izvoru kupnje, kvaliteti firmwarea, generiranju seeda, zaštiti sigurnosne kopije, provjeri podataka na zaslonu, načinu potpisivanja, ponašanju korisnika i praćenju sigurnosnih upozorenja proizvođača.

Dovoljna je jedna ozbiljna slabost da ugrozi cijeli sustav.

Hardware wallet može biti važan dio sigurnosnog modela, ali nije zamjena za razumijevanje transakcije, provjeru adrese i pažljivo upravljanje seedom.

## Što korisnik može praktično napraviti?

Korisnik hardware walleta trebao bi kupiti uređaj iz provjerenog izvora, samostalno generirati seed, instalirati službeni firmware i provjeravati adresu i iznos na zaslonu uređaja prije svake transakcije.

Kod većih prijenosa preporučljivo je najprije poslati mali testni iznos. Wallet za dugoročno čuvanje trebalo bi odvojiti od walleta koji se koristi za DeFi aplikacije i svakodnevne transakcije.

Važno je pratiti službena sigurnosna upozorenja proizvođača i znati na kojoj je verziji firmwarea postojeći seed izvorno generiran. Za veće iznose može se razmotriti snažan passphrase ili multisig, ali samo ako korisnik razumije postupak oporavka.

Najsigurniji wallet nije nužno onaj s najviše funkcija, nego onaj čiji sigurnosni model korisnik razumije i može dosljedno primjenjivati.

## Naš osvrt

* Hardware wallet značajno smanjuje rizik krađe privatnog ključa s računala ili mobitela povezanog s internetom.
* Air-gapped način rada dodatno ograničava izravnu komunikaciju sa zaraženim uređajem.
* Offline način rada nije jamstvo potpune sigurnosti.
* Predvidljivo generiran seed može biti rekonstruiran bez fizičkog pristupa uređaju.
* Ranjivi firmware može ugroziti generiranje ključeva, prikaz transakcije ili postupak potpisivanja.
* Naknadno ažuriranje firmwarea ne može nužno popraviti seed koji je već nastao na ranjivoj verziji.
* Zaslon uređaja služi za neovisnu provjeru adrese, iznosa i vrste transakcije.
* Hardware wallet može tehnički ispravno potpisati zlonamjernu radnju ako je korisnik potvrdi.
* Seed fraza ostaje najosjetljiviji dio cijelog sigurnosnog sustava.
* PIN štiti pristup uređaju, dok passphrase stvara dodatni wallet.
* Uređaj kupljen iz nepouzdanog izvora može biti preinačen ili unaprijed konfiguriran.
* Više odvojenih walleta može ograničiti štetu, ali povećava operativnu složenost.
* Multisig smanjuje ovisnost o jednom uređaju ili seedu, ali zahtijeva pažljivo planiranje.
* Sigurnost hardware walleta ovisi o cijelom procesu, a ne samo o tome je li uređaj povezan s internetom.

**Disclaimer:** Članak je informativnog i edukativnog karaktera te ne predstavlja financijski, investicijski ili sigurnosni savjet. Korisnici trebaju provjeravati službenu dokumentaciju i sigurnosna upozorenja proizvođača te nikada ne unositi seed frazu ili passphrase na web-stranice, u obrasce ili na nepouzdane uređaje.

U suradnji s AI-jem.
