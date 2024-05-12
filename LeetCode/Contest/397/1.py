class Solution:
	def findPermutationDifference(self, s: str, t: str) -> int:
		n=len(s)
		d={}
		for i,ch in enumerate(s):
			d[ch]=i
		ans=0
		for i,ch in enumerate(t):
			ans+=abs(i-d[ch])
		return ans

#test entry
so=Solution()
s = "abcde"
t = "edbac"
print(so.findPermutationDifference(s,t))