class Solution:
	def maxProfit(self, k: int, prices: List[int]) -> int:
		dp=[0]*(2*k)
		for i in range(2*k):
			if not  i%2:
				dp[i]=-prices[0]
		for i in range(1,len(prices)):
			for j in range(2*k):
				if j==0:
					dp[j]=max(dp[j],-prices[i])
					continue
				if j%2:
					dp[j]=max(dp[j],dp[j-1]+prices[i])
				else:
					dp[j]=max(dp[j],dp[j-1]-prices[i])
		return dp[-1]