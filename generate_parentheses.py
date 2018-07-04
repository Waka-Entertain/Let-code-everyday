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
        return result

class Solution2:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return ['']
        if n == 1: return ["()"]

        result = []
        for item in self.generateParenthesis(n-1):
            result.append('({})'.format(item))
            result.append('(){}'.format(item))
            result.append('{}()'.format(item))
        result.pop()
        return result

print(Solution2().generateParenthesis(6))
