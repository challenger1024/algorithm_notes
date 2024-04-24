mod=10**9+7
class Solution:
	def sumOfPower(self, nums: List[int], k: int) -> int:
		n=len(nums)
		dp=[[0]*(k+1) for _ in range(n+1)]
		dp[0][0]=1
		for i , num in enumerate(nums):
			for j in range(i,-1,-1):
				for x in range(k,nums[j]-1,-1):
					dp[j][x]=dp[j-1][x-nums[j]]+1
		ans=0
		



#solution
'''
设子序列为subse,对于数组中的nums[i],可以有两种选择：
1.选nums[i]构成子序列
2.不选nums[i]构成子序列
对于每一个子序列subse，又有，是否选择subse[j]构成和为k的更小子序列subsubse。


'''