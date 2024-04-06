class Solution:
	def combinationSum4(self, nums, target: int) -> int:
		dp=[0]*(target+1)
		dp[0]=1
		for i in range(target+1):
			for num in nums:
				if i-num>=0:
					dp[i]+=dp[i-num]
		return dp[target]

#test entry
s=Solution()
nums = [9]
target = 3
#nums = [1,2,3]
#target = 4
print(s.combinationSum4(nums,target))