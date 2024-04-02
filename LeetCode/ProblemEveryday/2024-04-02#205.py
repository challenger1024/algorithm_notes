class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		d1=dict()
		d2=dict()
		for i,c in enumerate(s):
			if c in d1 and d1[c]!=t[i]: return False
			if t[i] in d2 and d2[t[i]]!=c:return False
			d1[c]=t[i]
			d2[t[i]]=c
		return True

#test entry
so=Solution()
s = "foo"
t = "bar"
#s = "egg"
#t = "add"
print(so.isIsomorphic(s,t))