---
title: "iPhone, Zoom, IKEA, Salesforce: Hackers Exploit Optimizely"
slug: "iphone-zoom-ikea-salesforce-hackers-optimizely"
date: "2026-11-17T08:00:00+01:00"
category: "technology"
translationKey: "optimizely-hackers-zoom-ikea-salesforce-iphone-2026-11-17"
source: "Optimizely Service Status; Report URI; Reuters; StepSecurity"
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
featured_image: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
image: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
thumbnail: "/images/hack/Hackers-target-Iphone-Zoom-IKEA-Salesforce.jpg"
image_alt: "Hackers used Optimizely scripts on Zoom, IKEA and Salesforce websites to target crypto users, payment data and iPhones"
image_credit: "Metaadvisor.eu"
tags: ["Cybersecurity", "Optimizely", "Zoom", "IKEA", "Salesforce", "iPhone", "Apple", "Hacking", "Cryptocurrency", "Supply Chain Attack"]
description: "Malicious Optimizely scripts reached websites of 178 organizations, including Zoom, IKEA and Salesforce, targeting crypto wallets, payment details and iPhones."
summary: "Malicious Optimizely scripts reached websites of 178 organizations, including Zoom, IKEA and Salesforce, targeting crypto wallets, payment details and iPhones."
categories: ["technology"]
---

*The cover image is illustrative.*

**Websites associated with at least 178 organizations, including Zoom, IKEA and Salesforce, were caught up in a major hacking campaign on November 16 after attackers injected malicious JavaScript through the Optimizely platform. The code was designed to replace cryptocurrency wallet addresses, attempt to capture payment form data and target vulnerable iPhones through additional exploits. Security researchers confirmed that the malicious scripts were distributed and identified evidence of some cryptocurrency theft. The total number of affected users remains unknown, however, and there is no confirmation of widespread successful iPhone infections.**

## How did attackers reach so many major websites?

The common link was Optimizely, a platform businesses use to test and optimize website design and functionality. Such services load their own scripts in visitors' browsers. When a trusted third-party script is compromised, many unrelated websites can expose visitors to the same malicious code. Security researcher Scott Helme of Report URI said his team analyzed 1,611 Optimizely scripts and found 188 infected snippets associated with 178 organizations. That figure represents the team's confirmed findings, not necessarily the final scale of the incident.

CNN, the BBC, HSBC, Equifax, GitLab and other well-known organizations were also among those identified. There is an important distinction between a website loading a compromised script and hackers gaining full access to the company's internal systems. The findings reported so far do not prove that attackers took over those companies' customer databases, business systems or user accounts.

## What did Optimizely confirm?

In an official security notice, Optimizely confirmed that an unauthorized party exploited a vulnerability related to its Experimentation platform and added malicious JavaScript to certain customer projects. The company said it was taking steps to remove the code and secure affected systems. Security reports indicated that many of the malicious scripts identified by researchers had been removed by the evening of November 16, although investigation into the full extent of the incident was not complete.

The case illustrates a particular weakness of a *supply-chain attack*. A visitor does not need to click a suspicious link or visit a fake store. Malicious code can be delivered while browsing an otherwise legitimate website because that website relies on a compromised external service provider.

{{< support1 >}}

## Crypto addresses, card data and iPhones: one campaign

According to the researchers, the injected code performed several functions. One sought to recognize copied cryptocurrency wallet addresses and replace them with addresses controlled by the attackers. That could cause a user to send funds to the wrong recipient without noticing. Another function targeted information entered into payment forms. Investigators also observed funds reaching some addresses associated with the attack, but those observations do not establish the total financial damage.

**The attempted iPhone attacks were not a separate, unrelated story.** The analyzed code included logic to identify Apple mobile devices and their iOS versions, then attempt to launch additional exploit chains. Technical analyses identified references to Coruna and DarkSword. In other words, the same operation used different methods depending on the device or visitor. This does not mean every iPhone that opened an affected website was infected. Public evidence does not establish how many physical iPhones, if any, were successfully compromised through this campaign.

## What has been established and what remains unconfirmed?

Researchers confirmed that malicious scripts were distributed through trusted Optimizely infrastructure and that some were used by prominent websites. They also documented attempted theft techniques, including cryptocurrency address substitution. But a list of 178 organizations does not tell us how many people visited those websites during the attack, how many payment transactions were exposed or how many devices were actually compromised.

Nor should every company on the list be described as suffering the same level of breach. For each website, the relevant questions include when the infected code was loaded, how long it remained in place and which browser or website protections were effective. Further technical investigations and company disclosures will be needed to answer those questions.

{{< support2 >}}

## What should users and website operators do?

People who visited one of the named websites on November 16 should not automatically assume their information was stolen. Keeping browsers and operating systems updated is nevertheless prudent. When sending cryptocurrency, users should check the entire destination address immediately before confirming a transfer, particularly after copying and pasting it. Anyone who notices unknown card charges or suspicious transactions should contact their bank or the relevant platform promptly.

Organizations using Optimizely should review their scripts, access permissions and security logs, and follow the provider's incident guidance. Restricting which sources may load scripts, monitoring code changes and applying security updates can reduce the risk of similar incidents. These precautions do not imply that every visitor to an affected website suffered a loss.

## Our View (Metaadvisor)

* **Major brands amplified the potential reach.** Zoom, IKEA and Salesforce were among organizations with affected scripts, but that does not establish breaches of all their internal systems.
* **Optimizely was the shared route.** The attackers exploited the trust that many websites place in third-party code.
* **iPhones were part of the same campaign.** The scripts included attempted iOS exploits, but widespread successful infections have not been confirmed.
* **The crypto theft method was specific.** Replacing a recipient's wallet address can redirect funds without an obvious warning.
* **The figure of 178 refers to organizations, not individual victims.** It comes from researchers' findings about infected scripts.
* **The total impact remains unclear.** Confirmed code distribution, observed theft and unverified downstream consequences must be kept distinct.

**Follow Metaadvisor.eu for more independent news and analysis on technology, artificial intelligence, business and digital security.**

<small style="color:#757575; font-size:12px; font-weight:400; font-style:normal;">In collaboration with AI.</small>

**Disclaimer:** This article is based on Optimizely's official security notice, Report URI research and Reuters reporting available on November 17, 2026. The number of identified organizations refers to compromised scripts, not proven data theft from every organization. Attempts to exploit iPhone vulnerabilities are not proof of successful device compromise. This content is for informational purposes only and does not constitute individualized cybersecurity, legal or financial advice.
