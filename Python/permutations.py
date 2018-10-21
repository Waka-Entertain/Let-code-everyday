"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        used = [False] * len(nums)
        self.permuteRecu(result, used, [], nums)
        return result

    def permuteRecu(self, result, used, cur, nums):
        if len(cur) == len(nums):
            result.append(cur[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                cur.append(nums[i])
                self.permuteRecu(result, used, cur, nums)
                cur.pop()
                used[i] = False
