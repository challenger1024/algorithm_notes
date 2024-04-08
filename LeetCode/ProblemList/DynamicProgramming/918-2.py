class Solution:
	def maxSubarraySumCircular(self, nums) -> int:
		n=len(nums)
		pre1,pre2=nums[0],nums[0]
		mi,ma=pre1,pre2
		sum=nums[0]
		for i in range(1,n):
			sum+=nums[i]
			pre1=min(pre1+nums[i],nums[i])
			pre2=max(pre2+nums[i],nums[i])
			mi=min(mi,pre1)
			ma=max(pre2,ma)
		if ma<0:return ma
		return max(sum-mi,ma)


#test entry
s=Solution()
nums=[-3,-2,-3]
#nums=[3,-1,2,-1]
print(s.maxSubarraySumCircular(nums))