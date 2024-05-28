class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		n=len(nums)
		if not nums:
			return 0
		sum=0
		l=0
		ans=n+1
		for r , num in enumerate(nums):
			sum+=num
			while l<n and sum>=target:
				ans=min(ans,r-l+1)
				sum-=nums[l]
				l+=1
		return ans if ans!=n+1 else 0