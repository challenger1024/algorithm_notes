class Solution:
	def maxAbsoluteSum(self, nums) -> int:
		sum=0
		ans=0
		for num in nums:

			ans=max(ans,abs(sum))
		return ans

#test entry
s=Solution()
nums=[-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9]
print(s.maxAbsoluteSum(nums))