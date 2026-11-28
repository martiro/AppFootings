# AppFootings: maintainer guide for Claude Code

This repository publishes **AppFootings**, a skill that guides the analysis of an app or digital product, from the problem brief to the implementation prompts. You are maintaining the skill, not using it.

## Structure

| Path | What it is | Source of truth for |
|---|---|---|
| `app-footings/SKILL.md` | **The skill.** The only file users install | Phases, rules, levels, triggers, IDs, advisor |
| `README.md` | Public documentation | Derived from SKILL.md |
| `examples/lendloop/` | Worked example (fictional app, Standard level) | Derived from SKILL.md |
| `examples/lendloop/prototype/index.html` | Navigable prototype of the example. **Generated, never edit by hand** | — |
| `examples/reverse-analysis/` | Reverse-mode example (fictional project under way) | Derived from SKILL.md §2.1 |
| `scripts/make_images.py` | Generates every image in `docs/images/`, the walkthrough GIF and the example prototype | Images, prototype, screen drawings |
| `docs/images/` | SVG + PNG output. **Never edit by hand** | — |
| `scripts/package.sh` | Builds `dist/app-footings-<version>.zip` | — |
| `scripts/install-local.sh` | Installs the skill into `~/.claude/skills/` for testing | — |
| `.claude-plugin/marketplace.json`, `plugin.json` | Make the repo a plugin marketplace, so users install from GitHub. No `version` on purpose: installs track the latest commit | Plugin name, skill path |
| `VERSION`, `CHANGELOG.md` | Versioning | — |
| `.github/workflows/release.yml` | On a `v*` tag, builds the zip and attaches it to a GitHub release | — |

## Hierarchy and cascade (apply the skill's own rules to this repo)

`SKILL.md` → `README.md` → `examples/` → `scripts/make_images.py` → `docs/images/` and `examples/lendloop/prototype/`

Every change starts in `SKILL.md` (unless it only concerns docs or the example) and then cascades down. If you find something missing while working on a lower file, fix it in `SKILL.md` first.

### What must stay in sync between SKILL.md and README.md
- The two modes (forward and reverse) and the reverse-analysis steps
- The mindset (three competences, depth per level)
- The project-grade deliverables rule
- The list of phases and deliverables, their order, names and one-line descriptions ("Phases at a glance" in SKILL.md, "The phases and their deliverables" in README)
- The navigable prototype (what it does, levels)
- The recommended way of working (voice, chat, Claude Code)
- The change procedure and the analysis loop (SKILL.md §8 ↔ README "How documents stay aligned")
- The complexity level tables (deliverables and solution design aspects) and the legend
- The triggers table
- The ID prefixes
- The core rules, the change procedure and the advisor patterns (summarised in the README)
- The implementation prompt set (PR-00, PR-01, PR-02, PR-03…n, PR-last)
- Install instructions and the skill folder name (also `skills` in `.claude-plugin/plugin.json`; the plugin descriptions follow the SKILL.md `description`)

### What must stay in sync in the example and the images
- IDs, values and wording in `examples/lendloop/` must match each other (see its README, "Follow one feature end to end")
- The text in the images (in `make_images.py`) must match the example documents: S-02, S-04 and S-06 "What it covers" and "How it works", the P-03 header, steps, variants and screen sequence, and parameter defaults
- The prototype paths (`PATHS` in `make_images.py`) must match P-03 steps and variants, and its hotspots must sit on the drawn buttons
- The analysis loop animation (`LOOP_STEPS`) must follow SKILL.md §8 (check coherence, raise, decide, cascade, discoveries up, loop until stable), and its IDs (OP-12, OP-13, R-11, N-08, PAR-07, T-048) must match the alignment report image and the LendLoop README
- Every example document starts with the project-grade header (version, date, status, purpose)
- The document map in the images must match the SKILL.md hierarchy and level tables

## Conventions
- The skill is written in **English**. It tells Claude to talk to users and write deliverables in the user's language.
- Names: product **AppFootings**; skill and folder `app-footings` (lowercase, hyphens).
- The `description` in the SKILL.md frontmatter is short (under ~200 characters) and says when to use the skill. Keep only `name` and `description` in the frontmatter.
- The example is fictional and generic. Do not add real projects, people or brands.
- Images: run `python3 scripts/make_images.py` (needs `rsvg-convert` for PNGs). Do not commit hand-edited PNGs.

## Hero image and social preview
`hero()` in `make_images.py` draws the image at the top of the README and `docs/images/social-preview.png` (1280×640). GitHub does not read the social preview from the repository: upload it by hand in **Settings → General → Social preview** whenever it changes. Its piers must list the same deliverables as the SKILL.md hierarchy. Business & roadmap and the As-is report are deliberately left out, as separate or optional tracks.

## Release checklist
1. Update `SKILL.md`, then cascade to README, the example and the images.
2. Run the consistency check (`/consistency-check`).
3. Add an entry to `CHANGELOG.md` and bump `VERSION` (semver: major for changes to phases, hierarchy or IDs; minor for new aspects, triggers or patterns; patch for wording).
4. `scripts/package.sh` and `scripts/install-local.sh`, then try the skill on a small idea.
5. Commit, tag `v<VERSION>`, push the tag. The workflow publishes the release zip.

Custom commands in `.claude/commands/`: `/consistency-check`, `/release`.
