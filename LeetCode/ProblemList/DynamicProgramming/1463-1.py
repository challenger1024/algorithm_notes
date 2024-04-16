#1463#使用地推方程的代码，比较繁琐
class Solution:
	def cherryPickup(self, grid) -> int:
		m,n=len(grid),len(grid[0])
		dp=[[[float('-inf')]*n for _ in range(n)] for _ in range(m)]
#		for i in range(m):
#			dp[i][0][n-1]=grid[0][0]+grid[0][n-1]
		dp[0][0][n-1]=grid[0][0]+grid[0][n-1]
		for i in range(1,m):
			for j1 in range(min(i+1,n)):
				for j2 in range(max(n-i-1,0),n):
					res=dp[i-1][j1][j2]#都从上方走下来
					if j1!=0 :
						if j2!=0:
							res=max(res,dp[i-1][j1-1][j2-1])#都从左上方走过来
						res=max(res,dp[i-1][j1-1][j2])
						if j2!=n-1:
							res=max(res,dp[i-1][j1-1][j2+1])
					if j2!=0:
						res=max(res,dp[i-1][j1][j2-1])
					if j2!=n-1:
						res=max(res,dp[i-1][j1][j2+1])
					if j1!=n-1 :
						if j2!=n-1:
							res=max(res,dp[i-1][j1+1][j2+1])#都从右上方走下来
						res=max(res,dp[i-1][j1+1][j2])
						if j2!=0:
							res=max(res,dp[i-1][j1+1][j2-1])
					if j1!=j2:
						res+=grid[i][j1]+grid[i][j2]
					else:
						res+=grid[i][j1]
					dp[i][j1][j2]=res
		ans=float('-inf')
		for i in range(n):
			for j in range(n):
				ans=max(dp[m-1][i][j],ans)
		return max(ans,0)
