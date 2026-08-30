---
title: "Kako napraviti vlastiti QR kod izravno u Wordu"
slug: "kako-napraviti-vlastiti-qr-kod-u-wordu"
date: 2026-08-30T12:30:00+02:00
category: "Tech"
translationKey: "how-to-create-your-own-qr-code-in-microsoft-word-2026-08-30"
source: "Microsoft, Metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/metaadvisor1.png"
featured_image: "/images/metaadvisor1.png"
image: "/images/metaadvisor1.png"
thumbnail: "/images/metaadvisor1.png"
image_alt: "Kako napraviti vlastiti QR kod izravno u Microsoft Wordu"
image_credit: "Metaadvisor.eu"
tags: ["Microsoft Word", "QR code", "QR kod", "Microsoft", "Word trikovi", "Word savjeti", "tehnologija", "digitalni alati", "DISPLAYBARCODE", "Ctrl F9", "barcode", "productivity", "Office"]
description: "Microsoft Word može napraviti QR kod bez dodatnog programa ili online QR generatora. Dovoljno je koristiti ugrađenu naredbu DISPLAYBARCODE i nekoliko tipki."
summary: "QR kod ne morate izrađivati na vanjskim web-stranicama. Microsoft Word ima ugrađenu naredbu DISPLAYBARCODE kojom se web-link, tekst ili drugi podaci mogu pretvoriti u QR kod izravno u dokumentu."
---

# Kako napraviti vlastiti QR kod izravno u Microsoft Wordu

Za izradu QR koda nije uvijek potreban poseban program niti online QR generator. **Microsoft Word ima ugrađenu funkciju kojom se web-adresa, tekst ili drugi podaci mogu pretvoriti u QR kod izravno unutar dokumenta.**

Funkcija se zove **DISPLAYBARCODE**, a cijeli postupak traje svega nekoliko sekundi kada znate koju naredbu treba upisati.

To može biti posebno praktično za dokumente, ponude, letke, upute, prezentacije ili bilo koji sadržaj iz kojeg želite korisnika jednim skeniranjem poslati na web-stranicu.

## Kako napraviti QR kod u Wordu

Otvorite Microsoft Word i kliknite na mjesto u dokumentu na kojem želite napraviti QR kod.

Zatim pritisnite:

**Ctrl + F9**

Word će umetnuti posebne field zagrade:

`{ }`

Važno je da te zagrade ne upisujete ručno. Kombinacija **Ctrl + F9** stvara posebno Wordovo polje unutar kojeg se može izvršiti naredba.

Unutar zagrada zatim se upisuje DISPLAYBARCODE naredba.

Primjer za web-stranicu Metaadvisor.eu:

`{ DISPLAYBARCODE "https://metaadvisor.eu" QR \s 100 }`

Nakon toga označite field i pritisnite **F9**.

Word bi naredbu trebao pretvoriti u QR kod. Ako se QR kod ne pojavi automatski, ponovno pritisnite **F9**, ovaj put bez tipke Ctrl.

![Kako napraviti QR kod u Microsoft Wordu](/images/informative/how-to-make-qr-code1.png)

## Što znači DISPLAYBARCODE

DISPLAYBARCODE je Wordova naredba za generiranje različitih vrsta barkodova.

U primjeru:

`{ DISPLAYBARCODE "https://metaadvisor.eu" QR \s 100 }`

dio:

`"https://metaadvisor.eu"`

predstavlja sadržaj koji se sprema unutar QR koda.

Oznaka:

`QR`

govori Wordu da napravi QR kod, dok:

`\s 100`

određuje njegovu veličinu.

Broj se može mijenjati. Veća vrijednost stvara veći QR kod, dok manja vrijednost smanjuje njegov prikaz.

{{< support1 >}}

## QR kod može sadržavati više od web-linka

QR kodovi se najčešće povezuju s web-stranicama, ali URL nije jedina vrsta sadržaja koju mogu pohraniti.

Unutar QR koda moguće je spremiti i običan tekst.

Primjer:

`{ DISPLAYBARCODE "Grüße aus Hamburg" QR \s 100 }`

Moguće je napraviti i QR kod s njemačkim telefonskim brojem:

`{ DISPLAYBARCODE "tel:+491701234567" QR \s 100 }`

Ili s e-mail adresom:

`{ DISPLAYBARCODE "mailto:info@example.de" QR \s 100 }`

Način na koji će mobitel reagirati nakon skeniranja ovisi o vrsti sadržaja. Ako QR sadrži web-adresu, uređaj će najčešće ponuditi otvaranje stranice. Ako sadrži običan tekst, neki mobiteli mogu ga prikazati kao tekst, dok ga drugi mogu automatski poslati tražilici kao upit za pretraživanje.

## Koliko teksta može stati u QR kod

QR kod može sadržavati znatno više podataka od kratkog URL-a, ali s povećanjem količine teksta kod postaje sve gušći.

To se vrlo brzo vidi i u Wordu.

QR kod napravljen samo od kratkog linka sastoji se od relativno malog broja crno-bijelih polja. Ako u isti kod unesemo nekoliko rečenica, Word mora generirati znatno složeniji uzorak.

Rezultat može biti QR kod koji zauzima velik dio stranice.

Veličinu je moguće smanjiti promjenom vrijednosti `\s`, primjerice s:

`\s 100`

na:

`\s 50`

ili još manje.

No fizički manji QR kod s velikom količinom podataka može postati teži za skeniranje, posebno ako je ispisan u lošoj kvaliteti ili prikazan u vrlo maloj veličini.

Zbog toga je za duže sadržaje praktičnije napraviti QR kod koji vodi na web-stranicu nego pokušavati spremiti cijeli članak izravno unutar samog QR koda.

{{< support2 >}}

## Kako provjeriti radi li QR kod

Najjednostavniji test ne zahtijeva nikakav dodatni program.

Usmjerite kameru mobitela prema QR kodu.

Ako QR sadrži web-link, na zaslonu bi se trebala pojaviti poveznica koju je moguće otvoriti dodirom.

Primjer iz ovog članka vodi na:

`https://metaadvisor.eu`

Kod pojedinih mobitela može se dogoditi da se poveznica nakon skeniranja otvori samo nakratko ili da se preglednik vrati na prethodno otvorenu stranicu.

Ako se to dogodi, dodirnite otvorenu stranicu odmah nakon učitavanja ili ponovno skenirajte QR kod. To ne mora značiti da je QR kod neispravan, nego može biti posljedica načina na koji kamera ili preglednik obrađuju rezultat skeniranja.

## Zašto QR kod ima samo tri velika kvadrata

Pri prvom pogledu na QR kod može izgledati kao da mu u donjem desnom kutu nešto nedostaje.

To je normalno.

Standardni QR kod ima tri velika pozicijska markera:

* gore lijevo
* gore desno
* dolje lijevo

Četvrti veliki kvadrat u donjem desnom kutu nije potreban.

Ti markeri omogućuju uređaju da prepozna orijentaciju QR koda bez obzira na kut pod kojim ga skeniramo.

Zbog toga pravilno generiran QR kod često izgleda kao da mu jedan veliki kut nedostaje, iako je upravo takav raspored očekivan.

## Word može zamijeniti jednostavan online QR generator

Za naprednije QR kodove postoje specijalizirani alati koji nude promjenu boja, umetanje logotipa, praćenje skeniranja, dinamičke linkove i druge funkcije.

Ali za jednostavan QR kod koji vodi na web-stranicu ili sadrži kratki tekst Wordova ugrađena funkcija može biti sasvim dovoljna.

Prednost je i u tome što podatke nije potrebno unositi na nepoznatu vanjsku web-stranicu samo kako bi se generirala slika QR koda.

Za korisnika koji već radi u Wordu postupak se svodi na nekoliko koraka:

**Ctrl + F9 → DISPLAYBARCODE → F9 → QR kod.**

To je jedna od onih Wordovih funkcija koje su godinama dostupne u programu, ali ih velik broj korisnika nikada ne primijeti.

## Naš osvrt

* **Najzanimljiviji dio ove funkcije nije sam QR kod, nego činjenica da za osnovnu izradu QR koda nije potreban dodatni online servis.**
* **Word QR kod može sadržavati web-link, tekst, e-mail adresu ili telefonski broj**, ali ponašanje nakon skeniranja ovisi o tome kako mobitel interpretira podatke.
* **Što više teksta spremimo u QR kod, kod postaje složeniji i gušći.** Zbog toga nije uvijek dobra ideja pokušavati u njega spremiti velike količine sadržaja.
* **Za web-članke i druge duže sadržaje i dalje je praktičnije u QR kod spremiti samo URL.**
* **Ako QR kod izgleda kao da mu nedostaje donji desni veliki kvadrat, to je normalno.** Standardni QR kod koristi tri velika pozicijska markera.
* **DISPLAYBARCODE je dobar primjer koliko funkcija u Wordu ostane praktički nevidljivo sve dok netko slučajno ne otkrije pravu naredbu.**

**Pratite Metaadvisor.eu za više praktičnih tehnoloških trikova, AI alata, digitalnih savjeta, sigurnosnih tema i drugih načina kako bolje iskoristiti alate koje već svakodnevno koristimo.**

**Disclaimer:** Informacije u ovom članku služe u informativne i edukativne svrhe. Dostupnost pojedinih funkcija i način prikaza mogu ovisiti o verziji Microsoft Worda, operativnom sustavu i postavkama uređaja. Prije korištenja QR koda u važnim dokumentima preporučujemo da ga testirate na nekoliko uređaja i provjerite vodi li na očekivani sadržaj.

<small style="color:#999; font-size:0.8em;">U suradnji s AI-jem.</small>
