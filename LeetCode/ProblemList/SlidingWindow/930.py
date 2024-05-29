class Solution:
	def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
		sum1,sum2=0,0
		n=len(nums)
		l1,l2=0,0
		ans=0
		for r, num in enumerate(nums):
			sum1+=num
			while l1<=r and sum1>goal:
				sum1-=nums[l1]
				l1+=1
			sum2+=num
			while l2<=r and sum2>=goal:
				sum2-=nums[l2]
				l2+=1
			ans+=l2-l1
		return ans