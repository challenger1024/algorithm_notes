class Solution:
	def hasValidPath(self, grid: List[List[str]]) -> bool:
		m,n=len(grid),len(grid[0])
		if (m+n)%2==0 or grid[0][0]==')' or grid[m-1][n-1]=='(':return False
		@cache
		def dfs(c,i,j):
			if c>m-i+n-j-1:return False
			if i==m-1 and j==n-1:return c==1
			c+=1 if grid[i][j]=='(' else -1
			return c>=0 and ( (i<m-1 and dfs(c,i+1,j)) or (j<n-1 and dfs(c,i,j+1)))
		return dfs(0,0,0)