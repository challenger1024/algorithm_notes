class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		target=sum(nums)
		if target%2:return False
		target//=2
		dp=[True]+[False for _ in range(target)]
		s=0
		for num in nums:
			s=min(target,s+num)
			for j in range(s,num-1,-1):
				dp[j]=dp[j] or dp[j-num]
		return dp[-1]