class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # maps = {1: "I", 4: "IV", 5: "V", 9: "IX", \
        #        10: "X", 40: "XL", 50: "L", 90: "XC", \
        #        100: "C", 400: "CD", 500: "D", 900: "CM", \
        #        1000: "M"}
        # keyset, result = sorted(maps.keys()), []
        # while num > 0:
        #     for key in reversed(keyset):
        #         while num >= key:
        #             num -= key
        #             result += maps[key]
        # return "".join(result)

        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strs = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = []
        for i, val in enumerate(nums):
            while num >= val:
                num -= val
                res += strs[i]
        return "".join(res)
        
        # M = ['', 'M', 'MM', 'MMM']
        # C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        # X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        # I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        # return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num% 10]


if __name__ == "__main__":
    print(Solution().intToRoman(999))
    # print Solution().intToRoman(3999)