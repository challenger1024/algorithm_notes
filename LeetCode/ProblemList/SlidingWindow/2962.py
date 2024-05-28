class Solution:
	def countSubarrays(self, nums: List[int], k: int) -> int:
		x=max(nums)
		l=0
		ans=0
		for r, num in enumerate(nums):
			if num==x:
				k-=1
			while k<=0:
				if nums[l]==x:
					k+=1
				l+=1
			ans+=l
		return ans