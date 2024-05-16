class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		m,n=len(word1),len(word2)
		dp=[[0]*(n+1) for _ in range(m+1)]
		for i in range(m):
			for j in range(n):
				dp[i+1][j+1]=dp[i][j] +1 if word1[i]==word2[j] else max(dp[i][j+1],dp[i+1][j])
		return m-dp[m][n]+n-dp[m][n]
#solution
'''
使用两个字符串的长度和减去2*最长公共子序列的长度
求最长公共子序列的长度见题目#1143的题解
'''