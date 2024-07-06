class Solution:
	def specialArray(self, nums: List[int]) -> int:
		n=len(nums)
		ans=-1
		nums.sort(reverse=True)
		for i in range(1,n+1):
			if nums[i-1]>=i and (n==i or nums[i]<i):
				ans=i
				break
		return ans