#二分答案

class Solution:
	def minNumberOfSeconds(self, mountainHeight: int, workerTimes) -> int:
		def calc(t):
			res=0
			for wt in workerTimes:
				h=t//wt
				res+=(-1+sqrt(1+8*h))/2
			return int(res)<mountainHeight
		l,r=1,10**9
		ans=0
		while l<r:
			mid=(l+r)//2
			if calc(mid):
				l=mid+1
			else:
				r=mid-1
				ans=mid
		return l
