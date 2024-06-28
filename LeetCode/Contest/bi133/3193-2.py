MOD=10**9+7
class Solution:
	def numberOfPermutations(self, n: int, req: List[List[int]]) -> int:
		q=[-1]*n
		q[0]=0
		for end,cnt in req:
			q[end]=cnt
		if q[0]:
			return 0
		m=max(q)#最大的要求逆序对数量
		dp=[[0]*(m+1) for _ in range(n)]#dp[i][j]表示前i个元素有j个逆序对
		dp[0][0]=1#边界条件:当前0个元素有0个逆序对时，有一个满足条件的排列
		for i in range(1,n):
			mx=m if q[i]<0 else q[i]#第i个元素和前i-1个元素能形成的最多mx个逆序对,如果前i个元素有逆序对数量要求则mx=要求的数量，没有要求的话mx=最大要求逆序对数量
			r=q[i-1]
			if r>=0:
				for j in range(r,min(mx,i+r)+1):#需要满足最少和最多逆序对要求
					dp[i][j]=dp[i-1][r]#前i个元素有j个逆序对的排列数用前i-1个元素有r个逆序对的排列数更新
			else:
				for j in range(mx+1):#j没有最低限制,至少有0个
					dp[i][j]=sum(dp[i-1][j-k] for k in range(min(i,j)+1))%MOD
		return dp[n-1][q[-1]]