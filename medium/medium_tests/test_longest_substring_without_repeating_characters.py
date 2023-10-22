import pytest
from medium.medium_solutions.longest_substring_without_repeating_characters import Solution


data = (
    ("wkewd", 4),
    ("abcabc", 3),
    ("aaabcad", 4)
)


@pytest.mark.parametrize('line, result', data)
def test_simple(line,  result):
    sol = Solution()
    assert sol.lengthOfLongestSubstring(line) == result