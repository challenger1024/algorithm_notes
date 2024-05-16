class Solution:
	def minimumDeleteSum(self, s1: str, s2: str) -> int:
		m,n=len(s1),len(s2)
		dp=[[0]*(n+1) for _ in range(m+1)]
		for i in range(1,m+1):
			dp[i][0]=dp[i-1][0]+ord(s1[i-1])
		for j in range(1,n+1):
			dp[0][j]=dp[0][j-1]+ord(s2[j-1])
		for i in range(m):
			for j in range(n):
				dp[i+1][j+1]=dp[i][j] if s1[i]==s2[j] else min(dp[i][j+1]+ord(s1[i]),dp[i+1][j]+ord(s2[j]))
		return dp[m][n]

#solution
'''
和题目#583差不多，指示修改一下判断逻辑，把+1改成ascii码，具体题解可见文件#583-2.py
'''