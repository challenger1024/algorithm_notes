class Solution:
	def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
		if not envelopes:
			return 0
		envelopes.sort(key=lambda x:(x[0],-x[1]))
		n=len(envelopes)
		dp=[]
		for i in range(n):
			if not dp or dp[-1]<envelopes[i][1]:
				dp.append(envelopes[i][1])
			else:
				loc=bisect_left(dp,envelopes[i][1])
				dp[loc]=envelopes[i][1]
		return len(dp)