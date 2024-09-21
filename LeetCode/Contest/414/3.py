#score[i+1]=score[i]+nums[i]
#
class Solution:
	def findMaximumScore(self, nums) -> int:
		n=len(nums)
		score=[0 for _ in range(n)]
		prev=nums[0]
		idx=0
		for i in range(1,n):
			score[i]=score[idx]+nums[idx]*(i-idx)
			if nums[i]>prev:
				prev=nums[i]
				idx=i
		return score[-1]