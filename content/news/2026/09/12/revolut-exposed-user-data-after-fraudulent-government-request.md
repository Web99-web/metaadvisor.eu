---
title: "Revolut Exposed User Data After Fraudulent Government Request"
slug: "revolut-exposed-user-data-after-fraudulent-government-request"
date: 2026-09-12T18:00:00+02:00
category: "Cybersecurity"
translationKey: "revolut-exposed-user-data-after-fraudulent-government-request-2026-09-12"
source: "Revolut, Reuters, TechCrunch, ZachXBT, Metaadvisor.eu"
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/hack/Revolut-sent-user-data-to-scammers.jpg"
featured_image: "/images/hack/Revolut-sent-user-data-to-scammers.jpg"
image: "/images/hack/Revolut-sent-user-data-to-scammers.jpg"
thumbnail: "/images/hack/Revolut-sent-user-data-to-scammers.jpg"
image_alt: "Revolut handed over sensitive user data after a fraudulent request sent through the official domain of a government agency"
image_credit: "Metaadvisor.eu / AI"
tags: ["Revolut", "cybersecurity", "data breach", "personal data", "privacy", "identity theft", "phishing", "social engineering", "fintech", "banking", "cryptocurrency", "Bitcoin", "data protection", "online scams"]
description: "Revolut confirmed that it handed sensitive data belonging to some users to an unauthorized third party after fraudulent requests were sent through the official email domain of a real government agency."
summary: "Revolut was not hacked in the conventional sense. The company itself handed over sensitive data belonging to a limited number of users after trusting requests that appeared to be legitimate government inquiries. The identity of the agency and the country it belongs to remain unknown."
---

*Image is symbolic.*

# Revolut exposed customer data after trusting a fake government request

**Revolut has confirmed a serious security incident in which sensitive personal and financial data belonging to some customers ended up in the hands of an unauthorized third party. But this was not a conventional hack of Revolut's systems. The company handed over the data itself after trusting requests that appeared to be legitimate government inquiries and were sent through the official email domain of a real government agency.**

The incident is particularly troubling because it shows how little even strong technical security at a financial platform can achieve if an attacker successfully exploits a communication channel the institution already trusts. Revolut says only a limited number of customers were affected and that those users were contacted directly.

## Revolut was not hacked – it was deceived

According to information disclosed so far, the attackers did not break into Revolut's database or compromise its banking systems. Instead, they submitted requests for customer information that appeared to be official requests from a government institution.

Revolut concluded that the requests were legitimate and provided the requested information. Only after additional verification did the company discover that the person or account from which the requests had been sent was not authorized to make them.

After discovering the incident, Revolut blocked the address in question and said it notified the affected government agency, law enforcement authorities, the relevant data protection regulator and other competent authorities.

## The message came from a real government domain

The most striking part of the case is that the request did not come from an obviously fake address merely designed to resemble a government institution. Revolut confirmed that an unauthorized third party used the legitimate email domain of a real government agency.

That is precisely what made the fraud so convincing. When a message passes through the genuine infrastructure of a government institution, standard authentication checks can indicate that everything is technically valid even though the person sending the message has no authority to make the request.

This could happen if an attacker compromises an existing government account, gains access to an email system or otherwise obtains the ability to send messages through the legitimate domain. Revolut has not disclosed exactly how the attacker achieved this access.

In other words, a system may be able to confirm that a message really came through a particular domain. That does not automatically prove that the person behind it is an authorized government official.

{{< support1 >}}

## What data ended up with the attackers?

According to notifications received by affected customers, the exposed information may have included names, dates of birth, home addresses, email addresses, telephone numbers and other information linked to Revolut accounts.

Even more serious were the documents used for identity verification. The data handed over may have included copies of passports and driving licences, as well as facial photographs submitted during the customer verification process.

For some customers, the disclosed information may also have included bank statements, IBANs, account status, account opening dates, payout information and transaction histories. In some cases, this reportedly included information about Bitcoin transactions.

This combination of information is particularly sensitive because it allows an attacker to build an extremely detailed profile of an individual. Connecting a person's identity, address, telephone number, photograph, identification document and financial history can be highly valuable for targeted fraud, identity theft or attempts to take over other accounts.

## The government agency is still unknown

Revolut has not disclosed the name of the government agency whose domain was used, and the country to which the agency belongs is also unknown. The company has not revealed exactly how many users were affected or whether they were all located in the same country.

That leaves an especially important question unanswered: did the attackers request data only about customers from the country to which the compromised agency belongs, or were specific individuals targeted regardless of where they lived?

Revolut has also not answered whether the incident was limited to a single market. As a result, it is currently impossible to determine whether affected customers came from one country or several.

Crypto investigator ZachXBT said that, based on the available information, the incident appeared to be relatively limited and that high-net-worth users may have been targeted. Revolut has not officially confirmed that claim, so it should currently be treated as an assessment rather than an established fact.

{{< support2 >}}

## Were all Revolut customers affected?

No. Revolut says only a limited number of customers were affected and that the identified individuals were contacted directly. That means a Revolut customer who has not received a security notification currently has no specific reason to believe that their data was among the information handed over in this particular incident. However, this should not be interpreted as an absolute guarantee; it is a conclusion based on what Revolut has disclosed so far.

Affected customers began receiving warnings on September 11, while the incident became publicly known more widely on September 12 following posts from users and subsequent confirmation by Revolut.

Among the customers who publicly confirmed receiving such a warning was **Mark Karpelès, the former CEO of the collapsed cryptocurrency exchange Mt. Gox**. Karpelès said he received a Revolut message titled “Urgent security update about your Revolut account” on September 11 at 21:59 UTC. After he publicly shared parts of the notification, the case attracted considerably wider attention. Karpelès also argued that Revolut or the affected government agency should disclose which institution was involved so that other banks and cryptocurrency exchanges can check whether they may also have received requests from the same compromised address.

The exact date on which the fraudulent requests were sent to Revolut, and when the company actually handed over the data, has not yet been made public.

## How could a fraudulent request pass the checks?

The case highlights an important difference between verifying an email domain and verifying the person actually making a request.

Technologies such as SPF, DKIM and DMARC can help determine whether an email was sent through infrastructure authorized to send messages on behalf of a particular domain. This is useful protection against conventional spoofing, but it is not enough if an attacker has already gained access to a legitimate account or system.

In that situation, a message can look completely authentic. It can come from the correct domain, pass technical authentication checks and reach an employee who initially has no obvious reason to suspect that the sender is unauthorized.

That is why requests involving passports, bank statements and complete transaction histories would normally be expected to undergo additional verification. This could include checking a case number, confirming the identity of the official, verifying the legal basis for the request and obtaining confirmation through an independent communication channel.

And this raises an uncomfortable question for Revolut. If the company was able to contact the government agency after the incident and establish that the request had not been legitimately sent, why was that independent verification not carried out before the data was handed over?

## The attacker did not need to break into the bank

In this case, the attacker did not need to find a vulnerability in Revolut's app, break encryption or compromise the customer database. The attacker only needed to convince Revolut that they had the right to request the information. And they succeeded.

That may be the most important lesson from the entire incident. Financial institutions can spend enormous sums protecting their own infrastructure while simultaneously communicating every day with police, regulators, courts and other government bodies.

If an attacker compromises one of those external institutions, they can try to exploit the existing relationship of trust as an entry point. In such a scenario, the weakest link is not necessarily the bank itself, but the institution the bank trusts.

## Our take

* **This was not a conventional hack of Revolut. The company itself handed over data after trusting fraudulent requests sent through the official domain of a real government agency.**
* Revolut says its systems and customer funds were not affected.
* **Compromised information may have included addresses, telephone numbers, identity documents, verification photographs, bank statements and transaction histories.**
* Only a limited number of users were affected, according to Revolut, and the identified customers were contacted directly.
* **The identity of the compromised government agency and the country it belongs to remain unknown.**
* Revolut has also not disclosed whether all affected users came from the same country or whether several markets were involved.
* **Mark Karpelès, the former CEO of Mt. Gox, publicly confirmed receiving Revolut's warning and argued that the agency should be identified so other financial institutions can check whether they received similar requests.**
* **The biggest problem is not merely that the attacker sent a convincing email, but that the request was accepted far enough for real customer data to be handed over before the sender was found to be unauthorized.**
* The incident shows that technical authentication of an email domain is not sufficient when passports, personal information and complete financial histories are being disclosed.

**Follow Metaadvisor.eu for more news and analysis on cybersecurity, privacy, fintech, online fraud, personal data protection and the security of digital financial services.**

**Disclaimer:** This article is for informational purposes only and is based on publicly available information, statements from Revolut and media reports available as of September 12, 2026. The identity of the government agency, the country to which it belongs, the exact number of affected users and the full technical details of the incident had not been publicly confirmed at the time of publication. This article does not constitute legal, financial, security or investment advice.

<small style="color:#999; font-size:0.8em;">In collaboration with AI.</small>
