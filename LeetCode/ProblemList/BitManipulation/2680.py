class Solution:
	def maximumOr(self, nums: List[int], k: int) -> int:
		big=0
		ans=0
		for a in nums:
			if a>big:
				ans^=big<<k
				ans|=big
				big=a
				ans|=a<<k
			else:
				ans|=a
		return ans