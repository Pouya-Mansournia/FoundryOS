# Tutorials

## Beginner

**Tutorial 1 — Your first command.** Pick anything you're actually working on. Run `/prd` against it. Read the PRD that comes back and check: does the problem statement match what you actually meant? If not, correct it in your next message — the system builds on whatever you confirm, so catching a wrong assumption early is cheap.

**Tutorial 2 — Reading an Agent file.** Open `agents/CPO-Agent/AGENT.md`. Notice it's short: a mandate and a list of Skills, nothing else. This is deliberate — Agents don't hold knowledge directly, they point at Skills that do. Now open one of those Skills' `SKILL.md` files and see the actual "what this does / source modules / output" structure underneath.

**Tutorial 3 — Plain English vs. commands.** Ask the same question two ways: once as `/strategy Should we raise a seed round now or wait six months?`, and once as plain English with no command at all. Compare the two responses. They should converge on similar reasoning — commands are a shortcut to the same routing the Meta-Agent does on its own, not a different system.

## Intermediate

**Tutorial 4 — Chaining commands.** Run `/prd`, then feed its output into `/architecture`, then `/finance`. Notice each command consumes the previous one's output rather than starting cold — this mirrors the dependency chain in `knowledge-graph/ARTIFACT_GRAPH.md` (Problem Statement → PRD → Architecture → Financial Model).

**Tutorial 5 — Running a full Workflow.** Open `workflows/02-saas-product-workflow/WORKFLOW.md` and read it end to end. Then try to get the same outcome by running its component commands in order (`/cpo` → `/cto` → `/cro`) instead of invoking the Workflow as a single block. Compare which approach gave you more control over intermediate checkpoints.

**Tutorial 6 — Using the Critic.** Take any plan you've built and run `/critic` on it before treating it as final. Read its "Red Flags" section specifically — that's the one section designed to surface things the original Agent didn't think to mention.

## Advanced

**Tutorial 7 — Closing the loop with Memory.** After a real outcome happens (a launch, a hire, a pricing change), run `/reflection` and check that it writes something concrete into `memory/lessons-learned.md` — not a generic platitude, but a specific, falsifiable lesson tied to what actually happened. Then start a new, unrelated session and confirm the system references that lesson unprompted the next time a similar decision comes up.

**Tutorial 8 — Adding a Skill.** Pick a real gap in your own workflow that none of the 58 Skills cover well. Draft a new `SKILL.md` (purpose, source modules, output) following the format in any existing `skills/{NN}-{name}-skill/SKILL.md`, add it to the right Agent's `AGENT.md`, and update `registry/SKILL_REGISTRY.md`. This is the same process described in [`CONTRIBUTING.md`](../CONTRIBUTING.md).

**Tutorial 9 — Building a new command.** Once you've used the system for a while, you'll notice a request shape you run often that doesn't have a dedicated command. Write a new `commands/{name}.md` following the template in any existing command file, add it to [`COMMANDS.md`](../COMMANDS.md)'s table, and (if using Claude Code) copy it into `.claude/commands/`.

**Tutorial 10 — Tracing the Knowledge Graph.** Before changing anything structural (reassigning a Skill, merging two Agents), read `knowledge-graph/AGENT_GRAPH.md` and `knowledge-graph/SKILL_GRAPH.md` first to see what depends on what. This is the same discipline the system's own version history followed — see `CHANGELOG.md`'s v0.9 entry for a real example of a structural change made carefully, in order, rather than all at once.

**Tutorial 11 — Building a brand end to end, then reusing it.** Run `/brand` against a real idea to get an archetype, a naming shortlist, and a positioning statement. Then, in a *separate* session, run `/website` or `/copy` against the same idea and check whether the output references the archetype and positioning you just locked in — read from `memory/brand-memory.md` — instead of inventing a new tone from scratch. This is the same check `tests/07-brand-consistency-test.md` automates, and it's the clearest demonstration that Brand OS is woven into Memory rather than living in CBO-Agent's output alone.
