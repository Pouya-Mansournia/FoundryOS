# Windsurf Setup

Windsurf, like Cursor, works directly against project files — FoundryOS drops in the same way.

## Setup

1. Open the `FoundryOS` folder as a Windsurf workspace.
2. Add a rules file at the project root (Windsurf supports a `.windsurfrules` file) containing:

   ```
   This workspace uses FoundryOS as an operating system.
   Before answering any product, technical, or business question, read meta-agent/META_AGENT.md
   and act as the Meta-Agent: classify the request, select the right Agent(s) from agents/,
   and use their owned Skills.
   If a request starts with a /command, read the matching file in commands/ and follow its
   Activated Agents, Activated Skills, and Workflow exactly.
   ```

3. Open Cascade (Windsurf's AI panel) and run a command:

   > `/finance` Build an 18-month cash flow model under best/base/worst-case assumptions. Reference `commands/finance.md` and `agents/CFO-Agent/AGENT.md`.

   > `/voice` Define our brand's tone of voice and a banned-phrases list for support and marketing copy. Reference `commands/voice.md` and `agents/CBO-Agent/AGENT.md`.

## Tip

Windsurf's Cascade tends to proactively read referenced files when you name them explicitly — naming the exact `commands/{name}.md` and `agents/{Role}-Agent/AGENT.md` files in your first message of a session is the most reliable way to get correct routing before Cascade has built up its own sense of the codebase.
