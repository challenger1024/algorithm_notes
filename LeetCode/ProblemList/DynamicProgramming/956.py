class Solution:
	def tallestBillboard(self, rods) -> int:
		n=len(rods)
		s=sum(rods)
		dp=[[float('-inf')]*(s+1) for _ in range(n+1)]
		for i in range(1,n+1):
			num=rods[i-1]
			for j in range(s+1):
				dp[i][j]=dp[i-1][j]
				if dp[i-1][abs(j-num)]!=float('-inf'):
					dp[i][j]=max(dp[i][j],dp[i-1][abs(j-num)]+num,dp[i-1][j])
				if j+num<=s and dp[i-1][j+num]!=float('-inf'):
					dp[i][j]=max(dp[i][j],dp[i-1][j+num]+num,dp[i-1][j])
		return dp[n][0]//2# if dp[n][0]>=0 else 0

#test entry
s=Solution()
#rods=[2,4,8,16]
rods=[1,2,3,6]
print(s.tallestBillboard(rods))
#Solution
'''
设dp[i][j]是选择i 个数字时，差为j的最大正数和。
那么dp[i][j]应该有下面的转移状态：
1.选第[i]个数字，且另nums[i]放在较短的支架上
dp[i][j]=dp[i-1][j+nums[i]]+nums[i]
2.选第i 个数字，且放在较长的支架上
dp[i][j]=dp[i-1][j-nums[i]]+nums[i]
3.不选第i个数字
dp[i][j]=dp[i-1][j]
三种情况取得最大值
最终，选用n跟钢筋，差=0时的值//2及:dp[n][0]//2为答案

'''