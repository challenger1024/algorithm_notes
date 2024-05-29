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
	def searchRange(self, nums: List[int], target: int) -> List[int]:
		n=len(nums)
		l,r=self.binary_search(nums,target),self.binary_search(nums,target+1)
		return [-1,-1] if l==n or nums[l]!=target else [l,r-1]