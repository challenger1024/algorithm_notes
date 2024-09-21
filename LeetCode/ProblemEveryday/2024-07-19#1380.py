class Solution:
	def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
		m,n=len(matrix),len(matrix[0])
		smst=[10**6]*m
		bgst=[0]*n
		for i in range(m):
			for j in range(n):
				smst=matrix[i][j] if matrix[i][j]<smst[i] else smst[i]
				bgst[j]=