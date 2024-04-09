class Solution:
	def maxMoves(self, grid) -> int:
		m=len(grid)
		n=len(grid[0])
		dp=[[0]*n for _ in range(m)]
		for j in range(n-2,-1,-1):
			for i in range(m-1,-1,-1):
				x,y,z=0,0,0
				if (0<i<m) and (grid[i-1][j+1]>grid[i][j]):x=dp[i-1][j+1]
				else: x=-1
				if grid[i][j+1]>grid[i][j]:y=dp[i][j+1]
				else: y=-1
				if (0<=i<m-1) and (grid[i+1][j+1]>grid[i][j]):z=dp[i+1][j+1]
				else: z=-1
				dp[i][j]=max(x,y,z)+1
		return max([dp[i][0] for i in range(m)])

#Solution
'''结束位置是最左边的那一列，在最左边那一列中取最大值'''