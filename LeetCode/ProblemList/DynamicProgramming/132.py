class Solution:
	def minCut(self, s: str) -> int:
		t='#'+'#'.join(s)+'#'
		n=len(t)
		arms=[0]*n
		c=r=0
		for i in range(n):
			arm=min(arms[2*c-i],r-i) if r>i else 1
			while i-arm>=0 and i+arm<n and t[i-arm]==t[i+arm]:
				arm+=1
			arms[i]=arm
			if i+arm>r:
				c=i
				r=i+arm
		m=len(s)
		dp=[float('inf')]*(m+1)
		dp[0]=-1
		for i in range(1,m+1):
			for j in range(i,m+1):
				mid=i+j-1
				if arms[mid]-1>=j-i+1:
					dp[j]=min(dp[j],dp[i-1]+1)
#		print(arms)
		return dp[-1]

#test entry
so=Solution()
s='aa'
print(so.minCut(s))