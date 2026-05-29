# Changelog

A coarse-grained log of work organised by **round** (a coherent batch of
commits with a single goal). Individual commits live in `git log`; this
file exists to give a future reader the *why* and *what changed at a
glance* without having to reconstruct it.

Newest first. Each round cites its constituent commits by short SHA.

---

## Unreleased — Post-merge polish on `main`

Direct-on-`main` follow-up work after the navigation-polish round
merged as `5e6b02f`. Roughly three threads, in order:

**Visibility & cross-linking**
- `9d237aa` `feat(metadata): populate NeetCode 150 with 12 problems` ---
  extend `path_membership` of all 10 Blind 75 entries to include
  `"neetcode150"`, then add `0004` Median of Two Sorted Arrays and
  `0010` Regular Expression Matching as NeetCode-only entries.
- `0bb2d49` `feat(indexes): turn Study Card cells into clickable links to
  the brute-force section` --- wrap every non-empty `Study Card` cell in
  `CATALOG.md`, `TOPICS.md`, and `paths/<p>/README.md` with a markdown
  link pointing at `<problem>/README.md#brute-force-baseline`, so
  readers reach the extended write-up in one jump.

**High-frequency hard showcases**
- `146d7fc` `feat(showcase): create 0042 Trapping Rain Water from
  scratch` --- the first new-problem-from-scratch entry on `main`
  (Blind 75 had a gap). Two-pointer O(n)/O(1) solution + full AI
  card.
- `b4acdbb` `feat(showcase): migrate 0085 Maximal Rectangle to Study Card
  template` --- the only reviewed study card without `path_membership`.
  Documented as an intentional "orphan" pattern, not a schema gap: a
  problem can carry `study_card_status` without belonging to any
  curated path (e.g. a high-frequency interview hard that is not on
  Blind 75 or NeetCode 150). Surfaces in the README "Where to
  start" featured table and in CATALOG / TOPICS `Study Card` columns,
  but does NOT appear in any `paths/<p>/README.md`.
- `98dbc48` `feat(showcase): migrate 0004 median-of-two-sorted-arrays
  to Study Card`.
- `58482bf` `feat(showcase): migrate 0010 regular-expression-matching
  to Study Card`.

**Path framework deepening**
- `3bd64ed` `feat(validate): accept optional milestones field per
  problem` --- new optional metadata field
  `milestones: {path_id: milestone_id}`, validated per path. Adds
  three pytest cases. Suite grows 33 -> 36.
- `4580141` `feat(paths): auto-generate Milestones tables from
  metadata` --- replace hand-written milestone bullet lists with
  `<!-- MILESTONES_START -->` / `<!-- MILESTONES_END -->` sentinel
  blocks; `render_milestones()` in `generate_path.py` emits a
  5-column table (id / name / canonical / in-repo / reviewed) with
  bold Total row. Per-path milestone definitions (
  `PATH_MILESTONE_DEFS`) hardcoded in the generator: 6 milestones
  for Blind 75, 18 for NeetCode 150. Tag the 12 path-tagged
  showcase problems with their milestone classifications.

**This commit** (no SHA yet, see `git log -1` after landing)
- Featured table gains a Paths column between Difficulty and
  Primary topic, so a reader sees membership inline without
  scrolling down to CATALOG. 0085 is visible as the only row with
  an empty Paths cell --- the orphan-showcase pattern made
  visually explicit.
- `CONTRIBUTING.md` updated: documents the new `milestones`
  optional field; documents the path/Study Card independence
  invariant (an `study_card_status: reviewed` entry can omit
  `path_membership` --- the 0085 pattern); documents that adding a
  new curated path requires updates in four places
  (CONTRIBUTING.md, `VALID_PATH_MEMBERSHIPS`,
  `VALID_MILESTONE_IDS_PER_PATH`, `PATH_MILESTONE_DEFS`).
- Path README structure description updated: now lists both the
  Problem List and Milestones sentinels and which fields drive
  each.

---

## Unreleased — Navigation polish (`infra/navigation-polish` branch)

Goal: take the Study Card + paths machinery shipped in the standards-foundation
v2 round and make it visibly usable. Add a curated "Where to start" entry
point on the landing page, enforce that Study Card README sections and the
metadata `study_card_status` field cannot drift apart, and consolidate the
local check workflow into a single `make check`.

Five commits on top of `b61e63d` (the v2 merge commit on `main`):

- **`feat(topics): add Paths and Study Card columns to TOPICS.md tables`**
  (`575055e`, landed directly on `main` after the v2 merge). Mirrors
  CATALOG.md's 8-column schema so a visitor browsing by topic sees
  the same path / Study Card information they would see in the full
  catalog or in a path README.

- **`feat(featured): add "Where to start" curated entry-point section`**
  (`f608a45`). New `scripts/generate_featured.py` emits the `study_card_status:
  reviewed` problems as a five-column table between FEATURED_LIST
  sentinels in `README.md`. A `PRIMARY_CATEGORY_SPECIFICITY` ranking
  picks each problem's primary pattern (most-specific wins) instead of
  the lazy first-topic heuristic, which would otherwise lump 6/9
  showcases into "Arrays & Matrices" and lose the diversity signal.

- **`feat(validate): enforce Study Card README and metadata stay in sync`**
  (`272f58b`). New `validate_study_card_consistency()` cross-checks every
  problem README's marker heading (`## Brute-force baseline`, unique to
  the Study Card extension) against the corresponding `study_card_status`
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

Result: **reviewed study cards are surfaced in four places** (README
"Where to start" table, CATALOG.md `Study Card` column, TOPICS.md `AI
Card` column, paths/blind75/README.md `Study Card` column), all kept in
sync by `make sync` / `make sync-check` and enforced by CI.

### High-frequency showcases (same branch)

Additional showcase work on top of the navigation-polish infrastructure.
These commits exercise the new flow (CHANGELOG entry per commit,
auto-injected counts, Study Card consistency validator) rather than just
documenting it.

- **`feat(showcase): create 0042 Trapping Rain Water from scratch`**.
  The problem did not exist in `problems/` before --- this is the
  first new-problem-from-scratch entry on the branch, not a migration
  of an existing README. Adds the `problems/0042-trapping-rain-water/`
  directory with a two-pointer O(n) / O(1) solution, the standard six
  required README sections, and all five Study Card sections (brute-force
  baseline, common mistakes, failure cases, interview follow-ups,
  bilingual summary). Tagged `path_membership: ["blind75"]` and
  `study_card_status: "reviewed"` in `metadata.json`. Blind 75 path now
  10/75 (all 10 reviewed); Hard difficulty count moves from 18 to 19.

- **`feat(showcase): migrate 0085 Maximal Rectangle to Study Card`**.
  Append-only Study Card migration of the existing 0085 README (the
  original write-up survives verbatim). Five sections added: O(R^3 C^3)
  brute-force baseline + O(R^2 C) compress-rows alternative; common
  mistakes specific to the histogram + monotonic stack pattern
  (sentinel-0 flush, character-vs-int comparison, off-by-one on popped
  width); three failure cases including the canonical example;
  interview follow-ups pointing at LC 84 (Largest Rectangle in
  Histogram, the inner subroutine) and LC 221 (Maximal Square, the
  cousin DP).

  Deliberately NOT tagged with `path_membership` --- 0085 is not on
  the canonical Blind 75 or NeetCode 150 lists. It surfaces in the
  README "Where to start" featured list (`study_card_status` filter) and
  in CATALOG / TOPICS columns, but it does not appear in any
  `paths/<p>/README.md`. Reviewed study card count moves from 10 to 11.

### Second curated path

- **`feat(paths): scaffold NeetCode 150 path`**. Creates
  `paths/neetcode150/README.md` mirroring the structure of
  `paths/blind75/README.md` --- seven hand-written sections
  (Overview, Prerequisites, Milestones, Pattern Notes,
  Mock-Interview Tips, Weekly Plan) plus the auto-regenerated
  Problem List between sentinels. The eighteen NeetCode milestones
  (Arrays & Hashing, Two Pointers, Sliding Window, Stack, Binary
  Search, Linked List, Trees, Tries, Heap, Backtracking, Graphs,
  Advanced Graphs, 1-D DP, 2-D DP, Greedy, Intervals, Math &
  Geometry, Bit Manipulation) are documented up front with
  problem-count targets per milestone, plus a 12-week study plan
  pacing 12--14 problems per week.

  No problems are tagged with `"neetcode150"` yet, so the auto-
  generated Problem List shows the empty-state placeholder. As
  problems gain the tag in metadata.json, the list auto-populates
  on `make sync`. The validator (`VALID_PATH_MEMBERSHIPS = {blind75,
  neetcode150}`, set since `2c9efcb`) already accepts the
  identifier, so no script change is needed.

- **`feat(metadata): populate NeetCode 150 with 12 problems`**. Tag
  every Blind 75 problem in `metadata.json` with both `"blind75"` and
  `"neetcode150"` (NeetCode 150 is a strict superset, so the
  membership extension is structurally honest), plus add two
  NeetCode-only problems already in the repo: `0004` Median of Two
  Sorted Arrays (Binary Search milestone) and `0010` Regular
  Expression Matching (2-D DP milestone). The other 87 repo
  problems are mostly weekly-contest entries that do not appear on
  either canonical list.

  `paths/neetcode150/README.md` auto-populates with 12/150
  problems: the 10 from Blind 75 (all `study_card_status: reviewed`)
  plus `0004` and `0010` (untagged Study Card column for both).
  `paths/blind75/README.md` is unchanged --- still 10/75 problems,
  membership intersection is honored.

---

## 2026-05-27 — Standards foundation v2 (merged as `b61e63d`)

Goal: introduce the Study Card README extension and a `paths/` framework
without breaking any of the 98 existing problem entries. Add two
optional metadata fields (`path_membership`, `study_card_status`) gated by
a draft / reviewed / interview-ready review workflow so expanded review notes cannot land in the repo unreviewed.

The round splits into two sub-rounds.

### Foundation (5 commits, sets the contract)

- **`docs(contributing): add optional metadata, study-card, paths sections`**
  (`b4e042d`). Documents the two new optional fields, the five
  append-only "study card" README sections (Brute-force baseline, Common
  mistakes, Failure cases, Interview follow-ups, Bilingual summary),
  and the `paths/` directory structure.
- **`feat(template): add optional Study Card and bilingual sections`**
  (`d330d0d`). Extends `templates/problem_README.md` with the five
  optional headings after the six locked core sections.
- **`feat(validate): accept optional path_membership and study_card_status`**
  (`2c9efcb`). Extends `scripts/validate_repo.py` with
  `VALID_PATH_MEMBERSHIPS = {blind75, neetcode150}` and
  `VALID_STUDY_CARD_STATUSES = {draft, reviewed, interview-ready}`.
  Three new pytest cases.
- **`feat(paths): add Blind 75 path skeleton and generator script`**
  (`1093277`). `paths/blind75/README.md` with seven hand-written
  sections + one regenerated Problem List between sentinels. New
  `scripts/generate_path.py` wired into `update_indexes.py`. CI diff
  check extended to cover `paths/*/README.md`.
- **`feat(showcase): migrate 0001-two-sum to Study Card template`**
  (`ca99d1a`). First showcase, tagged `path_membership: ["blind75"]`
  and `study_card_status: "reviewed"`.

### Content (7 commits, exercises the contract)

- **`feat(metadata): tag 8 more Blind 75 problems`** (`b2cb3f3`):
  `0003`, `0005`, `0011`, `0015`, `0049`, `0121`, `0242`, `0347`.
- **Six more showcase migrations**: `0121` (`467a0b7`), `0242`
  (`863c40c`), `0049` (`cd3eaf5`), `0011` (`880ff9a`), `0003`
  (`49b9910`), `0005` (`09b8331`), `0015` (`7d732a1`), `0347`
  (`27c8df0`). Each migration is append-only on the existing README
  (the original write-up survives verbatim) and adds
  `study_card_status: "reviewed"`.
- **`docs(readme): surface paths/ framework on the landing page`**
  (`606f6a0`). Adds the `paths/` entry to the top-level README's
  Highlights, Repository Overview, and a new "Learning Paths" section.
- **`feat(catalog): surface Paths and Study Card columns in CATALOG.md`**
  (`59eac12`). CATALOG.md table widens from 6 to 8 columns; 200 lines
  of row churn, zero data change beyond the newly-visible fields.
- **`feat(stats): auto-inject blind75 and reviewed-Study Card counts`**
  (`2f16497`). Two new METRIC_MARKER entries
  (`BLIND75_COUNT` / `REVIEWED_STUDY_CARDS`) so the README's "9/75" and
  "9 reviewed" numbers stay live as the repo grows.
- **`feat(paths): add Study Card column to path Problem List tables`**
  (`282795a`). 5 columns → 6 columns on `paths/<p>/README.md`.

Outcome: 9/75 Blind 75 problems tagged, all nine carrying a reviewed
study card. CATALOG.md / TOPICS.md / paths/blind75/README.md all
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
introduced through the early tooling PRs #26 / #27 (May 2026), the
problems/ physical reorganisation in `0845a1a`, and the
`scripts/security_scan.py` / `scripts/update_indexes.py` pair added
in `5788257` / `1cc7589`. See `git log` between repository creation
and `1cc7589` for individual commits.
