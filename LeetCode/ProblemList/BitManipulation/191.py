class Solution:
	def hammingWeight(self, n: int) -> int:
		ans=0
		while n:
			n&=n-1
			ans+=1
		return ans

#solution
'''
运用与运算的性质：
n&(n-1)
得到将n最低位的1变成0之后的结果，据此循环n,当n=0时，所有1被去除。
'''