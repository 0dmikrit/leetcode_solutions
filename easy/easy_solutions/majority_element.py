from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = {}
        for i in nums:
            if data.get(i):
                data[i] += 1
            else:
                data[i] = 1
        temp = sorted(data.items(), key=lambda x: x[1])
        return temp[-1][0]