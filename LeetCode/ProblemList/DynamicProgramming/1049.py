class Solution:
	def lastStoneWeightII(self, stones: List[int]) -> int:
		t=sum(stones)
		s=t//2
		dp=[0 for _ in range(s+1)]
		for x in stones:
			for j in range(s,x-1,-1):
				dp[j]=max(dp[j] , dp[j-x]+x)
		return t-2*dp[s]

