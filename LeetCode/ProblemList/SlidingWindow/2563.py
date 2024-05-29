class Solution:
	def countFairPairs(self, nums, lower: int, upper: int) -> int:
		n=len(nums)
		l,r=n,n
		ans=0
		if n<2:
			return 0
		nums.sort()
		for j,x in enumerate(nums):
			while r and nums[r-1]>upper-x:
				r-=1
			while l and nums[l-1]>=lower-x:
				l-=1
			ans+=min(j,r)-min(j,l)
		return ans

#test entry
s=Solution()
nums=[0,1,7,4,4,5]
lower=3
upper=6
print(s.countFairPairs(nums,lower,upper))