class Solution:
	def minDifference(self, nums: List[int]) -> int:
		n=len(nums)
		if n<=4:
			return 0
		nums.sort()
		ans=nums[-1]-nums[0]
		for i in range(4):
			ans=ans if ans<nums[n-1-i]-nums[3-i] else nums[n-1-i]-nums[3-i]
		return ans