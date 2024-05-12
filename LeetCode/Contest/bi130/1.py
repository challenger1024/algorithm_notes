class Solution:
	def satisfiesConditions(self, grid) -> bool:
		m=len(grid)
		n=len(grid[0])
		dp=[[False]*n for _ in range(m)]
		for i in range(m):
			dp[i][0]=True
		for i in range(n):
			dp[0][i]=True
		for i in range(m):
			for j in range(1,n):
				dp[i][j]=grid[i][j]!=grid[i][j-1]
		for i in range(1,m):
			for j in range(n):
				dp[i][j]=grid[i][j]==grid[i-1][j]
		ans=True
		for i in range(m):
			for j in range(n):
				ans&=dp[i][j]
		return ans


s=Solution()
#grid = [[1,0,2],[1,0,2]]
#grid = [[1,1,1],[0,0,0]]
grid = [[1],[2],[3]]
print(s.satisfiesConditions(grid))