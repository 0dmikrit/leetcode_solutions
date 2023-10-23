from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        if target < nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)
        for i in range(len(nums) - 1):
            if nums[i] < target < nums[i + 1]:
                return i + 1
