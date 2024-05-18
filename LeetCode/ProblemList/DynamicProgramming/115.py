mod=10**9+7
class Solution:
	def numDistinct(self, s: str, t: str) -> int:
		m,n=len(s),len(t)
		if m<n:
			return 0
		dp=[[0]*(n+1) for _ in range(m+1)]
		dp[0][0]=1
		for i in range(m):
			dp[i+1][0]=dp[i][0]

		for i in range(m):
			for j in range(n):
				dp[i+1][j+1]=(dp[i][j]+dp[i][j+1] if s[i]==t[j] else dp[i][j+1])%mod
		return dp[m][n]%mod

