package main

import "fmt"

// 设字符串为string，长度为n，p[i][j]表示第i到第j个字符间的子序列的个数（i<=j），则：
//
// 状态初始条件：dp[i][i]=1 （i=0：n-1）
//
// 状态转移方程：dp[i][j]=dp[i+1][j-1] + 2  if（str[i]==str[j]）
//
// dp[i][j]=max(dp[i+1][j],dp[i][j-1])  if （str[i]!=str[j]）

func LongestPalindromicSubstring(s string) int {
	dp := make([][]int, 1)
	fmt.Println(dp)
	for i, m := range s {
		dp[i][i] = 1
		for j, n := range s {
			if m == n {
				dp[i][j] = dp[i+1][j-1] + 2
			} else {
				dp[i][j] = max(dp[i+1][j], dp[i][j-1])
			}
		}
	}
	return dp[0][len(s) - 1]
}

func main()  {
	LongestPalindromicSubstring("aba")
}
