---
title: "The 'first' AI-run ransomware attack still needed a human | TechCrunch"
date: 2026-07-06T23:56:14Z
category: "ai"
translationKey: "bd206ca68985755ccb9bcc41a95c67cb"
source: "TechCrunch"
source_url: "https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/"
image_url: "https://techcrunch.com/wp-content/uploads/2025/01/Connie-Loizos-1.jpg?w=150"
tags: ["ai"]
_build:
  publishResources: false
  render: never
  list: never
---

Last week, researchers at cloud security firm Sysdig said they’d documented the first known case of “agentic ransomware.” It was an extortion operation, dubbed JadePuffer, in which an AI agent — not a human — handled the technical execution of a real-world cyberattack from start to finish. The agent broke into a vulnerable server, stole credentials, moved through the target’s network, encrypted files, and even wrote its own ransom note, adapting to obstacles along the way like a human hacker would. Coverage of the funding described it as run “without any human oversight,” with “no human at the keyboard.”

That’s not quite the full picture. In an interview on Monday with CyberScoop, Sysdig’s Michael Clark, the company’s senior director of threat research, clarified that a human was still very much involved — just not in the technical execution. “A human still set up and pointed the operation and provisioned the infrastructure behind it, the command-and-control server, the staging server used for the stolen data and chose a victim,” Clark said. The credentials used to break into the victim’s database, he added, weren’t harvested by the AI agent itself; someone obtained them separately, through a prior compromise, and handed them to the operation.

None of this contradicts Sysdig’s original claim, and the technical details of the attack remain notable on their own — wild, even. The agent got in through a known bug in Langflow , a popular open-source tool for building LLM apps, then moved on to a production MySQL server and exploited another known flaw to gain admin access. It encrypted over 1,300 configuration records and not only left behind a ransom note that it wrote itself but it left a Bitcoin address where the ransom could be sent. Sysdig hasn’t disclosed who was
