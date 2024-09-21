class Solution:
	def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
		data={}
		for n,t in zip(names,heights):
			data[t]=n
		heights.sort(reverse=True)
		ans=[]
		for t in heights:
			ans.append(data[t])
		return ans