#解法2：位运算
#向抑或和里添加0到n-1的数字，使得0到n-1的每个数字都在原来的基础上多出现一次
#那么本来出现一次的就出现了两次，抑或和里就没有这些了
#原本出现两次的元素a和b现在出现了三次，作为a^b的形式被保留下来
#分组异或 ：利用  xor_all  的最高有效位，将索引和数组元素分成两组，这两组中的数要么在这一位上是 0，要么是 1。两个多出来的数会被分到不同的组中，因为它们异或的结果在这一位上是不同的。

class Solution:
	def getSneakyNumbers(self, nums: List[int]) -> List[int]:
		n=len(nums)-2
		xor_all=n^(n+1)
		for i,x in enumerate(nums):
			xor_all^=i^x
		shift=xor_all.bit_length()-1
		ans=[0,0]
		for i,x in enumerate(nums):
			if i<n:
				ans[i>>shift&1]^=i
			ans[x>>shift&1]^=x
		return ans