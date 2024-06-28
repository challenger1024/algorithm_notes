class Solution:
	def minOperations(self, nums: List[int]) -> int:
		k=3
		n=len(nums)
		ans=0
		status=0
		for i in range(n):
			if i>=k and nums[i-k]>1:
				status^=1
			if nums[i]==status:
				if i+k>n:
					return -1
				ans+=1
				status^=1
				nums[i]+=2
		return ans