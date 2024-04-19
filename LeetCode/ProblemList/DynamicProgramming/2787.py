mod=10**9+7
class Solution:
	def numberOfWays(self, n: int, x: int) -> int:
		nums=[]
		for i in range(1,n+1):
			if i**x>n:break
			nums.append(i**x)
		dp=[1]+[0 for _ in range(n)]
		for num in nums:
			for j in range(n,num-1,-1):
				dp[j]+=dp[j-num]%mod
		return dp[-1]%mod if dp[-1]!=0 else 0