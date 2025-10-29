---
title: "Globalni poremećaj: kada padnu Microsoft (Azure), Amazon (AWS), Google Cloud i Cloudflare"
slug: "globalni-cloud-outage-microsoft-azure-aws-google-cloud-cloudflare-akamai"
date: 2025-10-29T21:45:00+01:00
category: "tech"
translationKey: "f0c91c9b-72c4-4b31-b8c2-2bbf4cf44d11"
source: "Metaadvisor.eu"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/no-internet-Azure-Amazon.png"
featured_image: "/images/no-internet-Azure-Amazon.png"
image: "/images/no-internet-Azure-Amazon.png"
thumbnail: "/images/no-internet-Azure-Amazon.png"
image_alt: "Simbolična ilustracija prekida Azure i Amazon cloud servisa"
image_credit: "Ilustracija — Metaadvisor.eu"
tags: ["Microsoft","Azure","Amazon","AWS","Google Cloud","Cloudflare","Akamai","cloud","outage","internet","kolaps","otpornost","offline","business continuity","banke","plaćanja"]
summary: "Kada istovremeno padnu Microsoft Azure i Amazon AWS, milijuni servisa i aplikacija diljem svijeta prestaju raditi. U priči objašnjavamo što se danas dogodilo, kako nastaje lančana reakcija i zašto offline procedure odlučuju o tome tko nastavlja raditi."
---

<p style="text-align:center; margin:18px 0 8px 0;">
  <a href="/go/mexc" target="_blank" rel="nofollow sponsored"
     style="background:#1e40af; color:#fff; padding:12px 22px; border-radius:10px; text-decoration:none; font-weight:700; display:inline-block;">
     👉 Trguj BTC-om na MEXC
  </a>
</p>

Jutros je, gotovo neprimjetno, krenulo s nekoliko aplikacija koje „samo što nisu učitale“. Zatim su došli mailovi koji ne prolaze, web-trgovine bez košarica i backoffici koji se ne otvaraju. Ubrzo je postalo jasno: **Microsoft Azure** i **Amazon AWS** imaju ozbiljne probleme. Kada dva najveća cloud pružatelja zapnu istoga dana, to ne izgleda kao jedan kvar, već kao **kratki nestanak interneta** za ogroman dio korisnika.

Ovakvi događaji pokažu koliko je moderna svakodnevica čvrsto vezana uz tuđu infrastrukturu. Od fiskalizacije i kartičnih plaćanja do CRM-a i skladišta — sve je vani, u oblaku. Jedan timeout pretvori se u usko grlo, a to usko grlo u **lančanu reakciju**: sustavi za naplatu čekaju potvrde koje ne stižu; trgovine ostaju bez mogućnosti izdavanja računa; logistika gubi uvid u zalihe i rute. I dok korisnici vide samo „spori internet“, u pozadini se odvija borba s redovima poruka, ponovnim pokušajima i degradacijom opcija.

Danas je upravo tako izgledalo: mailovi su kasnili, prijave na servise vraćale greške, a dijelovi aplikacija prelazili u **ograničeni način rada**. Najviše su stradale one tvrtke koje **nisu imale plan B**: bez gotovine u blagajni, bez papirnatih obrazaca i bez procedura kako izdati robu i kasnije poravnati. One pripremljenije jednostavno su otvorile mapu s **offline runbookom** — izdavanje računa na papir, limit po kupcu, dnevna evidencija, zamjenski komunikacijski kanali.

U ovom trenutku vrijedi podsjetiti na naš temeljni tekst — **[“Što bi se dogodilo da u cijelom svijetu nestane internet”](/hr/news/sto-bi-se-dogodilo-da-u-cijelom-svijetu-nestane-internet)** — koji objašnjava zašto internet nije centraliziran prekidač i zašto, unatoč tome, lokalni i regionalni kolapsi mogu paralizirati život. Današnji slučaj to potvrđuje: ne treba „svjetski mrak“ da bismo osjetili posljedice; dovoljno je da **dva velika čvora** zastanu u pogrešno vrijeme.

Zašto se ovo događa? Zato što se, iz praktičnih razloga, veliki dio svijeta oslanja na **mali broj pružatelja**. Centralizacija donosi brzinu i niže troškove, ali stvara i **sistemski rizik** — jedan kvar povlači tisuće drugih. Rješenje nije u panici ni potpunom odricanju od clouda, nego u **otpornosti**: razdvojiti kritične komponente, uvesti **multi-region** i **multi-provider** gdje ima smisla, te definirati **graceful degradation** — što korisnik može raditi kad „pola sustava spava“.

**Napomena o Cloudflareu:** Cloudflare nije last-mile „provider interneta“ (ISP), nego **CDN/DNS/sigurnosna mreža** između korisnika i servera. Kad Cloudflare padne, velik broj sajtova i API-ja postaje nedostupan — što se korisnicima čini kao „internet je pao“, iako je problem u sloju iznad pristupne mreže.

Za građane, pouka je jednostavna: **gotovina i osnovne zalihe** znače slobodu izbora kad kartice ne rade. Za biznise, presudni su ljudi koji znaju „okrenuti stranicu“ na offline: koga se zove, kako izgleda papirni račun, tko čuva blagajnu, kako se sve poravnava kad se sustavi vrate.

**Naš osvrt (Metaadvisor)**  
Današnji prekid nije kraj svijeta, ali je **podsjetnik**. Što si **jednostavniji** u kritičnim trenucima, to ćeš se **brže oporaviti**. Tvrtke koje treniraju offline protokole rade i kad cloud zastane; one koje računaju na to da će „uvijek biti mreže“ — stoje u redu, zajedno sa svojim kupcima.

*Odricanje od odgovornosti: Informativni sadržaj, nije investicijski savjet. Cilj je edukacija o otpornosti i kontinuitetu poslovanja.*
