import pytest
from easy.easy_solutions.contains_duplicate import Solution


data = (
    ([1, 2, 2, 3], True),
    ([7, 5, 12, 43, 1], False)
)


@pytest.mark.parametrize('nums, result', data)
def test_simple(nums, result):
    sol = Solution()
    assert sol.containsDuplicate(nums) == result