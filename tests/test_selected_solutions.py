from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def load_solution(relative_path, injected=None):
    """Load a LeetCode solution module directly from its file path."""
    solution_path = ROOT / "problems" / relative_path
    module_name = "solution_" + "_".join(solution_path.parts[-2:]).replace(".", "_")
    spec = spec_from_file_location(module_name, solution_path)
    module = module_from_spec(spec)

    for name, value in (injected or {}).items():
        setattr(module, name, value)

    spec.loader.exec_module(module)
    return module.Solution


def normalize_nested_lists(values):
    return sorted(tuple(item) for item in values)


def normalize_anagram_groups(groups):
    return sorted(tuple(sorted(group)) for group in groups)


@pytest.mark.parametrize(
    ("relative_path", "method_name", "args", "expected", "normalizer"),
    [
        (
            "0001-two-sum/solution.py",
            "twoSum",
            ([2, 7, 11, 15], 9),
            [0, 1],
            None,
        ),
        (
            "0003-longest-substring-without-repeating-characters/solution.py",
            "lengthOfLongestSubstring",
            ("pwwkew",),
            3,
            None,
        ),
        (
            "0015-3sum/solution.py",
            "threeSum",
            ([-1, 0, 1, 2, -1, -4],),
            [(-1, -1, 2), (-1, 0, 1)],
            normalize_nested_lists,
        ),
        (
            "0049-group-anagrams/solution.py",
            "groupAnagrams",
            (["eat", "tea", "tan", "ate", "nat", "bat"],),
            [("ate", "eat", "tea"), ("bat",), ("nat", "tan")],
            normalize_anagram_groups,
        ),
        (
            "0121-best-time-to-buy-and-sell-stock/solution.py",
            "maxProfit",
            ([7, 1, 5, 3, 6, 4],),
            5,
            None,
        ),
        # Dynamic programming representative.
        (
            "1458-max-dot-product-of-two-subsequences/solution.py",
            "maxDotProduct",
            ([2, 1, -2, 5], [3, 0, -6]),
            18,
            None,
        ),
        # Graph/BFS representative.
        (
            "2092-find-all-people-with-secret/solution.py",
            "findAllPeople",
            (6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1),
            [0, 1, 2, 3, 5],
            sorted,
        ),
        # Heap / priority queue representative.
        (
            "2402-meeting-rooms-iii/solution.py",
            "mostBooked",
            (2, [[0, 10], [1, 5], [2, 7], [3, 4]]),
            0,
            None,
        ),
        # Binary search representative.
        (
            "2141-maximum-running-time-of-n-computers/solution.py",
            "maxRunTime",
            (2, [3, 3, 3]),
            4,
            None,
        ),
        # Geometry representative: count trapezoids once, including parallelograms.
        (
            "3625-count-number-of-trapezoids-ii/solution.py",
            "countTrapezoids",
            ([[0, 0], [2, 0], [1, 1], [3, 1]],),
            1,
            None,
        ),
        (
            "3625-count-number-of-trapezoids-ii/solution.py",
            "countTrapezoids",
            ([[0, 0], [1, 0], [0, 1], [1, 1]],),
            1,
            None,
        ),
    ],
)
def test_selected_array_string_dp_graph_heap_and_binary_search_solutions(
    relative_path, method_name, args, expected, normalizer
):
    solution = load_solution(relative_path)()
    result = getattr(solution, method_name)(*args)

    if normalizer is not None:
        result = normalizer(result)

    assert result == expected


class TreeNode:
    """Minimal test helper for tree problems whose LeetCode classes are comments."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_tree_solution_with_custom_treenode_helper():
    # The solution file references TreeNode in type annotations, but LeetCode
    # supplies that helper externally. Inject a small local TreeNode before import.
    solution_class = load_solution(
        "1161-maximum-level-of-a-binary-tree/solution.py",
        injected={"TreeNode": TreeNode},
    )
    root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))

    assert solution_class().maxLevelSum(root) == 2
