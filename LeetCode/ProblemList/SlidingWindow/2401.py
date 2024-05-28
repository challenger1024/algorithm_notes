class Solution:
	def longestNiceSubarray(self, nums: List[int]) -> int:
		ans=0
		l=0
		s=0
		for r,num in enumerate(nums):
			while s&num:
				s^=nums[l]
				l+=1
			s|=num
			ans=max(ans,r-l+1)
		return ans