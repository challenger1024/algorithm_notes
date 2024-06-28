#状态机dp:考虑至多剩余多少个元素
class Solution:
	def minimumOperations(self, nums: List[int]) -> int:
		dp=[0]*4
		for x in nums:
			dp[x]+=1#以x结尾的子序列长度+1
			dp[2]=max(dp[2],dp[1])#结尾为2 的最长子序列的长度为结尾为1的和结尾为2的子序列的长度的最大值
			dp[3]=max(dp[3],dp[2])#取以1为结尾、以2为结尾、以3为结尾三种子序列长度的最大值
		return len(nums)-max(dp)#nums的元素数量-最长递增子序列的长度=需要删除的元素数量