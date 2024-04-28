class Solution:
	def numberOfRightTriangles(self, grid) -> int:
		m,n=len(grid),len(grid[0])
		col=[0]*m
		row=[0]*n
		for i in range(m):
			for j in range(n):
				if grid[i][j]:
					col[i]+=1
					row[j]+=1
		ans=0
		for i in range(m):
			for j in range(n):
				if grid[i][j]==1:
					ans+=(col[i]-1)*(row[j]-1)
		return ans

#test entry
s=Solution()
grid = [[0,1,0],[0,1,1],[0,1,0]]
#grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
#grid = [[1,0,1],[1,0,0],[1,0,0]]
print(s.numberOfRightTriangles(grid))