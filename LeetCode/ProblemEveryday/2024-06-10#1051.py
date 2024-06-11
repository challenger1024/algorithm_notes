class Solution:
	def heightChecker(self, heights: List[int]) -> int:
		expected=sorted(heights)
		ans=0
		for i in range(len(heights)):
			ans+=expected[i]!=heights[i]
		return ans