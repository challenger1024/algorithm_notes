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
#		i,j=sum(zeros),sum(ones)
		dp=[[0]*(n+1) for _ in range(m+1)]
		for k in range(l):
			for i in range(m,-1,-1):
				for j in range(n,-1,-1):
					x=zeros[k]
					y=ones[k]
					if i>=x and j>=y:
						dp[i][j]=max(dp[i-x][j-y]+1,dp[i][j])
		return dp[m][n]


#solution
'''
设dp[i][j]是有i个0和j个1时子集的长度
统计strs中每个str里0和1的数目,保存到数组zeros,ones中
便利zeros和ones,则有两种情况
1.选用当前的zeros[k]和ones[k],那么状态有：
dp[i][j]=dp[i-zeros[k]][j-ones[k]]+1
2.不选data[k]
dp[i][j]=dp[i][j]
注意：i<=m,j<=n;
最后返回dp[m][n]
'''