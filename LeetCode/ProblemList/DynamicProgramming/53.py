class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		n=len(nums)
		pre=nums[0]
		ans=pre
		for i in range(1,n):
			pre=max(pre+nums[i],nums[i])
			ans=max(ans,pre)
		return ans

