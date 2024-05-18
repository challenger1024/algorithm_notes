class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		ans=0
		n=len(prices)
		dp=inf
		for i ,p in enumerate(prices):
			dp=min(dp,p)
			ans=max(ans,p-dp)
		return ans