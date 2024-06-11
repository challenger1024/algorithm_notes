#使用内置函数统计1的数量
class Solution:
	def sortByBits(self, arr: List[int]) -> List[int]:
		return sorted(arr,key=lambda x:(bin(x).count('1'),x))
