class Solution:
	def calc(self,days,m,k,x):
		l=0
		for d in days:
			if d<=x:
				l+=1
			else:
				l=0
			if l==k:
				m-=1
				l=0
			if m==0:
				return True
		return False
	def minDays(self, day: List[int], m: int, k: int) -> int:
		if len(day)<m*k:
			return -1
		l,r=min(day),max(day)
		while l<=r:
			mid=(l+r)//2
			flag=self.calc(day,m,k,mid)
			if flag :
				r=mid-1
			else:
				l=mid+1
		return l