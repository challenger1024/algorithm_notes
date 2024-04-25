class Solution:
	def maxVowels(self, s: str, k: int) -> int:
		n=len(s)
		l,r=0,0
		ans=0
		alpha=0
		t='aeiou'
		while l<n:
			while r<n and r<l+k:
				if s[r] in t:
					alpha+=1
				r+=1
			ans=max(ans,alpha)
			if s[l] in t:
				alpha-=1
			l+=1
		return ans
