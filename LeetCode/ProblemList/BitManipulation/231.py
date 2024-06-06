class Solution:
	def isPowerOfTwo(self, n: int) -> bool:
		if n<=0:
			return False
		return n&(n-1)==0 

#solution
'''
运用与运算的性质：
n&(n-1)#取消最低位的0
如果一个数字n是2的次幂，那么它的二进制表示中一定只有一个1，经过n&(n-1)运算后一定=0.
'''