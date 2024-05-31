class Solution:
	def splitArray(self, nums: List[int], m: int) -> int:
		n=len(nums)
		s=[0]
		for i in range(n):
			s.append(s[-1]+nums[i])
		dp=[[10**18]*(m+1) for _ in range(n+1)]
		dp[0][0]=0
		for i in range(1,n+1):
			for j in range(1,min(i,m)+1):
				for k in range(i):
					dp[i][j]=min(dp[i][j],max(dp[k][j-1],s[i]-s[k]))
		return dp[n][m]

#test entry
'''
动态规划
定义dp[i][j]为将数组中的前i个元素分成j组时，最小值的最大值。
1. 第一层循环便利每个元素
2. 第二层循环便利k组
3. 第三层循环便利当前第j组的第一个元素，当前的这个子数组就是[k,i]这一段。
dp[n][m]及为答案。
'''