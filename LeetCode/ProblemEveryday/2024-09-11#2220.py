class Solution:
	def minBitFlips(self, start: int, goal: int) -> int:
		ans=0
		s=start^goal
		while s:
			ans+=1
			s&=s-1
		return ans