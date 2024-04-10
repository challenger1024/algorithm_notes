class Solution:
	def minPathCost(self, grid, moveCost) -> int:
		m,n=len(grid),len(grid[0])
		dp=[[0]*n for _ in range(m)]
		for i in range(n):
			dp[0][i]=grid[0][i]
		for i in range(1,m):
			for j in range(n):
				dp[i][j] = grid[i][j] + min(dp[i-1][k] + moveCost[grid[i - 1][k]][j] for k in range(n))
		return min(dp[m-1])

