mod=10**9+7
class Solution:
	def profitableSchemes(self, n: int, minProfit: int, group, profit) -> int:
		dp=[[0]*(minProfit+1) for _ in range(n+1)]
		for i in range(n+1):
			dp[i][0]=1
		for people,money in zip(group,profit):
			for i in range(n,-1,-1):
				for j in range(minProfit,-1,-1):
					if i>=people :
						dp[i][j]+=dp[i-people][max(j-money,0)]
		return dp[n][minProfit]%mod

#test entry
s=Solution()
n=5
minProfit=3
group=[2,2]
profit=[2,3]
print(s.profitableSchemes(n,minProfit,group,profit))