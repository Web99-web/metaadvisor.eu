---
title: "ChatGPT UX: Zašto ne možemo uređivati i brisati poruke"
slug: "chatgpt-ux-zasto-ne-mozemo-uredivati-brisati-poruke-unutar-duzeg-razgovora"
date: 2026-10-02T07:00:00+02:00
category: "digital-tools"
translationKey: "chatgpt-ux-edit-delete-message-2026-10-02"
source: "OpenAI Help Center, Metaadvisor.eu"
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/informative/ChatGPT-UX-delete-message.jpg"
featured_image: "/images/informative/ChatGPT-UX-delete-message.jpg"
image: "/images/informative/ChatGPT-UX-delete-message.jpg"
thumbnail: "/images/informative/ChatGPT-UX-delete-message.jpg"
image_alt: "ChatGPT razgovor i prijedlog kontrola za uređivanje, brisanje i premještanje pojedinačne poruke."
image_credit: "Metaadvisor.eu"
tags: ["ChatGPT", "ChatGPT UX", "korisničko iskustvo", "uređivanje poruka", "brisanje poruka", "digitalni alati", "AI alati", "OpenAI", "UX"]
description: "ChatGPT dopušta brisanje cijelog razgovora, ali ne nudi jednostavnu kontrolu za uređivanje ili uklanjanje jedne već poslane poruke."
summary: "Jedan tipfeler, zaboravljeni zarez ili pogrešno poslana slika mogu promijeniti smisao cijelog razgovora. Predlažemo četiri UX kontrole: Edit message, Delete message, Move to another chat i Hide from context."
---

*Slika je simbolična.*
 
# Nervira li i vas ovaj ChatGPT UX? Jednu poruku ne možete jednostavno ispraviti ili izbrisati unutar dužeg razgovora

**ChatGPT danas omogućuje brisanje cijelog razgovora, ali ako usred dugog chata slučajno pošaljete pogrešnu sliku, dokument ili poruku s greškom, nemate jednostavnu kontrolu kojom biste tu jednu poruku naknadno ispravili ili uklonili. Kod razgovora koji se koriste satima, danima ili tjednima, to postaje puno veći UX problem nego što na prvi pogled izgleda.**

OpenAI u službenom Help Centeru objašnjava kako izbrisati ili arhivirati cijeli razgovor. Izbrisani chat odmah nestaje iz korisničkog prikaza i predviđen je za trajno brisanje iz sustava u roku od 30 dana, uz navedene sigurnosne i pravne iznimke. Arhiviranje uklanja razgovor iz glavne bočne trake, ali ga čuva na računu. Trenutačna dokumentacija opisuje kontrole na razini cijelog razgovora, ali ne navodi zasebno brisanje jedne poruke unutar postojećeg chata. 

## Jedna pogrešna poruka može ostati u vrlo važnom razgovoru

Zamislimo jednostavan primjer. Radite na poslovnom zadatku i već imate dugi razgovor s ChatGPT-om u kojem razvijate web stranicu, analizirate dokumente i dogovarate poslovna rješenja. U jednom trenutku primijetite da vam mačka stalno kašlje i želite o tome pitati ChatGPT, ali slučajno fotografiju mačke pošaljete u postojeći poslovni razgovor. Isto se može dogoditi sa screenshotom, dokumentom ili bilo kojim drugim sadržajem koji pripada potpuno drugom zadatku.

Tu sliku mačke ili drugi pogrešno poslani sadržaj više ne možete jednostavno ukloniti iz tog razgovora. Poruka možda nema nikakvu vrijednost za nastavak rada, ali ostaje kao crna mrlja u važnom poslovnom chatu. Ako vam je razgovor važan zbog desetaka prethodnih odluka, analiza, uploadanih dokumenata i konteksta, brisanje cijelog razgovora nije realno rješenje - niti opcija koju biste željeli koristiti.

## Problem nije samo brisanje nego i ispravak

Ponekad poruka uopće nije pogrešna tema. Problem može biti samo jedan tipfeler, broj ili zaboravljeni zarez.

Razlika između:

`Ne smeta me to.`

i:

`Ne, smeta me to.`

ogromna je. Jedan zarez može potpuno promijeniti značenje poruke. Ako korisnik grešku primijeti odmah nakon slanja, najprirodnije bi bilo očekivati mogućnost da je jednostavno ispravi prije nego što pogrešno protumačen sadržaj utječe na nastavak razgovora.

ChatGPT često iz šireg konteksta može pogoditi što je korisnik zapravo htio reći, ali to nije isto što i korisniku dati kontrolu nad vlastitom porukom.

## Prva opcija: Edit message

Najjednostavnija kontrola za ovakve situacije bila bi:

`⋯ → Edit message`

Korisnik bi mogao ispraviti tipfeler, broj, datum, zarez ili pogrešno napisanu riječ bez slanja dodatne poruke poput “ispravak”, “mislila sam...” ili “zaboravila sam zarez”.

Ako su kasniji odgovori već nastali na temelju stare verzije poruke, ChatGPT bi mogao jasno upozoriti da izmjena može utjecati na razumljivost nastavka razgovora ili ponuditi stvaranje nove grane od uređene poruke.

Takva funkcija posebno bi imala smisla ako korisnik pogrešku primijeti odmah nakon slanja.

## Druga opcija: Delete message

Za sadržaj koji uopće ne pripada razgovoru uređivanje nije dovoljno. Ako je slučajno poslana pogrešna slika, PDF ili poruka iz sasvim drugog projekta, korisniku treba:

`⋯ → Delete message`

Poruka bi se mogla ukloniti uz upozorenje da je model možda već koristio njezin sadržaj pri stvaranju kasnijih odgovora.

Takva kontrola dala bi korisniku izbor između zadržavanja nepotrebnog sadržaja i brisanja cijelog razgovora.

{{< support1 >}}

## Treća opcija: Move to another chat

Ponekad poruka nije pogrešna, nego je samo završila u pogrešnom razgovoru. Tada bi još korisnija opcija bila:

`Move to another chat`

Primjerice, korisnik u razgovor o web projektu slučajno ubaci screenshot vezan uz financije, putovanje ili drugi projekt. Umjesto ponovnog otvaranja novog razgovora, traženja originalne slike i ponovnog uploadanja, poruka bi se mogla premjestiti zajedno s privitkom.

To bi bilo posebno korisno kod slika, PDF-ova, tablica i drugih dokumenata koji su već prošli upload i obradu.

## Četvrta opcija: Hide from context

Postoji i blaže rješenje koje ne bi moralo fizički brisati poruku:

`Hide from context`

Poruka bi ostala vidljiva korisniku kao dio povijesti, ali ChatGPT je više ne bi koristio kao relevantan kontekst u nastavku razgovora.

Takva opcija bila bi korisna kada korisnik želi sačuvati zapis onoga što se dogodilo, ali zna da određena poruka više nema nikakvu vezu s aktualnim zadatkom.

To bi također smanjilo rizik da fizičko brisanje jedne poruke poremeti razumljivost kasnijeg dijela razgovora.

## Zašto obična korekcija u novoj poruci nije isto rješenje

Naravno, korisnik uvijek može poslati novu poruku i napisati da je prethodna bila pogrešna. U jednostavnom razgovoru to često radi dovoljno dobro.

Ali u dugim radnim chatovima takve korekcije stvaraju dodatni sloj nereda. Umjesto jedne ispravne poruke, u razgovoru ostaju originalna pogreška, zatim ispravak i eventualni odgovor nastao između njih.

Što razgovor dulje traje, to takve sitnice postaju sve vidljiviji UX problem.

## Chatovi sve više postaju radni prostori

Ovakve kontrole postaju važnije kako se način korištenja ChatGPT-a mijenja. Razgovor više nije nužno nekoliko pitanja i odgovora koje korisnik zatvori nakon pet minuta.

Jedan chat može sadržavati istraživanje, kod, slike, PDF dokumente, poslovne odluke, podatke iz više izvora i desetke iteracija istog projekta. Što razgovori postaju duži i važniji, to raste potreba za osnovnim alatima za upravljanje njihovim sadržajem.

Brisanje cijelog razgovora dovoljno je kada je chat nevažan. Za razgovor koji je postao radni prostor to je vrlo gruba kontrola.

{{< support2 >}}

## Brisanje cijelog razgovora već postoji

OpenAI trenutno nudi jasne kontrole za brisanje i arhiviranje cijelog razgovora. Chat se može ukloniti iz povijesti, arhivirati kako bi ostao spremljen bez prikaza u glavnoj bočnoj traci ili se svi razgovori mogu skupno arhivirati ili izbrisati. :chatgpt-content-reference{index="1"}

To rješava problem upravljanja cijelim razgovorima, ali ne i upravljanja sadržajem unutar jednog važnog razgovora.

Upravo tu postoji UX praznina: razina kontrole ide od cijelog chata do vrlo malo mogućnosti nad jednom pojedinačnom već poslanom porukom.

## Kako bi idealna kontrola mogla izgledati?

Najlogičnije bi bilo da se uz svaku korisničku poruku u izborniku s tri točke pojave četiri zasebne mogućnosti:

* **Edit message** — ispravlja tekst, broj, datum ili interpunkciju bez potrebe za dodatnom korektivnom porukom.
* **Delete message** — uklanja poruku iz razgovora uz upozorenje ako može utjecati na kasniji kontekst.
* **Move to another chat** — premješta poruku i pripadajuće privitke u drugi ili novi razgovor.
* **Hide from context** — ostavlja poruku u povijesti, ali je isključuje iz daljnjeg konteksta modela.

Ne mora svaka od tih opcija biti tehnički jednostavna za implementaciju. Odgovori modela mogu ovisiti o prethodnim porukama, uploadanim datotekama i cijeloj grani razgovora. Ali iz korisničke perspektive problem je vrlo jasan: dugoročni radni chat traži preciznije kontrole od “zadrži sve” ili “izbriši cijeli razgovor”.

## Naš osvrt

* **Najveća UX praznina nije samo brisanje, nego nedostatak fine kontrole nad jednom već poslanom porukom.**
* **Edit message bio bi posebno važan kod malih grešaka koje mijenjaju smisao.** Jedan zarez, broj ili pogrešna riječ mogu poslati razgovor u potpuno drugom smjeru.
* **Delete message bio bi koristan kada sadržaj uopće ne pripada razgovoru**, primjerice kod slučajno poslane slike ili dokumenta.
* **Move to another chat bio bi posebno koristan za privitke**, jer bi spriječio ponovno traženje i uploadanje istih datoteka.
* **Hide from context mogao bi biti najbolji kompromis** kada sadržaj treba ostati u povijesti, ali više ne bi trebao utjecati na nastavak razgovora.
* **Slanje dodatne poruke s ispravkom funkcionira, ali nije isto što i uređivanje originala.** U dugim radnim razgovorima to samo povećava količinu nepotrebnog sadržaja.
* **Kako AI chatovi postaju dugoročni radni prostori, granularno upravljanje sadržajem postaje sve važnije.**
* **OpenAI već nudi dobre kontrole na razini cijelog razgovora, ali između jedne poruke i cijelog chata još postoji velika UX praznina.**

**Pratite Metaadvisor.eu za više vijesti i analiza o umjetnoj inteligenciji, tehnologiji, digitalnim alatima, financijskim tržištima i globalnim tehnološkim trendovima.**

**Disclaimer:** Ovaj članak predstavlja UX analizu i prijedlog funkcionalnosti na temelju trenutačno dostupnih ChatGPT kontrola i službene OpenAI dokumentacije. Dostupnost pojedinih kontrola može se razlikovati ovisno o platformi, verziji proizvoda ili korisničkom sučelju, a funkcije se mogu mijenjati tijekom daljnjeg razvoja.

<small style="color:#999; font-size:0.8em;">U suradnji s AI-jem.</small>
