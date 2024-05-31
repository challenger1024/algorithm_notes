class Solution:
	def calc(self,nums,x):
		ans=1
		sum=0
		for num in nums:
			if sum+num>x:
				sum=0
				ans+=1
			sum+=num
		return ans
	def splitArray(self, nums: List[int], k: int) -> int:
		l,r=max(nums),sum(nums)
		while l<=r:
			mid=(l+r)//2
			if self.calc(nums,mid) <=k:
				r=mid-1
			else:
				l=mid+1
		return l