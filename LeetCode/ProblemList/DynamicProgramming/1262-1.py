#记忆化搜索
class Solution:
	def maxSumDivThree(self, nums: List[int]) -> int:
		@cache
		def dfs(i,j):
			if i<0:
				return -inf if j else 0
			return max(dfs(i-1,j),dfs(i-1,(j+nums[i])%3)+nums[i])
		return dfs(len(nums)-1,0)