---
title: "Dropbox hack preko Lenovo ID-a kompromitirao 5.000 računa"
slug: "dropbox-hack-lenovo-id-kompromitirao-5000-racuna"
date: 2026-09-02T18:00:00+02:00
category: "Tech"
translationKey: "dropbox-lenovo-id-hack-5000-accounts-2026-09-02"
source: "Dropbox, Lenovo, Reuters, BleepingComputer"
author: "Metaadvisor.eu"
image_url: "/images/hack/Dropbox-Lenovo-hack.png"
featured_image: "/images/hack/Dropbox-Lenovo-hack.png"
image: "/images/hack/Dropbox-Lenovo-hack.png"
thumbnail: "/images/hack/Dropbox-Lenovo-hack.png"
image_alt: "Dropbox sigurnosni incident u kojem je preko Lenovo ID propusta kompromitirano oko 5.000 korisničkih računa"
image_credit: "Metaadvisor.eu"
tags: ["Dropbox", "Lenovo", "Lenovo ID", "hakiranje", "cyber sigurnost", "sigurnost", "krađa podataka", "korisnički računi", "cloud", "2FA", "autentifikacija", "digitalni identitet", "sigurnosni propust", "lozinke", "zaštita podataka"]
description: "Dropbox je potvrdio da je oko 5.000 korisničkih računa kompromitirano preko sigurnosnog propusta povezanog sa starom Lenovo ID integracijom. Napadačima pritom nije trebala Dropbox lozinka."
summary: "Napadači su iskoristili slabost u Lenovo ID email verifikaciji kako bi se predstavili kao vlasnici tuđih email adresa i preko stare integracije pristupili Dropbox računima. Dio datoteka bio je pregledan ili preuzet, a pogođeni računi nisu imali uključen Dropbox 2FA."
---

*Slika je simbolična.*

# Dropbox hack: oko 5.000 računa kompromitirano preko Lenovo ID propusta

Dropbox je potvrdio sigurnosni incident u kojem je tijekom kolovoza kompromitirano oko **5.000 korisničkih računa**, a na dijelu njih napadači su pregledavali ili preuzimali datoteke. Posebno je zanimljiv način na koji je napad izveden: **hakerima nije trebala Dropbox lozinka korisnika**.

Problem je bio povezan sa starom integracijom između **Lenovo ID-a i Dropboxa**. Napadači su uspjeli iskoristiti slabost u provjeri email adrese na Lenovo strani te se preko te povezanosti predstaviti Dropboxu kao legitimni vlasnici računa.

## Kako je Lenovo ID mogao otvoriti tuđi Dropbox?

Dropbox je ranije omogućavao autentifikaciju preko Lenovo ID-a. Ideja je jednostavna: vanjski servis potvrdi identitet korisnika, a Dropbox toj potvrdi vjeruje bez potrebe da se svaki put ponovno unosi Dropbox lozinka.

Napadači su, prema informacijama objavljenima nakon incidenta, mogli registrirati **Lenovo ID koristeći email adresu druge osobe**. Ako je ista email adresa bila povezana s postojećim Dropbox računom, stara integracija mogla je omogućiti pristup tom Dropboxu.

Drugim riječima, napadač nije morao ukrasti ni pogoditi korisnikovu Dropbox lozinku. Dovoljno je bilo kompromitirati način na koji jedan sustav drugome potvrđuje identitet.

## Oko 5.000 računa bilo je kompromitirano

Neovlašteni pristupi zabilježeni su između **4. i 21. kolovoza 2026.**, a Dropbox je nakon istrage počeo obavještavati pogođene korisnike.

Oko **5.000 računa** bilo je kompromitirano, dok su na manje od trećine tih računa napadači pregledavali ili preuzimali sadržaj datoteka. To znači da kompromitiran račun ne mora nužno značiti da je cijeli sadržaj Dropboxa ukraden, ali je napadač uspio dobiti pristup koji nije smio imati.

Posebno je važno da pogođeni računi **nisu imali uključen Dropboxov two-factor authentication (2FA)**.

{{< support1 >}}

## Nije trebalo ni imati Lenovo računalo

Incident nije značio da su Lenovo laptopi hakirani niti da je posjedovanje Lenovo računala automatski stvaralo rizik.

Još je zanimljivije da korisnik **nije morao ni imati postojeći Lenovo ID**. Problem je bio upravo u mogućnosti da napadač napravi novi Lenovo ID koristeći tuđu email adresu i zatim iskoristi staru povezanost s Dropboxom.

Zato je ovo prije svega priča o **digitalnom identitetu i povjerenju između dvije platforme**, a ne o kompromitiranom Lenovo uređaju.

## Slaba karika nije bila Dropbox lozinka

Korisnike se godinama upozorava da koriste duge i jedinstvene lozinke, izbjegavaju phishing stranice i ne dijele pristupne podatke. Ovaj incident pokazuje da ni savršena lozinka ne rješava svaki problem.

Ako aplikacija dopušta prijavu preko drugog servisa, sigurnost računa djelomično ovisi i o tom vanjskom sustavu. Kada jedan identity provider pogrešno potvrdi da je napadač vlasnik određene email adrese, posljedice se mogu prenijeti na servis koji toj potvrdi vjeruje.

U ovom slučaju **lanac povjerenja između Lenovo ID-a i Dropboxa postao je sigurnosna slabost**, iako korisnik sam možda godinama nije koristio tu integraciju.

{{< support2 >}}

## Dropbox je promijenio način prijave

Nakon otkrivanja incidenta Dropbox je poništio aktivne sesije autentificirane preko Lenovo ID-a, uklonio postojeće veze između Lenovo ID-a i Dropbox računa te promijenio način na koji ta integracija funkcionira.

Lenovo ID više ne bi trebao biti dovoljan za samostalni pristup postojećem Dropbox računu. Kod takvog načina prijave sada se dodatno traži i **Dropbox lozinka**.

Dropbox je pogođenim korisnicima preporučio i promjenu lozinki te uključivanje 2FA zaštite.

## Zašto je 2FA ovdje posebno važan?

Kod 2FA zaštite lozinka ili potvrda identiteta preko drugog servisa nisu jedini uvjet za ulazak u račun. Potrebna je još jedna potvrda, primjerice kod iz authenticator aplikacije.

Upravo zato je važan podatak da kompromitirani računi nisu imali uključen Dropbox 2FA. Napadaču je bilo dovoljno iskoristiti problem u prvom sloju autentifikacije jer nije postojao dodatni korak koji bi ga zaustavio.

Incident je dobar primjer zašto je 2FA koristan čak i kada korisnik ima snažnu lozinku i nikada nije kliknuo na phishing link.

## Naš osvrt

* **Oko 5.000 Dropbox računa kompromitirano je preko slabosti povezane sa starom Lenovo ID integracijom.**
* **Napadačima nije trebala Dropbox lozinka korisnika.** Problem je bio u načinu na koji je Lenovo ID mogao potvrditi vlasništvo nad email adresom.
* **Na manje od trećine pogođenih računa napadači su pregledavali ili preuzimali datoteke.**
* **Posjedovanje Lenovo računala samo po sebi nije značilo da je korisnik pogođen**, a žrtva nije nužno morala prethodno imati Lenovo ID.
* **Pogođeni Dropbox računi nisu imali uključen 2FA**, što ponovno pokazuje vrijednost dodatnog sloja autentifikacije.
* **Najvažnija pouka nije samo vezana uz Dropbox i Lenovo.** Svaka stara opcija poput „Sign in with…“ ili povezanog vanjskog računa može postati dio sigurnosnog lanca koji korisnik više ni ne pamti.
* **Sigurnost računa zato ne ovisi samo o lozinci**, nego i o svim platformama kojima je tijekom godina dopušteno potvrđivati naš digitalni identitet.

**Pratite Metaadvisor.eu za više poslovnih i tehnoloških vijesti, AI tema, cyber sigurnosti, digitalnih platformi, praktičnih tech trikova i analiza promjena koje utječu na našu digitalnu sigurnost.**

**Disclaimer:** Ovaj članak služi isključivo u informativne svrhe. Informacije o Dropbox i Lenovo sigurnosnom incidentu temelje se na javno dostupnim izjavama kompanija i medijskim izvještajima u trenutku objave. Korisnici koji sumnjaju na neovlašten pristup trebali bi provjeriti aktivne sesije i povezane aplikacije, promijeniti lozinku te uključiti two-factor authentication.

<small style="color:#999; font-size:0.8em;">U suradnji s AI-jem.</small>
