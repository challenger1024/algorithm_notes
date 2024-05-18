class Solution:
	def minimumMountainRemovals(self, nums: List[int]) -> int:
		n=len(nums)
		big=[1]*n
		small=[1]*n
		ans=0
		for i in range(n):
			for j in range(i):
				if nums[i]>nums[j]:
					big[i]=max(big[i],big[j]+1)
		for i in range(n-1,-1,-1):
			for j in range(n-1,i,-1):
				if nums[i]>nums[j]:
					small[i]=max(small[i],small[j]+1)
		for i in range(n):
			if big[i]>1 and small[i]>1:
				ans=max(ans,big[i]+small[i]-1)
		return n - ans