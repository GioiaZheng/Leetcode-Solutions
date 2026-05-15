import pytest


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-3, 4, 3, 90], 0, [0, 2]),
    ],
)
def test_two_sum(solution_loader, nums, target, expected):
    Solution = solution_loader("0001-two-sum")
    assert Solution().twoSum(nums, target) == expected
