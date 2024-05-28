class Solution:
	def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
		n=len(nums)
		ans=0
		ret=1
		l=0
		for r, num in enumerate(nums):
			while l<=r and  ret*num>=k:
				ret//=nums[l]
				l+=1
			ans+=r-l+1
			if l>r:
				ret=1
			else:
				ret*=num
		return ans