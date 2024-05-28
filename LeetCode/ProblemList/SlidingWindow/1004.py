class Solution:
	def longestOnes(self, nums: List[int], k: int) -> int:
		n=len(nums)
		ans=0
		f,t=0,0
		ans=0
		lf,lt=0,0
		for r,c in enumerate(nums):
			if c==0:f+=1
			while lf<n and f>k:
				if nums[lf]==0:
					f-=1
				lf+=1
			ans=max(ans,r-lf+1)
		return ans