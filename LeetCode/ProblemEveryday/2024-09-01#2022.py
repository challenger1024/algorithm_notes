class Solution:
	def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
		l=len(original)
		if m*n != l:
			return []
		ans=[]
		for i in range(0,l,n):
			ans.append(list(original[i:i+n]))
		return ans