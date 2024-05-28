class Solution:
	def takeCharacters(self, s: str, k: int) -> int:
		n=len(s)
		cnt=Counter(s)
		ans=-1
		l=0
		for r,c in enumerate(s):
			cnt[c]-=1
			while l < n and (cnt['a']<k or cnt['b']<k or cnt['c']<k):
				cnt[s[l]]+=1
				l+=1
			if cnt['a']>=k and cnt['b']>=k and cnt['c']>=k:
				ans=max(ans,r-l+1)
		return n-ans if ans!=-1 else -1
