class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		m,n=len(text1),len(text2)
		dp=[[0]*(n+1) for _ in range(m+1)]
		for i in range(m):
			for j in range(n):
				dp[i+1][j+1]=dp[i][j] +1 if text1[i]==text2[j] else max(dp[i][j+1],dp[i+1][j])
		return dp[m][n]

#solution
'''
设二维数组dp作为动态规划数组
考虑以下两种情况:
1. text1[i]==text2[j],说明当前字符可以选，那么text1[0:i+1]和text2[0:j+1]的最长公共子序列的长度为:
dp[i][j]=dp[i-1][j-1]+1
2. 如果text1[i]!=text2[j]，说明第当前字符不可选，则：
dp[i][j]=max(dp[i-1][j],dp[i][j-1])
'''