MOD=10**9+7
class Solution:
	def checkRecord(self, n: int) -> int:
		dp=[[[0]*3 for _ in range(2)] for _ in range(n+1)]
		dp[0][0][0]=1
		for i in range(1,n+1):
			dp[i][0][0]+=(dp[i-1][0][0]+dp[i-1][0][1]+dp[i-1][0][2])%MOD
			dp[i][1][0]+=(dp[i-1][0][0]+dp[i-1][0][1]+dp[i-1][0][2])%MOD
			dp[i][0][1]+=dp[i-1][0][0]%MOD
			dp[i][0][2]+=dp[i-1][0][1]%MOD
			dp[i][1][1]+=dp[i-1][1][0]%MOD
			dp[i][1][2]+=dp[i-1][1][1]%MOD
			dp[i][1][0]+=(dp[i-1][1][0]+dp[i-1][1][1]+dp[i-1][1][2])%MOD
		return (dp[n][0][0]+dp[n][0][1]+dp[n][0][2]+dp[n][1][0]+dp[n][1][1]+dp[n][1][2])%MOD

#solution
'''
动态规划
'''