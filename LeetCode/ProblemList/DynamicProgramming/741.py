class Solution:
	def cherryPickup(self, grid) -> int:
		n=len(grid)
		dp=[[[float('-inf')]*n for _ in range(n)] for _ in range(2*n-1)]
		dp[0][0][0]=grid[0][0]
		for k in range(1,2*n-1):
			for x1 in range(max(k-n+1,0),min(k+1,n)):#当k属于[0,n-1]时，x1,y1可以覆盖grid的左上半区，当k属于区间[n,2*n-2]时，x1,y1可以覆盖grid的右下半区
				y1=k-x1
				if grid[x1][y1]==-1:
					continue
				for x2 in range(max(k-n+1,0),min(k+1,n)):
					y2=k-x2
					if grid[x2][y2]==-1:
						continue
					res=dp[k-1][x1][x2]#都从左边走过来
					if x1!=0 and x2!=0:
						res=max(res,dp[k-1][x1-1][x2-1])#都从上方走过来
					if x1!=0 :
						res=max(res,dp[k-1][x1-1][x2])#x1从上方走来，x2从左边走来
					if x2!=0:
						res=max(res,dp[k-1][x1][x2-1])#x1从左边走来，x2从上方走来
					if x1!=x2:
						res+=grid[x1][y1]+grid[x2][y2]
					else:
						res+=grid[x1][y1]
					dp[k][x1][x2]=res
		return max(dp[2*n-2][n-1][n-1],0)


#test entry
s=Solution()
grid = [[0,1,-1],[1,0,-1],[1,1,1]]
print(s.cherryPickup(grid))
