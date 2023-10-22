from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h_left = height[left]
            h_right = height[right]
            width = right - left
            current_area = min(h_left, h_right) * width
            max_area = max(max_area, current_area)

            if h_left < h_right:
                left += 1
            else:
                right -= 1

        return max_area

