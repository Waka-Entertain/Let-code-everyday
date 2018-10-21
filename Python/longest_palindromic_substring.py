class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s
        i = 0
        j = 0
        length = len(s)
        matrix = [[None for x in range(length)] for y in range(length)]
        enu_str = enumerate(s)
        longest=0
        max_length = 0
        def is_Palindrome(i, j):
            if matrix[i][j] is not None:
                return matrix[i][j]
            if i == j:
                matrix[i][j] = True
            elif j == i + 1:
                matrix[i][j] = s[i] == s[j]
            else:
                matrix[i][j] = is_Palindrome(i + 1, j - 1) and s[i] == s[j]
            nonlocal longest
            nonlocal max_length
            if (j-i) > max_length and matrix[i][j]:
                longest = i
                max_length=j-i
            return matrix[i][j]

        for i, si in enu_str:
            for j in range(i, length):
                is_Palindrome(i, j)

        start = longest
        return s[start:start+max_length+1]



if __name__ == '__main__':
    print(Solution().longestPalindrome("aaaaaaaaaaaaaaaaaaaaaabbcsdfaaaaaaaaaaaaaaaaaaaaa"))