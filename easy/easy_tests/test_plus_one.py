import pytest
from easy.easy_solutions.plus_one import Solution


data = (
    ([1, 0, 1], [1, 0, 2]),
    ([9, 9], [1, 0, 0])
)


@pytest.mark.parametrize('digits, result', data)
def test_simple(digits, result):
    sol = Solution()
    assert sol.plusOne(digits) == result