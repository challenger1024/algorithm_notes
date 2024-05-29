import math
class Solution:
	def calc(self,nums,x):
		ans=0
		for num in nums:
			ans+=math.ceil(num/x)
		return ans
	def minEatingSpeed(self, piles, h: int) -> int:
		l,r=0,max(piles)+1
		while l+1<r:
			mid=(l+r)//2
			if self.calc(piles,mid)<=h:
				r=mid
			else:
				l=mid
		return r

#test entry
s=Solution()
piles = [3,6,7,11]
h = 8
print(s.minEatingSpeed(piles,h))