#O(n2)时间复杂度求最长回文子串
class Solution:
	def longestPalindrome(self, s: str) -> str:
		n=len(s)
		ans=s[0]
		maxSize=1
		if n==1:
			return s
		dp=[[False]*n for _ in range(n)]
		for i in range(n):
			dp[i][i]=True
		for l in range(2,n+1):
			for i in range(n):
				j=i+l-1
				if j>=n:
					break
				elif l<=2:
					dp[i][j]=s[i]==s[j]
				else:
					dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
				if dp[i][j] and l>maxSize:
					ans=s[i:j+1]
					maxSize=l
		return ans
