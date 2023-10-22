from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = map(str, digits)
        s = str(int("".join(s)) + 1)
        return [int(i) for i in s]