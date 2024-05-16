class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		m,n=len(word1),len(word2)
		dp=[[0]*(n+1) for _ in range(m+1)]
		for i in range(1,m+1):
			dp[i][0]=i
		for j in range(1,n+1):
			dp[0][j]=j
		for i in range(m):
			for j in range(n):
				dp[i+1][j+1]=dp[i][j] if word1[i]==word2[j] else min(dp[i][j+1],dp[i+1][j])+1
		return dp[m][n]

#solution
'''
二维动态规划
设二维数组dp,其中dp[i][j]表示长度为i的字符串w1和长度为j的字符串w2中需要删除的最小字符数量
分为两种情况:
1. w1[i]==w2[j],那么
dp[i][j]=dp[i-1][j-1]
2. w1[i]!=w2[j],那么
dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1#因为需要删掉一个字符，可能是w1[i]也可能是w2[j]，这就要看在这之前哪边删除的少，求最小值
'''