class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        converted = ['' for i in range(numRows)]
        T = numRows*2-2
        length = len(s)
        cursor = 0
        while cursor < length:
            remain = (cursor+1) % T
            if not remain:
                converted[1] += s[cursor]
            elif remain <= numRows:
                converted[remain-1] += s[cursor]
            else:
                converted[numRows - (remain - numRows) - 1] += s[cursor]
            cursor += 1
        return ''.join(converted)


Solution().convert("PAYPALISHIRING", 3)
