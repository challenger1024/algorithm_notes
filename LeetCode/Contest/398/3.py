class Solution:
	def sumDigitDifferences(self, nums) -> int:
		n=len(nums)
		strs=list(map(str,nums))
		m=len(strs[0])
		dp=[[0]*10 for _ in range(m)]
		for s in strs:
			for i ,c in enumerate(s):
				dp[i][ord(c)-ord('0')]+=1
		ans=0
		for i in range(m):
			for j in range(10):
				ans+=dp[i][j]*(dp[i][j]-1)/2.0
		return int(m*n*(n-1)/2.0-ans)

#test entry
s=Solution()
#nums = [13,23,12]
nums = [10,10,10,10]
print(s.sumDigitDifferences(nums))