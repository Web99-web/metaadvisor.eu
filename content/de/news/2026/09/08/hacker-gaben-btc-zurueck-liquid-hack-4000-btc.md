---
title: "Hacker gaben BTC wie versprochen zurück: Liquid-Hack mit 4.000 BTC"
slug: "hacker-gaben-btc-zurueck-liquid-hack-4000-btc"
date: 2026-09-08T10:00:00+02:00
category: "Crypto"
translationKey: "liquid-white-hat-hackers-return-bitcoin-2026-09-08"
source: "Liquid Network, Blockstream, SideSwap, Bitquery, The Block, Metaadvisor.eu"
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
featured_image: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
image: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
thumbnail: "/images/hack/Liquid-white-hats-hack-4000-BTC.png"
image_alt: "White-Hat-Hacker zogen 4.000 BTC aus dem Liquid Network ab und gaben nach dem Patch 3.400 BTC zurück"
image_credit: "Metaadvisor.eu"
tags: ["Liquid Network", "Bitcoin", "Krypto", "Hacker", "White-Hat-Hacker", "Blockstream", "SideSwap", "Elements", "Blockchain", "OP_RETURN", "Sicherheit", "Cybersicherheit", "L-BTC", "Bitcoin-Sidechain", "Krypto-Sicherheit"]
description: "Akteure, die sich selbst als White-Hat-Hacker bezeichnen, zogen fast 4.000 BTC aus dem Liquid Network ab, forderten Blockstream auf, zuerst den Bug zu beheben, und gaben nach dem Patch 3.400 BTC zurück."
summary: "Das Liquid Network verlor nach der Ausnutzung eines Bugs in Elements fast 4.000 BTC. Die Akteure versprachen über direkt in die Bitcoin-Blockchain geschriebene Nachrichten, den Großteil der Mittel nach Behebung der Schwachstelle zurückzugeben – und gaben anschließend 3.400 BTC zurück."
---

*Symbolbild.*

# "White-Hat"-Hacker zogen 4.000 BTC aus Liquid ab, forderten "Behebt zuerst den Bug" – und gaben anschließend 3.400 BTC zurück

**Einer der ungewöhnlichsten Krypto-Sicherheitsvorfälle dieses Jahres nahm eine noch ungewöhnlichere Wendung: Akteure, die sich selbst als White-Hat-Hacker bezeichnen, zogen fast 4.000 BTC im damaligen Wert von rund 320 Millionen US-Dollar aus dem Liquid Network ab, erklärten Blockstream, sie würden den Großteil zurückgeben, sobald die Schwachstelle behoben sei – und gaben anschließend tatsächlich 3.400 BTC zurück.** Noch bemerkenswerter ist, dass ein großer Teil der Verhandlungen nicht per E-Mail, Telegram oder privatem Chat stattfand, sondern über Nachrichten, die direkt in die Bitcoin-Blockchain geschrieben wurden.

Der Vorfall betraf das **Liquid Network**, eine Bitcoin-Sidechain, die auf der Open-Source-Software Elements basiert. Nach den bislang veröffentlichten Informationen entstand das Problem nicht dadurch, dass jemand private Schlüssel der Liquid Federation gestohlen oder den Peg-out Authorization Key von SideSwap kompromittiert hätte. Ein mit Elements verbundener Bug ermöglichte offenbar die Erzeugung von L-BTC ohne entsprechende reale Bitcoin-Deckung. Anschließend durchliefen diese Token den Peg-out-Prozess und die Federation zahlte echte BTC aus.

## Fast 4.000 BTC verließen das System über eine scheinbar legitime Transaktion

Der Vorfall begann am 6. September, als rund **4.000 L-BTC an den Peg-out-Service von SideSwap gesendet wurden**. SideSwap erklärte, sein System habe die Transaktion wie einen normalen Kundenauftrag verarbeitet: Die L-BTC wurden mit einer gültigen Peg-out-Autorisierung verbrannt, woraufhin die Liquid Federation ungefähr **3.996 BTC** an die Bitcoin-Adresse des Nutzers auszahlte.

SideSwap zufolge wurde der eigene PAK nicht kompromittiert. Nach den bislang verfügbaren Informationen entstand das Problem bereits zuvor in der Elements-Software, auf der Liquid läuft. Dadurch konnten L-BTC ohne reale Deckung offenbar bis zu einem Punkt gelangen, an dem sie gegen echte Bitcoin eingelöst werden konnten.

Das Federation Wallet enthielt vor dem Vorfall ungefähr **4.200 BTC**, sodass die Auszahlung rund 95 Prozent seiner Bitcoin-Reserve ausmachte. Liquid deaktivierte nach dem Vorfall die Bridge-Nodes und forderte Börsen auf, Ein- und Auszahlungen von L-BTC zu stoppen. Das Bitcoin-Mainnet selbst wurde dabei nicht kompromittiert.

## Die erste Nachricht in der Blockchain: "Wir sind White-Hat-Hacker"

Wenige Stunden nach der Auszahlung geschah etwas, das dem gesamten Vorfall eine völlig neue Richtung gab. Am **6. September um 18:30 UTC**, also gegen 20:30 Uhr mitteleuropäischer Sommerzeit, verschickte die Adresse, auf der sich fast 4.000 BTC befanden, eine neue Bitcoin-Transaktion. In deren OP_RETURN-Output befand sich eine Nachricht.

**Hexadezimaler Eintrag in der Blockchain:**

**`776520617265207768697465686174732e20636f6e74616374207573206f6e20636861696e`**

**„Wir sind White-Hat-Hacker. Kontaktiert uns on-chain.“ (englisches Original: “we are whitehats. contact us on chain”)**

Dabei ist wichtig zu verstehen, wie jemand diese Nachricht unter Millionen von Bitcoin-Transaktionen überhaupt bemerkte. Niemand durchsuchte die gesamte Blockchain nach interessanten Sätzen. Nachdem fast 4.000 BTC abgezogen worden waren, stand die Adresse, auf der die Mittel gelandet waren, bereits unter intensiver Beobachtung von Blockstream, Sicherheitsteams und Blockchain-Analysten. Jede neue Transaktion dieser Adresse konnte automatisiert einen Alarm auslösen.

Ein OP_RETURN-Output lässt sich zudem leicht erkennen, weil er in Bitcoin-Skripten einen eigenen Opcode besitzt. Erkennt ein Analysewerkzeug oder Block Explorer darin Daten, die sich als Text dekodieren lassen, kann der hexadezimale Eintrag unmittelbar in eine lesbare Nachricht umgewandelt werden. Die Hacker warfen ihre Nachricht also nicht in einen unüberschaubaren Ozean von Blockchain-Daten und hofften, dass sie zufällig jemand findet. Sie sendeten sie genau von jener Adresse, die ohnehin bereits alle beobachteten.

Dadurch wird ihre Formulierung **„contact us on chain“** noch interessanter. Sinngemäß sagten sie damit: **„Wir wissen, dass ihr dieses Wallet beobachtet – meldet euch hier bei uns.“**

Der Hex-Code ist die tatsächliche computergestützte Darstellung des Satzes. In der Bitcoin-Blockchain werden Buchstaben nicht als direkt vom Menschen lesbarer Text gespeichert, sondern als Bytes, die beispielsweise hexadezimal dargestellt werden können. `77` steht etwa für den Buchstaben `w`, `65` für `e`, sodass der Beginn `7765` nach der Dekodierung das Wort `we` ergibt.

Ein Bitcoin Block Explorer kann diesen hexadezimalen Inhalt automatisch wieder in eine lesbare Zeichenfolge umwandeln. Wer die entsprechende Transaktion öffnet, kann daher die OP_RETURN-Daten und die von den Akteuren hinterlassene Nachricht lesen.

Noch ungewöhnlicher: Es handelte sich nicht einfach um einen Kommentar, der irgendwo neben der Transaktion gespeichert wurde. **Die Nachricht selbst wurde Teil des dauerhaften Datensatzes der Bitcoin-Blockchain.**

{{< support1 >}}

## Blockstream antwortet – ebenfalls über Bitcoin

Blockstream akzeptierte diese Art der Kommunikation. Etwa eine Stunde später, am **6. September um 19:31 UTC**, wurde von einer mit Blockstream verbundenen Adresse eine neue Bitcoin-Transaktion mit einer OP_RETURN-Nachricht gesendet.

**Hexadezimaler Eintrag in der Blockchain:**

**`506c6561736520636f6e7461637420736563757269747940626c6f636b73747265616d2e636f6d`**

**„Bitte kontaktiert security@blockstream.com.“ (englisches Original: “Please contact security@blockstream.com”)**

Damit antwortete auch Blockstream auf dieselbe Weise – mit einer innerhalb einer Bitcoin-Transaktion gespeicherten Nachricht. Statt die Kommunikation sofort auf E-Mail oder eine private Plattform zu verlagern, blieb die erste Antwort dauerhaft in der Blockchain erhalten.

Später schickte Blockstream auch eine PGP-signierte und verschlüsselte Nachricht. Die Signatur konnte anhand des öffentlich veröffentlichten Sicherheitsschlüssels von Blockstream überprüft werden, womit sich bestätigen ließ, dass die Nachricht tatsächlich von der Sicherheitsseite Blockstreams stammte.

Doch die White-Hat-Seite setzte das Gespräch on-chain fort.

## "Wir senden den Großteil zurück – ist das die richtige Adresse?"

Am **7. September um 02:20 UTC**, also gegen 04:20 Uhr mitteleuropäischer Sommerzeit, verschickten die Akteure eine weitere Transaktion. Diesmal enthielt die Nachricht auch die vollständige Adresse des Liquid Federation Wallets, an das sie die Bitcoin zurückschicken wollten.

**Hexadezimaler Eintrag in der Blockchain:**

**`73656e64696e67206d6f7374206261636b20746f2062633171646c6c6436616e746d76347875673234326564383371376b3472717735306377666e733338737a783471753266346a77617878737568777878722c2069732074686174206f6b`**

**„Wir senden den Großteil zurück an bc1qdlld6antmv4xug242ed83q7k4rqw50cwfns38szx4qu2f4jwaxxsuhwxxr, ist das in Ordnung?“ (englisches Original: “sending most back to bc1qdlld6antmv4xug242ed83q7k4rqw50cwfns38szx4qu2f4jwaxxsuhwxxr, is that ok”)**

Dies war möglicherweise der erste Moment, in dem deutlich wurde, dass ihre ursprüngliche Behauptung, White-Hat-Hacker zu sein, womöglich nicht nur ein Versuch war, Zeit zu gewinnen. **Sie sagten nicht lediglich, dass sie das Geld zurückgeben würden – sie nannten die Adresse, an die sie den Großteil der fast 4.000 BTC zurückschicken wollten, und fragten Blockstream, ob sie korrekt sei.**

Blockstream antwortete **“Yes, thank you.”**, also **„Ja, danke.“**

Vor der eigentlichen Rückzahlung folgte jedoch eine noch wichtigere Nachricht.

## "Behebt zuerst den Bug"

Am **7. September um 03:30 UTC**, also gegen 05:30 Uhr mitteleuropäischer Sommerzeit, schickte die White-Hat-Seite eine dritte öffentlich lesbare Nachricht. Sie erklärte praktisch, warum die Bitcoin noch nicht sofort zurückgeschickt würden.

**Hexadezimaler Eintrag des öffentlich lesbaren Teils der Nachricht in der Blockchain:**

**`506c656173652066697820746865206275672066697273742e2054686520636861696e20697320756e646572207269736b206174206c617465737420636f6d6d6974207269676874206e6f772e204d616b652073757265206576657279206e6f646520697320706174636865642e205468656e2077652077696c6c207472616e7366657220746865206d6f6e6579206261636b20736166656c7920616674657220636f6e6669726d696e6720746865206669782e`**

**„Bitte behebt zuerst den Bug. Die Chain ist im aktuellen Stand des neuesten Commits derzeit gefährdet. Stellt sicher, dass jeder Node gepatcht ist. Nachdem wir den Fix bestätigt haben, werden wir das Geld sicher zurücküberweisen.“ (englisches Original: “Please fix the bug first. The chain is under risk at latest commit right now. Make sure every node is patched. Then we will transfer the money back safely after confirming the fix.”)**

Nach diesem öffentlich lesbaren Text folgte im selben OP_RETURN-Eintrag auch ein **PGP-verschlüsselter technischer Teil**, der für Blockstream bestimmt war. Die Öffentlichkeit konnte die verschlüsselten Daten sehen, ihren Inhalt jedoch ohne den privaten Schlüssel nicht lesen. Nach Angaben von Forschern, die die Blockchain analysierten, enthielt dieser Abschnitt technische Informationen über die Schwachstelle.

Die Botschaft war eindeutig: **Bestätigt nicht einfach nur die Adresse und nehmt die Bitcoin zurück – stellt zuerst sicher, dass dieselbe Schwachstelle nicht weiterhin existiert.**

{{< support2 >}}

## Blockstream meldet, dass die Bridge-Nodes gepatcht sind

Nach der Arbeit an dem Sicherheitsproblem schickte Blockstream eine signierte On-Chain-Nachricht und bestätigte, dass das Problem an den Bridge-Nodes behoben worden sei.

**Hexadezimaler Eintrag in der Blockchain:**

**`427269646765206e6f6465732061726520706174636865642c207361666520746f2072657475726e207468652066756e64732e`**

**„Die Bridge-Nodes sind gepatcht. Die Mittel können nun sicher zurückgegeben werden.“ (englisches Original: “Bridge nodes are patched, safe to return the funds.”)**

Damit war die Bedingung erfüllt, die die Akteure wenige Stunden zuvor in die Bitcoin-Blockchain geschrieben hatten.

Und dann kam die entscheidende Wendung: **Sie hielten sich an das, was sie geschrieben hatten.**

Am **7. September um 16:09 UTC**, also gegen 18:09 Uhr mitteleuropäischer Sommerzeit, wurde in Bitcoin-Block 965.950 eine Transaktion bestätigt, mit der **exakt 3.400 BTC an die Adresse der Liquid Federation zurückgeschickt wurden**.

## Sie versprachen, den Großteil zurückzugeben – und gaben 3.400 BTC zurück

Die Rückzahlung ist vor allem wegen der Abfolge der Ereignisse bemerkenswert. Die Akteure erklärten zunächst, sie seien White-Hat-Hacker, fragten anschließend öffentlich, ob die Federation-Adresse die richtige Adresse für die Rückzahlung des Großteils der Mittel sei, und weigerten sich danach, die BTC sofort zu senden, solange die Schwachstelle nicht behoben war.

Blockstream bestätigte schließlich, dass die Bridge-Nodes gepatcht seien. Danach folgte die Transaktion über **3.400 BTC**.

Mit anderen Worten: Der entscheidende Satz dieser Geschichte – **„Nachdem wir den Fix bestätigt haben, werden wir das Geld sicher zurücküberweisen“** – blieb nicht nur eine Nachricht in der Blockchain. Nach Bestätigung des Fixes gaben die Akteure rund 85 Prozent der Mittel tatsächlich zurück.

Auf ihrer Adresse verblieben allerdings rund **598,5 BTC**, die damals ungefähr 47 Millionen US-Dollar wert waren.

## Rund 600 BTC wurden nicht zurückgegeben

Der Status der verbleibenden fast 600 BTC ist weiterhin offen. Es wurde spekuliert, dass es sich dabei um eine Art Bug Bounty handeln könnte, also eine Belohnung für das Auffinden einer kritischen Schwachstelle. Es gibt jedoch keine öffentlich bestätigte Vereinbarung, wonach Blockstream einem Bounty in dieser Größenordnung zugestimmt hätte.

Die fast 600 BTC entsprechen ungefähr 15 Prozent des Gesamtbetrags, der nach dem Vorfall unter Kontrolle der Akteure verblieben war. Deshalb wäre es nicht korrekt zu sagen, sämtliche Bitcoin seien zurückgegeben worden.

Präziser ist: Sie **versprachen, den „Großteil“ zurückzugeben – und genau den Großteil gaben sie zurück**.

Selbst das Wort **“most”** aus ihrer zweiten On-Chain-Nachricht wurde damit im Nachhinein bedeutsam. Sie schrieben nicht, dass sie alles zurückgeben würden. Sie schrieben **“sending most back”** – wir senden den Großteil zurück.

## Waren es wirklich White-Hat-Hacker?

Dass sie sich selbst als White-Hat-Hacker bezeichneten, bedeutet nicht automatisch, dass sie rechtlich oder sicherheitstechnisch auch so eingestuft werden können. Es gibt keine öffentlichen Informationen darüber, dass sie vor Ausnutzung der Schwachstelle eine Erlaubnis von Blockstream oder der Liquid Federation hatten, das System auf diese Weise zu testen.

Ein typischer White-Hat-Prozess würde darin bestehen, eine Schwachstelle zu entdecken und sie über einen Security-Disclosure- oder Bug-Bounty-Prozess an das Unternehmen zu melden – und nicht zunächst die Kontrolle über fast 320 Millionen US-Dollar zu übernehmen.

Andererseits entsprach auch ihr Verhalten nach dem Exploit nicht dem typischen Muster eines Krypto-Diebstahls. Sie versuchten nicht sofort, die Mittel über zahlreiche Wallets oder andere Netzwerke zu verschleiern. Sie blieben auf der Blockchain sichtbar, nahmen öffentlich Kontakt mit Blockstream auf, übermittelten technische Informationen, verlangten einen Patch und gaben anschließend 3.400 BTC zurück.

Gerade deshalb bleibt der Vorfall so ungewöhnlich. **Sie selbst bezeichneten sich als White-Hat-Hacker, doch ihre endgültige Einordnung dürfte auch davon abhängen, was mit den verbleibenden 598,5 BTC geschieht.**

## Wie sieht ein Gespräch auf der Bitcoin-Blockchain überhaupt aus?

Bitcoin ist keine Chat-App, doch OP_RETURN ermöglicht es, eine kleine Menge beliebiger Daten in einer Transaktion zu speichern. Sobald die Transaktion bestätigt ist, werden diese Daten Teil der Blockchain.

Was ein Nutzer in einem Explorer als

**“we are whitehats. contact us on chain”**

sieht, erscheint in hexadezimaler Darstellung so:

**`776520617265207768697465686174732e20636f6e74616374207573206f6e20636861696e`**

Der Explorer nimmt die gespeicherten Bytes und dekodiert sie, sofern sie Text darstellen, wieder in für Menschen lesbare Zeichen.

Noch wichtiger ist, dass jede solche Nachricht innerhalb einer **echten Bitcoin-Transaktion** übermittelt wird. In diesem Fall war die Adresse, die die White-Hat-Nachrichten versendete, genau jene Adresse, die die abgezogenen Bitcoin kontrollierte. Die Blockchain beweist damit nicht, wer die Personen hinter dem Wallet sind, aber sie bestätigt, dass die Nachrichten von jemandem gesendet wurden, der Transaktionen aus dem Wallet mit den Mitteln signieren konnte.

Deshalb ist dieses Gespräch weit mehr als nur ein Screenshot oder ein anonymer Beitrag im Internet.

## Die Verhandlungen über 320 Millionen US-Dollar fanden öffentlich statt

Der vielleicht interessanteste Teil des Vorfalls ist nicht einmal der Exploit selbst, sondern die Art und Weise, wie das Problem anschließend gelöst wurde. Die White-Hat-Seite und Blockstream führten einen Teil ihrer Verhandlungen über Bitcoin im Wert von Hunderten Millionen US-Dollar praktisch vor den Augen der ganzen Welt.

Die Nachrichten, ihre Zeitstempel und die Adressen, von denen sie gesendet wurden, blieben in der Blockchain gespeichert. Die Öffentlichkeit konnte verfolgen, wie die Akteure zunächst Kontakt suchten, dann die Rückgabe des Großteils der Mittel ankündigten, anschließend die Behebung der Schwachstelle verlangten und schließlich tatsächlich 3.400 BTC zurückgaben.

Es gab also keinen klassischen privaten Verhandlungskanal, dessen Inhalt der Öffentlichkeit erst später nacherzählt wurde. **Die wichtigsten Teile des Gesprächs waren direkt in Bitcoin selbst gespeichert.**

## Was ist das Liquid Network und warum war der Bug so gefährlich?

Liquid ist eine von **Blockstream** entwickelte Bitcoin-Sidechain, die für schnellere Bitcoin-Transfers und die Ausgabe verschiedener digitaler Vermögenswerte genutzt wird. L-BTC sollte dabei durch echte Bitcoin gedeckt sein, die im Federation-System gesperrt werden.

Ein Nutzer kann BTC sperren und dafür entsprechende L-BTC im Liquid Network erhalten. Will er zurück ins Bitcoin-Mainnet wechseln, werden die L-BTC über den Peg-out-Prozess aus dem Umlauf genommen und das Federation-System gibt die entsprechenden echten Bitcoin frei.

Genau deshalb war dieser Bug so kritisch. Wenn L-BTC erzeugt werden können, die nicht tatsächlich durch Bitcoin gedeckt sind, und diese anschließend über einen regulären Peg-out gegen echte BTC eingelöst werden können, ist eine grundlegende Annahme des Systems gefährdet.

SideSwap erklärt, dass weder die eigenen Systeme noch der PAK kompromittiert worden seien. Nach Angaben des Unternehmens lag die Ursache des Problems in einem Bug in **Elements**, der Open-Source-Software, auf der Liquid basiert.

## Das Bitcoin-Mainnet wurde nicht gehackt

Bei dem Vorfall handelte es sich nicht um einen Hack von Bitcoin selbst. Weder der Bitcoin-Konsens noch Bitcoin-Nodes oder private Wallets von Nutzern wurden kompromittiert.

Das Problem entstand auf der Liquid-Sidechain und in deren Mechanismus für die Ausgabe und Rückgabe von L-BTC. Das Bitcoin-Mainnet führte lediglich gültig signierte Transaktionen aus, die ihm übermittelt wurden.

Ironischerweise wurde ausgerechnet die Bitcoin-Blockchain anschließend zum **öffentlichen Protokoll der Problemlösung**. In ihr blieben die Nachrichten der Hacker, die Antworten Blockstreams und schließlich die Transaktion gespeichert, mit der 3.400 BTC zurückgegeben wurden.

## Unsere Einschätzung

* **Akteure, die sich selbst als White-Hat-Hacker bezeichnen, nutzten eine mit Elements verbundene Schwachstelle aus und zogen rund 4.000 BTC aus dem Liquid-System ab.**
* Am **6. September um 18:30 UTC** schrieben sie eine Nachricht in die Blockchain, deren hexadezimaler Eintrag mit **`776520...`** beginnt und nach der Dekodierung lautet: **„Wir sind White-Hat-Hacker. Kontaktiert uns on-chain.“**
* Am **7. September um 02:20 UTC** erklärten sie über eine weitere Bitcoin-Transaktion, sie würden **den Großteil der Mittel zurückgeben**, und fragten Blockstream, ob die Federation-Adresse korrekt sei.
* Etwas mehr als eine Stunde später folgte die entscheidende Nachricht: **„Bitte behebt zuerst den Bug.“** Sie verlangten, dass sämtliche Nodes gepatcht werden, bevor sie die Bitcoin zurückgeben.
* Die öffentlich lesbaren Teile aller drei Nachrichten können aus den Raw-Blockchain-Daten als **hexadezimale Zeichenfolgen** dargestellt werden, während Block Explorer sie in normalen Text dekodieren können.
* Blockstream erklärte nach dem Patch, die Mittel könnten sicher zurückgegeben werden.
* Am **7. September um 16:09 UTC** gaben die Akteure **3.400 BTC** zurück, nachdem die von ihnen gestellte Bedingung erfüllt worden war.
* Auf ihrer Adresse verblieben rund **598,5 BTC**, ohne dass öffentlich bestätigt worden wäre, dass dieser Betrag als Bug Bounty vereinbart wurde.
* Das Bitcoin-Mainnet selbst **wurde nicht gehackt**; das Problem betraf Liquid und Elements.
* Der ungewöhnlichste Aspekt des gesamten Vorfalls bleibt, dass die **Verhandlungen über Bitcoin im Wert von rund 320 Millionen US-Dollar teilweise öffentlich über dauerhaft in der Bitcoin-Blockchain gespeicherte Nachrichten geführt wurden**.
* Sie erklärten, den Großteil der Mittel nach Behebung des Bugs zurückzugeben – und **bei 3.400 BTC hielten sie ihr Wort**.

**Folgen Sie Metaadvisor.eu für weitere Nachrichten über Krypto, Bitcoin, Blockchain, Cybersicherheit, digitale Vermögenswerte, Technologie und Finanzmärkte.**

**Disclaimer:** Dieser Artikel dient ausschließlich Informationszwecken und stellt keine Finanz-, Anlage-, Rechts-, Steuer- oder Sicherheitsberatung und keine Empfehlung zur Nutzung eines bestimmten Krypto-Netzwerks, einer Plattform oder eines Dienstes dar. Informationen zu Sicherheitsvorfällen können sich ändern, sobald neue technische Erkenntnisse und Untersuchungsergebnisse veröffentlicht werden. Führen Sie vor finanziellen Entscheidungen Ihre eigene Recherche durch und prüfen Sie aktuelle Informationen bei offiziellen Quellen.

<small style="color:#999; font-size:0.8em;">In Zusammenarbeit mit KI.</small>
