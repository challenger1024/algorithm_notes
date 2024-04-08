class Solution:
	def maxSubarraySumCircular(self, nums) -> int:
		n=len(nums)
		pre=nums[0]
		leftSum=nums[0]
		ans=pre
		leftMax=[0]*n
		leftMax[0]=nums[0]
		rightSum=0
		for  i in range(1,n):
			pre=max(pre+nums[i],nums[i])
			ans=max(pre,ans)
			leftSum+=nums[i]
			leftMax[i]=max(leftSum,leftMax[i-1])
		for i in range(n-1,0,-1):
			rightSum+=nums[i]
			ans=max(ans,rightSum+leftMax[i-1])
		return ans

#test entry
s=Solution()
nums=[3,-1,2,-1]
print(s.maxSubarraySumCircular(nums))