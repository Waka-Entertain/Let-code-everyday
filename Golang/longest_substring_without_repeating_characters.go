package main

import "fmt"

func max(a , b int) int {
	if a > b {
		return a
	}
	return b
}

func lengthOfLongestSubstring(s string) int {
	lookup := make(map[string] int)
	j, ans := 0, 0
	for i := 0; i < len(s); i++ {
		if _, ok := lookup[string(s[i])]; ok {
			j = max(lookup[string(s[i])], j)
		}
		ans = max(ans, i - j + 1)
		lookup[string(s[i])] = i + 1
	}
	return ans
}

func main() {
	fmt.Println(lengthOfLongestSubstring("asssff"))
}