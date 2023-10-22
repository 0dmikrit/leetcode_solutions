import pytest
from easy.easy_solutions.search_insert_position import Solution


data = (
    ([1, 2, 3], 2, 1),
    ([1, 4, 6, 78], 100, 4),
    ([2, 3, 4], 1, 0)
)


@pytest.mark.parametrize('nums, target, result', data)
def test_simple(nums, target,  result):
    sol = Solution()
    assert sol.searchInsert(nums, target) == result