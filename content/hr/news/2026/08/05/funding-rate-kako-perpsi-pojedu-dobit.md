---
title: "Funding rate: kako perpsi pojedu dobit"
slug: "funding-rate-kako-perpsi-pojedu-dobit"
date: 2026-08-05T06:00:00+02:00
category: "crypto"
translationKey: "funding-rate-kako-perpsi-pojedu-dobit-2026-08-05"
source: "Hyperliquid, Binance i javno dostupna dokumentacija o perpetual futures ugovorima"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/informative/Funding-cost-perps.png"
featured_image: "/images/informative/Funding-cost-perps.png"
image: "/images/informative/Funding-cost-perps.png"
thumbnail: "/images/informative/Funding-cost-perps.png"
image_alt: "Funding rate kao skriveni trošak trgovanja perpetual futures ugovorima"
image_credit: "Metaadvisor.eu – slika je simbolična"
tags: ["funding rate", "perpetual futures", "perpsi", "kripto trgovanje", "poluga", "long pozicija", "short pozicija", "trgovačke naknade", "Hyperliquid", "Binance", "derivati", "margin trading", "likvidacija", "kripto rizik", "upravljanje rizikom"]
description: "Funding rate može postupno smanjivati dobit na perpetual futures pozicijama, osobito pri dugom držanju, većoj poluzi i visokim stopama."
summary: "Perpetual futures ugovori nemaju datum isteka, ali nisu besplatni za dugotrajno držanje. Funding se periodično obračunava na cijelu vrijednost pozicije i može značajno smanjiti konačnu zaradu."
---

# Funding rate: kako perpsi pojedu dobit

Perpetual futures ugovori, poznati kao perpsi, postali su jedan od najpopularnijih načina trgovanja kriptovalutama. Omogućuju otvaranje long ili short pozicije uz polugu, nemaju datum isteka i često nude duboku likvidnost te relativno niske naknade za trgovanje.

Ipak, postoji trošak koji trgovci lako zanemare: funding rate.

Pozicija može biti otvorena danima ili tjednima, cijena se može kretati u očekivanom smjeru, a dio dobiti može postupno nestajati zbog periodičnih funding plaćanja.

*Slika je simbolična.*

## Što su perpetual futuresi?

Klasični futures ugovor ima datum isteka. Perpetual futures nema, pa trgovac poziciju teoretski može držati neograničeno dugo, pod uvjetom da ima dovoljno margine i ne bude likvidiran.

Perpsi omogućuju trgovanje rastom i padom cijene bez stvarne kupnje tokena:

* long pozicija zarađuje ako cijena raste
* short pozicija zarađuje ako cijena pada
* poluga povećava veličinu pozicije u odnosu na položeni kolateral

Trgovci cijene perpse zbog njihove likvidnosti, relativno niskih naknada i velike tržišne izloženosti koju mogu ostvariti s malom količinom kolaterala.

Međutim, dugotrajno držanje pozicije može stvoriti dodatni trošak koji nije vidljiv samo iz naknade za otvaranje trgovine.

## Zašto funding rate postoji?

Budući da perpetual futures nema datum isteka, potreban je mehanizam koji njegovu cijenu drži blizu stvarne spot cijene kriptovalute.

Funding rate zato stvara periodična plaćanja između trgovaca koji drže long i short pozicije.

Kada previše trgovaca želi biti u longu, cijena perpa može porasti iznad spot cijene. Tada je funding obično pozitivan:

**Long pozicije plaćaju short pozicijama.**

Kada prevladavaju short pozicije, funding može postati negativan:

**Short pozicije plaćaju long pozicijama.**

Novac u pravilu ne ide burzi, nego se prenosi između dviju strana tržišta. Funding tako potiče trgovce da otvaraju pozicije na manje popularnoj strani i pomaže približiti cijenu perpa spot tržištu.

{{< support1 >}}

## Funding se računa na cijelu poziciju

Jedna od najvažnijih stvari jest da se funding ne računa samo na novac koji je trgovac položio kao marginu.

Računa se na punu vrijednost otvorene pozicije.

Ako trgovac položi 10 dolara i uz polugu 4x otvori poziciju vrijednu 40 dolara, funding se računa na 40 dolara.

Primjerice, uz funding od 0,05 posto:

* pozicija od 10 dolara plaća 0,005 dolara
* pozicija od 40 dolara plaća 0,02 dolara
* pozicija od 10.000 dolara plaća 5 dolara

Jedno plaćanje može izgledati beznačajno. Međutim, ono se ponavlja sve dok je pozicija otvorena i dok trgovac ostaje na strani koja plaća funding.

## Kako funding može pojesti dobit?

Zamislimo poziciju vrijednu 1.000 dolara koja tijekom nekoliko dana ostvari 20 dolara nerealizirane dobiti.

Ako trgovac u istom razdoblju plati tri dolara fundinga, naknadu pri otvaranju i zatvaranju pozicije te trošak spreada ili slippagea, njegova stvarna dobit bit će manja od iznosa koji je gledao u osnovnom prikazu kretanja cijene.

Kod vrlo visokog fundinga pozicija čak može pravilno predvidjeti smjer tržišta, a ipak završiti s vrlo malom dobiti ili gubitkom.

Funding je osobito važan kod pozicija koje se drže danima ili tjednima. Za trgovinu koja traje nekoliko minuta jedno funding razdoblje možda neće imati velik učinak, ali kod dugog držanja mali se iznosi zbrajaju.

{{< support2 >}}

## Kako funding radi na Hyperliquidu?

Hyperliquid funding obračunava svakog sata.

Plaćanje se računa na temelju veličine pozicije, oracle cijene i trenutačne funding stope. Službena dokumentacija navodi i gornju granicu od četiri posto po satu.

To ne znači da je funding uobičajeno četiri posto. Znači da u ekstremnim tržišnim okolnostima može narasti znatno više nego što trgovci očekuju.

Funding se razlikuje od tokena do tokena i može se brzo mijenjati. U jednom trenutku Hyperliquid može biti skuplji od druge platforme, a u drugom jeftiniji ili čak imati suprotan predznak.

Zato nije dovoljno pogledati funding samo pri otvaranju pozicije. Stopa se može promijeniti dok je trgovina još otvorena.

## Mali iznosi ne znače da funding nije važan

Kod pozicija vrijednih nekoliko dolara apsolutni iznos fundinga obično će biti vrlo malen.

To može biti samo djelić centa po obračunu. Takva trgovina vjerojatno neće pretrpjeti ozbiljan gubitak samo zbog fundinga.

Ipak, male pozicije korisne su za učenje jer jasno pokazuju:

* kada long plaća shortu
* kada short prima funding
* kako poluga povećava vrijednost pozicije
* zašto nerealizirani P&L nije isto što i konačna zarada
* kako se periodični trošak nakuplja tijekom vremena

Kod malih pozicija veći problem od fundinga često mogu biti trgovačke naknade, spread i činjenica da se očekivani pomak cijene nikada nije dogodio.

{{< support1 >}}

## Funding može biti i zarada

Funding nije uvijek trošak.

Trgovac koji se nalazi na strani koja prima funding može dobivati periodična plaćanja sve dok drži poziciju.

Zbog toga neki profesionalni trgovci koriste strategije čiji je cilj prikupljanje fundinga uz istodobno smanjivanje izloženosti promjeni cijene.

Međutim, visoki pozitivni funding nije automatski razlog za otvaranje short pozicije, kao što visoki negativni funding nije automatski signal za long.

Tržište može nastaviti snažno rasti ili padati mnogo dulje nego što trgovac može ostati solventan. Potencijalna zarada od fundinga tada može biti zanemariva u usporedbi s gubitkom na samoj poziciji ili likvidacijom.

## Hourly, osmosatni i godišnji funding nisu isto

Posebno je opasno izravno uspoređivati brojke dviju platformi ako jedna prikazuje hourly funding, druga osmosatnu stopu, a treća godišnju procjenu.

Stopa od 0,01 posto po satu nije isto što i 0,01 posto svakih osam sati.

Godišnja procjena također nije zajamčeni trošak za sljedećih godinu dana. Ona samo pokazuje koliko bi funding iznosio kada bi trenutačna stopa ostala nepromijenjena, što se u praksi rijetko događa.

Prije usporedbe potrebno je sve stope svesti na isto vremensko razdoblje.

{{< support2 >}}

## Što provjeriti prije otvaranja perpa?

Prije otvaranja pozicije potrebno je provjeriti:

* je li funding pozitivan ili negativan
* plaća li ga long ili short strana
* koliko često se obračunava
* odnosi li se prikazana stopa na jedan sat, osam sati ili godišnju procjenu
* kolika je puna vrijednost pozicije
* koliko dugo se pozicija planira držati
* koliko je funding bio promjenjiv tijekom posljednjih sati ili dana

Trgovac treba provjeriti i dosadašnja funding plaćanja na već otvorenoj poziciji. Nerealizirana dobit može izgledati dobro, ali konačni rezultat uključuje funding, trgovačke naknade i trošak zatvaranja pozicije.

## Perpsi nemaju datum isteka, ali imaju trošak

Perpetual futuresi izgledaju jednostavno: odabere se long ili short, postavi poluga i prati cijena.

Stvarni trošak ipak nije ograničen na malu naknadu za otvaranje i zatvaranje pozicije.

Funding rate može biti gotovo neprimjetan kod kratke trgovine i male pozicije, ali postati važan kod velike poluge, popularnih altcoina i dugotrajnog držanja.

Najvažnije je razumjeti da se funding računa na cijelu poziciju, da ga ne plaća uvijek ista strana i da se stopa može mijenjati dok je trgovina otvorena.

Perpsi nemaju datum isteka, ali to ne znači da ih je besplatno držati neograničeno dugo.

## Naš osvrt

* Perpetual futures ugovori nemaju datum isteka.
* Funding rate pomaže održavati cijenu perpa blizu spot cijene.
* Kod pozitivnog fundinga long pozicije obično plaćaju short pozicijama.
* Kod negativnog fundinga short pozicije obično plaćaju long pozicijama.
* Funding se računa na punu vrijednost pozicije, a ne samo na položenu marginu.
* Poluga zato povećava i iznos na koji se funding obračunava.
* Mala periodična plaćanja mogu se značajno nakupiti tijekom dugog držanja.
* Funding stopa može se promijeniti dok je pozicija otvorena.
* Hyperliquid funding obračunava svakog sata.
* Funding može biti trošak, ali i prihod za stranu koja ga prima.
* Visoki funding sam po sebi nije dovoljan signal za long ili short poziciju.
* Hourly, osmosatne i godišnje stope ne smiju se uspoređivati bez preračunavanja.
* Nerealizirani P&L ne pokazuje nužno konačnu zaradu nakon svih troškova.

**Disclaimer:** Članak je informativnog i edukativnog karaktera te ne predstavlja financijski ili investicijski savjet. Trgovanje izvedenicama i korištenje poluge uključuju visok rizik gubitka.

U suradnji s AI-jem.
