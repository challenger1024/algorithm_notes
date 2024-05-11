m=10**9+7
class Solution:
	def numRollsToTarget(self, n: int, k: int, target: int) -> int:
		if not n<=target <=n*k:
			return 0
		dp=[[0]*(target+1) for _ in range(n+1)]
		dp[0][0]=1
		for i in range(1,n+1):
			for j in range(target,0,-1):
				for d in range(1,min(k,j)+1):
					dp[i][j]+=dp[i-1][j-d]
					dp[i][j]%=m
		return dp[n][target]