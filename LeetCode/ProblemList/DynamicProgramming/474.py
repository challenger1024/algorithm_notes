class Solution:
	def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
		l=len(strs)
		zeros,ones=[0]*l,[0]*l
		for k ,str in enumerate(strs):
			zero,one=0,0
			for c in str:
				if c=='0':zero+=1
				else:one+=1
			zeros[k]=zero
			ones[k]=one
		i,j=sum(zeros),sum(ones)
		dp=[[0]*(j+1) for _ in range(i+1)]
		i,j=0,0
		for k in range(l):
#			if i+zeros[k]>m or j+ones[k]>n:
#				continue
			i+=zeros[k]
			j+=ones[k]
			x,y=0,0
			for o in range(k,-1,-1):
				x+=zeros[o]
				y+=ones[o]
				dp[i][j]=max(dp[i-x][j-y],dp[i-x][j-y]+1,dp[i][j])
		return dp[m][n]


'''
设dp[i][j]是有i个0和j个1时子集的长度
统计strs中每个str里0和1的数目,保存到数组zeros,ones中
便利zeros和ones,则有两种情况
1.选用当前的ones[k],那么状态有：
dp[i][j]=dp[i-zeros[k]][j-ones[k]]+1
2.不选data[k]
dp[i][j]=dp[i-zeros[k]][j-ones[k]]
注意：i<=m,j<=n;

'''