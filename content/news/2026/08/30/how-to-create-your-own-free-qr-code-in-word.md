---
title: "How to create your own QR code for free directly in Word"
slug: "how-to-create-your-own-free-qr-code-in-word"
date: 2026-08-30T12:30:00+02:00
category: "Tech"
translationKey: "how-to-create-your-own-qr-code-in-microsoft-word-2026-08-30"
source: "Microsoft, Metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/informative/how-to-make-your-own-qr-code.png"
featured_image: "/images/informative/how-to-make-your-own-qr-code.png"
image: "/images/informative/how-to-make-your-own-qr-code.png"
thumbnail: "/images/informative/how-to-make-your-own-qr-code.png"
image_alt: "How to create your own QR code for free directly in Microsoft Word"
image_credit: "Metaadvisor.eu"
tags: ["Microsoft Word", "QR code", "create QR code", "Microsoft", "Word tips", "Word tricks", "technology", "digital tools", "DISPLAYBARCODE", "Ctrl F9", "barcode", "productivity", "Office"]
description: "Microsoft Word can create a QR code for free without additional software or an online QR generator. All you need is the built-in DISPLAYBARCODE command and a few keystrokes."
summary: "You do not need an external website to create a simple QR code. Microsoft Word includes the DISPLAYBARCODE function, which can turn links, text and other data into a QR code directly inside a document."
---

# Did you know you can create your own QR code for free directly in Microsoft Word?

You do not always need special software or an online QR generator to create a QR code. **Microsoft Word has a built-in function that can turn a web address, text or other data into a QR code directly inside a document.**

The function is called **DISPLAYBARCODE**, and once you know the command, the entire process takes only a few seconds.

It can be particularly useful for documents, offers, flyers, instructions, presentations or any other content where you want to send someone to a website with a single scan.

## How to create a QR code in Word

Open Microsoft Word and click where you want the QR code to appear in the document.

Then press:

**Ctrl + F9**

Word will insert special field brackets:

`{ }`

It is important not to type these brackets manually. Pressing **Ctrl + F9** creates a special Word field in which the command can be executed.

Inside the brackets, enter the DISPLAYBARCODE command.

For example, to create a QR code for Metaadvisor.eu:

`{ DISPLAYBARCODE "https://metaadvisor.eu" QR \s 100 }`

Then select the field and press **F9**.

Word should convert the command into a QR code. If the QR code does not appear automatically, press **F9** again, this time without Ctrl.

![How to create a QR code in Microsoft Word](/images/informative/how-to-make-qr-code1.png)

## What does DISPLAYBARCODE mean?

DISPLAYBARCODE is a Word command used to generate different types of barcodes.

In this example:

`{ DISPLAYBARCODE "https://metaadvisor.eu" QR \s 100 }`

the part:

`"https://metaadvisor.eu"`

is the content stored inside the QR code.

The element:

`QR`

tells Word to create a QR code.

The part:

`\s 100`

controls its size.

The number can be changed. A higher value creates a larger QR code, while a lower value makes it smaller.

{{< support1 >}}

## A QR code can contain more than a website link

QR codes are most commonly associated with websites, but a URL is not the only type of content they can store.

You can also put plain text directly inside a QR code.

For example:

`{ DISPLAYBARCODE "Greetings from Hamburg" QR \s 100 }`

You can also create a QR code containing a phone number:

`{ DISPLAYBARCODE "tel:+491701234567" QR \s 100 }`

Or an email address:

`{ DISPLAYBARCODE "mailto:info@example.de" QR \s 100 }`

What happens after scanning depends on the type of data stored in the code. If the QR code contains a website address, the device will usually offer to open the page. If it contains plain text, some smartphones may display the text directly, while others may automatically send it to a search engine as a search query.

## How much text can fit inside a QR code?

A QR code can contain much more data than a short URL, but as the amount of text increases, the code becomes denser.

This becomes visible very quickly in Word.

A QR code containing only a short link consists of a relatively simple black-and-white pattern. If you store several sentences instead, Word has to generate a much more complex pattern.

The result can be a QR code that takes up a large part of the page.

You can reduce its displayed size by changing the `\s` value, for example from:

`\s 100`

to:

`\s 50`

or even smaller.

However, a physically smaller QR code containing a large amount of data can become more difficult to scan, especially if it is printed in poor quality or displayed at a very small size on a screen.

For longer content, it is therefore usually more practical to store only a website URL in the QR code rather than trying to embed an entire article directly inside it.

{{< support2 >}}

## How to check whether the QR code works

The easiest test does not require any additional app.

Point your smartphone camera at the QR code.

If the QR code contains a web link, a clickable address should appear on the screen.

The example in this article leads to:

`https://metaadvisor.eu`

On some smartphones, the linked page may open only briefly after scanning, or the browser may return to a previously opened page.

If that happens, tap the newly opened page immediately after it loads or scan the QR code again. This does not necessarily mean that the QR code is faulty. It can simply be caused by the way the camera or browser handles the scan result.

## Why does a QR code have only three large squares?

At first glance, a QR code can look as though a large square is missing from the bottom-right corner.

That is normal.

A standard QR code has three large position markers:

* top left
* top right
* bottom left

A fourth large square in the bottom-right corner is not required.

These markers help the device identify the orientation of the QR code regardless of the angle from which it is scanned.

That is why a correctly generated QR code may appear to be missing one large corner square even though the pattern is exactly as intended.

## Word can replace a simple online QR generator

For more advanced QR codes, there are specialized services that offer custom colors, logos, scan tracking, dynamic links and other additional features.

But for a simple QR code that leads to a website or contains a short text, Word's built-in function may be more than enough.

Another advantage is that you do not have to enter your data on an unknown external website just to generate a QR image.

For someone already working in Word, the process can be reduced to just a few steps:

**Ctrl + F9 → DISPLAYBARCODE → F9 → QR code.**

It is one of those Word features that has been available for years but remains almost invisible until someone happens to discover the right command.

## Our take

* **The most interesting part of this feature is not the QR code itself, but the fact that you do not need an additional online service to create a basic one.**
* **A Word QR code can contain a website link, text, an email address or a phone number**, although what happens after scanning depends on how the smartphone interprets the content.
* **The more text you store inside a QR code, the denser and more complex the pattern becomes.** That is why embedding large amounts of text is not always a good idea.
* **For web articles and other longer content, it is usually better to store only the URL in the QR code.**
* **If the QR code looks as though the large bottom-right square is missing, that is normal.** Standard QR codes use three large position markers.
* **DISPLAYBARCODE is a good example of how many useful Word features remain practically hidden until someone discovers the correct command.**

**Follow Metaadvisor.eu for more practical tech tips, AI tools, digital tricks, security topics and ideas for getting more out of the software and tools you already use every day.**

**Disclaimer:** This article is for informational and educational purposes only. The availability of individual functions and the way they are displayed may depend on the Microsoft Word version, operating system and device settings. Before using a QR code in an important document, test it on several devices and make sure it leads to the intended content.

<small style="color:#999; font-size:0.8em;">In collaboration with AI.</small>
