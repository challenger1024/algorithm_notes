class Solution:
	def binary_search(self,nums,target):
		l,r=0,len(nums)-1
		while l<=r:
			mid=(l+r)//2
			if nums[mid]<target:
				l=mid+1
			else:
				r=mid-1
		return l
	def maximumCount(self, nums: List[int]) -> int:
		n=len(nums)
		l,r=self.binary_search(nums,0),self.binary_search(nums,1)
		return max(l,n-r)