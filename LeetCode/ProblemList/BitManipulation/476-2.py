class Solution:
	def findComplement(self, num: int) -> int:
		bits=0
		for i in range(1,31):#统计num的位数
			if (1<<i)<=num:
				bits=i
			else:
				break
		mask=(1<<(bits+1))-1#构造所有位上都为1的掩码
		return num^mask