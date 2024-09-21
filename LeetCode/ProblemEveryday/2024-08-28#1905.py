class Solution:
	def countSubIslands(self, grid1, grid2) -> int:
		m=len(grid1)
		n=len(grid1[0])
		vis=[[False]*n for _ in range(m)]
		def dfs(i,j):
			vis[i][j]=True
			ret=grid1[i][j]
			for ti,tj in [[0,1],[0,-1],[1,0],[-1,0]]:
				ni=ti+i
				nj=tj+j
				if 0<=ni<m and 0<=nj<n and vis[ni][nj]==False and grid2[ni][nj]==1:
					ret&=dfs(ni,nj)
			return ret
		ans=0
		for i in range(m):
			for j in range(n):
				if vis[i][j]==False and grid2[i][j]==1:
					ans+=dfs(i,j)
		return ans