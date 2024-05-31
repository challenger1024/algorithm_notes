class Solution:
	def singleNumber(self, nums: List[int]) -> List[int]:
		n=len(nums)
		sum=0
		for num in nums:
			sum^=num
		low=sum&-sum
		a,b=0,0
		for num in nums:
			if low&num==0:
				b^=num
			else:
				a^=num
		return [a,b]