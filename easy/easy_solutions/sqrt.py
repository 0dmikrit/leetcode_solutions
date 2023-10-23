class Solution:
    def mySqrt(self, x: int) -> int:
        m = x
        while m ** 2 > x:
            m //= 2
        m *= 2
        while m ** 2 > x:
            m -= 1
        return m





