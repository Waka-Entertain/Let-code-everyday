"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        temp, reverse = x, 0

        while temp:
            reverse = 10 * reverse + temp % 10
            temp //= 10

        return x == reverse


if __name__ == "__main__":
    print(Solution().isPalindrome(22322))
