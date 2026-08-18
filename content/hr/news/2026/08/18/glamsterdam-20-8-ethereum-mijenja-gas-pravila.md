---
title: "Glamsterdam 20.8.: Ethereum mijenja gas pravila"
slug: "glamsterdam-20-8-ethereum-mijenja-gas-pravila"
date: 2026-08-18T22:46:00+02:00
category: "Crypto"
translationKey: "ethereum-glamsterdam-gas-rules-2026-08-18"
source: "Ethereum Foundation, Ethereum Improvement Proposals, Forkcast, Cointelegraph"
author: "Metaadvisor.eu"
image_url: "/images/eth4.jpg"
featured_image: "/images/eth4.jpg"
image: "/images/eth4.jpg"
thumbnail: "/images/eth4.jpg"
image_alt: "Ethereum Glamsterdam upgrade 20. kolovoza 2026. i promjene gas pravila"
image_credit: "Metaadvisor.eu – slika je simbolična"
tags: ["Ethereum", "Glamsterdam", "ETH", "gas", "EIP-8037", "wallet", "Ethereum wallet", "blockchain", "crypto"]
description: "Glamsterdam fork na Ethereumovu javnom Platåberget testnetu zakazan je za 20. kolovoza, a Ethereum Foundation upozorava developere da nove gas promjene mogu zahtijevati prilagodbu walleta, indexera i gas estimatora."
summary: "Ethereum Foundation upozorava developere da prije Glamsterdama provjere svoje wallete, indexere i gas estimatore. Fork na javnom Platåberget testnetu zakazan je za 20. kolovoza, a promjene uključuju novi način naplate stvaranja trajnog blockchain statea."
---

*Slika je simbolična.*

# Glamsterdam 20.8.: Ethereum mijenja gas pravila

Ethereum se približava sljedećoj fazi testiranja nadolazećeg Glamsterdam upgradea. Glamsterdam fork na javnom Platåberget testnetu zakazan je za 20. kolovoza 2026., a Ethereum Foundation upozorava developere da nove promjene u gas modelu mogu otkriti probleme u walletima, indexerima i alatima za procjenu gasa koji se oslanjaju na stare pretpostavke.

Platåberget je pokrenut 13. kolovoza kao dugotrajniji javni testnet na kojem developeri mogu provjeriti svoje aplikacije prije kasnijih faza testiranja i eventualne aktivacije Glamsterdama na mainnetu.

## Neki walleti i gas estimatori moraju se prilagoditi

Ethereum Foundation posebno upozorava na alate koji koriste hardkodirane pretpostavke o maksimalnom gas limitu ili načinu na koji se gas obračunava.

Promjene u Glamsterdamu zahvaćaju vrlo širok krug infrastrukture jer mogu utjecati na wallete, indexere i gas estimatore. Foundation zato poziva developere da upravo na Platåbergetu provjere koje pretpostavke u njihovom softwareu više ne vrijede prije nego što upgrade stigne na mainnet.

To upozorenje ne znači da će Ethereum walleti korisnicima 20. kolovoza odjednom prestati raditi. Datum 20.8. odnosi se na Glamsterdam fork na Platåberget testnetu, a cilj testiranja upravo je pronaći probleme prije šire implementacije.

## Ethereum uvodi novu cijenu stvaranja statea

Jedna od važnijih promjena je EIP-8037, koji povećava trošak operacija koje stvaraju novi trajni state na Ethereum mreži.

EIP uvodi trošak po novom bajtu statea i odvaja state gas od regularnog gasa. Cilj je spriječiti da povećavanje block gas limita automatski dovede do nekontroliranog rasta količine podataka koju Ethereumovi nodeovi moraju trajno čuvati.

Ethereumovi developeri navode da EIP-8037 cilja prosječni rast statea od približno 120 GiB godišnje pri referentnom block gas limitu od 150 milijuna gas jedinica.

{{< support1 >}}

## Zašto je to važno?

Ethereum već godinama pokušava povećavati kapacitet Layera 1, ali veći throughput donosi i veći pritisak na infrastrukturu.

Ako povećani gas limit omogućuje stvaranje mnogo više trajnog statea po bloku, baza podataka koju nodeovi moraju održavati može prebrzo rasti. Zato Glamsterdam ne donosi samo povećavanje kapaciteta nego i repricing operacija kako bi njihov trošak bolje odgovarao stvarnoj potrošnji resursa.

Drugim riječima: Ethereum želi omogućiti veću propusnost mreže, ali pritom pokušava spriječiti da skaliranje dugoročno napravi blockchain sve težim za održavanje.

## Glamsterdam je mnogo više od gas promjena

Promjena gas modela samo je jedan dio većeg upgradea.

Glamsterdam uključuje i enshrined proposer-builder separation, odnosno ePBS, Block-Level Access Lists te niz drugih izmjena Ethereum protokola. Ethereumovi developeri tijekom posljednjih mjeseci paralelno su testirali te promjene i radili na pripremi mreže za znatno veće gas limite.

Na interopu Ethereum core developera ranije ove godine kao vjerodostojan post-Glamsterdam cilj naveden je block gas limit od 200 milijuna, uz uvjet da optimizacije i nova pravila omoguće sigurno povećanje kapaciteta.

{{< support2 >}}

## Što to znači običnom korisniku ETH-a?

Za većinu korisnika najvažnije je da walleti, burze i aplikacije koje koriste budu ažurirani prije nego što Glamsterdam jednog dana stigne na Ethereum mainnet.

Trenutačno upozorenje prvenstveno je namijenjeno developerima. Platåberget im daje priliku da otkriju gdje software još uvijek očekuje stara gas pravila i prilagode ga prije produkcijskog upgradea.

Zato 20. kolovoza nije datum kada se svim Ethereum korisnicima mijenja mreža. To je važan datum u testiranju Glamsterdama.

## Naš osvrt

* Glamsterdam fork 20. kolovoza odnosi se na javni Platåberget testnet, ne na Ethereum mainnet.
* Ethereum Foundation otvoreno upozorava da promjene mogu otkriti probleme u walletima, indexerima i gas estimatorima koji koriste zastarjele pretpostavke.
* EIP-8037 uvodi precizniju naplatu stvaranja trajnog statea kako veći gas limit ne bi doveo do nekontroliranog rasta Ethereumove baze podataka.
* Glamsterdam je širi upgrade koji osim gas repricinga uključuje i ePBS, Block-Level Access Lists i druge promjene povezane sa skaliranjem Layera 1.
* Za obične korisnike trenutačno nema razloga za paniku — upravo zato Ethereum prvo provodi testiranje prije eventualnog mainnet upgradea.

**Disclaimer:** Članak je informativnog karaktera i ne predstavlja investicijski savjet. Glamsterdam fork 20. kolovoza 2026. odnosi se na Platåberget testnet. Datum aktivacije Glamsterdama na Ethereum mainnetu nije isto što i datum ovog testnet forka i može se odrediti zasebno tijekom daljnjeg razvojnog i testnog procesa.

*U suradnji s AI-jem.*
