class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		ans=[]
		def dfs(i,stack):
			ans.append(stack)
			for j in range(i,len(nums)):
				dfs(j+1,stack+[nums[j]])
		dfs(0,[])
		return ans