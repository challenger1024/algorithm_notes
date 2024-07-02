MOD=10**9+7
class Solution:
	def knightDialer(self, n: int) -> int:
		f={0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[3,9,0],5:[],6:[1,7,0],7:[2,6],8:[1,3],9:[2,4]}
		dp=[[0]*10 for _ in range(2)]
		for i in range(10):
			dp[1][i]=1
		dp[1][5]=0
		for i in range(2,n+1):
			for j in range(10):
				dp[i%2][j]=0
				for a in f[j]:
					dp[i%2][j]+=dp[1-i%2][a]%MOD
		ans=sum(dp[n%2][j] for j in range(10))%MOD
		return (ans+1)%MOD if n==1 else ans%MOD