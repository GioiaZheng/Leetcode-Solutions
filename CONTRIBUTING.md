# Contributing

This is primarily a personal study repository, so contributions should keep the
repo easy to browse, regenerate, and validate.

## Add A Problem

1. Create a directory under `problems/` using this format:

   ```text
   problems/####-problem-name
   ```

2. Add a `README.md` based on `templates/problem_README.md`.
3. Add a `solution.py` with one LeetCode-style `class Solution`.
4. Update `metadata.json` with title, difficulty, topics, status, and source.
5. Regenerate the derived indexes:

   ```bash
   python scripts/update_indexes.py
   ```

6. Commit the problem, `metadata.json`, and regenerated `README.md`,
   `CATALOG.md`, and `TOPICS.md` together.

## Problem Directory Rules

- Use a four-digit LeetCode ID prefix.
- Use lowercase kebab-case for the title slug.
- Keep names ASCII-only and shell-friendly.
- Do not put problem directories at the repository root; all solved problems
  belong under `problems/`.
- Keep each solution self-contained unless the LeetCode problem itself defines
  helper classes such as `ListNode` or `TreeNode`.

## Notes Rules

- Topic notes live under `0000-notes/`.
- Avoid nested `0000-notes/` directories.
- Keep entrypoint docs readable in plain UTF-8:
  `README.md`, `CATALOG.md`, `TOPICS.md`, `problems/README.md`, and
  `0000-notes/README.md`.

## Metadata

Each entry in `metadata.json` is an object with five required fields
and three optional ones (validated by `scripts/validate_repo.py`):

**Required:**

- `id` — four-digit string, matching the directory prefix.
- `title` — the LeetCode display title.
- `difficulty` — `Easy`, `Medium`, or `Hard`.
- `topics` — list of LeetCode topic tags.
- `status` — `solved`, `tested`, or `review-needed`.

**Optional:**

- `path_membership` — list of strings; subset of
  `{"blind75", "neetcode150"}`. Drives `paths/<name>/README.md`
  auto-generation.
- `ai_card_status` — one of `draft`, `reviewed`, or
  `interview-ready`. **Mandatory** when the problem's README ships
  any of the optional "AI card" sections (see below).
- `milestones` — dict mapping each path id (from `path_membership`)
  to a milestone id within that path. Blind 75 milestones run
  `M1`..`M6`; NeetCode 150 milestones run `M1`..`M18` (the
  canonical 18 pattern groupings). Drives the Milestones table at
  the top of each path README. Every key must also appear in
  `path_membership`; values are checked against the per-path
  milestone set defined in
  `VALID_MILESTONE_IDS_PER_PATH`.

## Optional Problem README Sections (AI Card)

The six required core sections (Problem / Intuition / Approach /
Complexity / Edge Cases / Code) are enforced by `validate_repo.py`.
Beyond those, a problem README may include any subset of:

- **Brute-force baseline** — the naive solution and its complexity.
- **Common mistakes** — concrete failure modes specific to this
  problem, not generic pitfalls.
- **Failure cases** — at least two inputs that defeat the naive
  approach.
- **Interview follow-ups** — plausible interviewer probes and the
  direction the answer should go.
- **Bilingual summary** — short English + 中文 summary with
  semantic parity (no machine-translation register).

When any of these sections is present, set `ai_card_status` in
`metadata.json` accordingly:

- `draft` — author wrote it, not yet self-reviewed.
- `reviewed` — self-reviewed once for accuracy, edge cases, and
  bilingual parity.
- `interview-ready` — usable for mock-interview revision.

This gates AI-assisted content from landing in the repo without a
manual review pass.

**`ai_card_status` is independent of `path_membership`.** A problem
can carry a reviewed AI card without belonging to any curated path
(e.g. a high-frequency interview problem that is not on the
canonical Blind 75 or NeetCode 150 lists). Such a problem surfaces
in the README "Where to start" featured table and in the `AI Card`
column of `CATALOG.md` / `TOPICS.md`, but does NOT appear in any
`paths/<p>/README.md`. The reverse is also true: a tagged problem
can omit `ai_card_status` (just appears in the path Problem List
with a blank AI Card column).

## Learning Paths (`paths/`)

Each curated learning path has its own directory under `paths/`
with a single `README.md`. Membership of a problem in a path is
declared via the `path_membership` field in `metadata.json`, not
by moving the problem directory.

Path README structure:

```text
# <Path name>

## Overview
## Prerequisites
## Milestones
## Problem List   <!-- regenerated; do not edit by hand -->
## Pattern Notes
## Mock-Interview Tips
## Weekly Plan
```

Two sections are auto-regenerated:

- **Problem List** between `<!-- PATH_LIST_START -->` /
  `<!-- PATH_LIST_END -->` sentinels: one row per tagged
  problem (sorted by id), reading
  `path_membership` from `metadata.json`.
- **Milestones** between `<!-- MILESTONES_START -->` /
  `<!-- MILESTONES_END -->` sentinels: a table grouped by
  milestone (`M1`..`Mn`) showing canonical / in-repo / reviewed
  counts. Reads the optional `milestones[<path_id>]` field on
  each problem (see the §Metadata section above; `M1`..`M6` for
  Blind 75, `M1`..`M18` for NeetCode 150).

The other sections (Overview, Prerequisites, Pattern Notes,
Mock-Interview Tips, Weekly Plan) are hand-written narrative and
survive regeneration.

Regenerate with:

```bash
python scripts/generate_path.py
```

Allowed path identifiers (used both in the directory name under
`paths/` and in the `path_membership` field): `blind75`,
`neetcode150`. Adding a new path requires updating four places:
this section, `VALID_PATH_MEMBERSHIPS` in
`scripts/validate_repo.py`, `VALID_MILESTONE_IDS_PER_PATH` in the
same file, and `PATH_MILESTONE_DEFS` in
`scripts/generate_path.py`.

## Local Checks

The easy path:

```bash
make check
```

This runs every check CI runs (`validate_repo.py`, the regenerated-doc
diff check, ruff, compileall, pytest, `security_scan.py`). Override the
interpreter via `PYTHON=python3 make check` on systems where `python`
is not Python 3.

The individual commands behind `make check`:

```bash
python scripts/validate_repo.py     # structure + schema validation
python scripts/update_indexes.py    # regenerate CATALOG / TOPICS / paths / README
python scripts/security_scan.py     # token / credential scan
python -m compileall -q .           # syntax sanity
ruff check .                        # lint
pytest                              # tests
```

The security scan is intentionally conservative. It should catch accidental
tokens, `.env` files, and private key material before they are committed.
