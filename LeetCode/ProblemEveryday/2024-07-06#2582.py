class Solution:
	def passThePillow(self, n: int, time: int) -> int:
		if (time//(n-1))%2:
			return n-time%(n-1)
		else:
			return 1+time%(n-1)
