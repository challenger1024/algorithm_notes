class Solution:
	def countSubarrays(self, nums, minK: int, maxK: int) -> int:
		ans=0
		n=len(nums)
		max_i=min_i=not_i=-1
		for i,num in enumerate(nums):
			if num==maxK:max_i=i
			if num==minK:min_i=i
			if not minK<=num<=maxK: not_i=i
			ans+=max(0,min(max_i,min_i)-not_i)
		return ans

#test entry
s=Solution()
nums = [1,3,5,2,7,5]
minK = 1
maxK = 5
#nums = [1,1,1,1],minK = 1,maxK = 1
print(s.countSubarrays(nums,minK,maxK))