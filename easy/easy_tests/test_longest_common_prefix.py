import pytest
from easy.easy_solutions.longest_common_prefix import Solution


data = (
    (["Car", "Core", "Care"], "C"),
    (["Fly", "Swim", "Run"], "")
)


@pytest.mark.parametrize('arr, result', data)
def test_simple(arr, result):
    sol = Solution()
    assert sol.longestCommonPrefix(arr) == result