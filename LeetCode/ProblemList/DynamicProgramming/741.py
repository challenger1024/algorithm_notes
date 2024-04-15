class Solution:
	def cherryPickup(self, grid) -> int:
		n=len(grid)
		dp=[[[-1]*(n+1) for _ in range(n+1)] for _ in range(2*n+1)]
		for k in range(2,2*n+1):
			for i in range(1,n+1):
				for j in range(1,n+1):
					
#test entry
s=Solution()
grid = [[0,1,-1],[1,0,-1],[1,1,1]]
print(s.cherryPickup(grid))
