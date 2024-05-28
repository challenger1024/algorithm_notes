class Solution:
	def numberOfSubstrings(self, s: str) -> int:
		cnt=Counter()
		ans=0
		l=0
		for r,c in enumerate(s):
			cnt[c]+=1
			while cnt['a']>0 and cnt['b']>0 and cnt['c']>0:
				cnt[s[l]]-=1
				l+=1
			ans+=l
		return ans