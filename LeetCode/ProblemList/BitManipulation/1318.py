class Solution:
	def minFlips(self, a: int, b: int, c: int) -> int:
		ans=0
		for i in range(31):
			if c&(1<<i):
				if a&(1<<i)==0 and b&(1<<i)==0:
					ans+=1
			else:
				ans+=1&(a>>i)
				ans+=1&(b>>i)
		return ans

#solution
'''
逐个枚举a/b/c的每一个二进制位。
如果c的第i位是1，那么a和b的第i位都为0时需要反转其中的一个，否则不需要反转；
如果c的第i位是0,那么a和b的第i位不是0的都要反转。
'''