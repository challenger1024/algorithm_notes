class Solution:
	def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
		n=len(arr)
		s=sum(arr[:k])
		ans=1 if s/k>=threshold else 0
		for i in range(1,n-k+1):
			s=s-arr[i-1]+arr[i+k-1]
			ans+=1 if s/k>=threshold else 0
		return ans