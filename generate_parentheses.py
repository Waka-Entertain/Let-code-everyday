"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return ['']

        result = []

        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - 1 - i):
                    result.append('{}({})'.format(left, right))
                    print(result)
        return result


print(Solution().generateParenthesis(2))
