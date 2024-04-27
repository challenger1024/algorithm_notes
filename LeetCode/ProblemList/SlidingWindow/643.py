class Solution:
	def findMaxAverage(self, nums: List[int], k: int) -> float:
		n=len(nums)
		s=sum(nums[:k])
		ans=s/k
		for i in range(1,n-k+1):
			s=s-nums[i-1]+nums[i+k-1]
			ans=max(ans,s/k)
		return ans