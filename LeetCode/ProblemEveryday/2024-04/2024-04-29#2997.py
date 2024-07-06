class Solution:
	def minOperations(self, nums: List[int], k: int) -> int:
		for num in nums:
			k=k ^ num
		ans=0
		while k:
			k &= k-1
			ans+=1
		return ans