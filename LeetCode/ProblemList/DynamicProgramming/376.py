class Solution:
	def wiggleMaxLength(self, nums: List[int]) -> int:
		n=len(nums)
		up=[1]+[0]*(n-1)
		down=[1]+[0]*(n-1)
		for i in range(1,n):
			if nums[i]>nums[i-1]:
				down[i]=down[i-1]
				up[i]=max(up[i-1],down[i-1]+1)
			elif nums[i]<nums[i-1]:
				up[i]=up[i-1]
				down[i]=max(down[i],up[i-1]+1)
			else:
				down[i]=down[i-1]
				up[i]=up[i-1]
		return max(up[-1],down[-1])