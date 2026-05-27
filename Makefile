PYTHON ?= python

.PHONY: help check validate sync sync-check lint compile test security

help:
	@echo "Targets:"
	@echo "  make check       - run every local check CI runs (validate / sync-check / lint / compile / test / security)"
	@echo "  make validate    - structural + schema validation (scripts/validate_repo.py)"
	@echo "  make sync        - regenerate CATALOG / TOPICS / paths / README (scripts/update_indexes.py)"
	@echo "  make sync-check  - run sync and fail if any generated file drifted"
	@echo "  make lint        - ruff check ."
	@echo "  make compile     - python -m compileall -q ."
	@echo "  make test        - pytest"
	@echo "  make security    - scripts/security_scan.py"
	@echo ""
	@echo "Override the interpreter via PYTHON=python3 (default 'python', matching CI)."

check: validate sync-check lint compile test security
	@echo "All checks passed."

validate:
	$(PYTHON) scripts/validate_repo.py

sync:
	$(PYTHON) scripts/update_indexes.py

sync-check: sync
	@git diff --exit-code -- CATALOG.md TOPICS.md README.md 'paths/*/README.md' \
		|| (echo "ERROR: regenerated indexes diverge from committed state. Run 'make sync' and commit the result." >&2; exit 1)

lint:
	$(PYTHON) -m ruff check .

compile:
	$(PYTHON) -m compileall -q .

test:
	$(PYTHON) -m pytest

security:
	$(PYTHON) scripts/security_scan.py
