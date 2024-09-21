class Solution:
	def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
		dic={}
		for i,num in enumerate(nums):
			temp=num
			x=int(''.join(str(mapping[int(digit)]) for digit in str(num)))
			dic[temp]=x
		nums.sort(key=lambda x:dic[x])
		return nums
