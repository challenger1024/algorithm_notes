class Solution:
	def calc(self,nums,x):
		ans=0
		for num in nums:
			ans+=(num-1)//x+1
		return ans
	def minimizedMaximum(self, n: int, q: List[int]) -> int:
		l,r=1,max(q)
		while l<=r:
			mid=(l+r)//2
			if self.calc(q,mid) <=n:
				r=mid-1
			else:
				l=mid+1
		return l