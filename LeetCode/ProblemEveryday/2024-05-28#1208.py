class Solution:
	def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
		n=len(s)
		l=0
		score=0
		ans=0
		for r,c in enumerate(s):
			score+=abs(ord(s[r])-ord(t[r]))
			while r<n and score>maxCost:
				score-=abs(ord(s[l])-ord(t[l]))
				l+=1
			ans=max(ans,r-l+1)

		return ans


#solution
'''

'''