class Solution:
	def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
		cnt=Counter(arr1)
		ans=[]
		for a in arr2:
			ans.extend([a]*cnt[a])
		ret=[]
		hash=set(arr2)
		for a in arr1:
			if a not in hash:
				ret.append(a)
		ret.sort()
		return ans+ret