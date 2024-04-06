class Solution:
	def rob(self, nums) -> int:
		n=len(nums)
		if n<4:
			return max(nums)
		dp1=[0]*(n-1)
		dp2=[0]*(n)
		dp1[0],dp1[1]=nums[0],max(nums[0],nums[1])
		dp2[1],dp2[2]=nums[1],max(nums[1],nums[2])
		for i in range(2,n-1):
			dp1[i]=max(dp1[i-1],dp1[i-2]+nums[i])
			dp2[i+1]=max(dp2[i],dp2[i-1]+nums[i+1])
		return max(dp1[n-2],dp2[n-1])

s=Solution()
nums=[1,2,3,1]
print(s.rob(nums))