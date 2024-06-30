class Solution:
	def maxScore(self, nums: List[int], x: int) -> int:
		res=nums[0]
		dp=[-inf,-inf]
		dp[nums[0]%2]=nums[0]
		for i in range(1,len(nums)):
			status=nums[i]%2
			cur=max(dp[status]+nums[i],dp[1-status]-x+nums[i])
			res=max(res,cur)
			dp[status]=max(dp[status],cur)
		return res