class Solution:
	def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
		n=len(ages)
		ans=0
		p=sorted(zip(scores,ages))
		dp=[0]*n
		for i in range(n):
			for j in range(i):
				if p[i][1]>=p[j][1]:
					dp[i]=max(dp[i],dp[j])
			dp[i]+=p[i][0]
			ans=max(ans,dp[i])
		return ans