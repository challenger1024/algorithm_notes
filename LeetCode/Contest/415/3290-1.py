#动态规划
class Solution:
	def maxScore(self, a, b):# -> int:
		n=len(b)
		dp=[[0]*5 for _ in range(n+1)]
		dp[0][1:]=[-inf]*4
		for i in range(n):
			for j in range(4):
				dp[i+1][j+1]=dp[i][j+1] if dp[i][j+1]>dp[i][j]+a[j]*b[i] else dp[i][j]+a[j]*b[i]
		return dp[-1][-1]