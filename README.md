# le-unslop

Make AI-written French read like a French person wrote it.

`le-unslop` is an agent skill that removes AI tells from French text and applies French (France) typography. It covers rewrites, translations into French, emails, letters, marketing copy and social posts.

## Before and after

A gîte web page from the test set:

> Niché au cœur du Luberon, à seulement 2 km de Gordes, notre gîte d'exception allie charme authentique et confort moderne pour vous offrir une expérience inoubliable. Que vous soyez en quête de détente ou d'aventure, nos 5 chambres raffinées sont une véritable invitation à l'évasion. Profitez de notre piscine chauffée (de mai à septembre) et d'un petit-déjeuner gourmand servi de 8h à 10h. Plus qu'un simple hébergement, c'est un art de vivre. Tarif : à partir de 95€ la nuit. N'attendez plus, réservez dès maintenant !

The same page rewritten with the skill, unedited test output:

> Notre gîte se trouve dans le Luberon, à 2 km de Gordes, et compte cinq chambres. La piscine est chauffée de mai à septembre. Le petit-déjeuner est servi de 8 h à 10 h.
>
> La nuit est à partir de 95 €.
>
> Réservation : [à préciser : téléphone, adresse e-mail ou lien de réservation]

The puffery is gone, every practical fact survives, and the typography follows French rules (`8 h`, `95 €`, a non-breaking space before `:`). Where a fact is missing, the skill leaves a placeholder instead of inventing one.

## What it fixes

The skill works on three causes rather than a word list, because lists of AI words go stale:

- **No referent.** Sentences with no concrete fact behind them. The skill puts the fact in or cuts the sentence.
- **Symmetry.** Forced contrasts ("Ce n'est pas X, c'est Y"), triplets, conclusions that repeat the introduction.
- **English translated into French.** Calques ("adresser un problème", "J'espère que vous allez bien"), English typography, translated email formulas.

It also enforces non-breaking spaces before `: ; ! ?` and inside `« »`, French number formats, and French letter conventions. In letters it keeps the expected formulas and cuts the stacked extras.

## Install

The repo is the skill: `SKILL.md` sits at the root. Clone it into a skill directory under the name `le-unslop`:

| Agent | Project | User-wide |
|---|---|---|
| Claude Code | `.claude/skills/le-unslop` | `~/.claude/skills/le-unslop` |
| Codex | `.agents/skills/le-unslop` | `~/.agents/skills/le-unslop` |
| OpenCode | `.opencode/skills/le-unslop` | `~/.config/opencode/skills/le-unslop` |

```sh
git clone https://github.com/painhardcore/le-unslop ~/.claude/skills/le-unslop
```

Update with `git -C ~/.claude/skills/le-unslop pull`. The skill triggers on any French writing task and has no dependencies.

For Codex, install user-wide with:

```sh
mkdir -p ~/.agents/skills
git clone https://github.com/painhardcore/le-unslop ~/.agents/skills/le-unslop
```

Update with `git -C ~/.agents/skills/le-unslop pull`. Check `/skills` and invoke `$le-unslop`. Codex detects changes automatically; restart it if the skill does not appear. See the [official Codex skill discovery documentation](https://learn.chatgpt.com/docs/build-skills).

## Test

Run the spacing checker's regression tests with Python 3:

```sh
python3 -m unittest discover -s evals -p 'test_*.py' -v
```

The optional checker accepts UTF-8 files containing plain France French prose. It reports incorrect spaces without modifying the file. Exclude technical literals, verbatim quotations, and numeric times such as `13:52` before using it. It does not parse Markdown or validate writing style.

`evals/evals.json` contains writing tasks and behavioral regression cases for preserving facts, technical literals, tone, regional conventions, and review output. Evaluate each prompt in a fresh conversation with the skill loaded, without showing the model `expected_output`. Compare the response against those criteria. Save the raw responses, model, settings, skill revision, and judging criteria alongside any reported results. These behavioral cases are separate from the automated spacing tests.

The [recorded regression run](evals/results/2026-10-16.json) includes seven raw responses, criteria, assessments, and file hashes. All seven passed review. It used one independent evaluator context and one response per case, without a baseline comparison or a test of automatic skill discovery. The exact model identifier was unavailable.

## What testing showed

An earlier evaluation used three tasks: rewriting a gîte web page, translating an email to a landlord, and writing a LinkedIn funding post. A blind AI judge scored each output from 1 to 10, with one run per configuration. The model, settings, rubric, and raw responses were not saved in this repository, so these historical scores cannot be independently verified and do not validate the current revision.

| Task | With skill | Without skill |
|---|---|---|
| Gîte web page | 7 | 4 |
| LinkedIn post | 8 | 3 |
| Email to landlord | 7 | 8 to 9 |

The earlier evaluation reported invented facts in the baseline LinkedIn post and none in the outputs using the skill. One run per configuration is insufficient to establish a reliable improvement; the landlord email also scored lower with the skill.

## Contents

```text
SKILL.md                   the skill
references/typographie.md  French typography details
references/sources.md      research sources and limits
evals/evals.json           test tasks
```

## Sources

See `references/sources.md`. No French corpus study of AI writing was found. The patterns come from French writing guides and blogs that agree with each other.

## License

MIT. See [LICENSE](LICENSE).
