class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		d=[]
		for num in nums:
			if not d or num>d[-1]:
				d.append(num)
			else:
				loc=bisect_left(d,num)
				d[loc]=num
		return len(d)