from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[1]
SOLUTION_PATH = ROOT / "problems" / "0001-two-sum" / "solution.py"


def load_solution_class():
    spec = spec_from_file_location("two_sum_solution", SOLUTION_PATH)
    module = module_from_spec(spec)
    module.List = List
    spec.loader.exec_module(module)
    return module.Solution


def test_two_sum_returns_indices_for_matching_pair():
    solution = load_solution_class()

    assert solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
