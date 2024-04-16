class Solution:
	def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
		m,n=len(matrix),len(matrix[0])
		dirs=[-1,0,1,0,-1]
		points=[]
		dp=[[1]*n for _ in range(m)]
		for i in range(m):
			for j in range(n):
				points.append([matrix[i][j],i,j])
		points.sort()
		ans=0
		for point in points:
			v, i,j=point[0],point[1],point[2]
			for k in range(4):
				di,dj=i+dirs[k],j+dirs[k+1]
				if 0<=di<m and 0<=dj<n and v>matrix[di][dj]:
					dp[i][j]=max(dp[i][j],dp[di][dj]+1)
			ans=max(ans,dp[i][j])
		return ans