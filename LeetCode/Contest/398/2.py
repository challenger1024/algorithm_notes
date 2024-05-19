class Solution:
	def isArraySpecial(self, nums, queries):
		n=len(nums)
		dp=[0]*n
		dp[0]=1
		for i in range(1,n):
			if (nums[i]%2)!=(nums[i-1])%2:
				dp[i]=dp[i-1]+1
			else:
				dp[i]=1
		m=len(queries)
		ans=[False]*m
		for i,(f,t) in enumerate(queries):
			if dp[t]>t-f:
				ans[i]=True
		return ans

#test entry
s=Solution()
nums=[1,3]
queries=[[0,1]]
#nums = [4,3,2,5]
#queries = [[0,2],[2,3]]
#nums = [3,4,1,2,6]
#queries = [[0,4]]
print(s.isArraySpecial(nums,queries))