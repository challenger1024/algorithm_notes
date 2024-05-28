class Solution:
	def incremovableSubarrayCount(self, nums: List[int]) -> int:
		n=len(nums)
		r=n-1
		while nums[r]>nums[r-1]:
			r-=1
			if r==0:
				break
		if r==0:
			return n*(n+1)//2
		ans=n-r
		l=0
		while l==0 or nums[l]<nums[l+1]:
			while nums[l]<nums[r]:
				r+=1
			ans+=n-r
			l+=1
		return ans