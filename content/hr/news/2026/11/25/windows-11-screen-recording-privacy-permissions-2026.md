---
title: "Windows 11: Tko sve može snimati vaš zaslon?"
slug: "windows-11-screen-recording-privacy-permissions-2026"
date: "2026-11-25T00:05:00+01:00"
category: "technology"
translationKey: "windows-11-screen-recording-privacy-permissions-2026-11-25"
source: "MetaAdvisor: vlastito testiranje i dokumentirane snimke zaslona, 23. studenoga 2026."
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/AI-general/Windows-11-Screen-Recording-Explained.jpg"
featured_image: "/images/AI-general/Windows-11-Screen-Recording-Explained.jpg"
image: "/images/AI-general/Windows-11-Screen-Recording-Explained.jpg"
thumbnail: "/images/AI-general/Windows-11-Screen-Recording-Explained.jpg"
image_alt: "Windows 11 na prijenosnom računalu s ilustracijom snimanja zaslona i dozvola aplikacija"
image_credit: "Metaadvisor.eu"
tags: ["Windows 11","Microsoft","AI","Privacy","Cybersecurity","Screen Recording","Microsoft Recall","App Permissions"]
description: "Na računalu sa sustavom Windows 11 pronašli smo četiri uključene kategorije dozvola. Donosimo rezultate vlastitog testiranja i upute za njihovo isključivanje."
summary: "Snimanje zaslona, uklanjanje okvira snimanja, generiranje AI sadržaja i mijenjanje teksta u aktivnom polju. Provjerili smo što se događa nakon isključivanja tih dozvola."
categories: ["technology"]
---

*Naslovna slika je ilustrativna.*

**Snimanje zaslona, uklanjanje vidljivog upozorenja tijekom snimanja, generiranje sadržaja umjetnom inteligencijom, pa čak i mijenjanje teksta u aktivnom tekstualnom polju. Sve četiri kategorije dozvola pronašli smo uključene na računalu sa sustavom Windows 11, a da se vlasnik računala ne sjeća njihova odobravanja niti objašnjenja što njihovim odobravanjem omogućuje aplikacijama.**

Ono što smo pronašli otvorilo je niz pitanja o sigurnosti, privatnosti, informiranosti korisnika, ali i potrošnji računalnih resursa.

Zamislimo programera zaposlenog u banci ili kompaniji koja razvija blockchain tehnologiju, upravlja kriptovalutama ili razvija sustave umjetne inteligencije.

Na njegovu zaslonu mogu se nalaziti povjerljivi programski kod, API ključevi, privatni ključevi kripto novčanika, podaci klijenata, poslovne tajne ili informacije o sigurnosnoj infrastrukturi kompanije.

Slična situacija postoji u odvjetničkim uredima, zdravstvenim ustanovama, državnim institucijama, ali i kod običnih korisnika koji putem računala pristupaju svojim bankovnim računima i osobnim dokumentima.

Koliko njih zna koje su dozvole aplikacijama uključene na njihovim računalima?

## Četiri kategorije uključenih dozvola

U izborniku Settings > Privacy & security pronašli smo četiri kategorije aktiviranih dozvola:

- **Screenshots and screen recording:** snimanje zaslona.
- **Screenshot borders:** dopuštenje aplikacijama da uklone vidljivi okvir tijekom snimanja zaslona.
- **Text and image generation:** pristup funkcijama generiranja teksta i slika umjetnom inteligencijom.
- **Foreground text access:** pristup radi mijenjanja teksta u aktivnom tekstualnom polju.

Riječ je o zasebnim dozvolama unutar operacijskog sustava, neovisno o Microsoftovoj funkciji Recall.

## Snimanje zaslona bez vidljivog upozorenja

Jedna od zanimljivijih postavki je Screenshot borders. Ona aplikacijama omogućuje uklanjanje vidljivog okvira koji prati određene metode snimanja zaslona.

Na testiranom računalu dopuštenje za snimanje zaslona i uklanjanje okvira imao je Microsoft Teams. Pristup je bio omogućen i desktop aplikacijama kroz odgovarajuće Windowsove postavke.

Iako postojanje dozvole ne znači da aplikacija zaista snima zaslon, postavlja se pitanje koliko je korisnika svjesno da takva mogućnost postoji.

Zašto je mogućnost uklanjanja vidljivog upozorenja tijekom snimanja zaslona bila omogućena na našem računalu, a da se vlasnik ne sjeća da ju je odobrio? Iz samih postavki nismo mogli utvrditi kada su i kako dozvole aktivirane.

## Umjetna inteligencija u svakodnevnim aplikacijama

U kategoriji Text and image generation pronašli smo osam aplikacija kojima je bio omogućen pristup funkcijama generiranja teksta i slika:

- Alat za izrezivanje (Snipping Tool)
- Blok za pisanje (Notepad)
- Bojanje (Paint)
- Fotografije (Photos)
- Local AI Manager for Microsoft 365
- Microsoft Clipchamp
- Outlook
- Xbox

Na testiranom računalu nije bio evidentiran nijedan zahtjev za korištenje tih funkcija tijekom posljednjih sedam dana.

Microsoft sve više integrira umjetnu inteligenciju u svakodnevne aplikacije. Međutim, korisnik koji želi jednostavno napisati tekst u Notepadu, pregledati fotografiju ili izrezati dio zaslona možda uopće ne želi koristiti AI funkcije.

{{< support1 >}}

## Aplikacije mogu mijenjati tekst u aktivnom prozoru

Posebnu pozornost privukla nam je postavka Foreground text access.

Prema opisu unutar Windowsa, ova postavka aplikacijama omogućuje pristup radi mijenjanja teksta u trenutno aktivnom tekstualnom polju.

Takve funkcije mogu biti korisne za AI asistente, automatsko uređivanje teksta i alate za pristupačnost. Međutim, riječ je o dodatnoj dozvoli čije bi sigurnosne posljedice korisnici trebali razumjeti.

Na testiranom računalu i ova je postavka bila uključena, iako na popisu nisu bile prikazane pojedinačne aplikacije.

## Potencijalni sigurnosni rizik

Svaka nepotrebna dozvola može predstavljati dodatnu površinu napada ako je aplikacija kompromitirana ili se njezine mogućnosti zloupotrijebe.

U slučaju tehnoloških i financijskih kompanija posljedice potencijalne zloupotrebe mogu biti znatno ozbiljnije od narušavanja privatnosti pojedinca.

Pritom ne govorimo nužno o Microsoftu kao izvoru prijetnje, nego o sigurnosnim posljedicama pristupa koji operacijski sustav omogućuje aplikacijama.

Postojanje dozvole nije dokaz da je ona zloupotrijebljena, ali je svakako razlog za provjeru je li takav pristup uopće potreban.

## Tko odlučuje o potrošnji resursa računala?

Privatnost nije jedino pitanje koje se otvara sve većom integracijom umjetne inteligencije u operacijske sustave.

Aktivne AI funkcije, pozadinski procesi i lokalni modeli mogu koristiti:

- Radnu memoriju (RAM)
- Procesor (CPU)
- Grafički procesor (GPU)
- Procesor za AI obradu (NPU)
- Prostor na disku
- Električnu energiju i bateriju

Samo uključivanje dozvole ne znači automatski da se ti resursi troše, a njihovu stvarnu potrošnju nismo mjerili tijekom ovog testiranja. Isključivanje dozvola također ne mora zaustaviti pozadinske procese niti ukloniti instalirane AI modele.

Međutim, korisnici bi trebali imati mogućnost odlučivanja o tome koje funkcije žele koristiti i koje će se aktivnosti izvršavati na njihovu računalu.

Zašto bi korisnik koji je kupio računalo morao naknadno istraživati koje mu funkcije trebaju, a koje može isključiti?

## Isključili smo sve četiri dozvole. Što se dogodilo?

Tijekom vlastitog testiranja 23. studenoga 2026. isključili smo sve četiri navedene kategorije dozvola.

| Postavka | Prije testiranja | Nakon testiranja |
|---|---|---|
| Screenshots and screen recording | ON | OFF |
| Screenshot borders | ON | OFF |
| Text and image generation | ON | OFF |
| Foreground text access | ON | OFF |

Nakon isključivanja dozvola i dalje smo mogli ručno snimati zaslon, pisati poruke i slati tekst i fotografije.

Tijekom testiranih aktivnosti nismo primijetili gubitak osnovne funkcionalnosti.

Sve promjene dokumentirali smo snimkama zaslona prije i nakon isključivanja pojedinih dozvola.

Rezultati se odnose na jedno testirano računalo. Isključivanje ovih postavki ne jamči zaštitu od svih metoda snimanja zaslona, a neke specijalizirane funkcije aplikacija mogu postati nedostupne.

{{< support2 >}}

## Kako provjeriti vlastito računalo?

Otvorite Windows postavke pritiskom na tipke **Windows + I**.

Odaberite **Settings → Privacy & security** (Postavke → Privatnost i sigurnost).

Pomaknite se prema dnu stranice, gdje se nalaze dozvole aplikacija. Nazivi i dostupnost postavki mogu se razlikovati ovisno o verziji Windowsa.

### 1. Screenshots and screen recording

**Settings → Privacy & security → Screenshots and screen recording**

- **Screenshots and screen recording access → Off**, ako želite ograničiti pristup snimanju zaslona kroz taj sustav dozvola.
- **Recent activity:** provjerite evidentirane zahtjeve za snimanje zaslona tijekom posljednjih sedam dana.

Na testiranom računalu bilo je evidentirano nula zahtjeva. Taj podatak nije sveobuhvatan zapis svih mogućih metoda snimanja zaslona.

### 2. Screenshot borders

**Settings → Privacy & security → Screenshot borders**

- **Screenshot border settings access → Off**

Time aplikacijama ograničavate mogućnost uklanjanja vidljivog okvira tijekom snimanja zaslona kroz taj Windowsov sustav dozvola.

Nakon isključivanja prve dvije postavke možete provjeriti radi li ručno snimanje zaslona pritiskom na **Windows + Shift + S**.

### 3. Text and image generation

**Settings → Privacy & security → Text and image generation**

- **Text and image generation → Off**
- **Recent activity:** provjerite koje su aplikacije zatražile korištenje tih funkcija tijekom posljednjih sedam dana.

Isključivanje ove postavke ograničava pristup određenim Windowsovim AI funkcijama. Ne znači da su isključene sve AI usluge ili svi pozadinski procesi na računalu.

### 4. Foreground text access

**Settings → Privacy & security → Foreground text access**

- **Foreground text access → Off**

Time aplikacijama ograničavate pristup radi mijenjanja teksta u aktivnom tekstualnom polju kroz taj mehanizam dozvola.

Ako želite zadržati određene funkcije, možete provjeriti i pojedinačne dozvole aplikacija umjesto isključivanja cijele kategorije. Nakon svake promjene provjerite rade li vam potrebne funkcije. Na poslovnom računalu promjene uskladite s pravilima IT sigurnosti kompanije.

## Dodatno provjerite Microsoft Recall

Microsoft Recall zasebna je funkcija dostupna na kompatibilnim Copilot+ računalima, koja nakon aktiviranja periodično snima sadržaj zaslona kako bi korisnik kasnije mogao pretraživati svoje prethodne aktivnosti.

Otvorite:

**Settings → Privacy & security → Recall & snapshots**

Ako imate tu opciju, provjerite:

- **Save snapshots → Off**, ako ne želite automatsko snimanje.
- **Delete snapshots → Delete all**, ako želite obrisati prethodno pohranjene snimke.

Ako ne možete pronaći ovu kategoriju, moguće je da vaše računalo ne podržava Recall ili da funkcija nije dostupna na vašoj konfiguraciji.

Na testiranom računalu nismo pronašli tu opciju.

## Naš osvrt

- **Privatnost kao polazište:** Sigurnost i privatnost trebale bi biti polazište operacijskog sustava, a ne rezultat naknadnog istraživanja korisnika.
- **Informiranost korisnika:** Uvođenje novih AI funkcija trebalo bi biti popraćeno jasnim objašnjenjem njihovih mogućnosti, dozvola i potencijalnih sigurnosnih rizika.
- **Poslovna sigurnost:** Tehnološke, financijske i druge kompanije koje obrađuju povjerljive podatke trebale bi redovito provjeravati dozvole aplikacija na poslovnim računalima.
- **Računalni resursi:** Korisnici bi trebali imati jasnu kontrolu nad potrošnjom računalnih resursa, posebno kada je riječ o funkcijama koje nisu sami zatražili.
- **Korisnički izbor:** Nepotrebne dozvole trebale bi biti isključene dok korisnik sam ne odluči da ih želi koristiti.

Naše testiranje nije pokazalo da Microsoft neovlašteno snima zaslon ili prikuplja podatke. Pokazalo je, međutim, da su na testiranom računalu bile uključene četiri kategorije dozvola čijeg se odobravanja vlasnik računala ne sjeća.

Razvoj umjetne inteligencije donosi brojne prednosti. Međutim, mogućnost korištenja određene tehnologije ne bi trebala automatski podrazumijevati i dopuštenje za njezino korištenje.

**Računalo pripada korisniku. Odluka o tome što aplikacije na njemu smiju raditi također bi trebala pripadati korisniku.**

**Pratite Metaadvisor.eu za više neovisnih vijesti i analiza o umjetnoj inteligenciji, tehnologiji, poslovanju i digitalnim alatima.**

<small style="color:#757575; font-size:12px; font-weight:400; font-style:normal;">In collaboration with AI.</small>

**Napomena:** Članak se temelji na vlastitom testiranju i dokumentiranim snimkama zaslona od 23. studenoga 2026. Rezultati ne predstavljaju potvrdu zadanih postavki na svim računalima sa sustavom Windows 11 niti dokaz neovlaštenog snimanja ili prijenosa podataka. Sadržaj je informativan.
