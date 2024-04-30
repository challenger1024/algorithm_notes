class Solution:
	def tallestBillboard(self, rods) -> int:
		n=len(rods)
		s=sum(rods)
		dp=[[float('-inf')]*(s+1) for _ in range(n+1)]
		dp[0][0]=0
		for i in range(1,n+1):
			num=rods[i-1]
			for j in range(s+1):
				dp[i][j]=dp[i-1][j]
				if dp[i-1][abs(j-num)]!=float('-inf'):
					dp[i][j]=max(dp[i][j],dp[i-1][abs(j-num)]+num)
				if j+num<=s and dp[i-1][j+num]!=float('-inf'):
					dp[i][j]=max(dp[i][j],dp[i-1][j+num]+num)
		return dp[n][0]//2 if dp[n][0]>=0 else 0

#test entry
s=Solution()
rods=[5160,9191,6410,4657,7492,1531,8854,1253,4520,9231,1266,4801,3484,4323,5070,1789,2744,5959,9426,4433,4404,5291,2470,8533,7608,2935,8922,5273,8364,8819,7374,8077,5336,8495,5602,6553,3548,5267,9150,3309]
#rods=[2,4,8,16]
#rods=[1,2,3,6]
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