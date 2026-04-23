#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
from pathlib import Path

# Ensure stdout uses UTF-8 to prevent UnicodeEncodeError on Windows when printing emojis
if sys.stdout.encoding.lower() != 'utf-8':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

# Root directory containing the template (directory of this script)
TEMPLATE_ROOT = Path(__file__).parent.resolve()

def print_step(msg):
    print(f"[*] {msg}")

def print_success(msg):
    print(f"[+] {msg}")

def print_error(msg):
    print(f"[-] {msg}")

def copy_template_dir(src_name, dest_path):
    src = TEMPLATE_ROOT / src_name
    dest = dest_path / src_name
    if src.exists() and src.is_dir():
        shutil.copytree(src, dest, dirs_exist_ok=True)
        print_step(f"Copied directory {src_name}/")

def copy_template_file(src_name, dest_path):
    src = TEMPLATE_ROOT / src_name
    dest = dest_path / src_name
    if src.exists() and src.is_file():
        shutil.copy2(src, dest)
        print_step(f"Copied file {src_name}")

def main():
    parser = argparse.ArgumentParser(description="Initialize an Antigravity Vibe Code project")
    parser.add_argument("project_name", nargs="?", help="Name of the project directory to create")
    parser.add_argument("--claude", action="store_true", help="Only install Claude Code configurations")
    parser.add_argument("--cursor", action="store_true", help="Only install Cursor configurations")
    parser.add_argument("--windsurf", action="store_true", help="Only install Windsurf configurations")
    parser.add_argument("--gemini", action="store_true", help="Only install Gemini CLI configurations")
    parser.add_argument("--codex", action="store_true", help="Only install Codex CLI configurations")
    parser.add_argument("--kiro", action="store_true", help="Only install Kiro IDE configurations")
    parser.add_argument("--opencode", action="store_true", help="Only install OpenCode configurations")
    parser.add_argument("--antigravity", action="store_true", help="Only install Antigravity IDE configurations")
    args = parser.parse_args()

    project_name = args.project_name
    if not project_name:
        project_name = input("Enter project name: ").strip()
        if not project_name:
            print_error("Project name cannot be empty!")
            sys.exit(1)

    project_path = Path(os.getcwd()) / project_name

    if project_path.exists():
        print_error(f"Directory '{project_name}' already exists! Please choose another name.")
        sys.exit(1)

    print(f"\n🚀 Initializing Ultimate Vibe Code Workspace at: {project_path}\n")

    try:
        # Create project root directory
        project_path.mkdir(parents=True, exist_ok=False)

        # ──── 2. MONOREPO: Code structure ────
        (project_path / "apps").mkdir(exist_ok=True)
        (project_path / "packages").mkdir(exist_ok=True)
        (project_path / "infra").mkdir(exist_ok=True)
        print_step("Created monorepo structure (apps/, packages/, infra/)")

        # ──── 3. CI/CD: GitHub Actions & Prompts ────
        copy_template_dir(".github", project_path)

        # ──── 1. CORE: Core architecture directories ────
        copy_template_dir(".antigravity", project_path)     # Memory Engine & Knowledge Hub
        copy_template_dir(".agent", project_path)           # Rules + Workflows + Core Skills
        copy_template_dir(".context", project_path)         # System Prompt + Coding Style
        copy_template_dir("docs", project_path)             # Architecture docs + API + Setup + Guides
        copy_template_dir("openspec", project_path)         # Spec-Driven Development Framework
        copy_template_dir("memory", project_path)           # Agent Long-term Memory
        copy_template_dir("scripts", project_path)          # Demo & utility scripts
        copy_template_dir("agents", project_path)           # 51 AI Personas (Reviewer, Architect, Security, etc.)
        copy_template_dir("references", project_path)       # Checklists (Security, Performance, A11y, Orchestration)
        copy_template_dir("hooks", project_path)            # Session hooks, SDD cache, ECC advanced hooks
        copy_template_dir("commands", project_path)         # 79 slash commands (/plan, /tdd, /code-review, etc.)
        copy_template_dir("contexts", project_path)         # Context modes (dev, research, review)
        copy_template_dir("mcp-configs", project_path)      # Extended MCP: Jira, Supabase, Playwright, Context7...
        copy_template_dir("examples", project_path)         # CLAUDE.md templates (Django, Go, Rust, NextJS...)
        # Check if any specific IDE flag was passed
        any_ide_flag = any([args.claude, args.cursor, args.windsurf, args.gemini, args.codex, args.kiro, args.opencode, args.antigravity])

        # ──── 4. IDE & CONFIG: Bootstrap files ────
        if not any_ide_flag or args.codex or args.windsurf:
            copy_template_file("AGENTS.md", project_path)
            
        if not any_ide_flag or args.claude:
            copy_template_dir(".claude", project_path)
            copy_template_dir(".claude-plugin", project_path)
            copy_template_file("CLAUDE.md", project_path)
            
        if not any_ide_flag or args.cursor or args.windsurf:
            copy_template_dir(".cursor", project_path)
            copy_template_file(".cursorrules", project_path)
            
        if not any_ide_flag or args.gemini:
            copy_template_dir(".gemini", project_path)
            
        if not any_ide_flag or args.kiro:
            copy_template_dir(".kiro", project_path)
            
        # Common configurations for all IDEs
        copy_template_file("mcp_servers.json", project_path)
        copy_template_file("mission.md", project_path)
        copy_template_file(".env.example", project_path)
        copy_template_file(".gitignore", project_path)
        copy_template_file("SOUL.md", project_path)
        copy_template_file("COMMANDS-QUICK-REF.md", project_path)
        copy_template_file("TROUBLESHOOTING.md", project_path)

        # ──── 5. DOCKER: Containerization ────
        copy_template_file("Dockerfile", project_path)
        copy_template_file("Dockerfile.sandbox", project_path)
        copy_template_file("docker-compose.yml", project_path)

        print_success("\n🎉 Project initialized successfully!")
        print("\n" + "="*65)
        print("💡 NEXT STEPS:")
        print(f"  1. cd {project_name}")
        print("  2. cp .env.example .env  (then fill in your API keys)")
        print("  3. Open in Cursor / Windsurf / Claude Code / Antigravity")
        print("  4. Pre-installed components:")
        print("     ✅ 26 Core Skills + 1500+ in Skill Library")
        print("     ✅ 51 AI Personas (Architect, Reviewer, Security, QA...)")
        print("     ✅ 79 Slash Commands (/plan, /tdd, /code-review, /ship...)")
        print("     ✅ OpenSpec (Spec-Driven Development)")
        print("     ✅ 25+ MCP Servers (DB, GitHub, Jira, Playwright, Vercel...)")
        print("     ✅ References (Security/Performance/A11y/Orchestration)")
        print("     ✅ Hooks + Context Modes + Docker + CI/CD")
        print("     ✅ Multi-IDE: Claude, Cursor, Gemini, Kiro, Codex")
        print("     ✅ CLAUDE.md templates (Django, Go, Rust, NextJS...)")
        print("     ✅ Karpathy Guidelines (Think → Simplify → Surgical → Goal-Driven)")
        print(f"  5. Extended Skill Library (1500+):")
        print(f"     {TEMPLATE_ROOT / 'skill_library'}")
        print(f"     Copy skills as needed to {project_name}/.agent/skills/")
        print("="*65 + "\n")

    except Exception as e:
        print_error(f"An error occurred during initialization: {e}")
        # Clean up on error
        if project_path.exists():
            shutil.rmtree(project_path)
        sys.exit(1)

if __name__ == "__main__":
    main()
