mod=10**9+7
class Solution:
	def maxProductPath(self, grid: List[List[int]]) -> int:
		m=len(grid)
		n=len(grid[0])
		bdp=[[1]*(n+1) for _ in range(m+1)]#保存最大值
		sdp=[[1]*(n+1) for _ in range(m+1)]#保存最小值
		bdp[0][0]=grid[0][0]
		sdp[0][0]=grid[0][0]
		for i in range(1,m):
			bdp[i][0]=max(bdp[i-1][0]*grid[i][0],sdp[i-1][0]*grid[i][0])
			sdp[i][0]=min(bdp[i-1][0]*grid[i][0],sdp[i-1][0]*grid[i][0])
		for j in range(1,n):
			bdp[0][j]=max(bdp[0][j-1]*grid[0][j],sdp[0][j-1]*grid[0][j])
			sdp[0][j]=min(bdp[0][j-1]*grid[0][j],sdp[0][j-1]*grid[0][j])
		for i in range(1,m):
			for j in range(1,n):
				bdp[i][j]=max(bdp[i-1][j]*grid[i][j],bdp[i][j-1]*grid[i][j],sdp[i-1][j]*grid[i][j],sdp[i][j-1]*grid[i][j])
				sdp[i][j]=min(bdp[i-1][j]*grid[i][j],bdp[i][j-1]*grid[i][j],sdp[i-1][j]*grid[i][j],sdp[i][j-1]*grid[i][j])
		return max(bdp[m-1][n-1]%mod if bdp[m-1][n-1]>=0 else bdp[m-1][n-1],-1)