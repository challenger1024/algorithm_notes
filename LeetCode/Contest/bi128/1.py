class Solution:
	def scoreOfString(self, s: str) -> int:
		n=len(s)
		def cal(c):
			return ord(c)-ord('a')
		ans=0
		for i in range(n-1):
			ans+=abs(cal(s[i])-cal(s[i+1]))
		return ans

#test entry
so=Solution()
s='zaz'
print(so.scoreOfString(s))