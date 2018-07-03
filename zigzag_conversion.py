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

    def convert1(self, s, numRows):
        if numRows == 1:
            return s

        zigzag = ['' for _ in range(numRows)]
        row, cursor = 0, 1
        for char in s:
            if row == 0:
                cursor = 1
            if row == numRows - 1:
                cursor = -1
            zigzag[row] += char
            print(zigzag)
            row += cursor
        return ''.join(zigzag)


if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 4))
    print(Solution().convert1("PAYPALISHIRING", 4))
