class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		m,n=len(grid),len(grid[0])
		dirs=[-1,0,1,0,-1]
		vis=[[0]*n for _ in range(m)]
		def dfs(i,j):
			if not 0<=i<m or not 0<=j<n or grid[i][j]=='0' or vis[i][j]==1:
				return
			vis[i][j]=1
			for k in range(4):
				x,y=i+dirs[k],j+dirs[k+1]
				dfs(x,y)
			return
		ans=0
		for i in range(m):
			for j in range(n):
				if grid[i][j]=='1' and vis[i][j]==0:
					ans+=1
					dfs(i,j)
		return ans