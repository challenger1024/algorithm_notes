class Solution:
	def maximumTotalCost(self, nums: List[int]) -> int:
		ans=0
		x,y=nums[0],nums[0]
		for i,a in enumerate(nums):
			if i>0:
				temp=x
				x=x+a if x>y else y+a
				y=temp-a
		return x if x>y else y
