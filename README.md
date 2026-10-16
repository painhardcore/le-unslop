# le-unslop

`le-unslop` is an agent skill that removes AI tells from French text and applies French (France) typography. It covers rewrites, translations into French, emails, letters, marketing copy and social posts.

The skill works on three causes rather than a word list:

- Sentences with no concrete fact behind them.
- Symmetry: forced contrasts, triplets, conclusions that repeat the introduction.
- English translated into French: calques, English typography, translated email formulas.

It also enforces non-breaking spaces before `: ; ! ?` and inside `« »`, French number formats, and French letter conventions.

## Install

The repo is the skill: `SKILL.md` sits at the root. Clone it into a skill directory under the name `le-unslop`:

| Agent | Project | User-wide |
|---|---|---|
| Claude Code | `.claude/skills/le-unslop` | `~/.claude/skills/le-unslop` |
| Codex | `.agents/skills/le-unslop` | see the Codex documentation |
| OpenCode | `.opencode/skills/le-unslop` | `~/.config/opencode/skills/le-unslop` |

```sh
git clone https://github.com/painhardcore/le-unslop ~/.claude/skills/le-unslop
```

Update with `git -C ~/.claude/skills/le-unslop pull`. The skill triggers on any French writing task and has no dependencies.

## What testing showed

`evals/evals.json` holds three tasks: rewriting a gîte web page, translating an email to a landlord, and writing a LinkedIn funding post. A blind AI judge scored each output from 1 to 10, with one run per configuration.

| Task | With skill | Without skill |
|---|---|---|
| Gîte web page | 7 | 4 |
| LinkedIn post | 8 | 3 |
| Email to landlord | 7 | 8 to 9 |

Without the skill, the LinkedIn post invented facts. With the skill, no output invented anything. For formal letters, the base model already writes well and the skill adds little beyond typography. One run per configuration means gaps of one or two points may be noise.

## Sources

See `references/sources.md`. No French corpus study of AI writing was found. The patterns come from French writing guides and blogs that agree with each other.
