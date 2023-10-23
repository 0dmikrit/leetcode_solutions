import pytest
from hard.hard_solutions.median_of_two_sorted_arrays import Solution


data = (
    ([1, 3], [2, 4], 2.5),
    ([1, 3], [2], 2)
)


@pytest.mark.parametrize('nums1, nums2, result', data)
def test_simple(nums1, nums2, result):
    sol = Solution()
    assert sol.findMedianSortedArrays(nums1, nums2) == result