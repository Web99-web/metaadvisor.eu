---
title: "French ZML wants to break Nvidia AI lock-in"
slug: "french-zml-wants-to-break-nvidia-ai-lock-in"
date: 2026-07-09T08:00:00+02:00
category: "ai"
translationKey: "zml-france-nvidia-ai-lock-in-2026-07-08"
source: "TechCrunch, ZML, Metaadvisor.eu"
source_url: "https://metaadvisor.eu"
author: "Metaadvisor.eu"
image_url: "/images/companies/ZML-France.png"
featured_image: "/images/companies/ZML-France.png"
image: "/images/companies/ZML-France.png"
thumbnail: "/images/companies/ZML-France.png"
image_credit: "Metaadvisor.eu"
tags: ["ZML", "ZML LLMD", "French AI startup", "AI inference", "LLM inference server", "Nvidia lock-in", "CUDA", "multi-chip AI", "AI infrastructure", "open-source LLM", "AI chips", "AMD GPU", "Google TPU", "Apple Metal", "Intel Arc"]
summary: "French AI startup ZML has released a free inference tool designed to run open-source AI models faster across different chips, not only on Nvidia GPUs. For ordinary users, this is not a new chatbot, but infrastructure under the hood that could help professionals reduce costs and dependence on a single hardware ecosystem."
disclaimer: "This article is for informational purposes only and does not constitute investment, technology or business advice."
draft: false
---

Image is symbolic.

# French ZML wants to break Nvidia AI lock-in: why this is not a new chatbot, but infrastructure under the hood

French AI startup **ZML** has released a free product that could be interesting for professionals building AI systems, cloud infrastructure, large chatbots and applications that use open-source language models. But for ordinary users, the most important thing is to understand first what ZML **is not**.

ZML is not a new ChatGPT. It is not a new AI agent that answers emails, writes posts, reads documents or handles customer support. ZML is not a tool that an average user opens, connects to Gmail or Google Sheets and instantly gets an “AI employee”.

ZML is something else: infrastructure under the hood. It is software that tries to help AI models run faster and more efficiently on different types of chips, not only on Nvidia GPUs.

In other words, ZML is not the restaurant where the user orders a finished meal. ZML is technology for the kitchen. It helps those building AI systems prepare the same “meal” faster, cheaper and on different types of ovens.

## Why does this matter at all?

Today, most people see AI through ready-made tools: ChatGPT, Claude, Gemini, Copilot, Sintra, Make, Zapier AI or various “AI agents” advertised on social media. These tools look simple to the user. You enter a question, connect documents, add email, CRM or a website, and the agent starts working.

But behind that simple interface there is a large technical layer that the user does not see. When an AI agent needs to answer a request, a whole chain happens in the background: the application receives the question, sends it to an AI model, the model runs on a server, the server uses specific chips, and the answer returns to the user.

For ordinary users, this is invisible. For companies building their own AI systems, it is a huge problem. They have to decide what the model will run on, how much it will cost, how fast the system needs to respond, how much energy it consumes, and whether it can run on **Nvidia** chips, **AMD**, **Google TPU**, **Apple Metal**, **Intel Arc** or some other hardware.

That is where ZML comes in.

{{< support1 >}}

## ZML tries to solve the AI “adapter” problem

One of the biggest problems in AI infrastructure is that different chips have different software ecosystems. Nvidia is not so dominant only because it has powerful chips, but also because it has built a huge software layer around them. The best-known part of that ecosystem is **CUDA**, which over the years has become almost a standard for many AI and computing tasks.

This creates what is often called **vendor lock-in**. If a system is built for the Nvidia ecosystem, it is not always easy to move it to other hardware. A company may have access to AMD GPUs, Apple chips or a European AI chip, but if the software is not well adapted, performance can be poor or development too expensive.

ZML is trying to be a layer that reduces this problem. Its new product, **ZML/LLMD**, is designed as an inference server that enables open-source large language models to run on different types of chips. According to TechCrunch, ZML is targeting support for **Nvidia**, **AMD**, **Google TPU**, **Apple Metal**, **Intel Arc** and other chips.

Put simply: ZML wants the same AI model to be able to run on several different “engines”, without developers having to manually adapt everything from scratch each time.

## What is inference and why is it becoming more important?

In the AI world, people often talk about model training. This is the phase in which a large model learns from huge amounts of data. It is expensive, demanding and usually reserved for large players.

But when a user uses AI, something else usually happens: **inference**. This is the moment when an already trained model receives a request and generates an answer. When you ask a chatbot to write an email, explain a law, summarize a document or generate code, you are using inference.

As AI becomes integrated into more and more applications, inference becomes increasingly important. It is no longer enough to have a good model. It has to be run quickly, reliably and at an acceptable cost. If millions of users constantly send requests, every answer costs money. Every token consumes computing resources. Every second of delay bothers the user.

That is why infrastructure has become a key issue. If an AI company can run the same model faster or cheaper, it can make a big difference.

{{< support1 >}}

## Who is ZML for?

ZML is not a tool for ordinary users who want to create a simple AI agent for work, marketing or administration. If you use ready-made tools such as Sintra, Make, Zapier, OpenAI Assistants or a no-code AI service, you usually do not think about chips. The platform solves that for you.

ZML is interesting to a different audience: programmers, AI engineers, cloud companies, startups building AI products, companies that host models themselves and organizations that want to avoid total dependence on one hardware provider.

If someone is building their own chatbot from start to finish, their own AI backend or their own platform for serving models, then the question of “what the model runs on” becomes very important. ZML is trying to help precisely that layer of the market.

That is why it is important not to confuse two things. Ready-made AI agents are user products. ZML is an infrastructure tool.

Sintra is like a ready-made restaurant: the user orders a meal and does not need to know what kind of oven is in the kitchen. ZML is technology for that kitchen: it helps professionals make the same meal faster, cheaper and on different types of equipment.

## Why is Nvidia mentioned all the time?

Nvidia is today a symbol of AI infrastructure. Its GPUs power a large part of the modern AI wave, and demand for them has exploded because of large models, clouds and AI applications. But Nvidia’s dominance also creates a problem: high prices, limited availability and dependence on one ecosystem.

ZML does not mean Nvidia’s dominance is over. That would be an exaggeration. Nvidia still has an enormous technological, market and software position. But ZML fits into a broader trend: more and more companies are trying to find ways to run AI models on other chips as well.

If this layer improves, the market gets more choice. Companies could use a combination of Nvidia, AMD, Google, Apple, Intel or specialized AI chips depending on price, availability, speed and energy consumption.

This may not be visible to ordinary users, but it can affect the price and availability of the AI tools they use.

{{< support2 >}}

## The European angle

It is also interesting that ZML comes from France. Europe often lags behind the United States in major platforms and consumer AI products, but it is trying to find room in infrastructure, chips, security and specialized technology layers.

TechCrunch writes that such a software layer could also help new AI chipmakers, many of which are from Europe. The article mentions **Axelera**, **Fractile**, **Kalray**, **OLIX**, **Q.ANT**, **SiPearl**, **SpiNNcloud** and **VSORA**. The point is not only where these companies come from, but that new AI hardware can hardly become widely usable if there is no software connecting it with models, applications and real use cases.

That is an important lesson: a chip alone is not enough. Hardware without good software struggles to enter real-world use. Nvidia knows this very well. Its success is not only in silicon, but also in the software ecosystem built around it over many years.

If Europe wants a more serious role in AI infrastructure, it has to develop both hardware and the software that makes that hardware useful.

## Why could this still matter to ordinary people?

Although ZML is not a tool for ordinary users, the consequences of such technologies can be felt more broadly. If AI models become cheaper to run, more companies can offer AI services. If dependence on a single hardware supplier decreases, the market can become more competitive. If inference becomes faster, AI tools can become quicker and more accessible.

An ordinary user may never install ZML/LLMD. But they may use an application that uses this or a similar infrastructure layer in the background. Just as most people do not know which server runs their banking app, but they definitely notice if the app is slow, expensive or unavailable.

ZML is therefore a story about the invisible part of AI. Not about the chatbot that answers the user, but about the layer that makes it possible for the chatbot to work quickly, reliably and at an acceptable cost.

{{< support2 >}}

## Our take

- ZML is not a new chatbot, AI agent or tool for ordinary users.
- ZML is infrastructure software for professionals who build, host or optimize AI models.
- Its goal is to help open-source LLM models run on different chips, not only on Nvidia GPUs.
- The main topic is not “new AI”, but reducing dependence on a single hardware ecosystem.
- For users of ready-made AI tools, this layer is mostly invisible.
- For companies building AI systems from scratch, inference, speed, cost and chip compatibility become key problems.
- If tools like ZML succeed, the AI market could eventually gain more competition, lower costs and less dependence on Nvidia.
- This is an infrastructure story, but stories like this often determine how accessible, fast and expensive AI will ultimately become.

**Disclaimer:** This article is for informational purposes only and does not constitute investment, technology or business advice.
