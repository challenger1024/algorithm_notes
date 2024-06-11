class Solution:
	def isPowerOfFour(self, n: int) -> bool:
		if n<=0: return False
		r=n&(n-1)
		return r==0 and n&(-n)&0x55555555!=0#二进制表示中1的位置
#		return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1#取模性质
