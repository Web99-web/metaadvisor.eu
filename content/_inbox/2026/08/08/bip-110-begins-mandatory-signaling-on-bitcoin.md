---
title: "BIP-110 Begins Mandatory Signaling on Bitcoin"
date: 2026-08-08T21:17:08Z
category: "crypto"
translationKey: "47d9c24491828f5b37abd74ef3d31cdb"
source: "Cointelegraph"
source_url: "https://cointelegraph.com/news/bitcoin-bip-110-mandatory-signaling?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound"
image_url: "https://s3-images.ctmedia.io/media/article-covers/alex-svanevik-interview.jpg"
tags: ["crypto", "bitcoin"]
_build:
  publishResources: false
  render: never
  list: never
---

The deployment milestone tests whether enforcing nodes can sustain the change amid limited miner signaling and discussion of a hard-fork fallback.

Bitcoin Improvement Proposal 110 entered its mandatory-signaling phase at block 961,632 on Saturday, with miners signaling support in just 51 of the preceding 2,016 blocks, or 2.53%, well below the 55% threshold required for early activation, according to the BIP-110 monitor.

Starting at block 961,632, nodes enforcing BIP-110 began rejecting blocks that did not set version bit 4, while ordinary Bitcoin nodes continued accepting both signaling and non-signaling blocks. A minority BIP-110 branch subsequently emerged, but quickly fell behind the dominant chain.

The low signaling rate makes a sustained rival chain unlikely without substantially greater miner participation. With relatively little mining support, a BIP-110 branch could advance slowly or stop producing blocks altogether.

The milestone tests whether supporters can advance a contentious consensus change without broad miner backing, potentially separating enforcing nodes from the dominant chain and escalating a dispute over how Bitcoin’s block space should be used.

Written by pseudonymous developer Dathon Ohm, BIP-110 proposes additional consensus restrictions lasting roughly one year.

It would limit most new output scripts to 34 bytes, cap OP_RETURN outputs at 83 bytes, restrict certain data pushes and witness elements to 256 bytes, and temporarily limit several Taproot features. Unspent transaction outputs created before activation would be exempt.

Supporters said the restrictions would discourage inscriptions and other non-monetary data that increase storage and bandwidth costs for node operators.

The proposal’s critics, including Strategy Executive
