---
description: Check that SKILL.md, README, the LendLoop example and the images are aligned
---

Run a consistency check of this repository, following the "Hierarchy and cascade" section of CLAUDE.md.

1. Read `app-footings/SKILL.md` and extract: phases and deliverables (names and order), level tables, legend, triggers, ID prefixes, prompt set, skill folder name.
2. Compare them with `README.md`, section by section. List every difference.
3. In `examples/lendloop/`, check that IDs, defaults and wording match across all documents (follow the "Follow one feature end to end" table) and that every linked file and anchor exists.
4. Compare the texts embedded in `scripts/make_images.py` with the example documents and with the SKILL.md hierarchy. Check that the prototype paths match the P-03 steps and variants.
5. Check `examples/reverse-analysis/` against SKILL.md §2.1: As-is report outline, provenance tags, AS- IDs, change prompts.
6. Check that the frontmatter has only `name: app-footings` and a short `description`.

Report the results as a list: issue → files involved → proposed fix. Do not change anything until I confirm. Then apply the fixes in hierarchy order and finish with an alignment report (updated / not yet aligned).
