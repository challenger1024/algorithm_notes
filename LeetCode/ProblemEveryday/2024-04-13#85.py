class Solution:
	def maximalRectangle(self, matrix: List[List[str]]) -> int:
		m,n=len(matrix),len(matrix[0])
		width=[[0]*n for _ in range(m)]
		for i in range(m):
			for j in range(n):
				if matrix[i][j]=='1':
					width[i][j]=1 if j==0 else width[i][j-1] +1
		ret=0
		for i in range(m):
			for j in range(n):
				w=width[i][j]
				area=w
				for k in range(i-1,-1,-1):
					w=min(width[k][j],w)
					area=max(area,w*(i-k+1))
				ret=max(ret,area)
		return ret