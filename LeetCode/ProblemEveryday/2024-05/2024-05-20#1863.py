class Solution:
	def subsetXORSum(self, nums: List[int]) -> int:
		ans=0
		def dfs(v,idx):
			if idx>=len(nums):
				nonlocal ans
				ans+=v
				return
			dfs(v,idx+1)
			dfs(v^nums[idx],idx+1)
		dfs(0,0)
		return ans