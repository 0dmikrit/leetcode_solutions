import pytest
from easy.easy_solutions.find_the_index_of_the_first_occurrence_in_a_string import Solution


data = (
    ("Find", "nd", 2),
    ("Result", "Search", -1)
)


@pytest.mark.parametrize('haystack, needle, result', data)
def test_simple(haystack, needle, result):
    sol = Solution()
    assert sol.strStr(haystack, needle) == result