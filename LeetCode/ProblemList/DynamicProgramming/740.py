from collections import Counter
class Solution:
	def deleteAndEarn(self, nums) -> int:
		cnt=Counter(nums)
		record=[0]+ [0]*max(nums)
		if len(record)<2:
			return 0 if len(record)==0 else 1
		dp=[0]*len(record)
		dp[0],dp[1]=0,cnt[1]
		for i in range(len(record)):
			if i>=2:
				dp[i]=max(i*cnt[i]+dp[i-2],dp[i-1])
		return dp[-1]

#test entry
s=Solution()
#nums = [3,4,2]
nums = [2,2,3,3,3,4]
print(s.deleteAndEarn(nums))