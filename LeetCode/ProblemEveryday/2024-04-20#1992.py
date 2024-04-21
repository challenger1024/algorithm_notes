class Solution:
	def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
		m,n=len(land),len(land[0])
		vis=[[False]*n for _ in range(m)]
		dirs=[-1,0,1,0,-1]
		def dfs(i,j):
			if not 0<=i<m or not 0<=j<n or vis[i][j] or land[i][j]==0:
				return [0,0]
			vis[i][j]=True
			if (i==m-1 and j==n-1) or (j<n-1 and i==m-1 and land[i][j+1]==0) or (i<m-1 and land[i+1][j]==0 and j==n-1)  or (i<m-1 and j<n-1 and land[i+1][j]==0 and land[i][j+1]==0):
				return [i,j]
			ret=[0,0]
			for k in range(4):
				di,dj=i+dirs[k],j+dirs[k+1]
				ret=max(ret,dfs(di,dj))
			return ret
		ans=[]
		for i in range(m):
			for j in range(n):
				if not vis[i][j] and land[i][j]:

					ans.append([i,j]+dfs(i,j))
		return ans