#状态机DP
class Solution:
	def largestMultipleOfThree(self, nums: List[int]) -> str:
		n=len(nums)
		nums.sort()
		@cache
		def dfs(i,j):
			if i<0:
				return -inf if j else 0
			return max(dfs(i-1,j),dfs(i-1,(j+nums[i])%3)+1)
		if dfs(n-1,0)==0:
			return ''
		ans=''
		@cache
		def build(i,j):
			nonlocal ans
			if i<0:
				return
			res1=dfs(i-1,j)
			res2=dfs(i-1,(j+nums[i])%3)+1
			if res1>res2:
				build(i-1,j)
			else:
				ans+=str(nums[i])
				build(i-1,(nums[i]+j)%3)
		build(n-1,0)
		if ans[0]=='0': return '0'
		return ans
