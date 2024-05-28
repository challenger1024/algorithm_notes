class Solution:
	def countSubarrays(self, nums: List[int], k: int) -> int:
		ans=0
		sum=0
		l=0
		for r,num in enumerate(nums):
			sum+=num
			while l<r and sum*(r-l+1)>=k:
				sum-=nums[l]
				l+=1
			ans+=r-l+1 if r>l else sum<k
		return ans