import pytest
from easy.easy_solutions.valid_parentheses import Solution


data = (
    ("([{]})", False),
    ("{}({[{}[]()]})[]", True)
)


@pytest.mark.parametrize('line, result', data)
def test_simple(line, result):
    sol = Solution()
    assert sol.isValid(line) == result