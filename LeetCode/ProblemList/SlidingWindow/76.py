class Solution:
	def minWindow(self, s: str, t: str) -> str:
		n,m=len(s),len(t)
#		if n<m:
#			return ''
		cntt=Counter(t)
		cnts=Counter()
		ansl,ansr=-1,n
		l=0
		for r,c in enumerate(s):
			cnts[c]+=1
			while l<n and cntt<=cnts:
				if r-l< ansr-ansl:
					ansr,ansl=r,l
				cnts[s[l]]-=1
				l+=1
		return '' if ansl<0 else s[ansl:ansr+1]