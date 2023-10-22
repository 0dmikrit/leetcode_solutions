class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = {}
        res = ""
        i = 0
        j = 0
        while i < len(s):
            if s[i] not in res:
                res += s[i]
            else:
                data[len(res)] = res
                res = ''
                j += 1
                i = j
                res += s[i]
            i += 1
        data[len(res)] = res
        return sorted(data.keys())[-1]