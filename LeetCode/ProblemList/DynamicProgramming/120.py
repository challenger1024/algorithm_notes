class Solution:
	def minimumTotal(self, triangle) -> int:
		n=len(triangle)
		for i in range(1,n):
			for j in range(len(triangle[i])):
				if j==0:triangle[i][j]+=triangle[i-1][j]
				elif j==len(triangle[i])-1:triangle[i][j]+=triangle[i-1][j-1]
				else:triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
		return min(triangle[n-1])
