from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        arr = []
        while (i < len(nums1)) and (j < len(nums2)):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        arr += nums1[i:]
        arr += nums2[j:]
        if len(arr) % 2 == 0:
            k = len(arr) // 2
            res = (arr[k] + arr[k-1]) / 2
            return round(res, 5)
        else:
            k = len(arr) // 2
            return round(arr[k], 5)