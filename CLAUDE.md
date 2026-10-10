# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## State of the project

Pre-production. **No Unity project exists yet** — no `Assets/`, no build/lint/test setup. Only planning artifacts and an economy simulator exist. Not a git repo.

Game: "Aquário Incremental", idle/incremental game for PC in Unity, solo dev (Murilo). Contemplative: income comes only from fish (tanks are stage + capacity), no randomness, events or game over. Docs and data are in Brazilian Portuguese (`document_output_language = Português (Brasil)`); keep new docs/data in pt-BR, identifiers in existing CSV style (snake_case pt-BR).

Source of truth for design: `_bmad-output/planning-artifacts/briefs/brief-aquario-incremental-2026-10-09/brief.md` (status: draft; `[ASSUMPTION]` tags mean unconfirmed), plus `addendum.md`, `.decision-log.md` and `_bmad-output/brainstorming-session-2026-10-09.md` (idea numbers like `#055` in code/data refer to this).

## Commands

Only runnable code is the economy simulator (run from `_bmad-output/dados/`; default CSV path is relative to cwd):

```
cd _bmad-output/dados
python sim_economia.py            # uses species.csv
python sim_economia.py other.csv
```

## Architecture

**Data-driven economy, calibrated before art/content.** Brief mandates: tune economy in simulator first, then produce content per tank.

- `_bmad-output/dados/species.csv` — species: `custo_base`, `razao_custo` (cost = base × ratio^copies owned, applies to cheap fish too), `renda_base_por_seg`, `cota_max`, `libera_apos_ter` (unlock rule `especie:qtd`), plus art fields (`sprite_base`, `paleta`).
- `_bmad-output/dados/tanks.csv` — tanks: `ordem`, `preco`, `capacidade_total`, `max_animados` (rest rendered as counter), `libera_prestigio` (penultimate tank), `ativo_no_prototipo`. Tank prices for tanks 2–3 are uncalibrated drafts; first sim showed tank 2 too cheap.
- `_bmad-output/dados/sim_economia.py` — greedy bot: always buys option with lowest payback time (cost / income gain), 48h cap. Hardcodes tank filter `agua_doce_01`, shoal milestones ×2 income at 25/50/100 copies (`MARCOS`), and starting money 10. Does not yet simulate tanks/prestige/shop.

Planned game rules (from brief): loop buy fish → income → buy more fish/new tank → prestige (Pérolas, tide shop with soft cap per shelf) at penultimate tank → rerun to final giant tank; small offline progress cap; multiple tanks coexist and keep earning. Prototype step 1 = single tank, ~5 species, exponential cost, income, quota, offline progress, save. Step 2 (only after step 1 approved) = 2nd tank, tank purchase, prestige with one shop item.

If a Unity implementation is added, the CSVs should remain the data source (keep them and the simulator in sync with whatever the game loads).

## BMAD tooling

`_bmad/` (installer-managed config; `_bmad/config.toml` is regenerated — put overrides in `_bmad/custom/config.toml` or `config.user.toml`) and `.claude/skills/` (bmad-*/gds-* skills) are workflow tooling, not game code. Outputs go to `_bmad-output/` (`planning-artifacts`, `implementation-artifacts`, `dados`).

## Workflow between chats

The user clears the chat after each task and just says "siga o proximo passo" (or similar). Then:
1. Take the next unchecked item of `game/docs/backlog-v1.md` (section 14 has the order; skip items marked DECIDIR until the dev answers section 13; one item per chat; tank/species roster lives in `game/docs/conteudo-tanques.md`); history lives in `game/docs/estado/`. Backlog was derived from the game brief; the workflow was copied from another game, so adjust it if it stops fitting.
2. Build features only; balancing waits until the last item of the queue (placeholder values are fine, don't ask for bot runs).
3. When done: check/annotate the backlog item, add a short entry to the matching theme file in `game/docs/estado/` (files `01-*` to `07-*`, or a new `NN-*.md`), and end the reply with a numbered "Como testar".

Each entry in `game/docs/estado/*.md` should say: what changed, which scenes to regenerate, whether `Create Default Data` is needed, what the bot/CSV does with it, and what was/wasn't verified (compiled with csc vs run in Test Runner vs seen in Editor).
