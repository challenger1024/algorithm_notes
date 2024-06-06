class Solution:
	def countBits(self, n: int) -> List[int]:
		dp=[0]*(n+1)
		i,j=1,1
		while i<=n:
			k=i
			while i<=n and i<=j+k-1:
				dp[i]=dp[i-j]+1
				i+=1
			j<<=1
		return dp

#solution
'''

'''