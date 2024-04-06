mod=10**9+7
class Solution:
	def countHousePlacements(self, n: int) -> int:
		if n<2:
			return 4
		dp=[0]+[0]*n
		dp[1]=2
		dp[2]=3
		for i in range(3,n+1):
			dp[i]=(dp[i-1]+dp[i-2])%mod
		return (dp[n]*dp[n])%mod

#test entry
s=Solution()
n=1
print(s.countHousePlacements(n))