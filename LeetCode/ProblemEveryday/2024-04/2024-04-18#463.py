class Solution:
	def islandPerimeter(self, grid: List[List[int]]) -> int:
		dirs=[-1,0,1,0,-1]
		m,n=len(grid),len(grid[0])
		ans=0
		for i in range(m):
			for j in range(n):
				if not grid[i][j]:continue
				for k in range(4):
					di,dj=i+dirs[k],j+dirs[k+1]
					if 0<=di<m and 0<=dj<n :
						if grid[di][dj]==0:ans+=1
					else:ans+=1
		return ans