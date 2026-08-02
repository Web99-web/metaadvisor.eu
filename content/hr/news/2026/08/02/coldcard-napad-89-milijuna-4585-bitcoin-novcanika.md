---
title: "Coldcard napad od 89 milijuna pogodio 4.585 Bitcoin novčanika"
slug: "coldcard-napad-89-milijuna-4585-bitcoin-novcanika"
date: 2026-08-02T12:00:00+02:00
category: "crypto"
translationKey: "coldcard-napad-89-milijuna-4585-bitcoin-novcanika-2026-08-02"
source: "Galaxy Research, Coinkite, CoinDesk, Cointelegraph i CryptoQuant"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/hack/Coldcard-hack-89M.png"
featured_image: "/images/hack/Coldcard-hack-89M.png"
image: "/images/hack/Coldcard-hack-89M.png"
thumbnail: "/images/hack/Coldcard-hack-89M.png"
image_alt: "Coldcard napad proširio se na 4.585 Bitcoin novčanika uz gotovo 89 milijuna dolara gubitaka"
image_credit: "Metaadvisor.eu – slika je simbolična"
tags: ["Coldcard", "Bitcoin", "Bitcoin wallet", "hardverski novčanik", "crypto hack", "kibernetička sigurnost", "seed fraza", "privatni ključ", "Coldcard Mk3", "Coldcard Mk4", "Bitcoin krađa", "self-custody", "Coinkite", "Galaxy Research", "kripto sigurnost"]
description: "Coldcard napad proširio se na 4.585 Bitcoin novčanika, dok su procijenjeni gubici porasli na 1.367 BTC-a, odnosno gotovo 89 milijuna dolara."
summary: "Napad povezan s ranjivim seedovima generiranima na određenim verzijama Coldcard firmwarea nastavio se u više valova. Napadači sada ciljaju i manje novčanike, a ukradeni bitcoin raspoređuju na veći broj odredišnih adresa."
---

*Slika je simbolična.*

# Coldcard napad od 89 milijuna pogodio 4.585 Bitcoin novčanika

Napad povezan s ranjivim seedovima generiranima na određenim verzijama Coldcard firmwarea više nije ograničen na prvi val u kojem je gotovo 1.200 Bitcoin adresa ispražnjeno u samo 41 minuti.

Prema novim procjenama Galaxy Researcha, u tri dosad identificirana vala napada ispražnjeno je ukupno 4.585 adresa, a ukradeno je približno 1.367 BTC-a, vrijednih gotovo 89 milijuna dolara.

Najnoviji val pokazuje da napadač više ne cilja samo veće iznose. Sustavno se prelazi i na novčanike vrijedne nekoliko tisuća dolara.

Napad se nastavio gotovo tri dana nakon prvih velikih transakcija, dok je način premještanja ukradenih sredstava postao složeniji i teži za praćenje.

## Treći val pogodio još 1.912 adresa

U trećem identificiranom valu napada ukradeno je približno 208 BTC-a s 1.912 adresa.

Prosječan iznos po pogođenoj adresi sada je nešto veći od 0,1 BTC-a. To je znatno manje nego u prvom valu, kada je s 1.196 adresa u 41 minuti povučeno približno 1.083 BTC-a, odnosno gotovo jedan bitcoin po adresi.

Pad prosječnog iznosa sugerira da su najveći i najprofitabilniji novčanici iz ranjivog prostora ključeva možda već ispražnjeni. Napadač sada prelazi na manje iznose koji mu i dalje mogu biti isplativi.

To je posebno zabrinjavajuće za korisnike koji su možda vjerovali da zbog relativno malog iznosa na novčaniku neće biti zanimljivi napadaču.

## Napadač je promijenio taktiku

Prva dva vala napada bila su relativno jednostavna za povezivanje jer su se ukradeni bitcoini slijevali na manji broj zajedničkih adresa.

U trećem valu sredstva s pojedinačnih pogođenih adresa šalju se prema zasebnim odredištima. Transakcije su istodobno grupirane, prosječno po šest žrtava u jednom sweepu.

Sredstva su prebačena u pay-to-witness-script-hash izlaze, koji mogu podržavati složenije uvjete poput multisig potpisa ili vremenskog zaključavanja. U prethodnim valovima češće su korišteni jednostavniji izlazi povezani s jednim ključem.

Napadač je u novom valu pretraživao samo zadanu derivacijsku putanju, odnosno standardnu granu stabla ključeva koju novčanik uobičajeno prvo provjerava.

{{< support1 >}}

## Isti napadač ili više neovisnih operatera?

Promjena načina rada može značiti da je isti napadač prilagodio sustav nakon što su njegove prve adrese javno identificirane.

Moguće je i da drugi napadač neovisno pretražuje isti ranjivi prostor ključeva.

Blockchain sam po sebi ne može pokazati jesu li sva tri vala međusobno koordinirana. Galaxy Research smatra da je svaki pojedinačni val vjerojatno djelo jednog operatera, ali zasad ne povezuje sva tri vala s istom osobom ili skupinom.

Najnovija promjena taktike ipak pokazuje da osobe koje iskorištavaju ranjivost prate javne analize i prilagođavaju način premještanja ukradenih sredstava.

## Kako je krađa moguća bez pristupa uređaju?

Problem nije nastao zato što su napadači fizički ukrali Coldcard uređaje, povezali se s njima ili presreli korisničke seed fraze putem interneta.

Ranjivost je bila u načinu generiranja slučajnih podataka potrebnih za stvaranje seeda.

Promjena uvedena tijekom migracije firmwarea u ožujku 2021. uzrokovala je da generiranje seeda u određenim verzijama koristi softverski generator slučajnih brojeva umjesto namjenskog hardverskog izvora slučajnosti.

Na pogođenim Mk2 i Mk3 uređajima efektivni prostor pretraživanja, prema preliminarnoj procjeni proizvođača, mogao je iznositi približno 40 bitova umjesto očekivane razine sigurnosti.

Kasniji modeli Mk4, Q i Mk5 imali su dodatnu entropiju iz sigurnosnih elemenata, ali je proizvođač procijenio da su određeni seedovi mogli imati približno 72 bita entropije, i dalje manje od planiranih 128 bitova.

{{< support2 >}}

## Napadač može rekonstruirati privatni ključ offline

Smanjena količina entropije ograničila je broj mogućih seedova koje je ranjivi firmware mogao proizvesti.

Napadaču s dovoljno računalne snage i informacijama o ranjivosti to omogućuje da offline reproducira moguće seedove, iz njih izvede privatne ključeve i provjeri postoje li sredstva na pripadajućim Bitcoin adresama.

Napadač zato ne mora dodirnuti Coldcard uređaj, znati korisnikov PIN niti dobiti fizičku kopiju njegove seed fraze.

Uređaj može ostati cijelo vrijeme isključen i odvojen od interneta, a sredstva svejedno mogu biti ugrožena jer napad nije usmjeren na komunikaciju s uređajem.

Napada se predvidljiv prostor mogućih privatnih ključeva.

## Ažuriranje firmwarea ne spašava stari seed

Coinkite je objavio ispravljene verzije firmwarea za pogođene modele i upozorio korisnike da ne generiraju novi seed prije instaliranja odgovarajućeg ažuriranja.

Međutim, nadogradnja firmwarea ne može popraviti seed koji je već generiran na ranjivoj verziji.

Korisnik mora:

* instalirati ispravljeni firmware
* generirati potpuno novi seed
* pažljivo zapisati i provjeriti novu sigurnosnu kopiju
* provjeriti novu adresu na zaslonu uređaja
* prvo poslati malu testnu transakciju
* nakon potvrde premjestiti preostala sredstva

Coinkite upozorava korisnike da tijekom migracije ne žure jer pogreška u prepisivanju seeda, provjeri adrese ili slanju sredstava može stvoriti dodatni i neposredniji rizik gubitka.

{{< support1 >}}

## Koji modeli i verzije mogu biti pogođeni?

Prema sigurnosnom upozorenju proizvođača, problem obuhvaća seedove generirane na Mk2 i Mk3 uređajima s firmwareom od verzije 4.0.1 do 4.1.9.

Pogođeni mogu biti i seedovi generirani na Mk4, Mk5 i Q uređajima prije objave ispravljenih verzija firmwarea za pojedini model i release track.

Ispravljene verzije koje proizvođač navodi uključuju:

* Mk2 i Mk3: verzija 4.2.0 ili novija
* Mk4 i Mk5 Standard: verzija 5.6.0 ili novija
* Q Standard: verzija 1.5.0Q ili novija
* Mk4 i Mk5 Edge: verzija 6.6.0X ili novija
* Q Edge: verzija 6.6.0QX ili novija

TAPSIGNER, OPENDIME i SATSCARD nisu pogođeni jer koriste drugačije codebaseove.

Korisnici ne bi trebali zaključiti da su sigurni samo zato što su nakon upozorenja ažurirali uređaj. Presudno je utvrditi na kojoj je verziji firmwarea njihov postojeći seed izvorno generiran.

## Dice rolls i snažan passphrase mogu smanjiti rizik

Coinkite navodi da seed možda nije ugrožen samo ovom RNG ranjivošću ako je korisnik pri izvornom stvaranju seeda dodao najmanje 50 poštenih, neovisnih i privatnih bacanja kocke.

Takva ručno dodana entropija proširuje prostor mogućih seedova koji bi napadač morao pretraživati.

Snažan i jedinstven BIP-39 passphrase također stvara dodatnu prepreku napadaču.

Međutim, kratak, uobičajen, ponovljen ili predvidljiv passphrase nije dovoljna zaštita. Passphrase također nije isto što i PIN kojim se otključava Coldcard uređaj.

Čak se i korisnicima sa snažnim passphraseom preporučuje migracija na potpuno novi seed jer passphrase samo smanjuje neposrednu izloženost. Ne popravlja ranjivi seed iz kojeg su izvedene adrese.

{{< support2 >}}

## Korisnici vraćaju bitcoin na burze

Incident je izazvao ponašanje suprotno onome koje je bilo vidljivo nakon propasti FTX-a.

Nakon kolapsa centralizirane burze korisnici su masovno povlačili kriptovalute prema privatnim novčanicima i hardverskim uređajima.

Sada dio vlasnika bitcoina sredstva šalje natrag na burze jer ih doživljava kao privremeno sigurnije od potencijalno pogođenih Coldcard adresa.

Podaci CryptoQuanta pokazali su snažan rast manjih Bitcoin transfera i depozita na burze. Dio transakcija može pripadati korisnicima koji premještaju sredstva na nove, sigurno generirane novčanike, dok ih drugi privremeno šalju na centralizirane platforme.

To ne znači da su centralizirane burze općenito sigurnije od self-custodyja.

Incident pokazuje da sigurnost ne ovisi samo o tome je li privatni ključ pohranjen offline, nego i o tome je li seed iz kojeg je ključ nastao generiran s dovoljno kvalitetne slučajnosti.

## Gdje se ukradeni bitcoin sada nalazi?

Prema dosadašnjim blockchain analizama, najveći dio ukradenog bitcoina još se nalazi na Bitcoin mreži, na adresama koje kontroliraju napadači.

Kod prvih valova dio sredstava bio je konsolidiran na manji broj adresa.

U trećem valu sredstva su raspoređena na veći broj zasebnih odredišta, zbog čega ih je teže prikazati kao jedan veliki saldo i jednostavno povezati s ranijim valovima.

Nema potvrde da je ukradeni BTC izravno poslan na identificiranu centraliziranu burzu, pretvoren u fiat novac ili zamijenjen za ETH i prebačen kroz Tornado Cash.

Native bitcoin ne može se izravno poslati kroz Tornado Cash jer taj protokol ne radi na Bitcoin mreži. Napadač bi ga najprije morao zamijeniti za imovinu na podržanoj EVM mreži, što bi stvorilo dodatne blockchain tragove i potencijalne točke za identifikaciju ili zamrzavanje sredstava.

{{< support1 >}}

## Air-gapped uređaj nije zaštita od slabog seeda

Coldcard uređaji poznati su po mogućnosti korištenja bez izravne internetske veze.

Air gap može smanjiti rizik napada tijekom komunikacije, povezivanja s računalom i potpisivanja transakcija.

Međutim, ne može zaštititi sredstva ako je privatni ključ izveden iz predvidljivog seeda.

U ovom slučaju uređaj može ostati cijelo vrijeme offline, a napadač svejedno može preuzeti sredstva jer ne napada sam uređaj. Umjesto toga pretražuje ograničeni skup ključeva koje je ranjivi firmware mogao proizvesti.

To ovaj incident čini važnim upozorenjem za cijelu industriju hardverskih novčanika.

Sigurnost ne ovisi samo o fizičkoj zaštiti uređaja, sigurnosnim elementima, PIN-u i air-gapped načinu rada. Temelj svega ostaje kvalitetna i stvarno nepredvidljiva entropija korištena pri stvaranju privatnog ključa.

## Napad se proširio na manje novčanike

Coldcard incident prerastao je iz jednog brzog napada u višednevno i sustavno pražnjenje tisuća Bitcoin adresa.

Dosad identificirani gubici porasli su na približno 1.367 BTC-a, gotovo 89 milijuna dolara i 4.585 pogođenih adresa.

Treći val pokazuje da napadači više ne ciljaju samo velike novčanike. Kako se najveći iznosi prazne, pretraživanje se nastavlja i prema adresama s manjim saldima.

To znači da korisnik ne bi trebao pretpostaviti da je siguran samo zato što na potencijalno ranjivoj adresi nema velik iznos bitcoina.

Najvažniji korak nije samo ažurirati firmware, nego na ispravljenom uređaju generirati potpuno novi seed i sredstva premjestiti na adrese izvedene iz tog novog seeda.

## Naš osvrt

* Coldcard napad proširio se na najmanje 4.585 Bitcoin adresa.
* Procijenjeni gubici porasli su na približno 1.367 BTC-a, odnosno gotovo 89 milijuna dolara.
* Treći val pogodio je još 1.912 adresa i odnio približno 208 BTC-a.
* Napadači sada ciljaju i manje novčanike s prosječno znatno nižim saldom.
* Promjena odredišnih adresa i grupiranje žrtava otežavaju praćenje transakcija.
* Nije potvrđeno stoji li ista osoba ili skupina iza sva tri vala.
* Napad ne zahtijeva fizički pristup Coldcard uređaju niti poznavanje PIN-a.
* Smanjena entropija omogućila je offline pretraživanje mogućih seedova i privatnih ključeva.
* Ažuriranje firmwarea sprječava generiranje novih ranjivih seedova, ali ne popravlja postojeći seed.
* Pogođeni korisnici moraju generirati novi seed na ispravljenom firmwareu i premjestiti sredstva.
* Snažan BIP-39 passphrase i ručno dodana entropija mogu smanjiti rizik, ali ne mijenjaju službenu preporuku za migraciju.
* Većina ukradenog bitcoina prema dosadašnjim analizama i dalje se nalazi na Bitcoin mreži.
* Ukradeni native BTC ne može se izravno poslati kroz Tornado Cash.
* Air-gapped novčanik nije siguran ako je seed iz kojeg su izvedeni privatni ključevi bio predvidljiv.
* Konačne brojke mogu dodatno rasti jer se blockchain analiza nastavlja.

**Disclaimer:** Članak je informativnog i edukativnog karaktera te ne predstavlja financijski, investicijski ili sigurnosni savjet. Korisnici koji bi mogli biti pogođeni trebaju pažljivo provjeriti službeno sigurnosno upozorenje proizvođača i nikada ne unositi seed frazu ili passphrase na web-stranice, u obrasce ili na nepouzdane uređaje.

U suradnji s AI-jem.
