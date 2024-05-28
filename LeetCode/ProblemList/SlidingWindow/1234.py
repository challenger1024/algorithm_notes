class Solution:
	def balancedString(self, s: str) -> int:
		cnt=Counter(s)
		r=0
		n=len(s)
		if not (cnt['Q']>n//4 or cnt['W']>n//4 or cnt['E']>n//4 or cnt['R']>n//4):
			return 0
		ans=n+1
		for l,c in enumerate(s):
			while r<n and( cnt['Q']>n//4 or cnt['W']>n//4 or cnt['E']>n//4 or cnt['R']>n//4):
				cnt[s[r]]-=1
				r+=1
			if  (cnt['Q']>n//4 or cnt['W']>n//4 or cnt['E']>n//4 or cnt['R']>n//4):
				break
			ans=min(ans,r-l)
			cnt[c]+=1
		return ans