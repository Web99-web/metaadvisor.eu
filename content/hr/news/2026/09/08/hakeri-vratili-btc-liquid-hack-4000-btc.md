---
title: "Hakeri vratili BTC kao što su obećali: Liquid hack od 4.000 BTC"
slug: "hakeri-vratili-btc-liquid-hack-4000-btc"
date: 2026-09-08T10:00:00+02:00
category: "Crypto"
translationKey: "liquid-white-hat-hackers-return-bitcoin-2026-09-08"
source: "Liquid Network, Blockstream, SideSwap, Bitquery, The Block, Metaadvisor.eu"
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
featured_image: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
image: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
thumbnail: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
image_alt: "White-hat hakeri povukli 4.000 BTC iz Liquid Networka i nakon zakrpe vratili 3.400 BTC"
image_credit: "Metaadvisor.eu"
tags: ["Liquid Network", "Bitcoin", "kripto", "hakeri", "white-hat hakeri", "Blockstream", "SideSwap", "Elements", "blockchain", "OP_RETURN", "sigurnost", "kibernetička sigurnost", "L-BTC", "Bitcoin sidechain", "kripto sigurnost"]
description: "Akteri koji se nazivaju white-hat hakerima povukli su gotovo 4.000 BTC iz Liquid Networka, poručili Blockstreamu da prvo popravi bug i nakon zakrpe vratili 3.400 BTC."
summary: "Liquid Network ostao je bez gotovo 4.000 BTC nakon iskorištavanja buga u Elementsu. Akteri su preko poruka zapisanih izravno u Bitcoin blockchain obećali vratiti većinu sredstava nakon popravka ranjivosti – i zatim vratili 3.400 BTC."
---

*Slika je simbolična.*

# "White-hat" hakeri povukli 4.000 BTC iz Liquida, poručili "prvo popravite bug" i zatim vratili 3.400 BTC

**Jedan od najneobičnijih crypto sigurnosnih incidenata ove godine dobio je još neobičniji nastavak: akteri koji se nazivaju white-hat hakerima povukli su gotovo 4.000 BTC iz Liquid Networka, vrijednih oko 320 milijuna dolara, poručili Blockstreamu da će većinu vratiti nakon što popravi ranjivost – i zatim doista vratili 3.400 BTC.** Još zanimljivije, velik dio pregovora nije se odvijao preko emaila, Telegrama ili privatnog chata, nego kroz poruke zapisane izravno u Bitcoin blockchain.

Incident je pogodio **Liquid Network**, Bitcoin sidechain koji koristi open-source softver Elements. Problem, prema dosad objavljenim informacijama, nije nastao zato što je netko ukrao privatne ključeve Liquid Federacije ili kompromitirao SideSwapov Peg-out Authorization Key. Bug povezan s Elementsom omogućio je stvaranje L-BTC-a bez odgovarajućeg stvarnog Bitcoin pokrića, nakon čega su tokeni prošli kroz peg-out proces i federacija je isplatila pravi BTC.

## Gotovo 4.000 BTC otišlo je kroz transakciju koja je izgledala legitimno

Incident je počeo 6. rujna kada je oko **4.000 L-BTC poslano SideSwapovu peg-out servisu**. SideSwap je objavio da je njegov sustav transakciju obradio kao normalan korisnički nalog: L-BTC je spaljen uz valjanu peg-out autorizaciju, a Liquid Federation zatim je isplatila približno **3.996 BTC** na Bitcoin adresu korisnika.

SideSwap tvrdi da njegov PAK nije bio kompromitiran. Prema dosad dostupnim informacijama, problem je nastao ranije, u Elements softveru na kojem Liquid radi, što je omogućilo da L-BTC bez stvarnog pokrića dođe do faze u kojoj ga je bilo moguće zamijeniti za pravi Bitcoin.

Federation wallet prije incidenta sadržavao je približno **4.200 BTC-a**, pa je povlačenje odnijelo oko 95% njegove Bitcoin rezerve. Liquid je nakon incidenta onemogućio bridge nodeove i zatražio od burzi da zaustave L-BTC depozite i povlačenja. Bitcoin mainnet pritom nije bio kompromitiran.

## Prva poruka u blockchainu: "Mi smo white-hat hakeri"

Nekoliko sati nakon povlačenja dogodilo se nešto što je cijelom incidentu potpuno promijenilo ton. Dana **6. rujna u 18:30 UTC**, odnosno oko 20:30 po hrvatskom vremenu, adresa koja je držala gotovo 4.000 BTC poslala je novu Bitcoin transakciju. U njezinu OP_RETURN outputu bila je poruka.

**Hexadecimalni zapis u blockchainu:**

**`776520617265207768697465686174732e20636f6e74616374207573206f6e20636861696e`**

**„Mi smo white-hat hakeri. Kontaktirajte nas on-chain.” (original engleski: “we are whitehats. contact us on chain”)**

To je stvarni računalni zapis rečenice. U Bitcoin blockchainu slova nisu spremljena kao tekst koji čovjek izravno čita, nego kao bajtovi koji se mogu prikazati hexadecimalno. Primjerice, `77` predstavlja slovo `w`, `65` slovo `e`, pa početak `7765` nakon dekodiranja daje riječ `we`.

Bitcoin block explorer taj hexadecimalni sadržaj može automatski pretvoriti natrag u čitljivu rečenicu. Zato korisnik koji otvori transakciju može vidjeti OP_RETURN podatak i pročitati poruku koju su akteri ostavili.

Još neobičnije, to nije bila samo poruka spremljena negdje uz transakciju. **Sama poruka postala je dio trajnog zapisa Bitcoin blockchaina.**

{{< support1 >}}

## Blockstream im odgovara – također kroz Bitcoin

Blockstream je prihvatio njihov način komunikacije. Oko sat vremena kasnije, **6. rujna u 19:31 UTC**, s adrese povezane s Blockstreamom poslana je nova Bitcoin transakcija s OP_RETURN porukom.

**Hexadecimalni zapis u blockchainu:**

**`506c6561736520636f6e7461637420736563757269747940626c6f636b73747265616d2e636f6d`**

**„Molimo kontaktirajte security@blockstream.com.” (original engleski: “Please contact security@blockstream.com”)**

To znači da je i Blockstream odgovorio na isti način – porukom zapisanom unutar Bitcoin transakcije. Umjesto da komunikacija odmah prijeđe na email ili neku privatnu platformu, prvi odgovor ostao je trajno zabilježen u blockchainu.

Kasnije je Blockstream poslao i PGP-potpisanu šifriranu poruku. Potpis je bilo moguće provjeriti prema javno objavljenom Blockstreamovu sigurnosnom ključu, čime se moglo potvrditi da poruke zaista dolaze od Blockstreamove sigurnosne strane.

No white-hat strana nastavila je razgovor on-chain.

## "Vraćamo većinu – je li ovo prava adresa?"

Dana **7. rujna u 02:20 UTC**, odnosno oko 04:20 po hrvatskom vremenu, akteri su poslali novu transakciju. Ovoga puta poruka je sadržavala i punu adresu Liquid Federation walleta na koju su namjeravali vratiti Bitcoin.

**Hexadecimalni zapis u blockchainu:**

**`73656e64696e67206d6f7374206261636b20746f2062633171646c6c6436616e746d76347875673234326564383371376b3472717735306377666e733338737a783471753266346a77617878737568777878722c2069732074686174206f6b`**

**„Vraćamo većinu na bc1qdlld6antmv4xug242ed83q7k4rqw50cwfns38szx4qu2f4jwaxxsuhwxxr, je li to u redu?” (original engleski: “sending most back to bc1qdlld6antmv4xug242ed83q7k4rqw50cwfns38szx4qu2f4jwaxxsuhwxxr, is that ok”)**

Ovo je možda prvi trenutak u kojem je postalo jasno da njihova početna tvrdnja da su white-hat hakeri možda nije samo pokušaj kupovanja vremena. **Nisu samo rekli da će vratiti novac – poslali su adresu na koju namjeravaju vratiti većinu gotovo 4.000 BTC-a i pitali Blockstream je li ispravna.**

Blockstream im je odgovorio **“Yes, thank you.”**, odnosno **„Da, hvala.”**

Ali prije samog povrata uslijedila je još važnija poruka.

## "Prvo popravite bug"

Dana **7. rujna u 03:30 UTC**, odnosno oko 05:30 po hrvatskom vremenu, white-hat strana poslala je treću javno čitljivu poruku. Ona je praktički objasnila zašto Bitcoin još neće odmah vratiti.

**Hexadecimalni zapis javno čitljivog dijela poruke u blockchainu:**

**`506c656173652066697820746865206275672066697273742e2054686520636861696e20697320756e646572207269736b206174206c617465737420636f6d6d6974207269676874206e6f772e204d616b652073757265206576657279206e6f646520697320706174636865642e205468656e2077652077696c6c207472616e7366657220746865206d6f6e6579206261636b20736166656c7920616674657220636f6e6669726d696e6720746865206669782e`**

**„Molimo prvo popravite bug. Mreža je trenutačno izložena riziku i na najnovijem commitu. Pobrinite se da svaki node bude zakrpan. Nakon što potvrdimo popravak, sigurno ćemo vratiti novac.” (original engleski: “Please fix the bug first. The chain is under risk at latest commit right now. Make sure every node is patched. Then we will transfer the money back safely after confirming the fix.”)**

Nakon tog javno čitljivog teksta u istom OP_RETURN zapisu slijedio je i **PGP-šifrirani tehnički dio** namijenjen Blockstreamu. Javnost je mogla vidjeti šifrirane podatke, ali ne i pročitati njihov sadržaj bez privatnog ključa. Prema istraživačima koji su analizirali blockchain, taj je dio sadržavao tehničke informacije o ranjivosti.

Poruka je bila vrlo jasna: **nemojte samo potvrditi adresu i uzeti Bitcoin natrag – prvo osigurajte da ista ranjivost više ne postoji.**

{{< support2 >}}

## Blockstream javlja da su bridge nodeovi zakrpani

Nakon rada na sigurnosnom problemu Blockstream je poslao potpisanu on-chain poruku kojom je potvrdio da je problem na bridge nodeovima zakrpan.

**Hexadecimalni zapis u blockchainu:**

**`427269646765206e6f6465732061726520706174636865642c207361666520746f2072657475726e207468652066756e64732e`**

**„Bridge nodeovi su zakrpani. Sredstva je sada sigurno vratiti.” (original engleski: “Bridge nodes are patched, safe to return the funds.”)**

Time je ispunjen uvjet koji su akteri nekoliko sati ranije zapisali u Bitcoin blockchain.

I tada se dogodio ključni obrat: **održali su ono što su napisali.**

Dana **7. rujna u 16:09 UTC**, odnosno oko 18:09 po hrvatskom vremenu, u Bitcoin blocku 965.950 potvrđena je transakcija kojom je **točno 3.400 BTC vraćeno na adresu Liquid Federacije**.
## Obećali su vratiti većinu – i vratili 3.400 BTC

Povrat je posebno zanimljiv zbog slijeda događaja. Akteri su prvo napisali da su white-hat hakeri, zatim javno pitali je li federation adresa prava adresa za povrat većine novca, a potom odbili odmah poslati BTC dok se ranjivost ne popravi.

Blockstream je potvrdio da su bridge nodeovi zakrpani. Nakon toga stigla je transakcija od **3.400 BTC**.

Drugim riječima, ključna rečenica cijele priče – **„nakon što potvrdimo popravak, sigurno ćemo vratiti novac”** – nije ostala samo poruka u blockchainu. Nakon potvrde popravka vratili su oko 85% sredstava.

Na njihovoj adresi ipak je ostalo približno **598,5 BTC-a**, tada vrijednih oko 47 milijuna dolara.

## Oko 600 BTC ipak nisu vratili

Status preostalih gotovo 600 BTC-a još je otvoren. Pojavila su se nagađanja da bi taj iznos mogao predstavljati svojevrsni bug bounty, odnosno nagradu za pronalazak kritične ranjivosti, ali nema javno potvrđenog dogovora prema kojem je Blockstream pristao na nagradu te veličine.

Gotovo 600 BTC predstavlja oko 15% ukupnog iznosa koji je ostao pod kontrolom aktera nakon incidenta. Zbog toga nije precizno govoriti da je sav Bitcoin vraćen.

Točnije je reći da su **obećali vratiti "većinu" i upravo su većinu vratili**.

Čak je i riječ **“most”** iz njihove druge on-chain poruke naknadno postala vrlo važna. Nisu napisali da vraćaju sve. Napisali su **“sending most back”** – vraćamo većinu.

## Jesu li to zaista white-hat hakeri?

Njihovo vlastito predstavljanje kao white-hat hakera ne znači automatski da ih tako treba pravno ili sigurnosno klasificirati. Nema javnih informacija da su prije iskorištavanja ranjivosti imali dopuštenje Blockstreama ili Liquid Federacije za sigurnosno testiranje sustava.

Uobičajeni white-hat postupak bio bi pronaći ranjivost i prijaviti je kompaniji kroz security disclosure ili bug bounty program, a ne prvo preuzeti kontrolu nad gotovo 320 milijuna dolara.

S druge strane, njihovo ponašanje nakon exploita također nije izgledalo poput tipične crypto krađe. Nisu pokušali odmah sakriti sredstva kroz niz walleta i drugih mreža. Ostali su na blockchainu, javno su stupili u kontakt s Blockstreamom, dostavili tehničke informacije, tražili zakrpu i zatim vratili 3.400 BTC.

Upravo zato incident ostaje toliko neobičan. **Sami su se nazvali white-hat hakerima, ali njihov će konačni status vjerojatno ovisiti i o tome što će se dogoditi s preostalih 598,5 BTC-a.**

## Kako uopće izgleda razgovor na Bitcoin blockchainu

Bitcoin nije chat aplikacija, ali OP_RETURN omogućuje zapisivanje male količine proizvoljnih podataka u transakciju. Kada se transakcija potvrdi, taj podatak postaje dio blockchaina.

Zato ono što korisnik na exploreru vidi kao:

**“we are whitehats. contact us on chain”**

u hexadecimalnom zapisu izgleda ovako:

**`776520617265207768697465686174732e20636f6e74616374207573206f6e20636861696e`**

Explorer jednostavno uzme spremljene bajtove i, kada oni predstavljaju tekst, dekodira ih u znakove koje čovjek može pročitati.

Još je važnije što svaka takva poruka dolazi unutar **prave Bitcoin transakcije**. U ovom slučaju adresa koja je slala white-hat poruke bila je upravo adresa koja je kontrolirala povučene Bitcoine. Time blockchain ne dokazuje tko su osobe iza walleta, ali potvrđuje da je poruke slao netko tko je mogao potpisivati transakcije iz walleta koji je držao sredstva.

To je razlog zbog kojeg je ovaj razgovor puno više od screenshota ili anonimne objave na internetu.

## Pregovori o 320 milijuna dolara odvijali su se javno

Najzanimljiviji dio incidenta možda nije čak ni sam exploit, nego način na koji je problem rješavan nakon njega. White-hat strana i Blockstream praktički su vodili pregovore o Bitcoinu vrijednom stotine milijuna dolara pred cijelim svijetom.

Poruke, vrijeme njihova slanja i adrese koje su ih poslale ostale su zapisane u blockchainu. Javnost je mogla pratiti kako akteri prvo traže kontakt, zatim najavljuju povrat većine sredstava, potom zahtijevaju popravak ranjivosti i na kraju stvarno vraćaju 3.400 BTC.

Nije postojao klasični privatni pregovarački kanal koji je javnosti kasnije prepričan. **Najvažniji dijelovi razgovora bili su zapisani u samom Bitcoinu.**

## Što je Liquid Network i zašto je bug bio toliko opasan

Liquid je Bitcoin sidechain koji je razvio **Blockstream**, a koristi se za brže prijenose Bitcoina i izdavanje različite digitalne imovine. Njegov L-BTC trebao bi biti pokriven stvarnim Bitcoinom zaključanim u federation sustavu.

Korisnik može zaključati BTC i dobiti odgovarajući L-BTC na Liquid mreži. Kada se želi vratiti na Bitcoin mainnet, L-BTC se kroz peg-out proces uklanja iz optjecaja, a federation sustav oslobađa stvarni Bitcoin.

Upravo je zato ovaj bug bio kritičan. Ako je moguće stvoriti L-BTC koji nije stvarno pokriven Bitcoinom i zatim ga kroz regularan peg-out zamijeniti za pravi BTC, ugrožena je osnovna pretpostavka sustava.

SideSwap tvrdi da njegovi sustavi i PAK nisu bili kompromitirani. Prema njihovim informacijama, izvor problema bio je bug u **Elementsu**, open-source softveru koji pokreće Liquid.

## Bitcoin mainnet nije hakiran

Incident nije bio hack samog Bitcoina. Bitcoin konsenzus, Bitcoin nodeovi i privatni walleti korisnika nisu kompromitirani.

Problem je nastao na Liquid sidechainu i u njegovu mehanizmu za izdavanje i povrat L-BTC-a. Bitcoin mainnet samo je izvršavao valjano potpisane transakcije koje su mu poslane.

Ironično, upravo je Bitcoin blockchain nakon toga postao **javni zapisnik rješavanja problema**. Na njemu su ostale poruke hakera, odgovori Blockstreama i konačna transakcija kojom je vraćeno 3.400 BTC.

## Naš osvrt

* **Akteri koji se sami nazivaju white-hat hakerima iskoristili su ranjivost povezanu s Elements softverom i izvukli približno 4.000 BTC iz Liquid sustava.**
* Dana **6. rujna u 18:30 UTC** u blockchain su upisali poruku čiji hexadecimalni zapis počinje s **`776520...`**, a koja nakon dekodiranja glasi: **„Mi smo white-hat hakeri. Kontaktirajte nas on-chain.”**
* Dana **7. rujna u 02:20 UTC** kroz novu Bitcoin transakciju napisali su da **vraćaju većinu sredstava** i pitali Blockstream je li federation adresa ispravna.
* Samo nešto više od sat vremena kasnije poslali su ključnu poruku: **„Molimo prvo popravite bug.”** Tražili su da svi nodeovi budu zakrpani prije nego što vrate Bitcoin.
* Javno čitljivi dijelovi sve tri poruke mogu se iz raw blockchain podataka prikazati i kao **hexadecimalni nizovi**, dok ih block exploreri mogu dekodirati u običan tekst.
* Blockstream je nakon zakrpe poručio da je sredstva sigurno vratiti.
* Dana **7. rujna u 16:09 UTC** akteri su vratili **3.400 BTC**, upravo nakon što je uvjet koji su postavili bio ispunjen.
* Na njihovoj adresi ostalo je približno **598,5 BTC-a**, a nema javno potvrđenog dogovora da taj iznos predstavlja bug bounty.
* Sam Bitcoin mainnet **nije bio hakiran**; problem se odnosio na Liquid i Elements.
* Najneobičniji dio cijelog incidenta ostaje činjenica da su se **pregovori o Bitcoinu vrijednom oko 320 milijuna dolara dijelom odvijali javno, kroz poruke trajno zapisane u Bitcoin blockchainu**.
* Rekli su da će nakon popravka vratiti većinu sredstava – i **za 3.400 BTC održali su riječ**.

**Pratite Metaadvisor.eu za više vijesti o cryptu, Bitcoinu, blockchainu, kibernetičkoj sigurnosti, digitalnoj imovini, tehnologiji i financijskim tržištima.**

**Disclaimer:** Ovaj članak služi isključivo u informativne svrhe i ne predstavlja financijski, investicijski, pravni, porezni ili sigurnosni savjet niti preporuku za korištenje bilo koje crypto mreže, platforme ili usluge. Informacije o sigurnosnim incidentima mogu se mijenjati kako se objavljuju novi tehnički podaci i rezultati istraga. Prije donošenja financijskih odluka provedite vlastito istraživanje i provjerite aktualne informacije kod službenih izvora.

<small style="color:#999; font-size:0.8em;">U suradnji s AI-jem.</small>
