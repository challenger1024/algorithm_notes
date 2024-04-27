class Solution:
	def minFallingPathSum(self, grid) -> int:
		n=len(grid)
		for i in range(1,n):
			for j in range(n):
				dp=10**9#让初始的dp[i][j]尽量大
				for k in range(n):
					if k!=j:
						dp=min(dp,grid[i-1][k])
				grid[i][j]+=dp
		return min(grid[n-1])