class Solution:
	def maxAbsoluteSum(self, nums) -> int:
		mi=nums[0]
		ma=nums[0]
		ans=max(abs(ma),abs(mi))
		for num in nums[1:]:
			mi=min(num,mi+num)
			ma=max(num,ma+num)
			ans=max(ans,abs(mi),abs(ma))
		return ans

#test entry
s=Solution()
nums=[-1]
#nums=[-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9]
print(s.maxAbsoluteSum(nums))