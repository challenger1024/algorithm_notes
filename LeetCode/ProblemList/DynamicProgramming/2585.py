mod=10**9+7
class Solution:
	def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
		dp=[1]+[0]*target
		for c,m in types:
			for j in range(target,0,-1):
				for k in range(1,min(c,j//m)+1):
					dp[j]+=dp[j-m*k]
					dp[j]%=mod
		return dp[-1]