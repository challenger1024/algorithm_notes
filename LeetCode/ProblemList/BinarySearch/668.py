class Solution:
	def findKthNumber(self, m: int, n: int, k: int) -> int:
		def calc(x):
			ans=0
			i,j=m,1
			while i>=1 and j<=n:
				if i*j<=x:
					ans+=i
					j+=1
				else:
					i-=1
			return ans
		l,r=1,m*n
		while l<=r:
			mid=(l+r)//2
			if calc(mid) >=k:
				r=mid-1
			else:
				l=mid+1
		return l