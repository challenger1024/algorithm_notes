class Solution:
	def findNumberOfLIS(self, nums) -> int:
		n=len(nums)
		if n==0:
			return 0
		dp=[1]*n
		cnt=[1]*n
		ret=0
		ans=0
		for i in range(n):
			for j in range(i):
				if nums[i]>nums[j]:
					if dp[j]+1>dp[i]:
						dp[i]=dp[j]+1
						cnt[i]=cnt[j]
					elif dp[j]+1==dp[i]:
						cnt[i]+=cnt[j]
			if dp[i]>ret:
				ret=dp[i]
				ans=cnt[i]
			elif dp[i]==ret:
				ans+=cnt[i]
		return ans

s=Solution()
nums=[1,1,1,1,1]
print(s.findNumberOfLIS(nums))