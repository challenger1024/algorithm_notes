class Solution:
	def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
		n=len(nums)
		dp=[0]+[float('-inf') for _ in range(target)]
		s=0
		for num in nums:
			s=min(s+num,target)
			for j in range(s,num-1,-1):
				dp[j]=max(dp[j],dp[j-num]+1)
		return dp[-1] if dp[-1]>0 else -1