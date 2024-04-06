class Solution:
	def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
		mod=10**9+7
		dp=[1]+[0]*high
		for i in range(1,high+1):
			if i-one>=0:dp[i]+=dp[i-one]%mod
			if i-zero>=0:dp[i]+=dp[i-zero]%mod
		ans=0
		for i in range(low,high+1):
			ans+=dp[i]
		return ans%mod

#test entry
s=Solution()
low = 2
high = 3
zero = 1
one = 2
#low = 3
#high = 3
#zero = 1
#one = 1
print(s.countGoodStrings(low,high,zero,one))