#优化后的状态机dp
class Solution:
	def maxAlternatingSum(self, nums) -> int:
		even,odd=nums[0],0
		for i in range(1,len(nums)):
			even,odd=max(odd+nums[i],even),max(odd,even-nums[i])
		return even