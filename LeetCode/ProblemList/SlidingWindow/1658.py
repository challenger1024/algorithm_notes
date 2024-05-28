class Solution:
	def minOperations(self, nums: List[int], x: int) -> int:
		k=sum(nums)-x
		l=0
		ans=-1
		n=len(nums)
		temp=0
		for r,num in enumerate(nums):
			temp+=num
			while l<n and temp>k:
				temp-=nums[l]
				l+=1
			if temp==k:
				ans=max(ans,r-l+1)
		return n-ans if ans!=-1 else -1