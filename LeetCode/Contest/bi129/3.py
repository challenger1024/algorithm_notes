mod=10**9+7
class Solution:
	def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
		dp=[0 for _ in range(zero+one)]
		@cache
		def dfs(j,k,l):
			if k>zero or l>one:
				return 0
			if k+l>limit and (0 not in dp[j-limit:j+1] or 1 not in dp[j-limit:j+1]):
				return 0
			if j==zero+one-1:
				return 1
			ret=0
			ret+=dfs(j+1,k+1,l)
			dp[j+1]=1
			ret+=dfs(j+1,k,l+1)
			dp[j+1]=0
			return ret%mod
		ans=0
		ans+=dfs(0,1,0)
		dp[0]=1
		ans+=dfs(0,0,1)
		return ans%mod
