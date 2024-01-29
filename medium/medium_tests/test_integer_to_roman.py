import pytest
from medium.medium_solutions.integer_to_roman import Solution


data = (
    (49, 'XLIX'),
    (101, 'CI')
)


@pytest.mark.parametrize('nums, result', data)
def test_simple(nums, result):
    sol = Solution()
    assert sol.intToRoman(nums) == result