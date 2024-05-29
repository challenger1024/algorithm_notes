class Solution:
	def hIndex(self, citations: List[int]) -> int:
		l,r=0,len(citations)-1
		n=len(citations)
		while l<=r:
			mid=(l+r)//2
			if citations[mid]<n-mid:
				l=mid+1
			else:
				r=mid-1
		return n-l