class Solution:
	def beautifulSubsets(self, nums: List[int], k: int) -> int:
		vis=[0]*(max(nums)+k*2)
		ans=-1
		def dfs(i):
			if i>=len(nums):
				nonlocal ans
				ans+=1
				return
			dfs(i+1)
			if vis[nums[i]+k]==0 and vis[nums[i]-k]==0:
				vis[nums[i]]+=1
				dfs(i+1)
				vis[nums[i]]-=1
		dfs(0)
		return ans