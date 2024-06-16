class Solution:
	def numberOfWays(self, s: str) -> int:
		dp=[[0]*2 for _ in range(2)]
		ans=0
		for c in s:
			i=ord(c)-ord('0')
			ans+=dp[1][i^1]
			dp[1][i]+=dp[0][i^1]
			dp[0][i]+=1
		return ans

#solution
'''
状态机DP
设dp[i][j]为选择第i+1栋建筑，类型为j时的方案数
所以有i长度为3，j长度为2；
i=[0,1,2]
j=[0,1]
1. 当i=0时，此时选择第一栋建筑，0或1都可以选，直接
`dp[0][j]+=1`
2. 当i=1时，此时需要考虑上移动建筑要与当前选的建筑类型不同，
`dp[1][1]+=dp[0][0] or dp[1][0]+=dp[0][1]`=`dp[1][j]+=dp[0][j^1]`
3. 当i=2时，与i=1时采取相同的动态转移策略，并且将dp[2][j]加入到答案当中。
此处直接省略了dp[2][j],直接将dp[1][j^1]加入到答案中
'''