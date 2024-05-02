class Solution:
	def hasAlternatingBits(self, n: int) -> bool:
		i=n&1
		while n:
			if n&1!=i:
				return False
			i^=1
			n>>=1
		return True