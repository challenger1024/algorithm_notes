class Solution:
	def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
		def cmp(x,y):
			return -1 if x[0]*y[1]<x[1]*y[0] else 1
		n=len(arr)
		ret=[]
		for i in range(n-1):
			for j in range(i+1,n):
				ret.append([arr[i],arr[j]])
		ret.sort(key=cmp_to_key(cmp))
		return ret[k-1]