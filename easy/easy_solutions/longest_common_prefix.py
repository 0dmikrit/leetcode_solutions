from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                res += i[0]
            else:
                return res
        return res

