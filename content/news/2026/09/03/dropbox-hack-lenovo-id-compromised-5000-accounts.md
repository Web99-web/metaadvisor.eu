---
title: "Dropbox Hack via Lenovo ID Compromised 5,000 Accounts"
slug: "dropbox-hack-lenovo-id-compromised-5000-accounts"
date: 2026-09-03T06:00:00+02:00
category: "Tech"
translationKey: "dropbox-lenovo-id-hack-5000-accounts-2026-09-02"
source: "Dropbox, Lenovo, Reuters, BleepingComputer"
author: "Metaadvisor.eu"
image_url: "/images/hack/Dropbox-Lenovo-hack.png"
featured_image: "/images/hack/Dropbox-Lenovo-hack.png"
image: "/images/hack/Dropbox-Lenovo-hack.png"
thumbnail: "/images/hack/Dropbox-Lenovo-hack.png"
image_alt: "Dropbox security incident in which around 5,000 user accounts were compromised through a flaw linked to the Lenovo ID integration"
image_credit: "Metaadvisor.eu"
tags: ["Dropbox", "Lenovo", "Lenovo ID", "hack", "cybersecurity", "security", "data breach", "user accounts", "cloud", "2FA", "authentication", "digital identity", "security flaw", "passwords", "data protection"]
description: "Dropbox confirmed that around 5,000 user accounts were compromised through a security flaw linked to an old Lenovo ID integration. The attackers did not even need the users’ Dropbox passwords."
summary: "Attackers exploited a weakness in Lenovo ID email verification to impersonate owners of other email addresses and access Dropbox accounts through an old integration. Files were viewed or downloaded on some accounts, while affected users did not have Dropbox 2FA enabled."
---

*Image is for illustrative purposes only.*

# Dropbox Hack: Around 5,000 Accounts Compromised Through Lenovo ID Flaw

Dropbox has confirmed a security incident in which around **5,000 user accounts were compromised** during August. On some of those accounts, attackers were able to view or download files. What makes the attack particularly notable is the method used: **the hackers did not need the users’ Dropbox passwords**.

The problem was linked to an older integration between **Lenovo ID and Dropbox**. Attackers were reportedly able to exploit a weakness in Lenovo’s email verification process and use that connection to present themselves to Dropbox as legitimate account owners.

## How Could Lenovo ID Open Someone Else’s Dropbox Account?

Dropbox previously allowed authentication through Lenovo ID. The basic idea behind such systems is simple: an external service confirms a user’s identity, and Dropbox trusts that confirmation without requiring the Dropbox password every time.

According to information released after the incident, attackers could **register a Lenovo ID using another person’s email address**. If that same email address was linked to an existing Dropbox account, the old integration could under certain conditions allow access to that account.

In other words, the attacker did not have to steal or guess the user’s password. It was enough to exploit a weakness in the way one system confirmed identity to another.

## Around 5,000 Accounts Were Compromised

Unauthorized access was recorded between **August 4 and August 21, 2026**, and Dropbox began notifying affected users after investigating the incident.

Around **5,000 accounts** were compromised. On fewer than one-third of them, attackers actually viewed or downloaded files. A compromised account therefore does not automatically mean that every file stored in Dropbox was stolen, but it does mean an unauthorized party gained access.

One particularly important detail is that the affected accounts **did not have Dropbox two-factor authentication enabled**.

{{< support1 >}}

## You Did Not Need to Own a Lenovo Laptop

The incident does not mean Lenovo laptops were hacked or that owning a Lenovo device automatically created a risk.

More importantly, a user **did not even need to already have a Lenovo ID**. That was part of the weakness: an attacker could potentially create a new Lenovo ID using the victim’s email address and then exploit the old connection with Dropbox.

This makes the incident primarily a story about **digital identity and trust between two platforms**, not about compromised Lenovo hardware.

## The Weak Link Was Not the Dropbox Password

For years, users have been told to use long and unique passwords, avoid phishing pages and never share login credentials. This incident shows that even a strong password cannot solve every security problem.

When a platform allows sign-in through another service, account security also depends partly on that external identity provider. If one provider incorrectly confirms that an attacker owns a certain email address, the mistake can carry over to another service that trusts that confirmation.

In this case, **the trust relationship between Lenovo ID and Dropbox itself became the security weakness**.

{{< support2 >}}

## Dropbox Changed the Login Process

After discovering the incident, Dropbox reset active sessions authenticated through Lenovo ID, removed existing links between Lenovo ID and Dropbox accounts and changed how the integration works.

A Lenovo ID alone should no longer be enough to access an existing Dropbox account. This login method now also requires the user’s **Dropbox password**.

Dropbox also recommended that affected users change their passwords and enable two-factor authentication.

## Why 2FA Matters Especially Here

With two-factor authentication enabled, a password or identity confirmation from another service is not enough on its own. A second verification step is required, such as a code from an authenticator app.

That is why it matters that the compromised accounts did not have Dropbox 2FA enabled. The attacker could exploit the weakness in the first layer of authentication without running into an additional security barrier.

The incident is a useful example of why 2FA matters even when a user has a strong password and never clicks on phishing links.

## Our Take

* **Around 5,000 Dropbox accounts were compromised through a flaw linked to an old Lenovo ID integration.**
* **The attackers did not need the users’ Dropbox passwords.** The key weakness was the way Lenovo ID could confirm ownership of an email address.
* **Files were viewed or downloaded on fewer than one-third of the affected accounts.**
* **Owning a Lenovo laptop did not automatically mean a user was affected**, and some victims did not even need to have had a Lenovo ID before the incident.
* **The affected Dropbox accounts did not have 2FA enabled**, once again showing the value of an additional authentication layer.
* **The broader lesson goes beyond Dropbox and Lenovo.** Old “Sign in with…” connections and external identity providers can remain part of a security chain long after users have forgotten that the connection exists.
* **Account security therefore depends on more than just a password**, including every platform that has been allowed over time to confirm our digital identity.

**Follow Metaadvisor.eu for more business & tech news, AI topics, cybersecurity, digital platforms, practical tech tips and analysis of developments affecting our digital security.**

**Disclaimer:** This article is for informational purposes only. Information about the Dropbox and Lenovo security incident is based on publicly available company statements and media reports available at the time of publication. Users who suspect unauthorized access should review active sessions and connected applications, change their password and enable two-factor authentication.

<small style="color:#999; font-size:0.8em;">In collaboration with AI.</small>
