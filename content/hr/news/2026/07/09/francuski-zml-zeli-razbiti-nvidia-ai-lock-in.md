---
title: "Francuski ZML želi razbiti Nvidia AI lock-in"
slug: "francuski-zml-zeli-razbiti-nvidia-ai-lock-in"
date: 2026-07-09T08:00:00+02:00
category: "ai"
translationKey: "zml-france-nvidia-ai-lock-in-2026-07-08"
source: "TechCrunch, ZML, Metaadvisor.eu"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/companies/ZML-France.png"
featured_image: "/images/companies/ZML-France.png"
image: "/images/companies/ZML-France.png"
thumbnail: "/images/companies/ZML-France.png"
image_credit: "Metaadvisor.eu"
tags: ["ZML", "ZML LLMD", "Francuski AI startup", "AI inference", "LLM inference server", "Nvidia lock-in", "CUDA", "multi-chip AI", "AI infrastruktura", "open-source LLM", "AI čipovi", "AMD GPU", "Google TPU", "Apple Metal", "Intel Arc"]
summary: "Francuski AI startup ZML objavio je besplatan inference alat koji želi omogućiti brže pokretanje open-source AI modela na različitim čipovima, ne samo na Nvidia GPU-ima. Za obične korisnike to nije novi chatbot, nego infrastruktura ispod haube koja bi profesionalcima mogla pomoći smanjiti troškove i ovisnost o jednom hardverskom ekosustavu."
disclaimer: "Ovaj članak služi isključivo u informativne svrhe i ne predstavlja investicijski, tehnološki ili poslovni savjet."
draft: false
---

Slika je simbolična.

# Francuski ZML želi razbiti Nvidia AI lock-in: zašto to nije novi chatbot, nego infrastruktura ispod haube

Francuski AI startup **ZML** objavio je besplatan proizvod koji bi mogao biti zanimljiv profesionalcima koji grade AI sustave, cloud infrastrukturu, velike chatbotove i aplikacije koje koriste open-source jezične modele. No za običnog korisnika najvažnije je odmah reći što ZML **nije**.

ZML nije novi ChatGPT. Nije novi AI agent koji odgovara na e-mailove, piše objave, čita dokumente ili vodi korisničku podršku. ZML nije alat koji će prosječan korisnik otvoriti, spojiti na Gmail ili Google Sheets i odmah dobiti “AI zaposlenika”.

ZML je nešto drugo: infrastruktura ispod haube. To je softver koji pokušava pomoći AI modelima da rade brže i učinkovitije na različitim vrstama čipova, ne samo na Nvidia GPU-ima.

Drugim riječima, ZML nije restoran u kojem korisnik naručuje gotovo jelo. ZML je tehnologija za kuhinju. Pomaže onima koji grade AI sustave da isto “jelo” skuhaju brže, jeftinije i na različitim vrstama pećnica.

## Zašto je to uopće važno?

Danas većina ljudi AI vidi kroz gotove alate: ChatGPT, Claude, Gemini, Copilot, Sintra, Make, Zapier AI ili razne “AI agente” koji se reklamiraju po društvenim mrežama. Ti alati korisniku izgledaju jednostavno. Upišeš pitanje, povežeš dokumente, dodaš e-mail, CRM ili web stranicu i agent počne raditi.

Ali iza tog jednostavnog sučelja postoji veliki tehnički sloj koji korisnik ne vidi. Kada AI agent treba odgovoriti na upit, negdje u pozadini događa se cijeli lanac: aplikacija primi pitanje, šalje ga AI modelu, model se izvršava na serveru, server koristi određene čipove, a odgovor se vraća korisniku.

Za običnog korisnika to je nevidljivo. Za tvrtke koje same grade AI sustave, to je ogroman problem. Moraju odlučiti na čemu će vrtjeti model, koliko će ih to koštati, koliko brzo sustav mora odgovarati, koliko energije troši, može li raditi na **Nvidia** čipovima, **AMD-u**, **Google TPU-u**, **Apple Metal-u**, **Intel Arc-u** ili nekom drugom hardveru.

Tu ulazi ZML.

{{< support1 >}}

## ZML pokušava riješiti problem AI “adaptera”

Jedan od najvećih problema AI infrastrukture je to što različiti čipovi imaju različite softverske ekosustave. Nvidia nije toliko dominantna samo zato što ima moćne čipove, nego i zato što ima ogroman softverski sloj oko njih. Najpoznatiji dio tog ekosustava je **CUDA**, koji je godinama postao gotovo standard za mnoge AI i računalne zadatke.

To stvara ono što se često naziva **vendor lock-in**. Ako je sustav građen za Nvidia ekosustav, nije ga uvijek jednostavno prebaciti na drugi hardver. Tvrtka može imati pristup AMD GPU-ima, Apple čipovima ili nekom europskom AI čipu, ali ako softver nije dobro prilagođen, performanse mogu biti loše ili razvoj preskup.

ZML pokušava biti sloj koji taj problem ublažava. Njihov novi proizvod, **ZML/LLMD**, zamišljen je kao inference server koji omogućuje pokretanje open-source velikih jezičnih modela na različitim vrstama čipova. Prema TechCrunchu, ZML cilja na podršku za **Nvidia**, **AMD**, **Google TPU**, **Apple Metal**, **Intel Arc** i druge čipove.

Jednostavno rečeno: ZML želi da isti AI model može raditi na više različitih “motora”, a da programeri ne moraju svaki put sve ručno prilagođavati od nule.

## Što je inference i zašto je sve važniji?

U AI svijetu često se govori o treniranju modela. To je faza u kojoj se veliki model uči na ogromnim količinama podataka. To je skupo, zahtjevno i obično rezervirano za velike igrače.

Ali kada korisnik koristi AI, najčešće se događa nešto drugo: **inference**. To je trenutak kada već trenirani model prima upit i generira odgovor. Kada pitate chatbot da napiše e-mail, objasni zakon, sažme dokument ili generira kod, vi koristite inference.

Kako AI ulazi u sve više aplikacija, inference postaje sve važniji. Nije više dovoljno imati dobar model. Treba ga pokrenuti brzo, pouzdano i po prihvatljivoj cijeni. Ako milijuni korisnika stalno šalju upite, svaki odgovor košta. Svaki token troši računalne resurse. Svaka sekunda kašnjenja smeta korisniku.

Zato je pitanje infrastrukture postalo ključno. Ako AI tvrtka može isti model vrtjeti brže ili jeftinije, to može napraviti veliku razliku.

{{< support1 >}}

## Za koga je ZML?

ZML nije alat za obične korisnike koji žele napraviti jednostavnog AI agenta za posao, marketing ili administraciju. Ako koristite gotove alate poput Sintre, Makea, Zapiera, OpenAI asistenta ili nekog no-code AI servisa, vi najčešće ne razmišljate o čipovima. Platforma to rješava umjesto vas.

ZML je zanimljiv drugoj publici: programerima, AI inženjerima, cloud kompanijama, startupima koji grade AI proizvode, tvrtkama koje same hostaju modele i organizacijama koje žele izbjeći potpunu ovisnost o jednom dobavljaču hardvera.

Ako netko gradi vlastiti chatbot od početka do kraja, vlastiti AI backend ili vlastitu platformu za posluživanje modela, tada pitanje “na čemu se model izvršava” postaje jako važno. ZML pokušava pomoći upravo tom sloju tržišta.

Zato je važno ne miješati dvije stvari. Gotovi AI agenti su korisnički proizvodi. ZML je infrastrukturni alat.

Sintra je kao gotov restoran: korisnik naruči jelo i ne mora znati kakva je pećnica u kuhinji. ZML je tehnologija za tu kuhinju: pomaže profesionalcima da isto jelo naprave brže, jeftinije i na različitim vrstama opreme.

## Zašto se stalno spominje Nvidia?

Nvidia je danas simbol AI infrastrukture. Njezini GPU-i pokreću velik dio modernog AI vala, a potražnja za njima eksplodirala je zbog velikih modela, cloudova i AI aplikacija. No dominacija Nvidije donosi i problem: visoke cijene, ograničenu dostupnost i ovisnost o jednom ekosustavu.

ZML ne znači da je Nvidia dominacija gotova. To bi bilo pretjerano. Nvidia i dalje ima ogroman tehnološki, tržišni i softverski položaj. Ali ZML se uklapa u širi trend: sve više tvrtki pokušava pronaći načine kako AI modele pokretati i na drugim čipovima.

Ako se taj sloj poboljša, tržište dobiva više izbora. Tvrtke bi mogle koristiti kombinaciju Nvidia, AMD, Google, Apple, Intel ili specijaliziranih AI čipova, ovisno o cijeni, dostupnosti, brzini i potrošnji energije.

To ne mora biti vidljivo običnom korisniku, ali može utjecati na cijenu i dostupnost AI alata koje koristi.

{{< support2 >}}

## Europski kut priče

Zanimljivo je i to što ZML dolazi iz Francuske. Europa često zaostaje za SAD-om u velikim platformama i potrošačkim AI proizvodima, ali pokušava pronaći prostor u infrastrukturi, čipovima, sigurnosti i specijaliziranim tehnološkim slojevima.

TechCrunch piše da bi takav softverski sloj mogao pomoći i novim AI chipmakerima, među kojima su mnogi iz Europe. U članku se spominju **Axelera**, **Fractile**, **Kalray**, **OLIX**, **Q.ANT**, **SiPearl**, **SpiNNcloud** i **VSORA**. Poanta nije samo u tome odakle te tvrtke dolaze, nego u tome da novi AI hardver teško može postati široko upotrebljiv ako nema softver koji ga povezuje s modelima, aplikacijama i stvarnim korisničkim slučajevima.

To je važna lekcija: čip sam po sebi nije dovoljan. Hardver bez dobrog softvera teško ulazi u stvarnu upotrebu. Nvidia to jako dobro zna. Njezin uspjeh nije samo u siliciju, nego i u softverskom ekosustavu koji se godinama gradio oko njega.

Ako Europa želi ozbiljniju ulogu u AI infrastrukturi, mora razvijati i hardver i softver koji ga čini korisnim.

## Zašto ovo ipak može biti važno i običnim ljudima?

Iako ZML nije alat za običnog korisnika, posljedice ovakvih tehnologija mogu se osjetiti i šire. Ako AI modeli postanu jeftiniji za pokretanje, više tvrtki može nuditi AI usluge. Ako se smanji ovisnost o jednom dobavljaču hardvera, tržište može postati konkurentnije. Ako se inference ubrza, AI alati mogu postati brži i dostupniji.

Običan korisnik možda nikada neće instalirati ZML/LLMD. Ali može koristiti aplikaciju koja u pozadini koristi takav ili sličan infrastrukturni sloj. Kao što većina ljudi ne zna koji server pokreće njihovu bankovnu aplikaciju, ali itekako osjeti ako je aplikacija spora, skupa ili nedostupna.

ZML je zato priča o nevidljivom dijelu AI-ja. Ne o chatbotu koji odgovara korisniku, nego o sloju koji omogućuje da chatbot uopće radi brzo, stabilno i po prihvatljivoj cijeni.

{{< support2 >}}

## Naš osvrt

- ZML nije novi chatbot, AI agent ili alat za obične korisnike.
- ZML je infrastrukturni softver za profesionalce koji grade, hostaju ili optimiziraju AI modele.
- Njegov cilj je pomoći open-source LLM modelima da rade na različitim čipovima, ne samo na Nvidia GPU-ima.
- Glavna tema nije “novi AI”, nego smanjenje ovisnosti o jednom hardverskom ekosustavu.
- Za korisnike gotovih AI alata, ovaj sloj je uglavnom nevidljiv.
- Za tvrtke koje grade AI sustave od nule, inference, brzina, cijena i kompatibilnost čipova postaju ključni problemi.
- Ako alati poput ZML-a uspiju, AI tržište bi dugoročno moglo dobiti više konkurencije, niže troškove i manje ovisnosti o Nvidiji.
- Ovo je infrastrukturna priča, ali upravo takve priče često određuju koliko će AI na kraju biti dostupan, brz i skup.

**Disclaimer:** Ovaj članak služi isključivo u informativne svrhe i ne predstavlja investicijski, tehnološki ili poslovni savjet.
