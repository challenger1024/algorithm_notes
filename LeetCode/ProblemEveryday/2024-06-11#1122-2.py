class Solution:
	def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
		pos=Counter()
		n=len(arr2)
		for i,a in enumerate(arr2):
			pos[a]=i-n
		def compare(x):
			return pos[x] if x in pos else x
		arr1.sort(key=compare)
		return arr1