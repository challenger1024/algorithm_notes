class Solution:
	def calc(self,nums,x):
		ans=0
		pre=-inf
		for num in nums:
			if num-pre>=x:
				ans+=1
				pre=num
		return ans
	def maximumTastiness(self, price: List[int], k: int) -> int:
		price.sort()
		l,r=1,price[-1]-price[0]
		while l<=r:
			mid=(l+r)//2
			if self.calc(price,mid)<k:
				r=mid-1
			else:
				l=mid+1
		return l-1