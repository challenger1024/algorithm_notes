class Solution:
	def countBits(self, n: int) -> List[int]:
		ans=[]
		x=0
		while x<=n:
			temp=x
			ret=0
			while temp:
				ret+=1
				temp&=temp-1
			ans.append(ret)
			x+=1
		return ans

#solution
'''
暴力枚举
利用与运算的性质，暴力枚举统计每个数字中1的个数。
'''