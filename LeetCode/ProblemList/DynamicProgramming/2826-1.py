#当最长非严格递增子序列做
class Solution:
	def minimumOperations(self, nums: List[int]) -> int:
		n=len(nums)
		if n==0:
			return 0
		dp=[1]*n
		for i in range(1,n):
			for j in range(i):
				if nums[i]>=nums[j]:
					dp[i]=max(dp[i],dp[j]+1)
		return n - max(dp)