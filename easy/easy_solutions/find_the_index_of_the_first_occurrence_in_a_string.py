class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        for i in range(len(haystack) - len(needle) + 1):
            success = True
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    success = False
                    break
            if success:
                index = i
                break
        return index


