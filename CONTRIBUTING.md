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
and two optional ones (validated by `scripts/validate_repo.py`):

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

Only the **Problem List** section is auto-regenerated, between
`<!-- PATH_LIST_START -->` / `<!-- PATH_LIST_END -->` sentinels.
The other sections are hand-written narrative and survive
regeneration.

Regenerate with:

```bash
python scripts/generate_path.py
```

Allowed path identifiers (used both in the directory name under
`paths/` and in the `path_membership` field): `blind75`,
`neetcode150`. Add new ones by extending both this section and the
`VALID_PATH_MEMBERSHIPS` set in `scripts/validate_repo.py`.

## Local Checks

Run these before committing:

```bash
python scripts/validate_repo.py
python scripts/security_scan.py
python -m compileall -q .
ruff check .
pytest
```

The security scan is intentionally conservative. It should catch accidental
tokens, `.env` files, and private key material before they are committed.
