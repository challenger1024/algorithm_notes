class Solution:
	def countBits(self, n: int) -> List[int]:
		ans=[0]*(n+1)
		for i in range(1,n+1):
			ans[i]=ans[i>>1]+(i&1)#二进制右移一位获得取消最低位时1的个数，再看i是奇数的话就+1,i是偶数的话就+0
		return ans

