# ChatGPT Setup

ChatGPT doesn't have native slash commands the way Claude Code does, but you can get the same behavior using Projects or a Custom GPT.

## Method 1: ChatGPT Projects

1. Create a new **Project** in ChatGPT.
2. Upload the `FoundryOS` folder's files into the Project's file area (or the most relevant subset: `meta-agent/META_AGENT.md`, `registry/AGENT_REGISTRY.md`, `registry/SKILL_REGISTRY.md`, and `commands/`).
3. Set the Project's custom instructions to:

   > Use FoundryOS as your operating system. Read `meta-agent/META_AGENT.md` and act as the Meta-Agent for every request in this project. When a message starts with a `/command`, read the matching file in `commands/` and follow its Activated Agents, Activated Skills, and Workflow.

4. Start chatting, or type a command directly:

   > `/gtm` Build a go-to-market plan for launching in a new vertical.

   > `/naming` Generate a naming shortlist for a robotics startup pivoting from B2B to B2C.

## Method 2: Custom GPT

1. Go to **Explore GPTs → Create**.
2. In the **Configure** tab, set the instructions to the same Meta-Agent instruction as above.
3. Under **Knowledge**, upload the FoundryOS files (ChatGPT has a file-count limit per Custom GPT — prioritize `meta-agent/`, `registry/`, `commands/`, and whichever `agents/` folders you'll use most).
4. Save and start a conversation with your new GPT using any command or plain-English request.

## Limitation to know about

ChatGPT reads its knowledge files when it decides they're relevant — it isn't guaranteed to open every file on every turn the way Claude Projects does. If a response seems to be missing context from a specific Agent or Skill, explicitly ask ChatGPT to open that file (e.g. "read `agents/CTO-Agent/AGENT.md` before answering") rather than assuming it already did.
