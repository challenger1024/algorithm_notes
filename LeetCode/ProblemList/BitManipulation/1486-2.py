#腧穴
class Solution:
	def xorOperation(self, n: int, start: int) -> int:
		def sumXor(x):
			if x%4==0:
				return x
			if x%4==1:
				return 1
			if x%4==2:
				return x+1
			return 0
		s=start>>1
		e=n&start&1
		ret=sumXor(s-1)^sumXor(s+n-1)
		return ret<<1 | e
