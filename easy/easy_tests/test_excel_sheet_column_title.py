import pytest
from easy.easy_solutions.excel_sheet_column_title import Solution


data = (
    (1, "A"),
    (54, "BB"),
    (701, "ZY")
)


@pytest.mark.parametrize('num, result', data)
def test_simple(num,  result):
    sol = Solution()
    assert sol.convertToTitle(num) == result