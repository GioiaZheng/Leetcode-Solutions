# Changelog

A coarse-grained log of work organised by **round** (a coherent batch of
commits with a single goal). Individual commits live in `git log`; this
file exists to give a future reader the *why* and *what changed at a
glance* without having to reconstruct it.

Newest first. Each round cites its constituent commits by short SHA.

---

## Unreleased — Navigation polish (`infra/navigation-polish` branch)

Goal: take the AI-card + paths machinery shipped in the standards-foundation
v2 round and make it visibly usable. Add a curated "Where to start" entry
point on the landing page, enforce that AI-card README sections and the
metadata `ai_card_status` field cannot drift apart, and consolidate the
local check workflow into a single `make check`.

Five commits on top of `b61e63d` (the v2 merge commit on `main`):

- **`feat(topics): add Paths and AI Card columns to TOPICS.md tables`**
  (`575055e`, landed directly on `main` after the v2 merge). Mirrors
  CATALOG.md's 8-column schema so a visitor browsing by topic sees
  the same path / AI-card information they would see in the full
  catalog or in a path README.

- **`feat(featured): add "Where to start" curated entry-point section`**
  (`f608a45`). New `scripts/generate_featured.py` emits the `ai_card_status:
  reviewed` problems as a five-column table between FEATURED_LIST
  sentinels in `README.md`. A `PRIMARY_CATEGORY_SPECIFICITY` ranking
  picks each problem's primary pattern (most-specific wins) instead of
  the lazy first-topic heuristic, which would otherwise lump 6/9
  showcases into "Arrays & Matrices" and lose the diversity signal.

- **`feat(validate): enforce AI-card README and metadata stay in sync`**
  (`272f58b`). New `validate_ai_card_consistency()` cross-checks every
  problem README's marker heading (`## Brute-force baseline`, unique to
  the AI-card extension) against the corresponding `ai_card_status`
  entry in `metadata.json`. Errors are reported in both directions
  (sections without status; status without sections). Three new pytest
  cases cover both failure modes plus the well-formed accept path.
  Suite grows 30 → 33.

- **`infra(make): add Makefile consolidating the local check workflow`**
  (`5369572`). One verb (`make check`) runs everything CI runs:
  validate, sync-check (regenerate + diff-exit-code on
  CATALOG/TOPICS/README/paths), ruff, compileall, pytest, security
  scan. `PYTHON ?= python` so CI works as-is; mac developers without a
  `python` symlink can `PYTHON=python3 make check`.

- **`docs: cross-link Where to start from notes; promote make check`**
  (`b56e016`). Blockquote at the top of `0000-notes/README.md` points
  readers to the README "Where to start" curated showcase list.
  `CONTRIBUTING.md` "Local Checks" section now leads with `make check`,
  with the individual commands preserved beneath it for explicit-control
  readers.

Result: **reviewed AI cards are surfaced in four places** (README
"Where to start" table, CATALOG.md `AI Card` column, TOPICS.md `AI
Card` column, paths/blind75/README.md `AI Card` column), all kept in
sync by `make sync` / `make sync-check` and enforced by CI.

### High-frequency showcases (same branch)

Additional showcase work on top of the navigation-polish infrastructure.
These commits exercise the new flow (CHANGELOG entry per commit,
auto-injected counts, AI-card consistency validator) rather than just
documenting it.

- **`feat(showcase): create 0042 Trapping Rain Water from scratch`**.
  The problem did not exist in `problems/` before --- this is the
  first new-problem-from-scratch entry on the branch, not a migration
  of an existing README. Adds the `problems/0042-trapping-rain-water/`
  directory with a two-pointer O(n) / O(1) solution, the standard six
  required README sections, and all five AI-card sections (brute-force
  baseline, common mistakes, failure cases, interview follow-ups,
  bilingual summary). Tagged `path_membership: ["blind75"]` and
  `ai_card_status: "reviewed"` in `metadata.json`. Blind 75 path now
  10/75 (all 10 reviewed); Hard difficulty count moves from 18 to 19.

---

## 2026-05-27 — Standards foundation v2 (merged as `b61e63d`)

Goal: introduce the AI-card README extension and a `paths/` framework
without breaking any of the 98 existing problem entries. Add two
optional metadata fields (`path_membership`, `ai_card_status`) gated by
a draft / reviewed / interview-ready review workflow so AI-assisted
content cannot land in the repo unreviewed.

The round splits into two sub-rounds.

### Foundation (5 commits, sets the contract)

- **`docs(contributing): add optional metadata, ai-card, paths sections`**
  (`b4e042d`). Documents the two new optional fields, the five
  append-only "AI card" README sections (Brute-force baseline, Common
  mistakes, Failure cases, Interview follow-ups, Bilingual summary),
  and the `paths/` directory structure.
- **`feat(template): add optional AI-card and bilingual sections`**
  (`d330d0d`). Extends `templates/problem_README.md` with the five
  optional headings after the six locked core sections.
- **`feat(validate): accept optional path_membership and ai_card_status`**
  (`2c9efcb`). Extends `scripts/validate_repo.py` with
  `VALID_PATH_MEMBERSHIPS = {blind75, neetcode150}` and
  `VALID_AI_CARD_STATUSES = {draft, reviewed, interview-ready}`.
  Three new pytest cases.
- **`feat(paths): add Blind 75 path skeleton and generator script`**
  (`1093277`). `paths/blind75/README.md` with seven hand-written
  sections + one regenerated Problem List between sentinels. New
  `scripts/generate_path.py` wired into `update_indexes.py`. CI diff
  check extended to cover `paths/*/README.md`.
- **`feat(showcase): migrate 0001-two-sum to AI-card template`**
  (`ca99d1a`). First showcase, tagged `path_membership: ["blind75"]`
  and `ai_card_status: "reviewed"`.

### Content (7 commits, exercises the contract)

- **`feat(metadata): tag 8 more Blind 75 problems`** (`b2cb3f3`):
  `0003`, `0005`, `0011`, `0015`, `0049`, `0121`, `0242`, `0347`.
- **Six more showcase migrations**: `0121` (`467a0b7`), `0242`
  (`863c40c`), `0049` (`cd3eaf5`), `0011` (`880ff9a`), `0003`
  (`49b9910`), `0005` (`09b8331`), `0015` (`7d732a1`), `0347`
  (`27c8df0`). Each migration is append-only on the existing README
  (the original write-up survives verbatim) and adds
  `ai_card_status: "reviewed"`.
- **`docs(readme): surface paths/ framework on the landing page`**
  (`606f6a0`). Adds the `paths/` entry to the top-level README's
  Highlights, Repository Overview, and a new "Learning Paths" section.
- **`feat(catalog): surface Paths and AI Card columns in CATALOG.md`**
  (`59eac12`). CATALOG.md table widens from 6 to 8 columns; 200 lines
  of row churn, zero data change beyond the newly-visible fields.
- **`feat(stats): auto-inject blind75 and reviewed-AI-card counts`**
  (`2f16497`). Two new METRIC_MARKER entries
  (`BLIND75_COUNT` / `REVIEWED_AI_CARDS`) so the README's "9/75" and
  "9 reviewed" numbers stay live as the repo grows.
- **`feat(paths): add AI Card column to path Problem List tables`**
  (`282795a`). 5 columns → 6 columns on `paths/<p>/README.md`.

Outcome: 9/75 Blind 75 problems tagged, all nine carrying a reviewed
AI card. CATALOG.md / TOPICS.md / paths/blind75/README.md all
in-sync, regenerated by a single `python scripts/update_indexes.py`.

Sub-branch `infra/standards-foundation-v2` was abandoned earlier:
its v1 (`infra/standards-foundation`, two commits `fc99374` +
`e7decf5`) was based on the assumption that problem directories lived
flat at the repo root, which `0845a1a refactor: organize problems
under problems directory` (2026-05-26 on `main`) overturned. The v2
sub-branch was re-done on top of the new layout; v1 never landed and
its remote ref was never created.

---

## Prior

Pre-foundation tooling — `metadata.json`, `scripts/validate_repo.py`,
`scripts/generate_catalog.py`, `scripts/update_stats.py`,
`templates/problem_README.md`, the initial CI workflow — was
introduced through Codex agent PRs #26 / #27 (May 2026), the
problems/ physical reorganisation in `0845a1a`, and the
`scripts/security_scan.py` / `scripts/update_indexes.py` pair added
in `5788257` / `1cc7589`. See `git log` between repository creation
and `1cc7589` for individual commits.
