import pytest
from medium.medium_solutions.container_with_most_water import Solution


data = (
    ([1, 2, 3, 4], 4),
    ([1, 1, 1, 1, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1], 14),
    ([2, 1, 7, 4, 10, 9], 21)
)


@pytest.mark.parametrize('arr, result', data)
def test_simple(arr,  result):
    sol = Solution()
    assert sol.maxArea(arr) == result