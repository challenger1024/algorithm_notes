class Solution:
	def lastStoneWeightII(self, stones: List[int]) -> int:
		l=len(stones)
		t=sum(stones)
		s=t//2
		dp=[[False]*(s+1) for _ in range(l+1)]
		dp[0][0]=True
		ans=0
		for i in range(l):
			for j in range(0,s+1):
				dp[i][j]=dp[i-1][j]
				if j>=stones[i]:
					dp[i][j]|=dp[i-1][j-stones[i]]
		return s-2*ans


#Solution
'''
求出stones的和sum.每次拿出两块石头就会减少2*stone[i],stone[i]是两块石头中重量更小的那个。
设被杂碎的石头的总重量为nig,那么剩下最后一块石头的重量就=sum-2nig
nig=sum//2
现在用stones里的石头组成一个最大的nig。
设dp[i][j]为选i块石头时，能形成重量j,那么会有以下几种情况:
1.不选用第i块石头：
dp[i][j]=dp[i-1][j]
2.选用第i块石头，此时应满足j>=stones[i]
dp[i][j]=dp[i-1][j-stones[i]]
'''