class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		m,n=len(word1),len(word2)
		if m*n==0:
			return m+n
		dp=[[0]*(n+1) for _ in range(m+1)]
		for i in range(1,m+1):
			dp[i][0]=i
		for j in range(1,n+1):
			dp[0][j]=j
		for i in range(m):
			for j in range(n):
				u=dp[i][j+1]+1
				l=dp[i+1][j]+1
				lu=dp[i][j]+1
				if word1[i]==word2[j]:
					lu-=1
				dp[i+1][j+1]=min(u,l,lu)
		return dp[m][n]
