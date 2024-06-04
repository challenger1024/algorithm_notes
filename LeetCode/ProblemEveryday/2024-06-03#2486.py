class Solution:
	def appendCharacters(self, s: str, t: str) -> int:
		m,n=len(s),len(t)
		sh,th=0,0
		while sh<m and th <n:
			if s[sh]==t[th]:
				th+=1
			sh+=1
		return n-th

#test entry
so=Solution()
s = "coaching"
t = "coding"
print(so.appendCharacters(s,t))