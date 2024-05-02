class Solution:
	def findMaxK(self, nums: List[int]) -> int:
		nums.sort()
		l,r=0,len(nums)-1
		ans=-1
		while l<r and nums[l]<0:
			if abs(nums[l])==nums[r]:
				ans=max(ans,nums[r])
				l+=1
				r-=1
			elif abs(nums[l])<nums[r]:
				r-=1
			else:
				l+=1
		return ans