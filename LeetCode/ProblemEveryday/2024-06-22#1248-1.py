class Solution:
	def numberOfSubarrays(self, nums: List[int], goal: int) -> int:
		sum1,sum2=0,0
		n=len(nums)
		l1,l2=0,0
		ans=0
		for r, num in enumerate(nums):
			sum1+=num%2
			while l1<=r and sum1>goal:
				sum1-=nums[l1]%2
				l1+=1
			sum2+=num%2
			while l2<=r and sum2>=goal:
				sum2-=nums[l2]%2
				l2+=1
			ans+=l2-l1
		return ans
