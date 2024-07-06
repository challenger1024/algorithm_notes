class Solution:
	def getMaximumGold(self, grid: List[List[int]]) -> int:
		m,n=len(grid),len(grid[0])
		dirs=[-1,0,1,0,-1]
		ans=0
		def dfs(i,j,gold):
			gold+=grid[i][j]
			nonlocal ans
			ans=max(ans,gold)
			temp=grid[i][j]
			grid[i][j]=0
			for k in range(4):
				di,dj=i+dirs[k],j+dirs[k+1]
				if 0<=di<m and 0<=dj<n and grid[di][dj]!=0:
					dfs(di,dj,gold)
			grid[i][j]=temp
		for i in range(m):
			for j in range(n):
				if grid[i][j]:
					dfs(i,j,0)
		return ans