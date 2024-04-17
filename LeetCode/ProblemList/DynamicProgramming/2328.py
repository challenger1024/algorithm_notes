mod=10**9+7
class Solution:
	def countPaths(self, grid: List[List[int]]) -> int:
		m,n=len(grid),len(grid[0])
		dirs=[-1,0,1,0,-1]
		points=[]
		dp=[[1]*n for _ in range(m)]
		for i in range(m):
			for j in range(n):
				points.append([grid[i][j],i,j])
		points.sort()
		ans=0
		for point in points:
			v, i,j=point[0],point[1],point[2]
			for k in range(4):
				di,dj=i+dirs[k],j+dirs[k+1]
				if 0<=di<m and 0<=dj<n and v>grid[di][dj]:
					dp[i][j]+=dp[di][dj]
			ans+=dp[i][j]
		return ans%mod



#Solution
'''
dp[i][j]位置的路径数量=四个方向上递增路径的长度的和+1。
'''