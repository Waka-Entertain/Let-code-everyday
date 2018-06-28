"""
Given a 32-bit signed integer, reverse digits of an integer.

"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        return result if result < 0x7fffffff else 0


print(Solution().reverse(-123))