#二维数组排序后展开成一维数组
class Solution:
	def sortByBits(self, arr: List[int]) -> List[int]:
		def flatten_list(nested_list):
			for item in nested_list:
				if isinstance(item, list):
					yield from flatten_list(item)
				else:
					yield item
		data=[[] for _ in range(14)]
		for num in arr:
			n=num
			i=0
			while n:
				n&=n-1
				i+=1
			data[i].append(num)
		for nums in data:
			nums.sort()
		return list(flatten_list(data))