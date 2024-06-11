class Solution:
	def minBitFlips(self, start: int, goal: int) -> int:
		ans=0
		s=start^goal
		while s:
			s&=s-1
			ans+=1
		return ans