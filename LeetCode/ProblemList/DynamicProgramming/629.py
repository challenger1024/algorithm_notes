MOD=10**9+7
class Solution:
	def kInversePairs(self, n: int, k: int) -> int:
		dp=[0]*(k+1)
		dp[0]=1#边界条件，0个数字有0个逆序对，形成一个排列
		for i in range(1,n):
			for j in range(1,k+1):
				dp[j]=(dp[j]+dp[j-1])%MOD
			for j in range(k,i,-1):
				dp[j]=(dp[j]-dp[j-i-1])%MOD
		return dp[k]