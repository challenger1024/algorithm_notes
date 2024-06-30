#地推
class Solution:
	def maxSumDivThree(self, nums: List[int]) -> int:
		dp=[[-inf]*3 for _ in range(2)]
		dp[0][0]=0
		for i,a in enumerate(nums):
			for j in range(3):
				dp[(i+1)%2][j]=max(dp[i%2][j],dp[i%2][(j+a)%3]+a)
		return dp[len(nums)%2][0]