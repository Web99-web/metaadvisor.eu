---
title: "Injective SDK hakiran: napadači ciljali ključeve kripto walleta"
slug: "injective-sdk-hakiran-napadaci-ciljali-kljuceve-kripto-walleta"
date: 2026-07-10T12:00:00+02:00
category: "crypto"
translationKey: "injective-sdk-npm-wallet-keys-2026-07-10"
source: "Cointelegraph, Socket, Aikido, OX Security, DefiLlama, CoinGecko, Metaadvisor.eu"
source_url: "https://cointelegraph.com/news/hackers-compromise-injective-npm-package-with-malware-to-steal-wallet-keys"
author: "Metaadvisor.eu"
image_url: "/images/hack/Injective-SDK-hacked.png"
featured_image: "/images/hack/Injective-SDK-hacked.png"
image: "/images/hack/Injective-SDK-hacked.png"
thumbnail: "/images/hack/Injective-SDK-hacked.png"
image_credit: "Metaadvisor.eu"
tags: ["Injective", "Injective SDK", "npm paket", "supply chain napad", "kripto sigurnost", "wallet ključevi", "privatni ključevi", "seed phrase", "mnemonic fraza", "Web3 sigurnost", "DeFi sigurnost", "developer alati", "GitHub", "npm malware", "kripto wallet"]
summary: "Kompromitiran je Injective npm paket @injectivelabs/sdk-ts, a zlonamjerna verzija ciljala je privatne ključeve i mnemonic fraze kripto walleta. Incident nije napad na sam blockchain, nego primjer sve važnijeg rizika u Web3 prostoru: napada na softverski lanac opskrbe."
disclaimer: "Ovaj članak služi isključivo u informativne svrhe i ne predstavlja investicijski, tehnološki, sigurnosni ni financijski savjet."
draft: false
---

Slika je simbolična.

# Injective SDK hakiran: napadači ciljali ključeve kripto walleta

Injective se našao u sigurnosnoj priči koja pokazuje koliko opasan može biti napad na softverski lanac opskrbe. Prema sigurnosnim istraživačima, kompromitiran je npm paket **@injectivelabs/sdk-ts**, TypeScript/JavaScript SDK koji se koristi pri razvoju aplikacija povezanih s Injective ekosustavom.

Važno je odmah razjasniti: ovo nije napad na sam blockchain. Napadači nisu ciljali kriptografiju protokola ili smart contracte, nego developerski alat kojem aplikacije vjeruju. Upravo zato je incident važan. U Web3 svijetu privatni ključ nije obična lozinka. Ako napadač dođe do privatnog ključa ili seed phrasea, može preuzeti kontrolu nad walletom.

## Što se dogodilo?

Zlonamjerna verzija paketa bila je **@injectivelabs/sdk-ts 1.20.21**. Prema Socketu, ta je verzija bilježila privatne ključeve i mnemonic fraze, a rizik se širio i kroz druge pakete unutar Injective Labs npm scopea koji su bili vezani uz zlonamjernu verziju.

Aikido navodi da je kompromitirani paket imao oko **50.000 tjednih preuzimanja**, što objašnjava zašto je incident brzo privukao pozornost sigurnosne zajednice. Zlonamjerni kod bio je maskiran kao telemetrija, odnosno naizgled bezazlen dio softvera, ali je u pozadini ciljao najosjetljivije podatke walleta.

To je tipičan primjer supply-chain napada. Napadači ne moraju probiti blockchain da bi došli do korisničke imovine. Ponekad je dovoljno kompromitirati alat koji developeri koriste za izgradnju aplikacija.

{{< support1 >}}

## Zašto je ovo ozbiljno?

U klasičnom napadu korisnik često mora kliknuti sumnjiv link, preuzeti lažnu aplikaciju ili upisati seed phrase na phishing stranici. Kod supply-chain napada opasnost dolazi iz smjera koji korisnik uopće ne vidi. Aplikacija može izgledati legitimno, a zlonamjerni kod može stići kroz paket koji je povučen tijekom razvoja ili build procesa.

U ovom slučaju malware je ciljao privatne ključeve i mnemonic fraze tijekom wallet workflowa. Ako takav kod završi u aplikaciji koja generira, učitava ili upravlja walletom, rizik postaje vrlo konkretan. Blockchain može raditi normalno, smart contracti mogu biti ispravni, a korisnik svejedno može biti ugrožen zbog kompromitirane developerske ovisnosti.

Zato je ova priča važnija od jednog paketa. Ona pokazuje da se sigurnost kripta ne svodi samo na protokole i smart contracte. Treba gledati i npm pakete, GitHub račune, dependency lance, lockfileove i CI/CD procese kojima se aplikacije grade.

## Koliki je bio doseg?

Prema Aikidu, zlonamjerna verzija bila je aktivna manje od sat vremena prije nego što je uočena i zamijenjena čistom verzijom. To je dobra vijest, ali ne uklanja rizik za sve koji su paket povukli u tom kratkom razdoblju.

OX Security dodatno navodi da je incident mogao utjecati na širi dependency lanac, s **87 dependent paketa** i više od **112.000 kombiniranih preuzimanja** u zahvaćenom okruženju. Kod ovakvih incidenata nije važno samo koliko je dugo zlonamjerna verzija bila javno dostupna. Važno je i je li završila u nekom projektu, cacheu, lockfileu ili aplikaciji koja ju je kasnije nastavila koristiti.

Zato developeri ne mogu gledati samo direktnu instalaciju paketa. Treba provjeriti i tranzitivne ovisnosti, odnosno pakete koji su mogli povući kompromitiranu verziju kao dependency.

{{< support1 >}}

## Tržišni kontekst: manji TVL i slabiji token

Injective je interoperabilni layer-1 blockchain usmjeren na DeFi aplikacije. No njegov ekosustav danas je znatno manji nego na vrhuncu. Prema podacima koje navodi Cointelegraph, ukupna zaključana vrijednost, odnosno TVL, pala je oko **88%**, s vrhunca od **71 milijun dolara** sredinom 2024. na oko **8,2 milijuna dolara**.

Sličan pad vidi se i na tržišnoj strani. INJ je na vrhuncu bio oko **52,62 dolara**, dok se sada kreće oko **4,8 dolara**. To ne znači da je ovaj sigurnosni incident uzrokovao pad TVL-a ili cijene tokena. Ti su se padovi dogodili kroz dulje razdoblje. Ali kontekst je važan: kada je ekosustav već znatno manji nego na vrhuncu, sigurnosni incidenti dodatno otvaraju pitanja o povjerenju, developerskoj aktivnosti i kvaliteti alata koji se koriste u aplikacijama.

Drugim riječima, ovo nije priča o tome da je jedan hack srušio tržište. Ovo je priča o reputacijskom riziku u ekosustavu koji se već bori s manjom aktivnošću nego prije dvije godine.

## Što trebaju napraviti developeri?

Developeri bi trebali provjeriti koriste li **@injectivelabs/sdk-ts 1.20.21** ili neki povezani paket koji je mogao povući tu verziju. Posebno treba pregledati **package.json**, lockfileove, buildove, deployment pipeline i sve Injective pakete korištene u projektu.

Ako je zlonamjerna verzija bila korištena, nije dovoljno samo ažurirati paket. Svaki privatni ključ ili mnemonic koji je mogao proći kroz kompromitirani SDK treba tretirati kao potencijalno kompromitiran. U kriptu se takav rizik ne “popravlja”. Ako postoji realna mogućnost da je seed phrase procurio, sredstva se premještaju na novi wallet s novim ključevima.

To može zvučati strogo, ali logika je jednostavna: ako netko možda zna privatni ključ, taj wallet više nije siguran.

{{< support2 >}}

## Što to znači za korisnike?

Obični korisnici ne moraju paničariti samo zato što koriste Injective aplikacije ili prate Injective ekosustav. Problem nije u tome da je svaki korisnik automatski ugrožen. Rizik je povezan s aplikacijama koje su možda koristile kompromitirani SDK u wallet workflowima.

Korisnici bi trebali pratiti sigurnosne obavijesti aplikacija koje koriste i biti posebno oprezni ako ih je neka aplikacija tražila unos, generiranje ili učitavanje seed phrasea. Seed phrase se ne unosi u aplikacije kojima se ne vjeruje, ne dijeli se i ne sprema na nesigurna mjesta.

Ako postoji sumnja da je seed phrase bio izložen, sigurnije je premjestiti sredstva na novi wallet. U kriptu je čekanje često najskuplja opcija.

## Zašto je ova priča veća od Injectivea?

Ovaj incident pokazuje širi problem Web3 sigurnosti. Aplikacije se danas ne grade od nule. Developeri koriste velik broj paketa, biblioteka i ovisnosti. Jedan kompromitirani paket može se brzo proširiti kroz cijeli lanac.

U Web3 prostoru taj je rizik posebno osjetljiv jer aplikacije često rade s walletima, potpisivanjem transakcija i imovinom koja se može nepovratno premjestiti. Napadači zato ne moraju uvijek tražiti bug u smart contractu. Ponekad je lakše kompromitirati developerski račun, npm paket ili build proces.

To je najvažnija lekcija ovog incidenta: najslabija točka ne mora biti blockchain. Može biti alat kojim se blockchain aplikacije grade.

{{< support2 >}}

## Naš osvrt

- Ovo nije priča o “hakiranom tokenu”, nego o kompromitiranom developerskom paketu.
- Zlonamjerna verzija bila je **@injectivelabs/sdk-ts 1.20.21**.
- Malware je ciljao privatne ključeve i mnemonic fraze kripto walleta.
- Najveći rizik odnosi se na developere, aplikacije i korisnike koji su mogli koristiti kompromitiranu verziju u wallet workflowima.
- Potencijalni doseg bio je ozbiljan jer se paket koristi u developerskom okruženju, a dio rizika mogao se širiti kroz dependency lance.
- Injectiveov TVL i tržišna cijena INJ-a znatno su niži nego na vrhuncu, što ovom incidentu daje dodatni reputacijski kontekst.
- To ne znači da je incident uzrokovao pad TVL-a ili tokena, nego da sigurnosni problemi imaju veću težinu kada ekosustav već ima manju aktivnost.
- Najvažnija lekcija je šira: u Web3 sigurnosti nije dovoljno gledati samo blockchain i smart contracte. Treba gledati i npm pakete, GitHub račune, dependency lance i alate kojima se aplikacije grade.

**Disclaimer:** Ovaj članak služi isključivo u informativne svrhe i ne predstavlja investicijski, tehnološki, sigurnosni ni financijski savjet.
