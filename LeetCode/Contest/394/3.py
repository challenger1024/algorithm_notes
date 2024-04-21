from collections import Counter
class Solution:
	def minimumOperations(self, grid) -> int:
		m,n=len(grid),len(grid[0])
		matrix=[[0]*10 for _ in range(n)]
		for i in range(n):
			for j in range(m):
				matrix[i][grid[j][i]]+=1
#		print(matrix)
		for i in range(1,n):
			for j in range(10):
				val=0
				for k in range(10):
					if k==j:continue
					val=max(val,matrix[i-1][k])
				matrix[i][j]+=val
#		print(matrix)
		return m*n-max(matrix[n-1])

#test entry
s=Solution()
#grid = [[1],[2],[3]]
#grid = [[1,1,1],[0,0,0]]
grid = [[1,0,2],[1,0,2]]
print(s.minimumOperations(grid))