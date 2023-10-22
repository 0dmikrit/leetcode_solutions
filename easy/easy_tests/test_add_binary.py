import pytest
from easy.easy_solutions.add_binary import Solution


data = (
    ("11", "1", "100"),
    ("100", "11", "111")
)


@pytest.mark.parametrize('a, b, result', data)
def test_simple(a, b, result):
    sol = Solution()
    assert sol.addBinary(a, b) == result