# Cursor Setup

Cursor reads project files directly, which makes FoundryOS feel native — no upload step required.

## Setup

1. Open the `FoundryOS` folder in Cursor (**File → Open Folder**), or copy its contents into an existing repository.
2. Add a `.cursorrules` file (or `.cursor/rules`, depending on your Cursor version) at the project root containing:

   ```
   This project uses FoundryOS as an operating system.
   Before answering any product, technical, or business question, read meta-agent/META_AGENT.md
   and act as the Meta-Agent: classify the request, select the right Agent(s) from agents/,
   and use their owned Skills.
   If a request starts with a /command, read the matching file in commands/ and follow its
   Activated Agents, Activated Skills, and Workflow exactly.
   ```

3. Open the chat panel (`Cmd/Ctrl + L`) and reference a command or file directly:

   > `/architecture` Design the system architecture for a multi-tenant analytics product. See `agents/CTO-Agent/AGENT.md` and `commands/architecture.md`.

   > `/design-system` Define color, typography, and component tokens for our product UI. See `agents/CBO-Agent/AGENT.md` and `commands/design-system.md`.

   Cursor's `@` file-reference syntax also works well here — try `@commands/architecture.md @agents/CTO-Agent/AGENT.md` in your prompt to force those files into context.

## Tip: keep context tight

Cursor's context window is shared with your actual codebase. For day-to-day use, `@`-reference only the specific `commands/`, `agents/`, or `workflows/` file you need rather than the whole repository — it keeps responses faster and more focused.
