class Solution:
	def countBits(self, n: int) -> List[int]:
		ans=[0]*(n+1)
		mlb=0
		for i in range(1,n+1):
			if i&(i-1)==0:#说明i是2的整数次密，更新最高有效位
				mlb=i
				ans[i]=1
			else:#直接利用前面已有的结果得到i中1的个数
				ans[i]=ans[i-mlb]+1
		return ans

#solution
'''
利用最高有效位更新答案
'''