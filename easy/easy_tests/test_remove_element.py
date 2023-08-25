import pytest
from easy.easy_solutions.remove_element import Solution


data = (
    ([1, 2, 2, 3], 2, 2),
    ([7, 5, 12, 43, 1], 3, 5)
)


@pytest.mark.parametrize('nums, val,  result', data)
def test_simple(nums, val, result):
    sol = Solution()
    assert sol.removeElement(nums, val) == result