class Solution:
	def calc(self,nums,x):
		ans=0
		for num in nums[:-1]:
			ans+=(num-1)//x +1
		return ans+nums[-1]/x
	def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
		n=len(dist)
		if n-1>=hour:
			return -1
		l,r=1,10**7
		while l<=r:
			mid=(l+r)//2
			if self.calc(dist,mid)<=hour:
				r=mid-1
			else:
				l=mid+1
		return l