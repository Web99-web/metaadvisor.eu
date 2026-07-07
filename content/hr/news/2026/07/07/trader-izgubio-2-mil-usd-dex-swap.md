---
title: "Trader izgubio 2 mil. USD na DEX swapu"
slug: "trader-izgubio-2-mil-usd-dex-swap"
date: 2026-07-07T18:00:00+02:00
category: "crypto"
translationKey: "trader-loses-2m-dex-swap-bad-route-2026-07-07"
source: "Cointelegraph, GoPlus Security, Metaadvisor.eu"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/news/MIllions-lost.png"
featured_image: "/images/news/MIllions-lost.png"
image: "/images/news/MIllions-lost.png"
thumbnail: "/images/news/MIllions-lost.png"
image_credit: "Metaadvisor.eu"
tags: ["DEX swap", "DeFi rizik", "MEV", "same-block backrun", "Titan Builder", "GoPlus Security", "Uniswap v3", "0x router", "slippage", "price impact", "crypto gubitak"]
summary: "Trader je izgubio gotovo 2 milijuna dolara nakon što je veliki ETH swap prošao kroz pool s vrlo malom likvidnošću. Slučaj pokazuje zašto su minimum received, slippage, price impact i ruta transakcije ključni prije svakog DEX potpisa."
disclaimer: "Ovaj članak služi isključivo u informativne svrhe i ne predstavlja financijski, investicijski, pravni ili sigurnosni savjet."
draft: false
---

Slika je simbolična.

# Trader izgubio 2 milijuna dolara na DEX swapu: nije bio klasični hack, nego katastrofalna ruta transakcije

Jedan crypto trader izgubio je gotovo cijeli iznos od oko **2 milijuna dolara** nakon što je na decentraliziranoj burzi pokušao napraviti veliki swap Ethera. Na kraju je, prema dostupnim izvještajima, ostao s tokenima vrijednima samo oko **14.500 dolara**.

Na prvi pogled priča zvuči kao još jedan crypto hack. Ali ovaj slučaj je zanimljiviji od toga. Ovdje se ne radi o tome da je netko jednostavno “ukrao wallet” ili prevario korisnika lažnim linkom. Problem je nastao zato što je transakcija prošla kroz **pool s vrlo malom likvidnošću**, a drugi sudionici na tržištu odmah su iskoristili razliku u cijeni.

Drugim riječima: trader je potpisao swap koji se izvršio po užasnoj cijeni.

Prema izvještaju Cointelegrapha i analizi GoPlus Securityja, trader je zamijenio **1.126,44 ETH**, vrijednih oko **2,01 milijun dolara**, ali je dobio samo **5.776 Lighter (LIT) tokena**. GoPlus Security opisao je incident kao “textbook case” takozvanog **same-block backrun extractiona**.

{{< support1 >}}

To znači da je u istom Ethereum bloku netko drugi mogao iskoristiti neravnotežu koju je stvorila ova velika i loše usmjerena transakcija.

Najveći dobitnik navodno je bio **Titan Builder**, koji je iz cijelog slučaja izvukao oko **1,8 milijuna dolara**.

## Što se zapravo dogodilo?

Trader je htio napraviti veliki swap na decentraliziranoj burzi. Kod takvih transakcija korisnik često ne ide direktno iz jednog tokena u drugi, nego DEX router pronalazi put kroz različite tokene i liquidity poolove.

U ovom slučaju swap je navodno usmjeren kroz **AVAIL/WETH pool na Uniswapu v3**, koji nije imao dovoljno likvidnosti za tako velik nalog.

To je ključ cijele priče.

Ako je pool mali, a nalog ogroman, cijena se može ekstremno pomaknuti. To je kao da pokušate zamijeniti 2 milijuna eura u malom kiosku umjesto preko velike banke. Kiosk nema dovoljno “dubine” za takvu transakciju, pa bi tečaj postao potpuno nepovoljan.

Prema GoPlus Securityju, dio transakcije završio je u poolu u kojem je cijena bila oko **120 puta viša** od cijene po kojoj se token kasnije mogao prodati.

Zato trader nije izgubio novac zato što “u poolu nije bilo novaca” u klasičnom smislu. Izgubio je novac zato što je njegova velika transakcija prošla kroz pool koji nije mogao normalno podnijeti taj volumen.

## Nije klasični sandwich attack

GoPlus Security naglašava da ovo nije bio klasični **sandwich attack**.

Kod sandwich napada bot obično vidi korisnikovu transakciju, kupi prije njega, pusti korisnika da pogura cijenu, a zatim proda odmah nakon njega. Korisnik se nađe “u sendviču” između dvije bot transakcije.

Ovdje je situacija bila drugačija.

GoPlus Security opisuje slučaj kao stvarnu, izrazito neuravnoteženu **backrunner arbitražu**. To znači da je loše izvršena transakcija sama stvorila priliku, a drugi sudionik ju je odmah iskoristio unutar istog bloka.

Zato je ovaj slučaj toliko neugodan: transakcija je možda tehnički prošla “kako je potpisana”, ali rezultat je za korisnika bio katastrofalan.

## Kako je trader mogao znati da nešto nije u redu?

Ovo je najvažniji i najzanimljiviji dio cijele priče.

Trader nije morao ručno znati koliko likvidnosti ima u svakom poolu. Nije trebao sam pregledavati svaki smart contract ili računati dubinu tržišta. Ali prije potpisa transakcije mogao je provjeriti nekoliko osnovnih signala koje DEX sučelje, wallet ili agregator često prikazuju prije nego korisnik klikne **Confirm**.

Prvi i najvažniji signal je **minimum received**.

To je minimalni iznos tokena koji će korisnik primiti ako se transakcija izvrši. Prije potvrde često piše nešto poput: “You will receive at least X tokens.”

Da je trader vidio da za ETH vrijedan oko **2 milijuna dolara** prima tokene koji nakon izvršenja vrijede samo oko **14.500 dolara**, to bi odmah bio znak da transakciju ne treba potpisati.

Drugi signal je **slippage** ili **price impact**.

Kod normalnog swapa price impact treba biti relativno mali. Ako sučelje pokazuje ogroman price impact, primjerice 30, 80 ili 99 posto, to znači da će sama transakcija snažno pomaknuti cijenu jer pool nema dovoljno likvidnosti.

Jednostavno rečeno: swap je prevelik za pool kroz koji prolazi.

Treći signal je **ruta transakcije**.

U naprednijem prikazu moguće je vidjeti kroz koje tokene i poolove swap prolazi. Ruta može izgledati kao:

ETH → WETH → AVAIL → LIT

ili nešto slično.

Da je trader vidio da ogroman iznos ide kroz mali ili čudan AVAIL/WETH pool, mogao je stati i ne potpisati transakciju.

## Kod 2 milijuna dolara ne klikće se samo Confirm

Kod swapa vrijednog oko **2 milijuna dolara** dodatno je važno usporediti rezultat na više DEX-ova i agregatora.

Takav iznos ne bi se trebao slati jednim brzim klikom bez provjere. Trader je mogao usporediti ponudu na servisima kao što su 1inch, Matcha, CoW Swap ili Uniswap. Mogao je razmotriti i OTC rješenje, pogotovo ako se radi o velikom nalogu i slabijoj likvidnosti.

Ako jedan router daje znatno lošiji rezultat od drugih, to je velika crvena zastava.

Postojala je i jednostavnija mogućnost: podijeliti transakciju na manje dijelove. Veliki swap kroz mali pool može izazvati ekstreman price impact. Manji nalozi, limit order ili OTC dogovor često smanjuju rizik da cijena pobjegne u potpuno nepovoljan smjer.

Zato se ova priča ne svodi samo na pitanje hakera ili MEV botova. Ona pokazuje koliko je opasno potpisivati DEX transakcije bez provjere detalja.

Trader nije morao unaprijed znati koliko “novca” ima u poolu, ali su mu posljedice toga vjerojatno mogle biti vidljive kroz četiri stvari: **minimum received, price impact, slippage i rutu swapa**.

Najkraće rečeno: problem nije bio samo u tome što je pool bio premalen. Problem je bio u tome što je transakcija potpisana iako su detalji swapa mogli pokazivati da je rezultat katastrofalan.

{{< support2 >}}

## Zašto su MEV i block builderi važni?

Ovaj incident ponovno otvara pitanje **MEV-a**, odnosno maximal extractable valuea.

MEV označava dodatnu vrijednost koju validatori, block builderi ili botovi mogu izvući iz načina na koji se transakcije slažu, izvršavaju i redaju u blockchain bloku.

U praksi to znači da netko tko vidi veliku ili loše postavljenu transakciju može pokušati izvući profit iz razlike u cijeni, arbitraže ili redoslijeda izvršavanja.

<a href="https://metaadvisor.eu/hr/news/sto-je-mev-trgovanje-defi/" target="_blank" rel="noopener">
  <img src="/images/MEV-explained.png" alt="Što je MEV trgovanje i zašto je postalo jedan od najvećih problema DeFi-ja" style="max-width: 360px; width: 100%; height: auto; display: block; margin: 1rem 0;">
</a>

<a href="https://metaadvisor.eu/hr/news/sto-je-mev-trgovanje-defi/" target="_blank" rel="noopener">Što je MEV trgovanje i zašto je postalo jedan od najvećih problema DeFi-ja</a>

U ovom slučaju Titan Builder je navodno bio najveći korisnik prilike koja je nastala nakon lošeg swapa. To ne znači nužno da je korisnikov wallet “hakiran”, nego da je tržišna infrastruktura iskoristila transakciju koja je već bila potpisana i poslana.

Za običnog korisnika razlika možda zvuči tehnički, ali posljedica je vrlo stvarna: gotovo cijeli iznos od 2 milijuna dolara nestao je kroz lošu egzekuciju swapa.

## Što korisnici mogu naučiti iz ovog slučaja?

Najvažnija lekcija je jednostavna: kod DEX transakcija nije dovoljno gledati samo koji token kupujete ili prodajete. Treba gledati i **kako** se transakcija izvršava.

Prije potpisa treba provjeriti:

- minimalni iznos koji ćete primiti,
- slippage,
- price impact,
- rutu transakcije,
- likvidnost poolova,
- razliku u cijeni između više DEX-ova ili agregatora.

Za male iznose greška može biti neugodna. Za velike iznose greška može biti razorna.

DEX-ovi daju korisnicima veću kontrolu, ali ta kontrola dolazi s odgovornošću. Banka ili centralizirana burza često imaju više zaštitnih mehanizama, dok decentralizirani swap može izvršiti ono što je korisnik potpisao, čak i ako je rezultat ekstremno nepovoljan.

To je upravo ono što ovaj slučaj čini važnim.

Nije riječ samo o jednom traderu koji je izgubio novac. Riječ je o upozorenju da u decentraliziranim financijama korisnik mora razumjeti što potpisuje.

## Naš osvrt

- Ovaj slučaj je važan jer pokazuje da crypto rizik ne dolazi samo od klasičnih hakera, phishing linkova ili lažnih tokena.
- Ponekad je dovoljan loše usmjeren swap, premalen liquidity pool i jedan klik na **Confirm**.
- Najzanimljiviji dio priče nije samo gubitak od 2 milijuna dolara, nego činjenica da je dio rizika vjerojatno bio vidljiv prije potpisa transakcije.
- **Minimum received**, **price impact**, **slippage** i **ruta swapa** nisu sitna tehnička slova. To su signali koji mogu pokazati da će transakcija završiti katastrofalno.
- Za male retail korisnike ovo je upozorenje da ne potpisuju transakcije bez čitanja detalja.
- Za veće tradere poruka je još jasnija: veliki nalozi ne smiju se izvršavati kao običan brzi swap bez provjere likvidnosti, alternative i zaštite od loše egzekucije.
- Crypto često obećava brzinu, slobodu i otvoreno tržište. Ali u DeFi-ju sloboda znači i da sustav neće uvijek stati umjesto vas.
- Ako potpišete lošu transakciju, blockchain je može izvršiti savršeno — čak i kada je rezultat za vas katastrofalan.


**Disclaimer:** Ovaj članak služi isključivo u informativne svrhe i ne predstavlja financijski, investicijski, pravni ili sigurnosni savjet. Crypto i DeFi transakcije nose visok rizik, a korisnici sami odgovaraju za provjeru transakcija prije potpisa.
