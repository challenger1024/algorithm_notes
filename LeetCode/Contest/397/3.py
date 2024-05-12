class Solution:
	def maxScore(self, grid) -> int:
		m,n=len(grid),len(grid[0])
		ans=-inf
		dp=[[inf]*(n+1) for _ in range(m+1)]
		for i,row in enumerate(grid):
			for j,now in enumerate(row):
				mn=min(dp[i][j+1],dp[i+1][j])
				ans=max(ans,now-mn)
				dp[i+1][j+1]=min(mn,now)
		return ans

#test entry
s=Solution()
#grid = [[4,3,2],[3,2,1]]
grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]
print(s.maxScore(grid))

