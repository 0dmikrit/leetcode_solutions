import pytest
from easy.easy_solutions.length_of_last_word import Solution


data = (
    ("Hello world", 5),
    ("Hey how are you     ", 3)
)


@pytest.mark.parametrize('s, result', data)
def test_simple(s, result):
    sol = Solution()
    assert sol.lengthOfLastWord(s) == result