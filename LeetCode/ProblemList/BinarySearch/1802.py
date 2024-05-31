class Solution:
	def calc(self,n,cnt,x):
		return (x+x-cnt+1)*cnt//2 if cnt<=x else (x+1)*x//2 +cnt-x
	def maxValue(self, n: int, index: int, maxSum: int) -> int:
		l,r=1,maxSum
		while l<=r:
			mid=(l+r)//2
			if self.calc(n,index,mid-1)+self.calc(n,n-index,mid) <=maxSum:
				l=mid+1
			else:
				r=mid-1
		return l-1