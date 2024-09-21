#几种情况
#|s1|==|s2|，直接比较大小
#|s1|>|s2|,
import functools
class Solution:
	def largestNumber(self, nums) -> str:   
		def compare(s1,s2):
			x,y=s1+s2,s2+s1
			if x>y:return -1
			elif x<y:return 1
			else: return 0
		for i,num in enumerate(nums):
			nums[i]=str(num)
		nums.sort(key=functools.cmp_to_key(compare))
		if nums[0]=='0':return '0'
		return ''.join(nums)

#test entry
s=Solution()
nums=[3,30,34,5,9]
print(s.largestNumber(nums))