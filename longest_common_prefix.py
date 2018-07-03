"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not len(strs):
            return ''

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if not i < len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]



print(Solution().longestCommonPrefix(["a"]))
