import pytest
from easy.easy_solutions.roman_to_integer import Solution


data = (
    ("XXI", 21),
    ("IV", 4)
)


@pytest.mark.parametrize('num, result', data)
def test_simple(num, result):
    sol = Solution()
    assert sol.romanToInt(num) == result