import pytest
from easy.easy_solutions.excel_sheet_column_number import Solution


data = (
    ("A", 1),
    ("BB", 54),
    ("ZY", 701)
)


@pytest.mark.parametrize('line, result', data)
def test_simple(line,  result):
    sol = Solution()
    assert sol.titleToNumber(line) == result