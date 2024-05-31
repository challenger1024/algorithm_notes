class Solution:
	def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
		n=len(matrix)
		def calc(x):
			ans=0
			i,j=n-1,0
			while i>=0 and j<n:
				if matrix[i][j]<=x:
					ans+=i+1
					j+=1
				else:
					i-=1
			return ans
		l,r=matrix[0][0],matrix[-1][-1]
		while l<=r:
			mid=(l+r)//2
			if calc(mid) >=k:
				r=mid-1
			else:
				l=mid+1
		return l