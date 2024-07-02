class Solution:
	def validPartition(self, nums) -> bool:
		n=len(nums)
		dp=[False]*(n+1)
		dp[0]=True
		for i in range(1,n+1):
			if i>=2:
				dp[i]=(dp[i-2] and nums[i-1]==nums[i-2]) 
			if i>=3:
				dp[i]=dp[i] or (dp[i-3] and ((nums[i-3]==nums[i-2] and nums[i-2]==nums[i-1]) or (nums[i-3]+1==nums[i-2] and nums[i-2]+1==nums[i-1])))
#		print(dp)
		return dp[n]

#test entry
s=Solution()
nums=[803201,803201,803201,803201,803202,803203]
print(s.validPartition(nums))