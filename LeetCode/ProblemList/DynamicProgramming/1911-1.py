#状态机dp
class Solution:
	def maxAlternatingSum(self, nums) -> int:
		n=len(nums)
		dp=[[0]*2 for _ in range(n)]
		dp[0][0]=nums[0]
		ans=nums[0]
		for i in range(1,n):
			dp[i][1]=max(dp[i-1][0]-nums[i],dp[i-1][1])
			dp[i][0]=max(dp[i-1][1]+nums[i],dp[i-1][0])
#			ans=max(dp[i][0],dp[i][1],ans)
#		print(dp)
		return dp[-1][0]

#test entry
s=Solution()
nums=[4,2,5,3]
print(s.maxAlternatingSum(nums))