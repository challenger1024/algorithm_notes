class Solution:
	def isArraySpecial(self, nums) -> bool:
		n=len(nums)
		dp=[0]*n
		dp[0]=1
		for i in range(1,n):
			if (nums[i]%2)!=(nums[i-1])%2:
				dp[i]=dp[i-1]+1
			else:
				dp[i]=1
		return dp[-1]==n

#test entry
s=Solution()
nums = [4,3,1,6]
print(s.isArraySpecial(nums))