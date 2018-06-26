class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_hash = {}
        temp_max = ""
        cursor = [0, 0]
        if s is '':
            return 0
        temp_max = s[0]
        for curr_pointer, letter in enumerate(s):
            cursor[1] = curr_pointer
            current_max_length = len(temp_max)
            start, end = cursor
            if letter in letter_hash and start<=letter_hash[letter]:
             
                current_length = end - start
                if current_length > current_max_length : temp_max = s[start:end]
                cursor[0] = letter_hash[letter] + 1
            else:
                current_length = end - start + 1
                if current_length > current_max_length : temp_max = s[start:end+1]

            letter_hash[letter] = curr_pointer
            
        return len(temp_max)
        
result = Solution().lengthOfLongestSubstring("pwwkew")
print(result)