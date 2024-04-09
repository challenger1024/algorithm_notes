class Solution:
	def jewelleryValue(self, frame) -> int:
		m,n=len(frame),len(frame[0])
		if n==0 and m==0:return 0
		dp=[[0]*(n+1) for _ in range(m+1)]
		for i in range(1,m+1):
			for j in range(1,n+1):
				dp[i][j]=max(dp[i-1][j],dp[i][j-1])+frame[i-1][j-1]
		return dp[m][n]

#test entry
s=Solution()
frame=[[1,3,1],[1,5,1],[4,2,1]]
print(s.jewelleryValue(frame))