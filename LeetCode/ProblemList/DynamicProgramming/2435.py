mod=10**9+7
class Solution:
	def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
		m,n=len(grid),len(grid[0])
		dp=[[[0]*k for _ in range(n+1)] for _ in range(m+1)]
		dp[0][1][0]=1
		for i in range(1,m+1):
			for j in range(1,n+1):
				for u in range(k):
					dp[i][j][(u+grid[i-1][j-1])%k]=(dp[i-1][j][u]+dp[i][j-1][u])%mod#[i,j]位置路径和为v+grid[i][j]%k的方案数=前两个路径和=v的两个方案和的方案和
		return dp[m][n][0]%mod