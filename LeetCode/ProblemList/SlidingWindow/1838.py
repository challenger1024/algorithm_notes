class Solution:
	def maxFrequency(self, nums: List[int], k: int) -> int:
		n=len(nums)
		nums.sort()
		temp=0
		l=0
		ans=0
		for r,num in enumerate(nums):
			temp+=num
			while temp+k<(r-l+1)*num:
				temp-=nums[l]
				l+=1
#			if temp+k==(r-l+1)*num:
			ans=max(ans,r-l+1)
		return ans