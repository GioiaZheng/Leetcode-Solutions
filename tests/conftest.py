from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def load_solution(problem_dir: str):
    """Import the ``Solution`` class from ``<repo>/<problem_dir>/solution.py``.

    Problem directories start with a digit, so they can't be imported as a
    regular Python package. We load the module from its path instead.
    """
    path = ROOT / problem_dir / "solution.py"
    spec = spec_from_file_location(f"_lc_{problem_dir}", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution


@pytest.fixture
def solution_loader():
    return load_solution
