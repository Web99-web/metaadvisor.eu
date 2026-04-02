---
title: "Here is how Drift attackers drained more than $270 million using a Solana feature designed for convenience"
date: 2026-04-02T15:08:48Z
category: "crypto"
translationKey: "d66f4e38b129b9a38a37fbe61be4a6b0"
source: "CoinDesk"
source_url: "https://www.coindesk.com/tech/2026/04/02/how-a-solana-feature-designed-for-convenience-let-an-attacker-drain-usd270-million-from-drift"
image_url: "https://www.coindesk.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fs3y3vcno%2Fproduction%2F19279f188fd985541125b59d44d4ad2fbf6af84d-7008x4672.jpg%3Fauto%3Dformat&w=3840&q=75"
tags: ["crypto"]
_build:
  publishResources: false
  render: never
  list: never
---

The attack on Drift Protocol was not a hack in the traditional sense.

Nobody found a bug or cracked a private key. There wasn't a flash loan exploit or manipulated oracle either.

Instead, an attacker used a legitimate Solana feature, 'durable nonces,' to trick Drift's security council into pre-approving transactions that would be executed weeks later, at a time and in a context the signers never intended.

The result was a drain of at least $270 million that took less than a minute to execute but more than a week to set up.

On Solana, every transaction includes a 'recent blockhash,' essentially a timestamp that proves the transaction was created recently. That blockhash expires after about 60 to 90 seconds. If the transaction is not submitted to the network within that window, it becomes invalid. This is a safety feature and helps prevent old, stale transactions from being replayed later.

Durable nonces override that safety feature. They replace the expiring blockhash with a fixed 'nonce,' a one-time code stored in a special onchain account, that keeps the transaction valid indefinitely until someone chooses to submit it.

The feature exists for legitimate reasons. Hardware wallets, offline signing setups, and institutional custody solutions all need the ability to prepare and approve transactions without being forced to submit them within 90 seconds.

But indefinitely valid transactions create a problem. If one can get someone to sign a transaction today, it can be executed next week or next month, per the system's hardcoded rules. The signer has no way to revoke their approval once it is given, unless the nonce account is manually advanced, which most users do not monitor.

Drift's protocol was governed by a 'Security Council multisig,' a system in which multiple
