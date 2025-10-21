---
title: "Mullenweg: WordPress i Tumblr — moj 'najveći neuspjeh' do sada"
slug: "mullenweg-wordpress-i-tumblr-najveci-neuspjeh-za-sada"
date: 2025-10-20T16:21:50Z
category: "ai"
translationKey: "7dd70dc2c082c409ed8b7ae2672a12d9"
source: "TechCrunch"
source_url: "https://techcrunch.com/2025/10/20/automattic-ceo-calls-tumblr-his-biggest-failure-so-far/"
author: "TechCrunch"
analysis_by: "Metaadvisor.eu"
image_url: "/images/tumblr.png"
featured_image: "/images/tumblr.png"
image: "/images/tumblr.png"
thumbnail: "/images/tumblr.png"
image_alt: "Tumblr — logotip, simbolična ilustracija"
image_credit: "Slika je simbolična."
tags: ["tumblr", "wordpress", "automattic", "matt mullenweg", "migracija", "wordpress backend", "fediverse", "activitypub", "open source", "cms", "tehnologija", "poslovanje", "restrukturiranje", "otkazi", "monetizacija", "saas", "cloud", "cdn", "seo", "id mapping"]
summary: "CEO Automattica Matt Mullenweg na WordCampu Canada 2025 nazvao je akviziciju Tumblra i njegovu odvojenost od WordPress infrastrukture svojim 'najvećim neuspjehom' do sada. Masovna migracija na WordPress back-end pauzirana je zbog skale i troška, ali projekt nije otkazan."
---

Su-osnivač WordPressa i CEO Automattica **Matt Mullenweg** na otvorenom je rekao ono što su mnogi u industriji već naslućivali: akvizicija **Tumblra** i višegodišnje oklijevanje oko potpunog tehničkog spajanja s WordPress infrastrukturom njegov je “**najveći neuspjeh do sada**”. Neuspjeh — ali ne i kapitulacija. Vizija ostaje ista: Tumblr **preseliti na WordPress back-end**, pojednostaviti razvoj, srezati troškove i uvesti Tumblr dublje u **fediverse**. Trenutno je taj plan **pauziran** jer je preskup i prekompleksan za stanje u kojem je Tumblr danas, no strateški cilj nije napušten.

## Zašto je plan zapinjao godinama
**Tehnički dug** i **različiti tech stackovi** — Tumblr i WordPress.com kroz vrijeme su razvijali odvojene sustave za identitet, pohranu medija, komentare, preporuke i moderaciju. To znači dupli kod, duple timove i dvostruko održavanje. Na to se nadovezuje **skala**: govorimo o **stotinama milijuna blogova**, milijardama URL-ova, slugova, slika, GIF-ova i videa, uz nestandardne formate iz različitih era Tumblra.

Istodobno, **ekonomija projekta** je tvrda: Tumblr **troši više nego što zarađuje**. Prihodi od oglasa i pretplata nisu pokrili operativne troškove, pa je Automattic morao **rezati troškove**, preusmjeravati ljude na profitabilnije linije (WordPress.com, WooCommerce, Jetpack) i tempirati migraciju tako da **ne ugrozi** zdrave dijelove poslovanja.

## Što bi WordPress back-end konkretno donio
- **Jedna platforma umjesto dvije**: zajednički auth, media, billing, anti-spam, sigurnost i observability — manje tehničkog duga i brži time-to-feature.  
- **Ekonomija razmjera**: dijeljeni timovi i alati, bolje iskorištenje CDN-a, keširanja i objedinjenog storagea, niži jedinični trošak.  
- **Uređena podatkovna linija**: standardizirani API-ji, stabilne sheme i lakše A/B testiranje na obje usluge.  
- **Put prema fediverseu**: kada je jezgra konsolidirana, lakše je izgraditi pouzdanu **ActivityPub** integraciju i interoperabilnost s decentraliziranim društvenim mrežama.

## Gdje su najveći tehnički rizici
1. **ID-mapiranje i trajna preusmjeravanja:** svaka promjena permalinkova ili internih identifikatora mora imati točnu mapu preusmjeravanja kako bi se **SEO i društveni signali** sačuvali.  
2. **Migracija medija i deduplikacija:** Tumblr je povijesno bogat medijima (posebno GIF-ovima). Potrebno je agresivno **keširanje**, **deduplikacija** i hladni storage za stare kolekcije.  
3. **Komentari, reblogovi, noteovi:** to je “društveni sloj” Tumblra; semantika se mora očuvati kako bi zajednica ostala živa.  
4. **Moderacija i sigurnost:** zajednice s jakim mem-kontekstom trebaju alate za **brzu moderaciju**, anti-spam i zaštitu od zlonamjernih kampanja.  
5. **Privatnost i compliance:** **GDPR**, retention politika i licence za medije prije retro-migracije; jasno razdvajanje privatnih i javnih signala.
---
<p style="text-align:center; margin:20px 0;">
  <a href="/go/mexc" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:white; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:600; display:inline-block;">
     👉 Trguj kripto na MEXC
  </a>
---
  
## Realističan operativni plan (faze bez skraćivanja)
**Faza 0 — stabilizacija troškova**  
Standardizirati CDN, uvesti agresivno keširanje, arhivirati neaktivne medije, smanjiti duplikate, unificirati observability (logovi, metričari, tracing).

**Faza 1 — “novi ide naprijed”**  
Svi **novi postovi** i mediji pišu se na WordPress servise, dok stari kontent ostaje čitljiv s postojećeg storagea. Time se sprječava rast duga.

**Faza 2 — vertikalni piloti**  
Migrirati **jedan tip sadržaja** (npr. tekst + slike bez videa) za ograničeni skup blogova. Uspostaviti **ID-mapu** i mjeriti gubitke/performance (TTFB, CTR, retention).

**Faza 3 — horizontalno širenje**  
Dodavati formate (video, GIF, ankete), uvesti **komentarni most**, očuvati reblog/like semantiku. U ovoj fazi kreću **trajna preusmjeravanja** i kanonski URL-ovi.

**Faza 4 — društveni sloj i fediverse**  
Prvo jednostrani publish u ActivityPub, potom dvosmjerni protok (praćenje, odgovori), uz granularne postavke privatnosti i kontrolu spama.

**Faza 5 — čišćenje repova**  
Deduplikacija starih medija, zatvaranje rubnih slučajeva, konsolidacija analitike i izvještavanja.

## Što znači za korisnike Tumblra
Idealan ishod je da **Tumblr ostane Tumblr**: isti urednici, isti osjećaj zajednice, ali brži i stabilniji. Promjene se događaju “**ispod haube**” — kraći zastoji, manje bugova i dosljedniji feedovi. Kreatorima to znači **predvidljiv reach**, bolje alate za objavu i manje “slomljenih” URL-ova prilikom promjena.

## Što znači za WordPress ekosustav
WordPress dobiva **povrat znanja** iz Tumblra: kreatorski formati, društvene integracije, brži eksperimenti. Ako migracija uspije, WordPress može isporučivati **socijalne značajke** korisnicima koji to žele, bez da se udalji od CMS korijena. Istovremeno, partnerima (agencijama, izdavačima) to je signal da je **infrastruktura jedinstvena** i dugoročno isplativa.

## Poslovna dimenzija i monetizacija
Bez zatvaranja tehničkog duga monetizacija je ograničena. Konsolidirani back-end otvara vrata **lakšim pretplatnim modelima**, **manje invazivnim oglasima**, “tip jar” donacijama i partnerstvima s izdavačima. Transparentniji troškovni model olakšava i **budžetiranje**: znat će se koliko košta novi feature i koja mu je stopa povrata.

## Rizici ako se nastavi status quo
- Trajni **tehnički dug** i dugoročno veći troškovi.  
- Odgođena isporuka značajki i sporiji oporavak brenda.  
- Potencijalno **curenje kreatora** prema platformama koje brže iteriraju.  

## Metrike po kojima se mjeri uspjeh
- **Stabilnost i performanse:** TTFB, error rate, vrijeme učitavanja medija.  
- **Integritet sadržaja:** postotak ispravno mapiranih URL-ova, nula izgubljenih komentara/reblogova.  
- **Ekonomija:** cijena po 1.000 pregleda medija, trošak storagea po TB, omjer prihoda i troška po korisniku.  
- **Zajednica:** aktivni kreatori, stopa zadržavanja, organski re-engagement nakon puštanja novih značajki.

---

**Naš osvrt (Metaadvisor):**  
- ✅ **Iskrenost** o “najvećem neuspjehu” je dobra vijest; stvara prostor za **disciplinirano restrukturiranje** umjesto kozmetike.  
- ⚙️ **Migracija bez gubitaka** traži beskompromisno ID-mapiranje, kanonske URL-ove, trajna preusmjeravanja i testiranje na uzorku — drugačije je preskupo.  
- 🧑‍⚖️ **Compliance** (GDPR, licence medija, retention) mora biti “gotov” prije retro-migracije; inače se rizik premješta s tehnike na pravni sektor.  
- 🌐 **Fediverse** neka bude nagrada nakon konsolidacije — diferencijator, ne distrakcija.  
- 📈 Kratkoročno očekujemo **oprez u investicijama** oko Tumblra; srednjoročno, jedinstveni back-end može vratiti povjerenje kreatora i oglašivača.

---

**Izvori (bez poveznica):** TechCrunch; WordCamp Canada 2025 (Town Hall).


</p>
