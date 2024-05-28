class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		oc=set()
		n=len(s)
		r,ans=-1,0
		for l in range(n):
			if l>0:
				oc.remove(s[l-1])
			while r+1<n and s[r+1] not in oc:
				oc.add(s[r+1])
				r+=1
			ans=max(ans,r-l+1)
		return ans