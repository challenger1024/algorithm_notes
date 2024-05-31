#闭区间二分
class Solution:
	def calc(self,nums,x):
		ans=0
		for num in nums:
			ans+=num//x
		return ans
	def maximumCandies(self, candies: List[int], k: int) -> int:
		s=sum(candies)
		if k>s:
			return 0
		l,r=1,max(candies)
		while l<=r:
			mid=(l+r)//2
			if self.calc(candies,mid) < k:
				r=mid-1
			else:
				l=mid+1
		return l-1