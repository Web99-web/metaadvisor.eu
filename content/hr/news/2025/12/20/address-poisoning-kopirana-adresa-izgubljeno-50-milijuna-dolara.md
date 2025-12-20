---
title: "Kopirao je adresu — i izgubio 50 milijuna dolara: najveća kripto greška godine"
slug: "address-poisoning-kopirana-adresa-izgubljeno-50-milijuna-dolara"
date: 2025-12-20T12:00:00
category: "crypto"
translationKey: "address_poisoning_50m_loss_20122025"
source: "Cointelegraph, CoinDesk"
source_url: "cointelegraph.com, coindesk.com"
author: "Metaadvisor.eu"
image_url: "/images/Lost-50-mil-usd.png"
featured_image: "/images/Lost-50-mil-usd.png"
image: "/images/Lost-50-mil-usd.png"
thumbnail: "/images/Lost-50-mil-usd.png"
image_alt: "Address poisoning prevara i gubitak 50 milijuna dolara nakon kopiranja kripto adrese"
image_credit: "MetaAdvisor illustration"
tags:
  - bitcoin
  - kripto
  - sigurnost
  - prijevara
  - address poisoning
  - usdt
  - ethereum
  - wallet
  - on-chain
  - tornado cash
  - cyber kriminal
summary: "Jedna pogrešno kopirana kripto adresa bila je dovoljna da nestane gotovo 50 milijuna USDT-a. Ovaj slučaj pokazuje kako address poisoning napadi iskorištavaju ljudske navike, a ne slabosti blockchaina."
---

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter"
     target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Ostvari Bitget bonus do 6200 USDT — započni trgovanje
  </a>
</p>

U jednom od najskupljih individualnih kripto incidenata ove godine, korisnik je **izgubio gotovo 50 milijuna USDT-a** nakon što je postao žrtva sofisticirane *address poisoning* prevare. Nije došlo do hakiranja walleta, krađe privatnih ključeva niti tehničkog propusta u blockchainu. Sve se dogodilo unutar onoga što većina korisnika smatra “normalnim” korištenjem kripto novčanika — i upravo zato je ovaj slučaj posebno opasan.

Riječ je o napadu koji cilja **ljudsko ponašanje**, a ne tehnologiju.

## Što se točno dogodilo

Prema on-chain podacima, žrtva je najprije povukla veliku količinu **USDT-a (Tether)** sa svoje burze. Kao mjeru opreza, poslala je **mali testni iznos (0,005 USDT)** na adresu za koju je vjerovala da je ispravna. Test-transakcija prošla je bez problema.

Međutim, prije slanja glavnog iznosa, napadači su uspjeli **zatrovati povijest transakcija** žrtvinog walleta. U povijesti se pojavila **lažna adresa** koja je vizualno izgledala gotovo identično pravoj — imala je **ista prva tri i ista zadnja četiri znaka**.

Kada je korisnik kasnije kopirao adresu iz povijesti transakcija, nesvjesno je kopirao **adresu napadača** i poslao **oko 49.999.950 USDT-a**. Transakcija je bila tehnički ispravna — i nepovratna.

Test-transakcija u ovom slučaju nije pomogla jer je:
- test poslan na ranije spremljenu adresu  
- glavni iznos poslan na adresu **kopiranu iz povijesti transakcija**

Dvije adrese. Jedna pogreška. Ogroman gubitak.

## Što je address poisoning prevara

*Address poisoning* je vrsta prevare koja ne pokušava razbiti kriptografiju niti kompromitirati blockchain. Umjesto toga, napadači **masovno generiraju nove kripto adrese** dok ne dobiju one koje izgledaju vrlo slično pravim adresama primatelja — isti početak i isti kraj, ali drugačija sredina.

Zatim šalju **minimalne “dust” transakcije** prema walletima potencijalnih žrtava. Wallet aplikacije takve transakcije legitimno prikazuju u povijesti, bez ikakvog upozorenja. Kada korisnik kasnije kopira adresu iz “recent” popisa, vjerujući da je sigurna jer je “već korištena”, zapravo kopira **krivu adresu**.

Ovo je napad koji:
- ne zahtijeva malware  
- ne zahtijeva phishing link  
- ne ostavlja tehnički trag pogreške  

Sve se odvija unutar standardnog korisničkog sučelja wallet aplikacija.

## Munjevita pretvorba i pranje sredstava

Nakon što je napadač primio gotovo **50 milijuna USDT-a**, sredstva su vrlo brzo preusmjerena kroz nekoliko koraka:

- USDT je pretvoren u **DAI**, decentralizirani stablecoin  
- DAI je zatim zamijenjen za oko **16.690 ETH**  
- Gotovo cijeli iznos (**oko 16.680 ETH**) poslan je kroz **Tornado Cash**

Ovim postupkom izvor sredstava je učinkovito zamagljen, a mogućnost praćenja i povrata svedena na minimum. Iako Tornado Cash više ne funkcionira kao klasičan projekt s javnim sučeljem, njegovi **pametni ugovori i dalje postoje na blockchainu** i mogu se izravno pozivati — što kriminalci i dalje koriste.

### Tornado Cash: Roman Storm, Lazarus i najkontroverzniji kripto sudski slučaj desetljeća
*(interni link u plavom naslovu u produkciji)*

## Zašto je ova prevara posebno značajna

Ovaj slučaj pokazuje da najveći rizici u kriptu danas **više nisu tehnički**, već **operativni**. Umjesto bugova u pametnim ugovorima, sve češće gledamo napade koji iskorištavaju:

- ljudsku nepažnju  
- loš UX wallet aplikacija  
- naviku kopiranja adresa bez potpune provjere  

Takvi napadi mogu rezultirati **gubicima u desecima milijuna dolara**, čak i kada korisnici misle da postupaju sigurno.

## Kako se zaštititi

**Nikada ne kopiraj adresu iz povijesti transakcija — koristi address book, ENS ili domenske adrese i uvijek provjeri sredinu adrese, ne samo početak i kraj.**

<p style="font-size:0.85em; color:#6b7280; margin-top:18px;">
<strong>Odricanje od odgovornosti:</strong> Ovaj sadržaj služi isključivo u informativne svrhe i ne predstavlja investicijski savjet. Kriptovalute su volatilne i rizične; prije bilo kakvih financijskih odluka provedi vlastito istraživanje.
</p>
