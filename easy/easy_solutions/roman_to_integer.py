class Solution:
    def romanToInt(self, s: str) -> int:
        digit = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000
                 }
        count = 0
        for i in range(len(s) - 1):
            if digit.get(s[i]) >= digit.get(s[i + 1]):
                count += digit.get(s[i])
            else:
                count -= digit.get(s[i])
        count += digit.get(s[-1])
        return count
