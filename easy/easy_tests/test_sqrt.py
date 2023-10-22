import pytest
from easy.easy_solutions.sqrt import Solution


data = (
    (0, 0),
    (1, 1),
    (5, 2),
    (100, 10),
    (226, 15)
)


@pytest.mark.parametrize('x, result', data)
def test_simple(x, result):
    sol = Solution()
    assert sol.mySqrt(x) == result