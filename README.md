<div align="center">

<img src="assets/images/hero.png" alt="Antigravity Awesome Workspace" width="800"/>

# Antigravity Awesome Workspace

### The Ultimate AI-Powered Vibe Code Template

**51 AI Agents · 79 Slash Commands · 26 Core Skills · 1500+ Skill Library · 25 MCP Servers**

Language: **English** | [Tiếng Việt](README_VI.md) | [简体中文](README_CN.md) | [Español](README_ES.md)

[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)

<br/>

<img src="https://img.shields.io/badge/Antigravity-✓-8B5CF6?style=flat-square" alt="Antigravity"/>
<img src="https://img.shields.io/badge/Claude_Code-✓-D97757?style=flat-square" alt="Claude Code"/>
<img src="https://img.shields.io/badge/Cursor-✓-000000?style=flat-square" alt="Cursor"/>
<img src="https://img.shields.io/badge/Windsurf-✓-06B6D4?style=flat-square" alt="Windsurf"/>
<img src="https://img.shields.io/badge/Gemini_CLI-✓-4285F4?style=flat-square" alt="Gemini CLI"/>
<img src="https://img.shields.io/badge/Codex-✓-412991?style=flat-square" alt="Codex"/>
<img src="https://img.shields.io/badge/Kiro-✓-FF6B6B?style=flat-square" alt="Kiro"/>
<img src="https://img.shields.io/badge/OpenCode-✓-22C55E?style=flat-square" alt="OpenCode"/>

</div>

---

> **Consolidated from 4 world-class Vibe Code systems** into a single, production-ready workspace template. One `python init_vibe_project.py my-app` and you get everything.

<br/>

## 🎯 What is This?

The **most comprehensive AI Agentic Coding workspace template** — a production-ready scaffold with everything you need to build software with AI coding agents.

One command. Every IDE. All the skills. Zero lock-in.

```bash
python init_vibe_project.py my-app
# → 26 core skills, 51 agents, 79 commands, 25 MCP servers, Docker, CI/CD, OpenSpec... done.
```

---

## 🚀 Quick Start

### Option A — Create a New Project (Recommended)

```bash
# Clone this template
git clone https://github.com/your-org/antigravity-awesome-workspace-skill.git
cd antigravity-awesome-workspace-skill

# Create a new project with the full Vibe Code suite
python init_vibe_project.py my-awesome-app
```

```
🚀 Initializing Ultimate Vibe Code Workspace at: /path/to/my-awesome-app

[*] Copied directory .antigravity/
[*] Copied directory .agent/
[*] Copied directory agents/
[*] Copied directory commands/
...
[+] 🎉 Project initialized successfully!

=================================================================
💡 NEXT STEPS:
  1. cd my-awesome-app
  2. cp .env.example .env  (then fill in your API keys)
  3. Open in Cursor / Windsurf / Claude Code / Antigravity
  4. Pre-installed components:
     ✅ 26 Core Skills + 1500+ in Skill Library
     ✅ 51 AI Personas (Architect, Reviewer, Security, QA...)
     ✅ 79 Slash Commands (/plan, /tdd, /code-review, /ship...)
     ✅ 25+ MCP Servers (DB, GitHub, Jira, Playwright, Vercel...)
     ✅ Karpathy Guidelines (Think → Simplify → Surgical → Goal-Driven)
     ...
=================================================================
```

### Option B — Add to an Existing Project

Copy specific directories into your project:

```bash
# Copy just the core skill framework
cp -r .agent/ /your-project/.agent/
cp AGENTS.md /your-project/
cp .cursorrules /your-project/

# Or copy everything
cp -r agents/ commands/ hooks/ references/ /your-project/
```

---

## 📐 Architecture

<div align="center">
<img src="assets/images/architecture.png" alt="Architecture Overview" width="800"/>
</div>

### Development Lifecycle

```
  DEFINE          PLAN           BUILD          VERIFY         REVIEW          SHIP
 ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐
 │ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │  QA  │ ───▶ │  Go  │
 │Refine│      │  PRD │      │ Impl │      │Debug │      │ Gate │      │ Live │
 └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘
  /spec          /plan          /build        /test         /review       /ship
```

Each phase has **dedicated skills, agents, and commands** that activate automatically.

---

## 📦 What's Inside

### Complete Directory Structure

```
my-project/
│
├── 🧠 .antigravity/              Memory Engine & Knowledge Hub
│   ├── memory/                    Agent long-term memory logs
│   ├── agents/                    Auto-generated module knowledge docs
│   ├── conventions.md             Coding conventions (auto-learned)
│   └── map.md                     Knowledge graph routing map
│
├── 📋 .agent/                    Vibe Code Static Framework
│   ├── rules/                     28 rule files across 15 languages
│   │   ├── 00-global.md           Universal coding standards
│   │   ├── common/                Cross-language: coding-style, testing, security
│   │   ├── typescript/            TS-specific: React, Node, async patterns
│   │   ├── python/                Python: PEP8, type hints, Django/FastAPI
│   │   ├── golang/                Go: idiomatic patterns, concurrency
│   │   ├── rust/                  Rust: ownership, lifetimes, error handling
│   │   ├── kotlin/                Kotlin: coroutines, null safety
│   │   ├── java/                  Java: Spring, Maven/Gradle
│   │   ├── csharp/                C#: .NET patterns
│   │   ├── dart/                  Dart/Flutter patterns
│   │   ├── cpp/                   C++: modern idioms, memory safety
│   │   ├── swift/                 Swift: iOS/macOS patterns
│   │   ├── php/                   PHP: Laravel, PSR standards
│   │   ├── perl/                  Perl best practices
│   │   └── web/                   Frontend: CSS, HTML, accessibility
│   ├── workflows/                 9 step-by-step processes
│   │   ├── plan_feature.md        Feature planning workflow
│   │   ├── review_requirement.md  Requirement review
│   │   ├── design_database.md     Database schema design
│   │   ├── generate_tests.md      Test generation
│   │   ├── refactor_safely.md     Safe refactoring
│   │   ├── prepare_release.md     Release preparation
│   │   ├── openspec-proposal.md   Create spec change proposal
│   │   ├── openspec-apply.md      Implement approved change
│   │   └── openspec-archive.md    Archive deployed change
│   └── skills/                    26 Core Skills
│       ├── test-driven-development/
│       ├── spec-driven-development/
│       ├── code-review-and-quality/
│       ├── api-and-interface-design/
│       ├── frontend-ui-engineering/
│       ├── ci-cd-and-automation/
│       ├── security-and-hardening/
│       ├── debugging-and-error-recovery/
│       ├── code-simplification/
│       ├── context-engineering/
│       ├── planning-and-task-breakdown/
│       ├── incremental-implementation/
│       ├── performance-optimization/
│       ├── shipping-and-launch/
│       ├── architecture-decision-records/
│       ├── documentation-and-adrs/
│       ├── git-workflow-and-versioning/
│       ├── deprecation-and-migration/
│       ├── python-patterns/
│       ├── postgres-patterns/
│       ├── docker-patterns/
│       ├── browser-testing-with-devtools/
│       ├── source-driven-development/
│       ├── idea-refine/
│       ├── using-agent-skills/
│       └── karpathy-guidelines/        ★ Think → Simplify → Surgical → Goal-Driven
│
├── 🤖 agents/                    51 AI Specialist Personas
│   ├── architect.md               System architecture design
│   ├── planner.md                 Implementation planning
│   ├── code-reviewer.md           5-axis code review
│   ├── security-auditor.md        OWASP vulnerability detection
│   ├── security-reviewer.md       Security-focused review
│   ├── test-engineer.md           QA strategy & Prove-It pattern
│   ├── performance-optimizer.md   Performance analysis
│   ├── typescript-reviewer.md     TypeScript specialist
│   ├── python-reviewer.md         Python specialist
│   ├── go-reviewer.md             Go specialist
│   ├── rust-reviewer.md           Rust specialist
│   ├── kotlin-reviewer.md         Kotlin specialist
│   ├── java-reviewer.md           Java specialist
│   ├── csharp-reviewer.md         C# specialist
│   ├── cpp-reviewer.md            C++ specialist
│   ├── flutter-reviewer.md        Flutter specialist
│   ├── database-reviewer.md       Database review
│   ├── a11y-architect.md          Accessibility specialist
│   ├── seo-specialist.md          SEO optimization
│   ├── tdd-guide.md               TDD workflow guide
│   ├── e2e-runner.md              End-to-end testing
│   ├── healthcare-reviewer.md     HIPAA compliance
│   ├── opensource-forker.md       Open source forking
│   ├── opensource-packager.md     Package publishing
│   └── ... (51 total)
│
├── ⚡ commands/                   79 Slash Commands
│   ├── plan.md                    /plan — Implementation planning
│   ├── tdd.md                     /tdd — Test-driven development
│   ├── code-review.md             /code-review — Full code review
│   ├── build-fix.md               /build-fix — Auto-fix build errors
│   ├── verify.md                  /verify — Build+lint+test+typecheck
│   ├── e2e.md                     /e2e — Playwright E2E testing
│   ├── save-session.md            /save-session — Save session state
│   ├── resume-session.md          /resume-session — Resume from save
│   ├── learn.md                   /learn — Extract reusable patterns
│   ├── evolve.md                  /evolve — Evolve skill structures
│   ├── multi-plan.md              /multi-plan — Multi-model planning
│   ├── orchestrate.md             /orchestrate — Multi-agent orchestration
│   ├── python-review.md           /python-review — Python review
│   ├── go-build.md, go-review.md, go-test.md
│   ├── rust-build.md, rust-review.md, rust-test.md
│   ├── kotlin-build.md, kotlin-review.md, kotlin-test.md
│   ├── cpp-build.md, cpp-review.md, cpp-test.md
│   ├── flutter-build.md, flutter-review.md, flutter-test.md
│   └── ... (79 total — see COMMANDS-QUICK-REF.md)
│
├── 🎯 .context/                  System Prompt & Coding Style
│   ├── system_prompt.md           AI persona (Senior Architect)
│   └── coding_style.md            Architecture patterns & standards
│
├── 📐 openspec/                  Spec-Driven Development
│   ├── project.md                 Project conventions & tech stack
│   ├── AGENTS.md                  3-step workflow (Propose → Implement → Archive)
│   ├── specs/                     Current truth — what IS built
│   └── changes/                   Proposals — what SHOULD change
│
├── 📚 docs/                      24 Documentation Files
│   ├── en/                        Architecture docs
│   │   ├── PHILOSOPHY.md          Artifact-First, Think-Act-Reflect
│   │   ├── SWARM_PROTOCOL.md      Multi-Agent Swarm (Router-Worker)
│   │   ├── ZERO_CONFIG.md         Auto Tool & Skill Discovery
│   │   ├── MCP_INTEGRATION.md     Model Context Protocol guide
│   │   ├── SANDBOX.md             Sandboxed code execution
│   │   ├── ROADMAP.md             Development roadmap
│   │   └── QUICK_START.md         Quick start guide
│   ├── setup/                     IDE setup guides
│   │   ├── cursor-setup.md
│   │   ├── gemini-cli-setup.md
│   │   ├── windsurf-setup.md
│   │   ├── copilot-setup.md
│   │   └── opencode-setup.md
│   ├── the-security-guide.md      29KB comprehensive security guide
│   ├── the-longform-guide.md      Deep dive: tokens, memory, evals
│   ├── the-shortform-guide.md     Quick setup & philosophy
│   ├── ANTIGRAVITY-GUIDE.md       Antigravity IDE integration
│   ├── SKILL-DEVELOPMENT-GUIDE.md How to create skills
│   ├── COMMAND-AGENT-MAP.md       Command ↔ Agent mapping
│   └── token-optimization.md      Context window optimization
│
├── 📖 references/                Expert Checklists
│   ├── orchestration-patterns.md  Multi-agent patterns & anti-patterns
│   ├── security-checklist.md      Security audit checklist
│   ├── performance-checklist.md   Performance optimization checklist
│   ├── accessibility-checklist.md Accessibility (a11y) checklist
│   └── testing-patterns.md        Testing strategy patterns
│
├── 🔌 hooks/                     Automation Hooks
│   ├── hooks.json                 Session hooks config
│   ├── ecc-hooks.json             48KB advanced hook workflows
│   ├── session-start.sh           Session initialization
│   ├── sdd-cache-pre.sh           SDD cache pre-hook
│   ├── sdd-cache-post.sh          SDD cache post-hook
│   └── simplify-ignore.sh         Code simplification ignore
│
├── 🔀 contexts/                  Context Switching Modes
│   ├── dev.md                     Development mode
│   ├── research.md                Research mode
│   └── review.md                  Code review mode
│
├── 🔧 mcp-configs/               Extended MCP Server Catalog
│   └── mcp-servers.json           25 pre-configured MCP servers
│
├── 📝 examples/                  CLAUDE.md Project Templates
│   ├── django-api-CLAUDE.md       Django REST API template
│   ├── go-microservice-CLAUDE.md  Go microservice template
│   ├── rust-api-CLAUDE.md         Rust API template
│   ├── laravel-api-CLAUDE.md      Laravel API template
│   ├── saas-nextjs-CLAUDE.md      SaaS Next.js template
│   └── user-CLAUDE.md             User-level CLAUDE.md template
│
├── 💾 memory/                    Persistent Agent Memory
│   └── agent_summary.md           Interaction history & decisions
│
├── 🔧 scripts/                   Utility Scripts
│   └── demo_tools.py              Tool discovery demo
│
├── ⚙️ .github/                   CI/CD & AI Prompts
│   ├── workflows/test.yml         GitHub Actions CI pipeline
│   └── prompts/                   Reusable AI prompt templates
│
├── 📦 Monorepo Structure
│   ├── apps/                      Deployable applications
│   ├── packages/                  Shared libraries
│   └── infra/                     Infrastructure configs
│
├── 🐳 Docker
│   ├── Dockerfile                 Production container
│   ├── Dockerfile.sandbox         Sandboxed execution
│   └── docker-compose.yml         Docker Compose orchestration
│
├── 🤖 IDE Bootstrap Files
│   ├── AGENTS.md                  Central behavior rulebook (all IDEs)
│   ├── CLAUDE.md                  Claude Code bootstrap
│   ├── SOUL.md                    Core identity & principles
│   ├── .cursorrules               Cursor IDE bootstrap
│   ├── .cursor/rules/             Cursor project rules (Karpathy guidelines)
│   ├── .gemini/GEMINI.md          Gemini CLI config
│   ├── .kiro/                     Kiro IDE config
│   ├── .claude/                   Claude Code commands
│   └── .claude-plugin/            Claude plugin config
│
├── 📋 Quick References
│   ├── COMMANDS-QUICK-REF.md      79 commands quick reference table
│   ├── TROUBLESHOOTING.md         Common issues & solutions
│   ├── mission.md                 Project objective & success criteria
│   └── .env.example               Environment config template
│
└── 📚 skill_library/             1500+ Skills Catalog
    ├── agent-skills/              Engineering process skills
    ├── everything-claude-code/    ECC skills collection
    └── antigravity-awesome/       Domain-specific skills
```

---

## 🤖 AI Agents (51 Personas)

Specialist personas that play a single role with a single perspective. Each agent is auto-discovered by your IDE.

| Category | Agents | Purpose |
|----------|--------|---------|
| **Architecture** | `architect`, `planner`, `chief-of-staff` | System design, planning, coordination |
| **Code Review** | `code-reviewer`, `typescript-reviewer`, `python-reviewer`, `go-reviewer`, `rust-reviewer`, `kotlin-reviewer`, `java-reviewer`, `csharp-reviewer`, `cpp-reviewer`, `flutter-reviewer` | Language-specific code review |
| **Security** | `security-auditor`, `security-reviewer`, `healthcare-reviewer` | Vulnerability detection, HIPAA compliance |
| **Testing** | `test-engineer`, `tdd-guide`, `e2e-runner`, `pr-test-analyzer` | Test strategy, coverage, E2E |
| **Build** | `build-error-resolver`, `go-build-resolver`, `rust-build-resolver`, `kotlin-build-resolver`, `cpp-build-resolver`, `java-build-resolver`, `dart-build-resolver`, `pytorch-build-resolver` | Auto-fix build errors per language |
| **Performance** | `performance-optimizer`, `harness-optimizer` | Performance analysis & optimization |
| **Documentation** | `doc-updater`, `docs-lookup`, `seo-specialist` | Docs, API lookup, SEO |
| **AI/ML** | `gan-planner`, `gan-generator`, `gan-evaluator` | GAN architecture & training |
| **Open Source** | `opensource-forker`, `opensource-packager`, `opensource-sanitizer` | Fork, package, sanitize OSS |
| **Analysis** | `code-architect`, `code-explorer`, `code-simplifier`, `comment-analyzer`, `conversation-analyzer`, `type-design-analyzer`, `silent-failure-hunter`, `refactor-cleaner` | Deep code analysis |
| **Operations** | `loop-operator`, `a11y-architect`, `database-reviewer` | Operations, accessibility, DB |

---

## ⚡ Commands Quick Reference

> 79 slash commands. Type `/` in any session to invoke.

| Category | Commands |
|----------|----------|
| **Core Workflow** | `/plan`, `/tdd`, `/code-review`, `/build-fix`, `/verify`, `/quality-gate` |
| **Testing** | `/tdd`, `/e2e`, `/test-coverage`, `/go-test`, `/kotlin-test`, `/rust-test`, `/cpp-test`, `/flutter-test` |
| **Code Review** | `/code-review`, `/python-review`, `/go-review`, `/kotlin-review`, `/rust-review`, `/cpp-review`, `/flutter-review` |
| **Build Fixers** | `/build-fix`, `/go-build`, `/kotlin-build`, `/rust-build`, `/cpp-build`, `/gradle-build`, `/flutter-build` |
| **Planning** | `/plan`, `/multi-plan`, `/multi-workflow`, `/multi-backend`, `/multi-frontend`, `/multi-execute`, `/orchestrate`, `/devfleet` |
| **Session** | `/save-session`, `/resume-session`, `/sessions`, `/checkpoint`, `/aside`, `/context-budget` |
| **Learning** | `/learn`, `/learn-eval`, `/evolve`, `/promote`, `/instinct-status`, `/instinct-export`, `/instinct-import`, `/skill-create`, `/skill-health`, `/rules-distill` |
| **Docs** | `/docs`, `/update-docs`, `/update-codemaps` |
| **Automation** | `/loop-start`, `/loop-status`, `/claw` |

📋 Full reference: [COMMANDS-QUICK-REF.md](COMMANDS-QUICK-REF.md)

---

## 🔌 MCP Servers (25 Pre-configured)

Two MCP config files for maximum flexibility:

### `mcp_servers.json` — Core Infrastructure
| Server | Purpose |
|--------|---------|
| **PostgreSQL** | Database operations |
| **GitHub** | PR, issues, repos |
| **Puppeteer** | Browser automation |
| **GitNexus** | Code graph analysis |

### `mcp-configs/mcp-servers.json` — Extended Catalog
| Server | Purpose |
|--------|---------|
| **Jira** | Issue tracking |
| **Supabase** | Database + auth |
| **Playwright** | Browser testing |
| **Context7** | Live documentation lookup |
| **Vercel** | Deployments |
| **Railway** | Deployments |
| **Cloudflare** | Docs, Workers, Observability |
| **ClickHouse** | Analytics queries |
| **Exa Search** | Web research |
| **Memory** | Persistent cross-session memory |
| **Omega Memory** | Semantic search + knowledge graphs |
| **Sequential Thinking** | Chain-of-thought reasoning |
| **Magic UI** | UI components |
| **Filesystem** | Filesystem operations |
| **fal.ai** | AI image/video generation |
| **BrowserBase** | Cloud browser sessions |
| **Browser Use** | AI browser agent |
| **DevFleet** | Multi-agent orchestration |
| **Token Optimizer** | Context compression |
| **Confluence** | Confluence Cloud integration |
| **EvalView** | Agent regression testing |

---

## 📐 OpenSpec: Spec-Driven Development

A structured 3-step workflow for managing changes like a professional engineer:

```
1. PROPOSE  →  Create a change proposal in openspec/changes/
2. IMPLEMENT →  Apply the approved changes
3. ARCHIVE  →  Archive deployed specs
```

Use the OpenSpec workflows in `.agent/workflows/`:
- `openspec-proposal.md` — Create new spec proposals
- `openspec-apply.md` — Implement approved specs
- `openspec-archive.md` — Archive completed specs

---

## 📖 Skill Library (1500+)

The `skill_library/` directory contains the **complete catalog** of skills from all source repositories. These are NOT loaded by default — they serve as an on-demand library.

**How to use:**

```bash
# Browse available skills
ls skill_library/

# Copy a skill you need into your project
cp -r skill_library/some-skill/ my-project/.agent/skills/
```

**Categories include:** DevOps, Machine Learning, Mobile (Flutter/React Native), Game Development (Unity/Unreal), CMS (WordPress/Shopify), Cloud (AWS/GCP/Azure), Blockchain/Web3, Data Science, and 50+ more domains.

---

## 🛡️ Security

This template includes comprehensive security infrastructure:

- **Security Auditor Agent** — OWASP vulnerability detection
- **Security Checklist** — Production-ready security audit reference
- **The Security Guide** — 29KB deep-dive on agentic security (CVEs, sandboxing, prompt injection)
- **Docker Sandbox** — Isolated execution environment
- **`.env.example`** — Never hardcode secrets

📖 Read: [docs/the-security-guide.md](docs/the-security-guide.md)

---

## 🏗️ Multi-IDE Support

This template works across every major AI coding IDE:

| IDE | Config File | How It Works |
|-----|------------|--------------|
| **Antigravity** | `.agent/` | Native `.agent/rules/`, `.agent/skills/`, `.agent/workflows/` |
| **Claude Code** | `CLAUDE.md`, `.claude/` | Commands, agents, hooks, plugin |
| **Cursor** | `.cursorrules` | Rules injected via cursor config |
| **Gemini CLI** | `.gemini/GEMINI.md` | Native Gemini instructions |
| **Kiro** | `.kiro/` | Native Kiro skills |
| **Codex** | `AGENTS.md` | Agent definitions |
| **Windsurf** | `.cursorrules` | Compatible with Cursor format |
| **OpenCode** | `.opencode/` | OpenCode plugin |

---

## 📊 Init Script Reference

```
python init_vibe_project.py [project-name]
```

**What it creates:**

| Category | Components | Count |
|----------|-----------|-------|
| Core Framework | `.antigravity/`, `.agent/`, `.context/`, `openspec/`, `memory/` | 5 dirs |
| AI System | `agents/`, `commands/`, `hooks/`, `contexts/`, `references/` | 5 dirs |
| Infrastructure | `.github/`, `mcp-configs/`, `examples/`, `scripts/` | 4 dirs |
| IDE Configs | `.claude/`, `.claude-plugin/`, `.gemini/`, `.kiro/` | 4 dirs |
| Monorepo | `apps/`, `packages/`, `infra/` | 3 dirs |
| Docker | `Dockerfile`, `Dockerfile.sandbox`, `docker-compose.yml` | 3 files |
| Bootstrap | `AGENTS.md`, `CLAUDE.md`, `SOUL.md`, `.cursorrules`, `mission.md` | 5 files |
| Config | `mcp_servers.json`, `.env.example`, `.gitignore`, `COMMANDS-QUICK-REF.md`, `TROUBLESHOOTING.md` | 5 files |
| Documentation | `docs/` (24 files across architecture, setup, guides) | 24 files |

**Total: ~21 directories + ~40 files + 25 core skills scaffolded automatically**

---

## 🔄 Workflow Example

```bash
# 1. Create project
python init_vibe_project.py my-saas-app
cd my-saas-app

# 2. Configure environment
cp .env.example .env
# Edit .env with your API keys

# 3. Open in your IDE
# The AI agent will automatically discover:
#   - Rules from .agent/rules/
#   - Skills from .agent/skills/
#   - Agent personas from agents/
#   - Commands from commands/

# 4. Start building with AI
# Type /plan to plan a feature
# Type /tdd to write tests first
# Type /code-review for quality check
# Type /ship for production readiness check
```

---

## 📚 References & Inspiration

This template is inspired by and references these outstanding open-source projects in the AI coding community:

<table>
<tr>
<td align="center" width="120">
<a href="https://github.com/AffaanMustafa/everything-claude-code">
<img src="https://img.shields.io/github/stars/AffaanMustafa/everything-claude-code?style=social" alt="Stars"/>
</a>
</td>
<td>

**[Everything Claude Code](https://github.com/AffaanMustafa/everything-claude-code)** — The performance optimization system for AI agent harnesses. 47 agents, 181 skills, 79 commands, hooks, MCP configs. Anthropic Hackathon Winner.

</td>
</tr>
<tr>
<td align="center" width="120">
<a href="https://github.com/addyosmani/agent-skills">
<img src="https://img.shields.io/github/stars/addyosmani/agent-skills?style=social" alt="Stars"/>
</a>
</td>
<td>

**[Agent Skills](https://github.com/addyosmani/agent-skills)** — Production-grade engineering skills by Addy Osmani (Google). "Process over Prose" philosophy, lifecycle-mapped skills, orchestration patterns.

</td>
</tr>
<tr>
<td align="center" width="120">
<a href="https://github.com/forrestchang/andrej-karpathy-skills">
<img src="https://img.shields.io/github/stars/forrestchang/andrej-karpathy-skills?style=social" alt="Stars"/>
</a>
</td>
<td>

**[Karpathy Skills](https://github.com/forrestchang/andrej-karpathy-skills)** — Behavioral guidelines derived from Andrej Karpathy's observations on LLM coding pitfalls: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution.

</td>
</tr>
<tr>
<td align="center" width="120">
<a href="https://github.com/study8677/antigravity-workspace-template">
<img src="https://img.shields.io/github/stars/study8677/antigravity-workspace-template?style=social" alt="Stars"/>
</a>
</td>
<td>

**[Antigravity Workspace Template](https://github.com/study8677/antigravity-workspace-template)** — Multi-agent knowledge engine. `ag-refresh` builds knowledge base, `ag-ask` routes Q&A to ModuleAgents. Swarm protocol, OpenSpec framework.

</td>
</tr>
<tr>
<td align="center" width="120">
<a href="https://github.com/anthropics/claude-code">
<img src="https://img.shields.io/github/stars/anthropics/claude-code?style=social" alt="Stars"/>
</a>
</td>
<td>

**[Claude Code](https://github.com/anthropics/claude-code)** — Anthropic's official agentic coding tool. CLAUDE.md convention, hook system, MCP integration, permission model.

</td>
</tr>
<tr>
<td align="center" width="120">
<a href="https://github.com/anthropics/anthropic-cookbook">
<img src="https://img.shields.io/github/stars/anthropics/anthropic-cookbook?style=social" alt="Stars"/>
</a>
</td>
<td>

**[Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)** — Official recipes and best practices for building with Claude. Prompt engineering, tool use, and agent patterns.

</td>
</tr>
<tr>
<td align="center" width="120">
<a href="https://github.com/modelcontextprotocol/servers">
<img src="https://img.shields.io/github/stars/modelcontextprotocol/servers?style=social" alt="Stars"/>
</a>
</td>
<td>

**[MCP Servers](https://github.com/modelcontextprotocol/servers)** — Official Model Context Protocol servers. GitHub, filesystem, memory, sequential thinking, and more.

</td>
</tr>
<tr>
<td align="center" width="120">
<a href="https://github.com/punkpeye/awesome-mcp-servers">
<img src="https://img.shields.io/github/stars/punkpeye/awesome-mcp-servers?style=social" alt="Stars"/>
</a>
</td>
<td>

**[Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)** — Curated list of MCP servers for extending AI agent capabilities with external tools and data sources.

</td>
</tr>
<tr>
<td align="center" width="120">
<a href="https://github.com/anthropics/courses">
<img src="https://img.shields.io/github/stars/anthropics/courses?style=social" alt="Stars"/>
</a>
</td>
<td>

**[Anthropic Courses](https://github.com/anthropics/courses)** — Educational materials for prompt engineering, tool use, and building AI agents.

</td>
</tr>
</table>

> All referenced projects are under MIT or Apache 2.0 license. This project is MIT licensed.

---

## ⭐ Support This Project

<div align="center">

If this workspace template saves you hours of setup time, **please consider starring this repo** — it helps others discover it!

<a href="https://github.com/dangindev/antigravity-awesome-workspace-skill/stargazers">
<img src="https://img.shields.io/github/stars/dangindev/antigravity-awesome-workspace-skill?style=for-the-badge&logo=github&color=yellow" alt="GitHub Stars"/>
</a>
<a href="https://github.com/dangindev/antigravity-awesome-workspace-skill/network/members">
<img src="https://img.shields.io/github/forks/dangindev/antigravity-awesome-workspace-skill?style=for-the-badge&logo=github&color=blue" alt="GitHub Forks"/>
</a>

### ⭐ Star the Referenced Projects Too!

<a href="https://github.com/AffaanMustafa/everything-claude-code"><img src="https://img.shields.io/github/stars/AffaanMustafa/everything-claude-code?style=social&label=Everything%20Claude%20Code" alt="ECC Stars"/></a>
&nbsp;&nbsp;
<a href="https://github.com/addyosmani/agent-skills"><img src="https://img.shields.io/github/stars/addyosmani/agent-skills?style=social&label=Agent%20Skills" alt="Agent Skills Stars"/></a>
&nbsp;&nbsp;
<a href="https://github.com/forrestchang/andrej-karpathy-skills"><img src="https://img.shields.io/github/stars/forrestchang/andrej-karpathy-skills?style=social&label=Karpathy%20Skills" alt="Karpathy Skills Stars"/></a>
&nbsp;&nbsp;
<a href="https://github.com/study8677/antigravity-workspace-template"><img src="https://img.shields.io/github/stars/study8677/antigravity-workspace-template?style=social&label=Workspace%20Template" alt="Workspace Template Stars"/></a>
&nbsp;&nbsp;
<a href="https://github.com/anthropics/claude-code"><img src="https://img.shields.io/github/stars/anthropics/claude-code?style=social&label=Claude%20Code" alt="Claude Code Stars"/></a>
&nbsp;&nbsp;
<a href="https://github.com/modelcontextprotocol/servers"><img src="https://img.shields.io/github/stars/modelcontextprotocol/servers?style=social&label=MCP%20Servers" alt="MCP Servers Stars"/></a>

</div>

---

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

1. **Fork** this repository
2. **Create** your feature branch (`git checkout -b feature/amazing-skill`)
3. **Add** your skill to `.agent/skills/` or `skill_library/`
4. **Follow** the [Skill Development Guide](docs/SKILL-DEVELOPMENT-GUIDE.md)
5. **Submit** a Pull Request

### What We're Looking For

- 🆕 **New Skills** — Domain-specific skills for emerging technologies
- 🌍 **Translations** — Help us reach more developers worldwide
- 🐛 **Bug Fixes** — Issues with the init script, missing files, broken paths
- 📖 **Documentation** — Improve guides, add examples, fix typos
- 🤖 **New Agents** — Specialist personas for niche domains

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

All integrated components retain their original MIT licenses from their respective repositories.

---

<div align="center">

### 🌟 Built with ❤️ for the AI-powered development community

**Stop configuring. Start building.**

One template. Every IDE. All the skills. Zero lock-in.

<br/>

<a href="https://github.com/dangindev/antigravity-awesome-workspace-skill">
<img src="https://img.shields.io/badge/⭐_Star_This_Repo-171515?style=for-the-badge&logo=github&logoColor=white" alt="Star This Repo"/>
</a>
&nbsp;&nbsp;
<a href="https://github.com/dangindev/antigravity-awesome-workspace-skill/fork">
<img src="https://img.shields.io/badge/🔱_Fork_It-171515?style=for-the-badge&logo=github&logoColor=white" alt="Fork It"/>
</a>
&nbsp;&nbsp;
<a href="https://github.com/dangindev/antigravity-awesome-workspace-skill/issues">
<img src="https://img.shields.io/badge/🐛_Report_Issue-171515?style=for-the-badge&logo=github&logoColor=white" alt="Report Issue"/>
</a>

<br/><br/>

**Made by [Hai-Dang Nguyen](https://nguyenhaidang.io.vn/)** · PhD Student, College of Engineering & Computer Science, [VinUniversity](https://vinuni.edu.vn/)

[![Website](https://img.shields.io/badge/🌐_Website-nguyenhaidang.io.vn-8B5CF6?style=flat-square)](https://nguyenhaidang.io.vn/)
[![GitHub](https://img.shields.io/badge/GitHub-dangindev-171515?style=flat-square&logo=github)](https://github.com/dangindev)

<sub>If you use this template in your project, consider adding a badge to your README:</sub>

```markdown
[![Built with Antigravity](https://img.shields.io/badge/Built_with-Antigravity_Awesome_Workspace-8B5CF6?style=flat-square)](https://github.com/dangindev/antigravity-awesome-workspace-skill)
```

<br/>

[![Built with Antigravity](https://img.shields.io/badge/Built_with-Antigravity_Awesome_Workspace-8B5CF6?style=flat-square)](https://github.com/dangindev/antigravity-awesome-workspace-skill)

</div>
