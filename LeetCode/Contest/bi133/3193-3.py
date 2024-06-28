#dp+前缀和(时间)优化+空间优化
MOD=10**9+7
class Solution:
	def numberOfPermutations(self, n: int, req: List[List[int]]) -> int:
		q=[-1]*n
		q[0]=0
		for end,cnt in req:
			q[end]=cnt
		if q[0]:
			return 0
		m=max(q)#最大要求的逆序对数量
		dp=[0]*(m+1)#优化一个维度，因为只需要用到dp[i-1]来更新dp[i]
		dp[0]=1#边界条件，有0个逆序对时，方案数为1
		for i in range(1,n):
			mx=m if q[i]<0 else q[i]
			r=q[i-1]
			if r>=0:
				for j in range(m+1):
					dp[j]=dp[r] if r<=j<=min(mx,i+r) else 0
			else:
				for j in range(1,mx+1):
					dp[j]=(dp[j]+dp[j-1])%MOD
				for j in range(mx,i,-1):
					dp[j]=(dp[j]-dp[j-i-1])%MOD
		return dp[q[-1]]