import pytest
from easy.easy_solutions.majority_element import Solution


data = (
    ([4, 4, 4, 2, 2, 1], 4),
    ([1, 4, 6, 78, 1, 78, 6], 4),
    ([2, 3, 4, 2, 3, 4, 0], 0)
)


@pytest.mark.parametrize('arr, result', data)
def test_simple(arr,  result):
    sol = Solution()
    assert sol.majorityElement(arr) == result