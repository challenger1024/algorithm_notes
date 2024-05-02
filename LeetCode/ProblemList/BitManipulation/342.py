class Solution:
	def isPowerOfFour(self, n: int) -> bool:
		if n<=0: return False
		r=n&(n-1)
		return r==0 and n&(-n)&0x55555555!=0