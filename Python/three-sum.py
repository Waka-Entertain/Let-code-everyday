class Solution:
    def threeSum(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        lookup = {}
        while nums:
            a = nums.pop()
            if (a in lookup):
                continue
            r = self.twoSum(nums, -a)
            j = [t + [a] for t in r]
            res = res + j
            lookup[a] = True
        return res

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        res = []
        for num in nums:
            remain = lookup.get(target - num)
            if remain is not num and remain is not None:
                res.append([num, target - num])
                lookup[num] = target - num
            else:
                lookup[num] = True
        return res


print(Solution().threeSum([0, 0, 0, 0]))
