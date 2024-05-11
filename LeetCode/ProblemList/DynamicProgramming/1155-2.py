mod=10**9+7
class Solution:
	def numRollsToTarget(self, n: int, k: int, target: int) -> int:
		@cache
		def dfs(i,c):
			if i==0 and c==0:
				return 1
			if i<0 or c<0:
				return 0
			ret=0
			for j in range(1,k+1):
				ret+=dfs(i-1,c-j)
			return ret%mod
		return dfs(n,target)%mod