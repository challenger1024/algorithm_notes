class Solution:
	def incremovableSubarrayCount(self, nums: List[int]) -> int:
		n=len(nums)
		l=0
		while l<n-1 and nums[l]<nums[l+1]:
			l+=1
		if l==n-1:
			return n*(n+1)//2
		ans=l+2
		r=n-1
		while r==n-1 or(nums[r]<nums[r+1]):
			while l>=0 and nums[l]>=nums[r]:
				l-=1
			ans+=l+2
			r-=1
		return ans