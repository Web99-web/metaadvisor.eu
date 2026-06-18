---
title: "Fortinet ili FortiBleed? VPN lozinke, firewalli i rizik za 194 zemlje"
slug: "fortinet-ili-fortibleed-vpn-lozinke-firewalli-rizik-194-zemlje"
date: 2026-06-18T06:00:00+02:00
category: "cybersecurity"
translationKey: "fortinet-fortibleed-vpn-lozinke-firewalli-rizik-194-zemlje-2026-06-18"
source: "Reuters, BleepingComputer, SOCRadar, Arctic Wolf, CISA, Metaadvisor.eu"
source_url: "https://metaadvisor.eu/"
author: "Metaadvisor.eu"
image_url: "/images/hack/Fortinet-Fortibleed.png"
featured_image: "/images/hack/Fortinet-Fortibleed.png"
image: "/images/hack/Fortinet-Fortibleed.png"
thumbnail: "/images/hack/Fortinet-Fortibleed.png"
image_alt: "Fortinet ili FortiBleed kao simbol cyber sigurnosnog rizika za VPN lozinke, firewalle i mrežnu infrastrukturu"
image_credit: "Metaadvisor.eu"
tags: ["Fortinet", "FortiBleed", "FortiGate", "VPN", "firewall", "lozinke", "cyber sigurnost", "hakiranje", "credential harvesting", "brute force", "mrežna infrastruktura", "Heartbleed", "CISA", "SOCRadar", "BleepingComputer", "Reuters", "Metaadvisor"]
summary: "FortiBleed nije službeni naziv nove Fortinet ranjivosti, nego nadimak za veliki leak i kampanju vezanu uz Fortinet/FortiGate VPN vjerodajnice, firewalle i rizik koji se prema sigurnosnim izvještajima proteže kroz 194 zemlje."
---

Slika je simbolična.

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="https://www.bitgetapps.com/referral/register?clacCode=2QZSXTW1&from=%2Fevents%2Freferral-all-program&source=events&utmSource=PremierInviter" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Ostvari Bitget bonus do 6200 USDT — registriraj se ovdje
  </a>
</p>

# Fortinet ili FortiBleed? VPN lozinke, firewalli i rizik za 194 zemlje

Na prvi pogled, **FortiBleed** zvuči kao naziv videoigre ili nekog cyberpunk scenarija. Ali iza tog naziva krije se ozbiljna cyber-security priča vezana uz **Fortinet**, **FortiGate firewalle**, **VPN pristupe** i navodno veliko curenje vjerodajnica koje se, prema sigurnosnim istraživačima, proteže kroz **194 zemlje**.

Fortinet je jedna od velikih svjetskih cybersecurity tvrtki. Njegovi FortiGate firewalli i VPN sustavi koriste se u tvrtkama, javnim institucijama, školama, bolnicama, telekomima, bankama, hosting kompanijama i državnim sustavima. Za laike, najjednostavnije objašnjenje je ovo: **Fortinetovi uređaji često stoje na ulazu u poslovnu mrežu**. Oni su digitalna vrata, brava i portir koji odlučuje tko smije ući u sustav, a tko ne.

{{< support1 >}}

## FortiBleed nije službeni naziv nove Fortinet ranjivosti

Važno je odmah razjasniti: **FortiBleed nije službeni Fortinetov naziv i nije službeno ime nove Fortinet ranjivosti**. To je nadimak koji se pojavio u cyber zajednici i medijima za leak i kampanju povezanu s Fortinet/FortiGate VPN vjerodajnicama.

Prema izvještajima koji su se pojavili u sigurnosnoj zajednici, leak navodno uključuje Fortinet i FortiGate VPN podatke za **73.932 firewall URL-a**, **21.632 domene** i organizacije u **194 zemlje**. Fortinet je objavio da je svjestan **credential-harvesting kampanje** koja cilja njegove firewall i VPN uređaje, ali tvrdi da se zlonamjerna aktivnost oslanja na podatke iz ranijih incidenata i brute-force pokušaje, a ne na novi incident ili novi sigurnosni advisory.

To je važna razlika. Ne radi se nužno o jednoj novoj “rupi” koja je upravo otkrivena, nego o širem problemu starih pristupa, ukradenih ili recikliranih lozinki, konfiguracija i uređaja koji su možda već ranije bili izloženi.

## Zašto se to zove FortiBleed?

Naziv **FortiBleed** očito podsjeća na **Heartbleed**, jednu od najpoznatijih sigurnosnih ranjivosti iz 2014. godine. Heartbleed je bio ozbiljan problem u OpenSSL kriptografskoj biblioteci koji je mogao omogućiti napadačima pristup osjetljivim podacima, uključujući korisničke vjerodajnice i tajne ključeve.

Tada je riječ **“bleed”** simbolično označavala da sustav “krvari” podatke koje ne bi smio otkrivati. FortiBleed koristi sličnu logiku naziva: sugerira da sigurnosni sustav, odnosno firewall i VPN infrastruktura, navodno “krvari” pristupne podatke.

{{< support1 >}}

U tome ima i malo cyber sarkazma. Naziv zvuči dramatično, gotovo marketinški, ali poruka je jasna: **ako alat koji bi trebao štititi ulaz u mrežu počne otkrivati ključeve za taj ulaz, posljedice mogu biti ozbiljne**. To nije samo problem za IT odjele. To može biti problem za zaposlenike, korisnike, klijente i sve čiji se podaci nalaze iza tih digitalnih vrata.

## Kako istraživači znaju koje su zemlje i domene obuhvaćene?

Kod ovakvih leakova podaci se ne moraju sastojati samo od jedne lozinke. U izvještajima o FortiBleedu spominju se **firewall URL-ovi**, domene, konfiguracijski podaci, VPN zapisi i vjerodajnice povezane s Fortinet/FortiGate uređajima.

Iz takvih podataka moguće je grupirati pogođene sustave prema domenama, IP adresama, nacionalnim nastavcima, organizacijama, geolokaciji i zapisima iz same konfiguracije. Zato se pojavljuju brojke poput **73.932 firewall URL-a**, **21.632 domene** i **194 zemlje**.

Ipak, pojavljivanje neke domene u takvoj bazi **ne znači automatski da je cijela organizacija potvrđeno kompromitirana**. To znači da se njezin Fortinet/FortiGate endpoint, domena ili povezani zapis navodno pojavljuje u skupu podataka koji istraživači povezuju s kampanjom.

## Poljski primjer pokazuje širu sliku

Poljski primjer pokazuje zašto FortiBleed nije samo američka ili velika-korporativna priča. Pojedini istraživači već objavljuju nacionalne popise domena koje se navodno pojavljuju u FortiBleed podacima, uključujući telekom operatere, javne servise i lokalne institucije.

U jednoj takvoj objavi za Poljsku spominju se domene poput **orange(.)pl**, **netia(.)pl**, **praca(.)gov(.)pl**, **zoo(.)lodz(.)pl**, **komornik(.)pl**, **sig(.)pl**, **veracomp(.)pl** i **krosoft(.)pl**.

{{< support2 >}}

Takve objave ne dokazuju same po sebi puni kompromis svake navedene organizacije, ali pokazuju širinu problema. Ako se kampanja zaista proteže kroz **194 zemlje**, onda se ne radi o izoliranom incidentu, nego o **globalnom riziku za mrežnu infrastrukturu**.

Danas se objavljuju poljske domene, sutra se mogu analizirati domene iz neke druge zemlje. I upravo to čini ovu priču važnom za Europu, javne institucije, telekome, hosting tvrtke i privatni sektor.

## Patch nije isto što i sanacija

Još jedan važan dio priče je razlika između patcha i stvarne sanacije. Kada se otkrije sigurnosni problem, prva reakcija često je: instalirajte update. To je nužno, ali nije uvijek dovoljno.

Ako su lozinke, hash-evi ili konfiguracijski podaci već izvučeni, napadač možda više ne treba istu ranjivost. Možda već ima ključ.

To je najvažnija lekcija FortiBleed priče. **Patch može zatvoriti rupu, ali ne briše ukradene lozinke.** Ako su administratorske lozinke reciklirane, ako VPN korisnici nisu resetirani, ako postoje stari računi, ako se ne provjere logovi i ako se ne uklone sumnjive promjene u konfiguraciji, organizacija može ostati izložena i nakon tehničkog ažuriranja.

## Zašto je ovo važno i običnim korisnicima?

Za obične korisnike ova tema možda zvuči daleko. Većina ljudi ne zna koristi li njihova banka, škola, poslodavac, grad, bolnica, telekom ili hosting provider Fortinet uređaje. Ali upravo u tome je problem. Naša digitalna sigurnost često ovisi o opremi i konfiguracijama koje nikada ne vidimo.

Ako je firewall ulaz u mrežu, onda kompromitiran firewall nije samo “još jedan hakirani uređaj”. To je potencijalni ulaz u cijeli sustav.

FortiBleed zato nije samo priča o Fortinetu. To je priča o tome kako **stari pristupi, slabe lozinke, ranije kompromitirani uređaji i nedovoljna sanacija** mogu godinama ostati sigurnosni problem. Napadači ne moraju uvijek pronaći novu ranjivost ako mogu iskoristiti stare ključeve koji još uvijek rade.

Ova priča se posebno uklapa u širi trend napada na **edge uređaje**, odnosno uređaje koji stoje na rubu mreže i povezuju unutarnje sustave s internetom. Firewalli, VPN gatewayi i slična infrastruktura sve su češća meta jer napadaču mogu dati izravan pristup prema unutra.

U cyber sigurnosti najopasniji trenutak nije uvijek sama ranjivost. Često je opasniji trenutak nakon toga, kada svi misle da je problem riješen jer je instaliran update, a nitko nije provjerio tko je bio unutra dok su vrata bila otvorena. Ako su konfiguracije izvezene, ako su lozinke crackane ili ako su VPN pristupi ostali aktivni, napad se može nastaviti drugim putem.

## Naš osvrt (Metaadvisor)

FortiBleed zvuči kao igra riječi, ali poruka iza tog naziva je ozbiljna. Kada sigurnosni sustav “krvari” pristupne podatke, problem nije samo u jednom proizvodu ili jednoj tvrtki. Problem je u načinu na koji organizacije upravljaju pristupima, lozinkama, starim računima i sanacijom nakon incidenata.

* **FortiBleed nije službeni naziv nove Fortinet ranjivosti**, nego nadimak za širu kampanju i leak povezane s Fortinet/FortiGate VPN vjerodajnicama.
* **Naziv podsjeća na Heartbleed iz 2014. godine**, kada je riječ “bleed” simbolično označavala da sustav “krvari” podatke koje ne bi smio otkrivati.
* **Patch nije kraj priče.** Ako je napadač već došao do ključeva, treba promijeniti ključeve, provjeriti brave i pregledati tko je ulazio.
* **Pojavljivanje domene u leak podacima ne znači automatski puni kompromis cijele organizacije**, ali znači da postoji signal koji bi trebalo ozbiljno provjeriti.
* **VPN i firewall uređaji nisu obični alati.** Oni često stoje na ulazu u poslovne, javne i državne mreže. Kada su oni kompromitirani, rizik se može širiti prema cijelom sustavu.
* **Digitalna higijena više nije luksuz.** Reset lozinki, provjera logova, uklanjanje starih pristupa, višefaktorska autentifikacija i redovita provjera konfiguracija danas su osnovna sigurnosna pravila.
* **Za obične korisnike ovo je podsjetnik da njihovi podaci često ovise o infrastrukturi koju nikada ne vide.** Banka, bolnica, škola, grad, telekom ili hosting provider mogu koristiti sustave o kojima korisnik ne zna ništa, ali posljedice propusta mogu osjetiti svi.

<p style="font-size:0.82em; color:#888; line-height:1.5; margin-top:24px;">
Disclaimer: Ovaj sadržaj služi isključivo u informativne svrhe i ne predstavlja financijski ni investicijski savjet.
</p>
```
