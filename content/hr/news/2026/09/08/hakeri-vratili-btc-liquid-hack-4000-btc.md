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

**Jedan od najvećih crypto sigurnosnih incidenata ove godine dobio je neobičan nastavak: akteri koji se nazivaju white-hat hakerima povukli su gotovo 4.000 BTC iz Liquid Networka, vrijednih oko 320 milijuna dolara, poručili Blockstreamu da će većinu vratiti nakon što popravi ranjivost – i zatim doista vratili 3.400 BTC.** Još neobičnije, velik dio pregovora nije se odvijao preko emaila, Telegrama ili privatnog chata, nego kroz kratke poruke zapisane izravno u Bitcoin blockchain.

Incident je pogodio **Liquid Network**, Bitcoin sidechain koji koristi softver Elements i kojim upravlja federacija članova. Problem prema dosad dostupnim informacijama nije nastao zato što je netko ukrao privatne ključeve. Bug u Elementsu omogućio je stvaranje L-BTC-a koji nisu imali odgovarajuće stvarne Bitcoine kao pokriće, a zatim je kroz normalni peg-out proces Liquid Federation isplatila pravi BTC. Nakon što je mreža ostala bez gotovo cijelog Bitcoin salda federation walleta, Liquid je zaustavio bridge nodeove i obustavio dio mrežnih operacija.

## Gotovo 4.000 BTC otišlo je kroz transakciju koja je izgledala legitimno

Prema informacijama koje su objavili SideSwap i istraživači koji su pratili transakcije, incident je počeo 6. rujna kada je oko **4.000 L-BTC poslano SideSwapovu peg-out servisu**. Tokeni su prošli autorizaciju valjanim Peg-out Authorization Keyem, odnosno PAK-om, nakon čega je Liquid Federation isplatila približno **3.996 BTC** na Bitcoin adresu korisnika.

Najvažniji detalj je da SideSwapov PAK, prema objavljenim informacijama, nije bio kompromitiran. Ključevi su radili ono za što su dizajnirani, ali je problem bio u L-BTC-u koji je ušao u sustav. Prema SideSwapu, ti su tokeni stvoreni iskorištavanjem buga u **Elements open-source softveru**, što je omogućilo da se kroz normalan proces otkupa dobije stvarni Bitcoin za L-BTC koji nije imao odgovarajuće pokriće.

Federation wallet prije incidenta sadržavao je oko **4.200 BTC-a**, pa je jedna transakcija odnijela približno 95% njegovih Bitcoin rezervi. Bitcoin mainnet pritom nije bio kompromitiran; ranjivost se odnosila na Liquid sidechain i njegov peg mehanizam.

## Onda se u blockchainu pojavila poruka: "we are whitehats"

Nekoliko sati nakon povlačenja dogodilo se nešto potpuno neuobičajeno. Dana **6. rujna u 18:30 UTC**, odnosno oko 20:30 po hrvatskom vremenu, u Bitcoin transakciji povezanoj s adresom na kojoj su završila sredstva pojavio se OP_RETURN zapis.

**Originalna on-chain poruka:**

**“we are whitehats. contact us on chain”**

**Prijevod:**

**„Mi smo white-hat hakeri. Kontaktirajte nas on-chain.”**

To nije bio komentar na društvenoj mreži niti poruka poslana kroz neku aplikaciju. Bila je to **prava Bitcoin transakcija** u kojoj je jedan output sadržavao OP_RETURN podatak. Sirovi zapis u blockchainu tehnički je spremljen kao računalni podatak, ali ga Bitcoin explorer može dekodirati i prikazati kao običan tekst. Svatko tko otvori odgovarajuću transakciju može vidjeti poruku zajedno s TXID-em, block heightom i vremenom potvrde.

Prema rekonstrukciji transakcija, poruka je bila umetnuta u transakciju koja je istodobno slala i malu količinu Bitcoina prema drugoj strani. Blockchain je tako postao svojevrsni javni komunikacijski kanal u pregovorima o stotinama milijuna dolara.

{{< support1 >}}

## Blockstream odgovara – također preko Bitcoin blockchaina

Blockstream nije ignorirao poruku. Oko sat vremena kasnije, **6. rujna u 19:31 UTC**, poslao je vlastitu Bitcoin transakciju s OP_RETURN porukom.

**Originalna Blockstreamova poruka:**

**“Please contact security@blockstream.com”**

**Prijevod:**

**„Molimo kontaktirajte security@blockstream.com.”**

Komunikacija se nakon toga nastavila. Dio tehničkih informacija razmijenjen je i u šifriranom obliku, a **7. rujna u 02:20 UTC** akteri su najavili da namjeravaju vratiti većinu sredstava i provjeravali adresu na koju bi Bitcoin trebao biti poslan.

Međutim, ubrzo nakon toga postavili su novi uvjet. Dana **7. rujna u 03:30 UTC**, odnosno oko 05:30 po hrvatskom vremenu, u blockchainu se pojavila poruka koja je postala središnji dio cijelog slučaja.

**Originalna on-chain poruka:**

**“Please fix the bug first. The chain is under risk at latest commit right now. Make sure every node is patched. Then we will transfer the money back safely after confirming the fix.”**

**Prijevod:**

**„Molimo prvo popravite bug. Mreža je trenutačno ugrožena u najnovijoj verziji. Pobrinite se da svaki node bude zakrpan. Nakon što potvrdimo da je problem riješen, sigurno ćemo vratiti novac.”**

Drugim riječima, ljudi koji su upravo kontrolirali Bitcoin vrijedan stotine milijuna dolara javno su poručili Blockstreamu: **prvo popravite bug i zakrpajte mrežu – tek onda vraćamo Bitcoin.**

## Blockstream javlja da je bug popravljen

Nakon rada na ranjivosti Blockstream je poslao novu potpisanu on-chain poruku kojom je potvrdio da su ključni bridge nodeovi zakrpani.

**Originalna Blockstreamova poruka:**

**“Bridge nodes are patched, safe to return the funds.”**

**Prijevod:**

**„Bridge nodeovi su zakrpani. Sredstva je sada sigurno vratiti.”**

Time je ispunjen uvjet koji su akteri prethodno javno postavili. I tada se dogodilo ono zbog čega je cijela priča toliko neobična: **održali su obećanje.**

Dana **7. rujna u 16:09 UTC**, odnosno nešto poslije 18 sati po hrvatskom vremenu, Bitcoin blockchain zabilježio je veliku transakciju kojom je **3.400 BTC vraćeno na Liquid Federation adresu**.

{{< support2 >}}

## Obećali su vratiti većinu – i 3.400 BTC zaista se vratilo

Povrat 3.400 BTC posebno je važan jer nije došao bez prethodne najave. Nekoliko sati prije toga akteri su javno zapisali u Bitcoin blockchain da će sredstva vratiti nakon što se ranjivost popravi i svi relevantni nodeovi budu zakrpani. Blockstream je zatim također on-chain potvrdio da je popravak proveden, nakon čega je velika transakcija zaista stigla natrag.

To ne znači da je cijeli iznos vraćen. Nakon transakcije na adresi povezanoj s incidentom ostalo je približno **598,5 BTC-a**, vrijednih oko 47 milijuna dolara. Nema javno potvrđenog dogovora prema kojem bi taj iznos predstavljao bug bounty niti je Blockstream objavio da je akterima dopušteno zadržati ga.

Zbog toga je preciznije reći da su akteri **vratili većinu Bitcoina kao što su obećali**, ali ne i sve. Status preostalih gotovo 600 BTC-a i eventualni daljnji povrat sredstava zasad ostaju otvoreni.

## Jesu li to zaista white-hat hakeri?

Sam naziv "white hat" treba koristiti oprezno. Akteri su se sami tako predstavili, ali nije poznato da su prije iskorištavanja ranjivosti imali dopuštenje Blockstreama, Liquid Federacije ili SideSwapa za izvođenje sigurnosnog testa ove veličine.

Klasični white-hat istraživač obično otkrije ranjivost, prijavi je kompaniji kroz security disclosure ili bug bounty program i zatim čeka da se problem riješi. Ovdje su akteri najprije povukli gotovo 4.000 BTC-a, a tek nakon toga stupili u kontakt s odgovornima.

S druge strane, njihovo ponašanje također nije izgledalo poput tipičnog crypto exploita u kojem napadač pokušava sredstva brzo prebaciti kroz mixere, bridgeove i niz novih adresa. Ovi su akteri ostali u komunikaciji s Blockstreamom, poslali tehničke informacije o bugu, zahtijevali popravak mreže i na kraju vratili 3.400 BTC-a.

Upravo zato slučaj ostaje teško svrstati u klasičnu kategoriju napada. Njihovo ponašanje nakon exploita ima obilježja white-hat sigurnosnog disclosurea, ali način na koji su prvo preuzeli kontrolu nad gotovo 320 milijuna dolara daleko je od standardne prakse sigurnosnih istraživača.

## Kako uopće izgleda razgovor "na blockchainu"

Bitcoin nije chat aplikacija, ali OP_RETURN omogućuje da se u transakciju upiše mala količina proizvoljnih podataka. Nakon potvrde transakcije ti podaci ostaju zapisani u blockchainu zajedno s TXID-em, block heightom i vremenom potvrde.

Na block exploreru korisnik zato vidi klasičnu Bitcoin transakciju s inputima i outputima, a među njima i output označen kao **OP_RETURN**. Kada je sadržaj kodiran kao tekst, explorer ga može prikazati ljudski čitljivo.

Dakle, korisnik ne mora gledati nešto poput `10110111010110`. U blockchainu je poruka računalno kodirana, ali explorer je može prikazati ovako:

**“we are whitehats. contact us on chain”**

I kasnije:

**“Please fix the bug first.”**

To cijeloj priči daje gotovo filmski element. Ljudi koji su kontrolirali gotovo 4.000 BTC i kompanija čiji je sustav bio pogođen ostavljali su jedni drugima poruke u **javnoj, trajnoj knjizi Bitcoin transakcija** koju je istodobno mogao čitati cijeli svijet.

## Što je Liquid Network i zašto je bug bio toliko opasan

Liquid je Bitcoin sidechain koji je razvio **Blockstream** kako bi omogućio brže transfere Bitcoina, povjerljivije transakcije i izdavanje različite digitalne imovine. Na njemu se koristi **L-BTC**, odnosno Liquid Bitcoin, koji bi trebao biti pokriven stvarnim BTC-om zaključanim u federation walletima.

Osnovna ideja je jednostavna: korisnik unese Bitcoin u Liquid sustav i dobije odgovarajuću količinu L-BTC-a. Kada se želi vratiti na Bitcoin mainnet, L-BTC se uništi, odnosno burna, a federation sustav oslobađa odgovarajući stvarni BTC.

Upravo je zato ovaj incident toliko ozbiljan. Ako je moguće stvoriti L-BTC bez stvarnog Bitcoin pokrića, a zatim ga provesti kroz normalan peg-out i dobiti pravi BTC, tada je ugrožen osnovni računovodstveni mehanizam cijelog bridgea.

Prema SideSwapu, njihovi sustavi i autorizacijski ključ nisu bili kompromitirani. Problem je bio u Elements softveru na kojem Liquid radi, zbog čega je transakcija mogla izgledati legitimno sve dok stvarni BTC nije već napustio federation wallet.

## Bitcoin mainnet nije hakiran

Važno je napraviti jasnu razliku između Liquid Networka i samog Bitcoina. Incident nije kompromitirao Bitcoin konsenzus, Bitcoin nodeove, privatne walletove korisnika niti sigurnost Bitcoin mainneta.

Problem je nastao na **Liquid sidechainu i njegovom mehanizmu za pretvaranje L-BTC-a natrag u stvarni BTC**. Bitcoin mreža je samo izvršavala valjano potpisane transakcije koje joj je federation sustav poslao.

Ironično, upravo je Bitcoin mainnet zatim poslužio kao javni zapisnik cijelog incidenta. Preko njega su poslane poruke **“we are whitehats”** i **“Please fix the bug first”**, preko njega je Blockstream potvrdio zakrpu i preko njega je na kraju vidljiv povrat 3.400 BTC-a.

## Naš osvrt

* **Akteri koji se nazivaju white-hat hakerima iskoristili su ranjivost povezanu s Elements softverom i iz Liquid Federation walleta izvukli približno 4.000 BTC.**
* Povlačenje je predstavljalo oko **95% Bitcoina koji se tada nalazio u federation walletu**, zbog čega je Liquid privremeno zaustavio bridge nodeove i dio mrežnih aktivnosti.
* Dana **6. rujna u 18:30 UTC** u Bitcoin blockchain upisali su poruku: **“we are whitehats. contact us on chain” – „Mi smo white-hat hakeri. Kontaktirajte nas on-chain.”**
* Blockstream im je također odgovorio kroz Bitcoin transakciju: **“Please contact security@blockstream.com” – „Molimo kontaktirajte security@blockstream.com.”**
* Dana **7. rujna u 03:30 UTC** akteri su poslali ključnu poruku: **“Please fix the bug first” – „Molimo prvo popravite bug”**, te zatražili da svi nodeovi budu zakrpani prije povrata sredstava.
* Blockstream je nakon zakrpe odgovorio: **“Bridge nodes are patched, safe to return the funds” – „Bridge nodeovi su zakrpani. Sredstva je sada sigurno vratiti.”**
* Nakon toga su akteri **7. rujna u 16:09 UTC vratili 3.400 BTC**, upravo kako su prethodno obećali.
* Na njihovoj adresi ostalo je približno **598,5 BTC-a**, bez javno potvrđenog dogovora da taj iznos predstavlja bug bounty.
* Bitcoin mainnet **nije bio hakiran**; problem je bio u Liquid sidechainu i njegovom peg-out mehanizmu.
* Najneobičniji dio cijelog slučaja jest da se **pregovor o gotovo 320 milijuna dolara odvijao dijelom javno, kroz poruke trajno zapisane u Bitcoin blockchainu**.
* Akteri su poručili da će vratiti Bitcoin kada se bug popravi – i **za 3.400 BTC održali su riječ**.

**Pratite Metaadvisor.eu za više vijesti o cryptu, Bitcoinu, blockchainu, kibernetičkoj sigurnosti, digitalnoj imovini, tehnologiji i financijskim tržištima.**

**Disclaimer:** Ovaj članak služi isključivo u informativne svrhe i ne predstavlja financijski, investicijski, pravni, porezni ili sigurnosni savjet niti preporuku za korištenje bilo koje crypto mreže, platforme ili usluge. Informacije o sigurnosnim incidentima mogu se mijenjati kako se objavljuju novi tehnički podaci i rezultati istraga. Prije donošenja financijskih odluka provedite vlastito istraživanje i provjerite aktualne informacije kod službenih izvora.

<small style="color:#999; font-size:0.8em;">U suradnji s AI-jem.</small>
