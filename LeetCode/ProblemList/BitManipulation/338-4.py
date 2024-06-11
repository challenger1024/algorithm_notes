class Solution:
	def countBits(self, n: int) -> List[int]:
		ans=[0]*(n+1)
		for i in range(1,n+1):
			ans[i]=ans[i&(i-1)]+1#去除最低位的1之后的数字中1的个数再+1，即为当前数字i中1的个数
		return ans