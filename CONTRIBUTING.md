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
