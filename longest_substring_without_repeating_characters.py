"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_hash = {}
        cursor = [0, 0]
        if s is '':
            return 0
        temp_max = s[0]
        for curr_pointer, letter in enumerate(s):
            cursor[1] = curr_pointer
            current_max_length = len(temp_max)
            start, end = cursor
            if letter in letter_hash and start <= letter_hash[letter]:
                current_length = end - start
                if current_length > current_max_length: temp_max = s[start:end]
                cursor[0] = letter_hash[letter] + 1
            else:
                current_length = end - start + 1
                if current_length > current_max_length: temp_max = s[start:end + 1]

            letter_hash[letter] = curr_pointer

        return len(temp_max)

    def lengthOfLongestSubstring1(self, s):
        longest, start, visited = 0, 0, {}
        for i, char in enumerate(s):
            try:
                if visited[char]:
                    while char != s[start]:
                        visited[s[start]] = False
                        start += 1
                    start += 1
            except KeyError:
                visited[char] = True
            longest = max(longest, i - start + 1)
        return longest

if __name__ == '__main__':
    Solution().lengthOfLongestSubstring("pwwkew")
