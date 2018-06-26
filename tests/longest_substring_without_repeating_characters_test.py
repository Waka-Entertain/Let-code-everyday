from longest_substring_without_repeating_characters import Solution


def test_longest_unrepeat_substring():
    strs = ["abcabcbb", "bbbbb", "pwwkew", ""]
    assert [Solution().lengthOfLongestSubstring(s) for s in strs] == [3, 1, 3, 0], "Find unrepeated substring failed"
