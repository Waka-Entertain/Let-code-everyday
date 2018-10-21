"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, lookup = [], {"(": ")", "[": "]", "{": "}"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif not len(stack) or lookup[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

if __name__ == "__main__":
    print(Solution().isValid(']'))
