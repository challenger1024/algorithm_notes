class Solution:
	def findComplement(self, num: int) -> int:
		i=1
		while i<=num:
			num^=i
			i<<=1
		return num

#solution
'''
一次便利，每一位都抑或2的i次幂，以此使得数字每一位都能取反且不影响到其他位。
'''