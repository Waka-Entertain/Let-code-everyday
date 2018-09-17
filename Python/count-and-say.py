class Solution:
    def countAndSay(self, n ):
        s = "1"
        for i in range(n-1):
            count = 1
            temp = ''
            for pos in range(0, len(s)):
                if pos == len(s) - 1:
                    temp += str(count)+s[pos]
                    s = temp
                else:
                    if s[pos] == s[pos+1]:
                        count += 1
                    else:
                        temp += str(count)+s[pos]
                        count = 1
        return  s


print(Solution().countAndSay(5))