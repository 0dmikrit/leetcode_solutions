import pytest
from easy.easy_solutions.two_sum import Solution


data = (
    ([1, 2, 3], 4, [0, 2]),
    ([4, 2, 3, 2, 3], 6, [0, 1])
)


@pytest.mark.parametrize('nums, target, result', data)
def test_simple(nums, target, result):
    sol = Solution()
    assert sol.twoSum(nums, target) == result