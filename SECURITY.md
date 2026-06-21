# Security Policy

## Is there anything to secure?

FoundryOS is a markdown knowledge system — Modules, Skills, Agents, Workflows, and Commands are all plain-text files an AI assistant reads. There's no server, no runtime, no database, and no user data collection anywhere in the repository itself. The one piece of executable code in this repo is `scripts/generate_claude_commands.py`, a local maintenance script that reads `commands/*.md` and writes `.claude/commands/*.md` — it takes no network input and doesn't execute anything it reads.

That said, two categories of report are genuinely useful here:

- **Prompt-injection-style risk**: if you find content inside any `AGENT.md`, `SKILL.md`, `WORKFLOW.md`, or example file that could cause an AI assistant reading it to behave unsafely, exfiltrate data, or act against the user's interest when FoundryOS is loaded into a project, that's a real finding — please report it the same way as a code vulnerability, not as a normal content bug.
- **Supply-chain risk**: if a future contribution to `scripts/` ever introduces a dependency, a vulnerability in that dependency is in scope.

## Supported Versions

| Version | Supported |
|---|---|
| 4.0.x | ✅ |
| < 4.0 | ❌ |

Only the latest tagged release is actively supported. Given this is a markdown-only system with no deployed instances, there's no backporting program.

## Reporting a Vulnerability

Please **do not** open a public issue for a security concern.

Instead, use GitHub's private vulnerability reporting on this repository: go to the **Security** tab → **Report a vulnerability**. This opens a private advisory visible only to maintainers until it's resolved and ready to disclose.

If private reporting isn't available on this repository for any reason, open an issue titled `[security] <one-line summary, no details>` asking a maintainer to open a private channel — don't include exploit details in the public issue itself.

Please include:

- What file(s) are involved and why the content/behavior is unsafe.
- The realistic scenario where it causes harm (e.g. "if an assistant loads `X-Agent/AGENT.md` and a user asks Y, it produces Z").
- A suggested fix, if you have one — most fixes here are a one-line content edit, not a patch.

## Response

This is a community-maintained, markdown-only project — there's no SLA, but reports are taken seriously and addressed as soon as a maintainer is available. You'll get an acknowledgment, then a resolution or an explanation of why something is or isn't in scope.
