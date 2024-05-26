class Solution:
	def minSwaps(self, nums: List[int]) -> int:
		n=len(nums)
		k=sum(nums)
		c=0
		e=0
		ans=0
		for i,v in enumerate(nums):
			c+=v
			e+=v
			if i>=k:
				c-=nums[i-k]
			if i>=k-1:
				ans=max(ans,c)
			if i>=n-k:
				e-=nums[i-(n-k)]
			if i>=n-k-1:
				ans=max(ans,k-e)
		return k-ans