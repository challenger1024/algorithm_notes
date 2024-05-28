class Solution:
	def findLengthOfShortestSubarray(self, arr) -> int:
		n=len(arr)
		r=n-1
		while r and arr[r]>=arr[r-1]:
			r-=1
		if r==0:
			return 0
		ans=r
		l=0
		while l==0 or arr[l-1]<=arr[l]:
			while r<n and arr[r]<arr[l]:
				r+=1
			ans=min(ans,r-l-1)
			l+=1
		return ans

#test entry
s=Solution()
arr=[1]
print(s.findLengthOfShortestSubarray(arr))