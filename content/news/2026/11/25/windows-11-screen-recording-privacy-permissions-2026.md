---
title: "Windows 11: Who Can Record Your Screen?"
slug: "windows-11-screen-recording-privacy-permissions-2026"
date: "2026-11-25T00:05:00+01:00"
category: "technology"
translationKey: "windows-11-screen-recording-privacy-permissions-2026-11-25"
source: "MetaAdvisor: own testing and documented screenshots, November 23, 2026."
source_url: ""
author: "Metaadvisor.eu"
image_url: "/images/AI-general/Windows-11-Screen-Recording-Explained.jpg"
featured_image: "/images/AI-general/Windows-11-Screen-Recording-Explained.jpg"
image: "/images/AI-general/Windows-11-Screen-Recording-Explained.jpg"
thumbnail: "/images/AI-general/Windows-11-Screen-Recording-Explained.jpg"
image_alt: "Windows 11 on a laptop with an illustration of screen recording and app permissions"
image_credit: "Metaadvisor.eu"
tags: ["Windows 11","Microsoft","AI","Privacy","Cybersecurity","Screen Recording","Microsoft Recall","App Permissions"]
description: "We found four categories of permissions enabled on a Windows 11 computer. Here are the results of our own testing and instructions for disabling them."
summary: "Screen recording, removal of capture borders, AI content generation and editing text in an active field. We tested what happens when these permissions are disabled."
categories: ["technology"]
---

*The cover image is illustrative.*

**Screen recording, removal of visible recording warnings, AI content generation and even modification of text in an active text field. We found all four categories of permissions enabled on a Windows 11 computer, although its owner does not recall approving them or receiving an explanation of what these permissions allow apps to do.**

What we found raised a number of questions about security, privacy, user awareness and the consumption of computing resources.

Imagine a software developer working for a bank or a company that develops blockchain technology, manages cryptocurrencies or builds artificial intelligence systems.

Their screen may display confidential source code, API keys, private keys for crypto wallets, customer data, trade secrets or information about the company's security infrastructure.

The same applies to law firms, healthcare institutions, government agencies and ordinary users accessing their bank accounts and personal documents on their computers.

How many of them know which app permissions are enabled on their computers?

## Four categories of enabled permissions

Under Settings > Privacy & security, we found four categories of enabled permissions:

- **Screenshots and screen recording:** capturing the screen.
- **Screenshot borders:** allowing apps to remove the visible border during screen capture.
- **Text and image generation:** access to AI-powered text and image generation features.
- **Foreground text access:** access to modify text in the active text field.

These are separate operating system permissions, independent of Microsoft's Recall feature.

## Screen recording without a visible warning

One of the more interesting settings is Screenshot borders. It allows apps to remove the visible border associated with certain screen capture methods.

On the computer we tested, Microsoft Teams had permission to capture the screen and remove the border. Access was also enabled for desktop apps through the corresponding Windows settings.

Although having permission does not mean an app is actually recording the screen, it raises the question of how many users are aware that such a capability exists.

Why was the option to remove the visible warning during screen capture enabled on our computer when its owner does not recall approving it? The settings alone did not allow us to establish when or how these permissions were enabled.

## Artificial intelligence in everyday applications

Under Text and image generation, we found eight apps with access to text and image generation features:

- Snipping Tool
- Notepad
- Paint
- Photos
- Local AI Manager for Microsoft 365
- Microsoft Clipchamp
- Outlook
- Xbox

The tested computer showed no recorded requests to use these features during the previous seven days.

Microsoft is increasingly integrating artificial intelligence into everyday applications. However, a user who simply wants to write something in Notepad, view a photo or capture part of the screen may not want to use AI features at all.

{{< support1 >}}

## Apps can modify text in the active window

The Foreground text access setting particularly caught our attention.

According to the description in Windows, this setting allows apps to access and modify text in the currently focused text field.

Such features can be useful for AI assistants, automated text editing and accessibility tools. Nevertheless, this is an additional permission whose security implications users should understand.

This setting was also enabled on the tested computer, although no individual apps were displayed in the list.

## Potential security risks

Every unnecessary permission can create an additional attack surface if an app is compromised or its capabilities are abused.

For technology and financial companies, the consequences of potential misuse can be considerably more serious than a breach of an individual's privacy.

We are not necessarily referring to Microsoft as the source of a threat, but rather to the security implications of the access an operating system grants to apps.

The existence of a permission is not evidence that it has been abused, but it is certainly a reason to check whether such access is needed at all.

## Who decides how computing resources are used?

Privacy is not the only question raised by the increasing integration of artificial intelligence into operating systems.

Active AI features, background processes and local models can use:

- Random access memory (RAM)
- Central processing unit (CPU)
- Graphics processing unit (GPU)
- Neural processing unit (NPU)
- Disk space
- Electricity and battery power

An enabled permission does not automatically mean these resources are being consumed, and we did not measure actual resource usage during this test. Disabling permissions does not necessarily stop background processes or remove installed AI models either.

However, users should be able to decide which features they want to use and which activities take place on their computers.

Why should someone who has purchased a computer subsequently have to investigate which features they need and which they can turn off?

## We disabled all four permissions. What happened?

During our own testing on November 23, 2026, we disabled all four categories of permissions.

| Setting | Before testing | After testing |
|---|---|---|
| Screenshots and screen recording | ON | OFF |
| Screenshot borders | ON | OFF |
| Text and image generation | ON | OFF |
| Foreground text access | ON | OFF |

After disabling the permissions, we could still manually capture the screen, write messages and send text and photos.

We observed no loss of basic functionality during the activities tested.

We documented every change with screenshots taken before and after disabling the individual permissions.

These results apply to one tested computer. Disabling these settings does not guarantee protection against every screen capture method, and some specialised app features may become unavailable.

{{< support2 >}}

## How to check your own computer

Open Windows Settings by pressing **Windows + I**.

Select **Settings → Privacy & security**.

Scroll down to the app permissions section. Setting names and availability may vary depending on your version of Windows.

### 1. Screenshots and screen recording

**Settings → Privacy & security → Screenshots and screen recording**

- **Screenshots and screen recording access → Off**, if you want to restrict screen capture access through this permission system.
- **Recent activity:** check the recorded screen capture requests for the previous seven days.

The tested computer showed zero recorded requests. This is not a comprehensive record of every possible screen capture method.

### 2. Screenshot borders

**Settings → Privacy & security → Screenshot borders**

- **Screenshot border settings access → Off**

This restricts the ability of apps to remove the visible border during screen capture through this Windows permission system.

After disabling the first two settings, you can check whether manual screenshots still work by pressing **Windows + Shift + S**.

### 3. Text and image generation

**Settings → Privacy & security → Text and image generation**

- **Text and image generation → Off**
- **Recent activity:** check which apps requested access to these features during the previous seven days.

Disabling this setting restricts access to certain Windows AI features. It does not mean that all AI services or background processes on the computer have been disabled.

### 4. Foreground text access

**Settings → Privacy & security → Foreground text access**

- **Foreground text access → Off**

This restricts apps' access to modify text in an active text field through this permission mechanism.

If you want to retain certain features, you can review individual app permissions instead of disabling an entire category. After each change, check whether the features you need still work. On a work computer, make sure any changes comply with your company's IT security policies.

## Also check Microsoft Recall

Microsoft Recall is a separate feature available on compatible Copilot+ PCs. Once enabled, it periodically captures screen content so users can search through their previous activities later.

Open:

**Settings → Privacy & security → Recall & snapshots**

If this option is available, check:

- **Save snapshots → Off**, if you do not want automatic screen capture.
- **Delete snapshots → Delete all**, if you want to delete previously saved snapshots.

If you cannot find this category, your computer may not support Recall or the feature may not be available on your configuration.

We did not find this option on the computer we tested.

## Our perspective

- **Privacy as a starting point:** Security and privacy should be fundamental to an operating system, not the result of users having to investigate its settings afterwards.
- **User awareness:** New AI features should be introduced with clear explanations of their capabilities, permissions and potential security risks.
- **Business security:** Technology, financial and other companies handling confidential data should regularly review app permissions on work computers.
- **Computing resources:** Users should have clear control over resource consumption, particularly for features they did not request themselves.
- **User choice:** Unnecessary permissions should remain disabled until users decide they want to use them.

Our testing did not show that Microsoft was capturing screens or collecting data without authorisation. It did, however, show that four categories of permissions were enabled on the tested computer and that its owner did not recall approving them.

The development of artificial intelligence offers numerous benefits. However, the ability to use a particular technology should not automatically imply permission to use it.

**The computer belongs to the user. The decision about what apps are allowed to do on it should belong to the user as well.**

**Follow Metaadvisor.eu for more independent news and analysis on artificial intelligence, technology, business and digital tools.**

<small style="color:#757575; font-size:12px; font-weight:400; font-style:normal;">In collaboration with AI.</small>

**Note:** This article is based on our own testing and documented screenshots from November 23, 2026. The results do not establish the default settings on all Windows 11 computers and are not evidence of unauthorised screen capture or data transmission. The content is for informational purposes.
