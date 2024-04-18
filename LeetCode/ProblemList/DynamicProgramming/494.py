class Solution:
	def findTargetSumWays(self, nums, target: int) -> int:
		n=len(nums)
		addition=sum(nums)
		target=addition-target
		if target <0 or target%2!=0:return 0
		target//=2
		dp=[1]+[0 for _ in range(target)]
		for num in nums:
			for j in range(target,num-1,-1):
				dp[j]+=dp[j-num]
		return dp[-1]

#test entry
s=Solution()
nums=[2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53]
target=1000
#nums=[1,1,1,1,1]
#target=3
#nums=[1,0]
#target=1
print(s.findTargetSumWays(nums,target))

#Solution
'''
若nums的和=sum,加负号的数字和=nig，那么加证号的数字和=sum-nig
target=sum-2*nig
nig=(sum-target)//2
题目转化为从数组中选元素，使其和=nig,计算总共有多少种取法。

'''