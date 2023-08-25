import pytest
from easy.easy_solutions.palindrome_number import Solution


data = (
    (123, False),
    (12321, True)
)


@pytest.mark.parametrize('num, result', data)
def test_simple(num, result):
    sol = Solution()
    assert sol.isPalindrome(num) == result