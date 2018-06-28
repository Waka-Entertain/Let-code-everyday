"""
Example 1:

Input: "III"
Output: 3
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        ans = 0
        for i in range(len(s)):
            if i > 0 and maps[s[i]] > maps[s[i - 1]]:
                ans += maps[s[i]] - 2 * maps[s[i - 1]]
            else:
                ans += maps[s[i]]
        return ans

print(Solution().romanToInt('CMXCIX'))