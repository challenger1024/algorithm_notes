class Solution:
	def maxPoints(self, points: List[List[int]]) -> int:
		m,n=len(points),len(points[0])
		dp=[[0]*n for _ in range(m)]
		for i in range(n):
			dp[0][i]=points[0][i]
		for i in range(1,m):
			score=float('-inf')
			for j in range(n):
				score=max(score,dp[i-1][j]+j)
				dp[i][j]=max(dp[i][j],score+points[i][j]-j)
			score=float('-inf')
			for j in range(n-1,-1,-1):
				score=max(score,dp[i-1][j]-j)
				dp[i][j]=max(dp[i][j],score+points[i][j]+j)
		return max(dp[m-1])