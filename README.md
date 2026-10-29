<div align="center">

<picture>
  <!-- A README renders in the VIEWER's theme. The ink banner bleeds to true
       black so it dissolves into dark chrome; on a white README that same
       bleed becomes a hard rectangle, so light mode gets the paper register. -->
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.png?v=achroma-v5">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.png?v=achroma-v5">
  <img alt="nyk — agent operating systems, Solana infrastructure, open source" src="assets/banner.png?v=achroma-v5">
</picture>

**Agents fail on the harness, not the model.**  
Agent operating systems, Solana infrastructure, open source.  
Personal brand / hub: [nyk.dev](https://nyk.dev) · GitHub: [github.com/0xNyk](https://github.com/0xNyk)

Founder of [Builderz](https://builderz.dev), a development studio for Solana products and AI agent systems.

<p>
  <a href="https://builderz.dev"><img src="https://img.shields.io/badge/Builderz-builderz.dev-6B5CFF?style=flat-square" alt="Builderz" /></a>
  <a href="https://nyk.dev"><img src="https://img.shields.io/badge/nyk.dev-FFFFFF?style=flat-square&logo=vercel&logoColor=0D0D0C" alt="nyk.dev" /></a>
  <a href="https://github.com/0xNyk"><img src="https://img.shields.io/badge/GitHub-0xNyk-181717?style=flat-square&logo=github&logoColor=FFFFFF" alt="GitHub 0xNyk" /></a>
  <a href="https://github.com/sponsors/0xNyk"><img src="https://img.shields.io/github/sponsors/0xNyk?style=flat-square&label=Sponsor" alt="GitHub Sponsors" /></a>
  <a href="https://github.com/0xNyk?tab=repositories"><img src="assets/badges/total.svg" alt="OSS stars" /></a>
  <a href="https://x.com/nykdotdev"><img src="https://img.shields.io/badge/X-@nykdotdev-0D0D0C?style=flat-square&logo=x&logoColor=FFFFFF" alt="X" /></a>
</p>

<p>
  <a href="https://builderz.dev"><b>Build with Builderz →</b></a> ·
  <a href="https://nyk.dev/products/agent-os-kit">Agent OS Kit</a> ·
  <a href="https://nyk.dev">Field notes</a>
</p>

</div>

---

I build the **ops layer for AI agent fleets** - quotas, safety gates, orchestration, control planes - and prove it in daily use: my ventures run on the same agent stack I open-source, down to the live star counts on this page. <!-- oss-total -->**18.6K+ OSS stars** (18,627 live across every repo I have authored, listed on this page)<!-- /oss-total -->.

## Builderz

I founded [Builderz](https://builderz.dev) to build Solana products. Today, the studio also delivers AI agent systems, infrastructure integrations, and product design.

We work from architecture through launch, and help teams repair systems that are failing in production. Our open-source work lives at [builderz-labs](https://github.com/builderz-labs).

→ [Explore the studio](https://builderz.dev) · [Send a project brief](https://builderz.dev/contact)

## Agent operator resources

| Use it when | Resource |
|---|---|
| One Hermes thread is carrying too much unrelated history | [Hermes session management guide](https://www.nyk.dev/blog/hermes-agent-session-management-guide?utm_source=github&utm_medium=profile&utm_campaign=guide&utm_content=operator_resources) |
| You need to find the missing controls in an agent setup | [30-point Agent OS checklist](https://www.nyk.dev/resources/agent-os-checklist?utm_source=github&utm_medium=profile&utm_campaign=lead_magnet&utm_content=operator_resources) |
| You want to practice authority, verification, recovery, skill admission, and release operations | [Production Agent Systems course](https://www.nyk.dev/go/production-agent-course?utm_source=github&utm_medium=profile&utm_campaign=production_agent_course&utm_content=operator_resources) |

**Latest open source (shipping):**

| Project | One-liner | Stars |
|---|---|---|
| [hermes-buzz](https://github.com/0xNyk/hermes-buzz) | Hermes Agent × Buzz starter kit (buzz-acp + hermes-acp onboarding)| [![stars](assets/badges/0xNyk--hermes-buzz.svg)](https://github.com/0xNyk/hermes-buzz/stargazers) |
| [llmquota](https://github.com/0xNyk/llmquota) | Terminal roster for LLM CLI quotas - see usage, reset times, and which agent still has headroom | [![stars](assets/badges/0xNyk--llmquota.svg)](https://github.com/0xNyk/llmquota/stargazers) |
| [agent-security](https://github.com/0xNyk/agent-security) | Safety gates for agent-touched repos - scan leaks, vet code, trip on prompt injection, guard destructive ops | [![stars](assets/badges/0xNyk--agent-security.svg)](https://github.com/0xNyk/agent-security/stargazers) |
| [silo](https://github.com/0xNyk/silo) | Isolated Claude Code profiles via `CLAUDE_CONFIG_DIR` - no credential vault swap | [![stars](assets/badges/0xNyk--silo.svg)](https://github.com/0xNyk/silo/stargazers) |
| [unmachined](https://github.com/0xNyk/unmachined) | Anti-AI-slop skill - text + UI that reads written, not generated | [![stars](assets/badges/0xNyk--unmachined.svg)](https://github.com/0xNyk/unmachined/stargazers) |

**Upstream:** contributor to [**Hermes Agent**](https://github.com/NousResearch/hermes-agent) (Nous Research) - cron/timezone fix on `main` via [co-authored commit](https://github.com/NousResearch/hermes-agent/commit/605ba4adea51af2580f1ab94fd6372e873c108e7), plus [open PRs](https://github.com/NousResearch/hermes-agent/pulls?q=author%3A0xNyk) for session continuity, skills, and subagent isolation. Also proposing fixes to [OpenClaw](https://github.com/openclaw/openclaw/pulls?q=author%3A0xNyk).

## Work with me

Fixed scope, fixed price band, agreed before anything starts. You get the system
and the handoff, not a dependency on me.

| | | |
|---|---|---|
| **Agent Reliability Audit** | 2 weeks · from $4K | Trajectory evals that locate where your agents actually fail, plus a fix list in priority order |
| **Agent OS Setup** | 2-4 weeks · from $5K | A working agent stack your team can run without me |
| **Solana infra** | 2-6 weeks · from $8K | Latency-sensitive execution paths, data and transaction sending |
| **Agent OS Kit** | €149 · instant | The controls as editable files, if you would rather install it yourself |

→ [See all packages](https://nyk.dev/consulting#packages) · [Book a 30-min intro](https://nyk.dev/contact)

Public OSS stays public. [Sponsor maintenance](https://github.com/sponsors/0xNyk).


## Selected open-source work

**Top 10 by stars.** Live badges. Profile: [github.com/0xNyk](https://github.com/0xNyk).

| # | Project | What it does | Stars |
|---|---|---|---|
| 1 | [mission-control](https://github.com/builderz-labs/mission-control) | Agent fleet dashboard - tasks, quality gates, cost tracking, real-time orchestration | [![stars](assets/badges/builderz-labs--mission-control.svg)](https://github.com/builderz-labs/mission-control/stargazers) |
| 2 | [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) | Curated skills, tools, and integrations for the Hermes Agent ecosystem (Nous Research) | [![stars](assets/badges/0xNyk--awesome-hermes-agent.svg)](https://github.com/0xNyk/awesome-hermes-agent/stargazers) |
| 3 | [council-of-high-intelligence](https://github.com/0xNyk/council-of-high-intelligence) | Multi-perspective reasoning skill - historical thinkers deliberate on your problem | [![stars](assets/badges/0xNyk--council-of-high-intelligence.svg)](https://github.com/0xNyk/council-of-high-intelligence/stargazers) |
| 4 | [marketing-dashboard](https://github.com/builderz-labs/marketing-dashboard) | Marketing ops control center for AI agent teams - CRM, outreach, content, analytics | [![stars](assets/badges/builderz-labs--marketing-dashboard.svg)](https://github.com/builderz-labs/marketing-dashboard/stargazers) |
| 5 | [lacp](https://github.com/0xNyk/lacp) | Local Agent Control Plane - policy gates, memory layers, hook pipeline | [![stars](assets/badges/0xNyk--lacp.svg)](https://github.com/0xNyk/lacp/stargazers) |
| 6 | [xint](https://github.com/0xNyk/xint) | X intelligence CLI (TypeScript + Bun) - search, monitor, analyze, engage | [![stars](assets/badges/0xNyk--xint.svg)](https://github.com/0xNyk/xint/stargazers) |
| 7 | [awesome-agent-cortex](https://github.com/0xNyk/awesome-agent-cortex) | Sovereign agent stack - scripts, on-chain identity, knowledge graphs | [![stars](assets/badges/0xNyk--awesome-agent-cortex.svg)](https://github.com/0xNyk/awesome-agent-cortex/stargazers) |
| 8 | [builderz-solana-dapp-scaffold](https://github.com/builderz-labs/builderz-solana-dapp-scaffold) | Production-ready Solana dApp starter (Next.js, Tailwind, web3.js) | [![stars](assets/badges/builderz-labs--builderz-solana-dapp-scaffold.svg)](https://github.com/builderz-labs/builderz-solana-dapp-scaffold/stargazers) |
| 9 | [openclaw-to-hermes](https://github.com/0xNyk/openclaw-to-hermes) | Battle-tested migration from OpenClaw to Hermes Agent | [![stars](assets/badges/0xNyk--openclaw-to-hermes.svg)](https://github.com/0xNyk/openclaw-to-hermes/stargazers) |
| 10 | [xint-rs](https://github.com/0xNyk/xint-rs) | X intelligence CLI as a single Rust binary - &lt;5ms startup | [![stars](assets/badges/0xNyk--xint-rs.svg)](https://github.com/0xNyk/xint-rs/stargazers) |

<details>
<summary><b>More open-source repositories</b> - sorted by stars</summary>

<br>

| Project | What it does | Stars |
|---|---|---|
| [builderz-xNFT-scaffold-next](https://github.com/builderz-labs/builderz-xNFT-scaffold-next) | Solana xNFT scaffold (Next.js, TypeScript, Tailwind) | [![stars](assets/badges/builderz-labs--builderz-xNFT-scaffold-next--gray.svg)](https://github.com/builderz-labs/builderz-xNFT-scaffold-next/stargazers) |
| [solana-claude-md](https://github.com/builderz-labs/solana-claude-md) | Open-source CLAUDE.md pack for Solana program work | [![stars](assets/badges/builderz-labs--solana-claude-md--gray.svg)](https://github.com/builderz-labs/solana-claude-md/stargazers) |
| [hermes-cf-bypass](https://github.com/0xNyk/hermes-cf-bypass) | Cloudflare TLS fingerprint bypass for Hermes on datacenter VPS | [![stars](assets/badges/0xNyk--hermes-cf-bypass--gray.svg)](https://github.com/0xNyk/hermes-cf-bypass/stargazers) |
| [renaissance-xnft](https://github.com/builderz-labs/renaissance-xnft) | Royalty tracking and redemption for NFT communities | [![stars](assets/badges/builderz-labs--renaissance-xnft--gray.svg)](https://github.com/builderz-labs/renaissance-xnft/stargazers) |
| [obsidian-curator](https://github.com/0xNyk/obsidian-curator) | Deterministic knowledge-graph maintenance for Claude + Obsidian | [![stars](assets/badges/0xNyk--obsidian-curator--gray.svg)](https://github.com/0xNyk/obsidian-curator/stargazers) |
| [homebrew-xint](https://github.com/0xNyk/homebrew-xint) | Homebrew tap for xint and xint-rs | [![stars](assets/badges/0xNyk--homebrew-xint--gray.svg)](https://github.com/0xNyk/homebrew-xint/stargazers) |

</details>

## Other ventures

[rpc edge](https://rpcedge.com): Solana infrastructure with dedicated RPC, Yellowstone gRPC, shred streams, and transaction sending. [Docs](https://docs.rpcedge.com) · [@rpcedge](https://x.com/rpcedge).

<details>
<summary>rpc edge open-source tooling</summary>

| Project | What it does | Stars |
|---|---|---|
| [rpcedge-toolkit](https://github.com/rpc-edge/rpcedge-toolkit) | TypeScript SDK, CLI, and MCP server for rpc edge / Solana trading infra | [![stars](assets/badges/rpc-edge--rpcedge-toolkit.svg)](https://github.com/rpc-edge/rpcedge-toolkit/stargazers) |
| [rpcedge-copy-ref](https://github.com/rpc-edge/rpcedge-copy-ref) | Minimal paper copy-watch reference for rpc edge (doctor → poll → paper log) | [![stars](assets/badges/rpc-edge--rpcedge-copy-ref.svg)](https://github.com/rpc-edge/rpcedge-copy-ref/stargazers) |
| [rpcedge-dlmm-ref](https://github.com/rpc-edge/rpcedge-dlmm-ref) | Paper Meteora DLMM pool-watch reference for rpc edge (not financial advice) | [![stars](assets/badges/rpc-edge--rpcedge-dlmm-ref.svg)](https://github.com/rpc-edge/rpcedge-dlmm-ref/stargazers) |

</details>

## What I believe

- Infrastructure wins on **latency, reliability, and sharp defaults**.
- Agent teams need **operations**, not demos.
- The strongest stack is **open-core control plane + premium operator UX**.

## Build surface

<p align="center">
  <img src="assets/stack.png" alt="Build surface: Solana infra, AI agent ops, Dev tools" width="900" />
</p>


## Connect

| | |
|---|---|
| **Profile** | [github.com/0xNyk](https://github.com/0xNyk) · [nyk.dev](https://nyk.dev) · [@nykdotdev](https://x.com/nykdotdev) |
| **Builderz** | [Studio](https://builderz.dev) · [GitHub](https://github.com/builderz-labs) · [Project enquiries](https://builderz.dev/contact) |
