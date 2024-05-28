class Solution:
	def longestSemiRepetitiveSubstring(self, s: str) -> int:
		n=len(s)
		same=0
		ans=0
		l,r=0,0
		while r<n:
			if r>0 and s[r]==s[r-1]:
				same+=1
			while l+1<n and same>1:
				if s[l+1]==s[l]:
					same-=1
				l+=1
			ans=max(ans,r-l+1)
			r+=1
		return ans

#test entry
so=Solution()
s='54433'
print(so.longestSemiRepetitiveSubstring(s))