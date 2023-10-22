class Solution:
    def mySqrt(self, x: int) -> int:
        # x = main_number
        # m = copy
        m = x
        while m ** 2 > x:
            m //= 2
        m *= 2
        while m ** 2 > x:
            m -= 1
        return m





