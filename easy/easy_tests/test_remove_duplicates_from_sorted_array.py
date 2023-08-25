import pytest
from easy.easy_solutions.remove_duplicates_from_sorted_array import Solution


data = (
    ([1, 2, 3, 3, 4, 5], 5),
    ([1, 2, 3], 3)
)


@pytest.mark.parametrize('nums, result', data)
def test_simple(nums, result):
    sol = Solution()
    assert sol.removeDuplicates(nums) == result