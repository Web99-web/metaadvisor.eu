---
title: "Chainflip: Validator, čuvar kriptotrezora, ukrao 12,6 milijuna?"
slug: "chainflip-validator-crypto-vault-heist-12-million-2026"
date: "2026-11-24T08:00:00+01:00"
category: "markets"
translationKey: "chainflip-validator-vault-exploit-2026-11-24"
source: "Chainflip Labs; Chainflip Incident Report; The Block"
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/hack/Chainflip-Crypto-Vault-Heist-by-validator.jpg"
featured_image: "/images/hack/Chainflip-Crypto-Vault-Heist-by-validator.jpg"
image: "/images/hack/Chainflip-Crypto-Vault-Heist-by-validator.jpg"
thumbnail: "/images/hack/Chainflip-Crypto-Vault-Heist-by-validator.jpg"
image_alt: "Ilustracija Chainflipova kriptotrezora i napada na validatorsku mrežu, nakon kojeg je ukradeno 12,6 milijuna dolara"
image_credit: "Metaadvisor.eu"
tags: ["Chainflip", "Validator", "Crypto Vault", "Crypto Hack", "Bitcoin", "Ethereum", "Tornado Cash", "Blockchain Security"]
description: "Napadač se registrirao kao kandidat za Chainflipova validatora, pribavio dijelove ključeva i ukrao 12,6 milijuna USD. Chainflip tvrdi da prati njegove digitalne tragove."
summary: "Chainflipov napadač nije postao aktivni validator, ali je preko mrežnog pristupa prema preliminarnoj istrazi ukrao dijelove ključeva. Tvrtka je rekonstruirala dio njegovih tragova i ponudila 10% za povrat imovine."
categories: ["markets"]
---

*Naslovna slika je ilustrativna.*

**Prijavio se kao kandidat za čuvara digitalnog trezora, ali nikada nije dobio mjesto među aktivnim validatorima. Ipak, sljedećeg jutra iz Chainflipovih trezora nestalo je približno 12,6 milijuna dolara. Sada tvrtka tvrdi da je rekonstruirala njegovu kupnju tokena, registraciju računa i server kojim se koristio. Napadač je, čini se, ostavio tragove prije nego što je uopće došao do novca.**

U petak, 20. studenoga 2026., nepoznati napadač registrirao je novi validatorski račun na mreži Chainflip. Sam čin registracije nije ga pretvorio u jednog od aktivnih čuvara sredstava, ali mu je otvorio mogućnost mrežne komunikacije s njihovim računalima. Prema preliminarnoj istrazi objavljenoj 23. studenoga, upravo je taj pristup iskoristio za napad na softver validatora i pribavljanje dijelova kriptografskih ključeva. Ono što je na blockchainu izgledalo kao valjano potpisana isplata zapravo nikada nije odobrila Chainflipova mreža.

## Čuvari trezora koji nemaju cijeli ključ

Validator nije osoba koja fizički čuva novac, nego računalo koje pokreće poseban softver i sudjeluje u radu blockchain protokola. Kod Chainflipa validatori zajednički kontroliraju pristup trezorima s kriptovalutama koje se koriste za razmjenu između različitih blockchain mreža. Sustav je osmišljen tako da jedan validator ne bi smio moći samostalno potpisati isplatu.

Najjednostavnije ga je zamisliti kao trezor čiji je ključ podijeljen na više dijelova. Svaki čuvar posjeduje svoj dio, a za odobrenje isplate potrebno je prikupiti dovoljan broj odgovarajućih potpisa. Takva zaštita smanjuje opasnost da jedan kompromitirani sudionik isprazni trezor. Međutim, ako napadač uspije ukrasti dovoljno dijelova ključa iz računala različitih čuvara, mogao bi sastaviti potpis bez njihove stvarne suglasnosti.

**Chainflipova preliminarna istraga upućuje upravo na takav scenarij: napadač nije razbio kriptografski algoritam, nego je iskoristio slabost softvera koji je štitio dijelove ključeva.**

## Registrirao se kao validator, ali nikada nije postao aktivan

Prema službenoj kronologiji, napadačev račun registriran je 20. studenoga u **11:00:18 UTC**, samo 79 sekundi nakon što je financiran minimalnim ulogom od **20.500 FLIP tokena**. U 11:07:06 registriran je i mrežni identitet preko kojeg se mogao povezivati s drugim validatorima. Njegov račun nikada nije pristupio aktivnom skupu validatora, no postojeći čvorovi svejedno su prihvaćali mrežne veze jer novi kandidati moraju moći komunicirati s mrežom prije eventualnog uključivanja.

Prema dosadašnjim nalazima, napadač je tu mogućnost iskoristio za napad na ranjivost povezanu sa sigurnošću memorije u vanjskoj programskoj biblioteci za mrežnu komunikaciju. Chainflip navodi da je tako mogao izvršavati kod na računalima validatora i izdvojiti pohranjene dijelove ključeva. Nakon što je prikupio dovoljno dijelova, stvorio je potpise za prijenos sredstava bez uobičajenog odobravanja protokola. Istraga se nastavlja i Chainflip upozorava da svi pojedini koraci još nisu definitivno potvrđeni.

{{< support1 >}}

## Prva isplata, alarm koji nije eskaliran i drugi udar

U subotu, 21. studenoga, u **06:41:01 UTC** iz Bitcoin trezora otišlo je **122,86137042 BTC**. Samo osam minuta poslije automatizirani nadzor objavio je upozorenje o trezoru na internom kanalu. Taj je sustav još bio u fazi procjene i ranije je davao lažne uzbune, zbog čega upozorenje nije automatski eskalirano u sigurnosni incident. U međuvremenu je ukradeni Bitcoin prebačen na drugu adresu.

U **07:10:59 UTC** slijedila je transakcija iz Ethereum trezora: ukradeno je **520,2243399 ETH**, **3.249.631,41 USDC** i **758.141,33 USDT**. Napadač je zatim stablecoine zamijenio za ETH, a ukupno **2.909 ETH** uplatio u Tornado Cash, sustav koji otežava povezivanje ulaznih i izlaznih blockchain transakcija. Član tima podigao je uzbunu u 07:41 UTC, a trgovanje, depoziti i isplate obustavljeni su do 08:31 UTC.

Ni to nije bio kraj. Iako je Chainflip pokrenuo promjenu mrežnih ključeva, prethodno kompromitirani ključ jednog Bitcoin trezora ostao je upotrebljiv dovoljno dugo da napadač u **11:24:18 UTC** povuče dodatnih **10,48288011 BTC**. Ukupno je iz Bitcoin trezora otišlo **133,34425053 BTC**, a vrijednost sve ukradene imovine prema cijenama na jutro napada procijenjena je na **12,6 milijuna USD**. Ta imovina predstavljala je praktički cjelokupno stanje pogođenih trezora u tom trenutku.

## Kako je Chainflip počeo pratiti napadača?

Ovo je jedan od najzanimljivijih dijelova slučaja. U službenoj poruci upućenoj napadaču Chainflip Labs tvrdi da je rekonstruirao pripremu napada: **financiranje povezano s Tornado Cashom 11. studenoga, kupnju FLIP tokena, registraciju validatorskog računa 20. studenoga i server korišten za tu registraciju**. Tvrtka navodi i da je prikupila identifikacijske metapodatke povezane s računom i korištenim internetskim uslugama koji bi, uz pomoć nadležnih tijela, mogli otkriti počinitelja.

Kako je moguće da imaju te tragove, a još ne znaju tko je? Registracija blockchain validatora ne mora značiti predaju osobnog dokumenta, imena ili kućne adrese. Blockchain bilježi adrese i transakcije, a mrežna infrastruktura može ostaviti dodatne tehničke tragove. Podaci o serveru i uslugama koje je napadač koristio mogli bi postati korisni ako ih policija uspije povezati s pouzdanim identifikacijskim podacima. Međutim, **Chainflip nije javno objavio identitet napadača niti potvrdio da ga je identificirao**.

Chainflip također tvrdi da su adrese povezane s ukradenom imovinom označene kod velikih tvrtki za blockchain analitiku te da se nadziru izlazne transakcije iz korištenih Tornado Cash fondova. Takvo praćenje može otežati unovčavanje sredstava, ali ne jamči ni identifikaciju počinitelja ni povrat novca. Chainflip je potvrdio suradnju s policijom i angažman specijalizirane tvrtke ZeroShadow za praćenje i pokušaj povrata imovine.

## Napadaču ponuđeno 10% za povrat sredstava

Chainflip Labs pokušao je postići povrat ukradene imovine ponudom prema kojoj bi napadač mogao zadržati **10% sredstava kao nagradu**, pod uvjetom da vrati preostalih **90%**. U javnoj poruci navedeni su konkretni iznosi za povrat, **110,57523337 BTC** i **2.618,1 ETH**, te adrese na koje ih treba poslati. Tvrtka je obećala da će pravovremeni povrat tretirati kao dobrovoljni sigurnosni povrat sredstava (*white-hat recovery*) i povući vlastite prijave i pritužbe nadležnim tijelima.

Rok naveden u ponudi bio je **23. studenoga u 18:38 UTC**. Chainflip je u poruci upozorio napadača da su njegove blockchain adrese pod povećalom analitičara i da bi daljnje korištenje ukradenih sredstava moglo stvoriti nove tragove. **U provjerenim službenim izvorima nije potvrđeno da je ponuda prihvaćena niti da je novac vraćen nakon isteka roka.** Čak i kada bi tvrtka povukla svoje prijave, to samo po sebi ne znači da može jamčiti obustavu eventualnog kaznenog postupka.

{{< support2 >}}

## Gdje je nestao novac i kada se mreža vraća?

Prema Chainflipovu izvješću od 23. studenoga, ukradeni Bitcoin tada se još nalazio na dvije identificirane adrese, dok je imovina iz Ethereum trezora pretvorena u ETH i prebačena u Tornado Cash. To je stanje prema vremenu izvješća, a ne jamstvo da se sredstva poslije nisu pomaknula. Njihovo praćenje i eventualni povrat ostaju predmet daljnje istrage.

Chainflip je 21. studenoga distribuirao zakrpanu verziju softvera validatorima, a 22. studenoga proveo dodatnu rotaciju ključeva. Prema službenoj potvrdi od **23. studenoga u 11:31 UTC**, svi aktivni validatori koristili su zakrpanu verziju. Ipak, u posljednjem provjerenom izvješću razmjene, depoziti i isplate ostali su obustavljeni, a datum ponovnog otvaranja nije bio potvrđen. Dio slobodnih sredstava pružatelja likvidnosti na nepogođenim mrežama preventivno je upućen na njihove adrese za povrat.

Još je teže pitanje tko će nadoknaditi gubitke. Chainflip navodi da utvrđuje koje su korisnike i pružatelje likvidnosti transakcije pogodile te priprema plan oporavka i mogućeg ponovnog financiranja protokola. **Potvrđeni plan naknade, individualni iznosi i rokovi isplata nisu objavljeni** u dostupnom službenom izvješću.

## Drugi veliki sigurnosni incident u nekoliko mjeseci

Slučaj dobiva dodatnu težinu zbog ranijeg Chainflipova incidenta na mreži Tron. U rujnu 2026. napadač je iskoristio drukčiju ranjivost u obradi transakcijskih poruka i prouzročio gubitak od približno **736.000 USDT**. Taj napad nije isti kao studeni incident i ne treba pretpostaviti da iza oba stoji ista osoba. Ipak, ponavljanje ozbiljnih problema nameće pitanja o provjerama vanjskih programskih biblioteka, zaštiti ključeva i brzini reakcije na sigurnosna upozorenja.

## Naš osvrt

- **Kandidat, ne aktivni validator:** Napadač se registrirao i dobio mrežni pristup, ali nikada nije postao član aktivnog skupa. Zato bi bilo netočno tvrditi da je krađu počinio potvrđeni aktivni validator.
- **Slabost oko ključeva:** Preliminarni nalazi upućuju na kompromitaciju softvera i krađu dijelova ključeva, a ne na razbijanje same kriptografije.
- **Upozorenje nije bilo dovoljno:** Prvi alarm zabilježen je osam minuta nakon prve krađe, ali još nije bio povezan s automatskom eskalacijom.
- **Tragovi postoje, identitet nije potvrđen:** Financiranje, kupnja tokena, validatorska registracija i korišteni server daju istražiteljima tragove, no javne potvrde o identitetu nema.
- **Ponuda od 10% ne znači povrat novca:** Rok je prošao, a uspješan povrat sredstava nije potvrđen u provjerenim službenim objavama.
- **Sigurnosna zakrpa nije odšteta:** Ažuriranje validatora i zamjena ključeva ne rješavaju automatski gubitke pogođenih korisnika.

**Najveći paradoks Chainflipova slučaja jest što je sustav bio zamišljen tako da nijedan čuvar trezora nema dovoljno ovlasti samostalno odnijeti novac. Napadač, prema preliminarnoj istrazi, nije morao postati jedan od tih čuvara. Pronašao je ranjivost u njihovoj komunikaciji, pribavio dovoljno dijelova ključa i stvorio potpise kojima je trezor povjerovao.**

A sada bi ga upravo tragovi ostavljeni prije napada mogli razotkriti. Chainflip tvrdi da zna kako je financirao pripremu, kada je kupio potrebne tokene i kojim je serverom registrirao validatorski račun. Hoće li taj niz digitalnih tragova dovesti do stvarne osobe i pomoći u povratu sredstava, još nije poznato.

**Pratite Metaadvisor.eu za više neovisnih vijesti i analiza o kriptovalutama, umjetnoj inteligenciji, tehnologiji i poslovanju.**

<small style="color:#757575; font-size:12px; font-weight:400; font-style:normal;">In collaboration with AI.</small>

**Izvori:** Chainflip Labs, *Incident Report: Bitcoin and Ethereum Vault Exploit (Part 1)* (23.11.2026.); Chainflip Labs, *Message from Chainflip Labs*; Chainflip Labs, *Getting Chainflip Back Up and Running* (15.09.2026.); The Block (21.–22.11.2026.).

**Napomena:** Članak je pripremljen 24. studenoga 2026. prema dostupnim službenim dokumentima i izvještajima. Opis uzroka napada preliminaran je i Chainflip ga još istražuje. Identitet napadača, naknada korisnicima i ishod ponude za povrat sredstava nisu javno potvrđeni u provjerenim službenim izvorima. Sadržaj je informativan i ne predstavlja financijski ni investicijski savjet.
