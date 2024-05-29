class Solution:
	def calc(self,nums,x):
		ans=0
		for num in nums :
			ans+=math.ceil(num/x)
		return ans
	def smallestDivisor(self, nums: List[int], threshold: int) -> int:
		total=sum(nums)
		l,r=1,total
		while l<=r:
			mid=(l+r)//2
			if self.calc(nums,mid)>threshold:
				l=mid+1
			else:
				r=mid-1
		return l