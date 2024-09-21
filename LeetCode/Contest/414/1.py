class Solution:
	def convertDateToBinary(self, date: str) -> str:
		t=date.split('-')
		ans=[]
		for x in t:
			ans.append(bin(int(x))[2:])
		return '-'.join(ans)