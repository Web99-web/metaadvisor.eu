---
title: "ETH news: Ethereum Foundation says AI found bug that could take validators offline"
date: 2026-07-11T12:00:00Z
category: "crypto"
translationKey: "26391e0400b93ed7be9cc85b3404319d"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/07/10/ai-found-an-ethereum-bug-that-could-take-validators-offline-but-humans-had-to-prove-it"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2Fe66950b0e6ed69b66abb166d8961c9cff1c8bfb1-720x406.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

Developers at the Ethereum Foundation recently set AI agents loose on the software Ethereum runs on, hoping to discover bugs in an ongoing effort to keep strengthening the largest blockchain by value locked.

And while bugs were found, meticulous human judgment was still required to differentiate between what was real and what were false positives - with the Protocol Security team publishing field notes on tips the broader ecosystem should follow in their own AI workflows.

Ethereum runs on thousands of nodes, or ordinary computers running the network's software, each keeping a copy of the chain and passing messages to its neighbors.

Validators, the nodes that stake ether and vote on which blocks are valid, sit on top of that layer. They only work if messages reach them.

The bug these engineers found sat in gossipsub . The flaw let a remote system trigger a crash — wherein the node's software hits an impossible calculation, gives up and shuts itself down, taking a validator offline until an operator restarts it.

This was quickly fixed and disclosed as 'CVE-2026-34219' with credit to the team. The broader concern, however, was separating the agents' real bugs from the ones that were confidently masquerading as such.

"The surprise was how little of the work went into finding them, and how much went into telling the real bugs from the ones that just looked real," wrote Nikos Baxevanis, who authored the post.

The difficulty started with what an agent produces. A fuzzer, the standard tool that hurls malformed data at software until something breaks, returned a crash and a record of where it happened, which an engineer can confirm in minutes.

An agent, however, returns a created narrative. It traces how the flaw could be reached, argues why it matters, proposes a
