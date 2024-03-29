class Solution:
    def intToRoman(self, num: int) -> str:
        data = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        res = ''
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        while num > 0:
            if num - nums[i] >= 0:
                res += data.get(nums[i])
                num -= nums[i]
            else:
                i += 1
        return res

