class Solution:
	def averageWaitingTime(self, cus: List[List[int]]) -> float:
		f=ans=0
		for i,(a,w) in enumerate(cus):
			f=w +(f if f>a else a)
			ans+=f-a
		return ans/len(cus)