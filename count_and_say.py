"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
#
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
#
Note: The sequence of integers will be represented as a string.
"""
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n - 1):
            res = self.count(res)
        return res

    def count(self, string):
        i, res = 0, ''
        while i < len(string):
            count = 1
            while i < len(string) - 1 and  string[i] ==  string[i + 1]:
                count += 1
                i += 1
            res += str(count) + string[i]
            i += 1
        return res


if __name__ == "__main__":
    for i in range(1, 4):
        print(Solution().countAndSay(i))
