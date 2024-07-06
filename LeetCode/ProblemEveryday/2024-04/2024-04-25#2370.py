class Solution:
	def longestIdealString(self, s: str, k: int) -> int:
		dp=[0]*26
		for c in s:
			n=ord(c)-ord('a')
			dp[n]=max(dp[max(n-k,0):n+k+1])+1
		return max(dp)

#solution
'''
建立长度为26的数组dp,dp[i]表示以i为结尾的子序列的长度。
便利字符串s,对于字符串中的每个字符c,求出其在dp中的位置。
因为dp[c]的状态有下面范围的字符结尾的序列转换而来,取最大值：
max(dp[max(c-k,0):min(c+k,25)])
最终返回dp中的最大值。
'''