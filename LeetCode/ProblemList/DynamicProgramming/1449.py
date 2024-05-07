class Solution:
	def largestNumber(self, cost, target: int) -> str:
		def make(s,ch):
			ch=str(ch)
			s=str(s)
			for i,c in enumerate(s):
				if ch>=c:
					return int(s[:i]+ch+s[i:])
			return int(s+ch)
		dp=[0]*(target+1)
		for i ,c in enumerate(cost):
			for j in range(c,target+1):
				dp[j]=max(dp[j],make(dp[j-c],i+1))
		return str(dp[target])

#test entry
s=Solution()
cost = [4,3,2,5,6,7,2,5,5]
target = 9
print(s.largestNumber(cost,target))