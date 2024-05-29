class Solution:
	def minimumTime(self, time: List[int], trips: int) -> int:
		def calc(x):
			ans=0
			for num in time:
				if num>x:
					break
				ans+=x//num
			return ans
		time.sort()
		l,r=1,time[-1]*trips
		while l<=r:
			mid=(l+r)//2
			if calc(mid)<trips:
				l=mid+1
			else:
				r=mid-1
		return l