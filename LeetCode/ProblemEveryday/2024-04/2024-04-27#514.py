class Solution:
	def findRotateSteps(self, ring: str, key: str) -> int:
		n,m=len(ring),len(key)
		pos=[[] for _ in range(26)]
		for i,c in enumerate(ring):
			pos[ord(c)-ord('a')].append(i)
		dp=[[float('inf')]*n for _ in range(m)]
		for i in pos[ord(key[0])-ord('a')]:
			dp[0][i]=min(i,n-i)+1
		for i in range(1,m):
			for j in pos[ord(key[i])-ord('a')]:
				for k in pos[ord(key[i-1])-ord('a')]:
					dp[i][j]=min(dp[i][j],dp[i-1][k]+min(abs(j-k),n-abs(j-k))+1)
		return min(dp[m-1])