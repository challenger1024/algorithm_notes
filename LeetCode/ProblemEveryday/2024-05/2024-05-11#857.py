from heapq import heappush,heappop
class Solution:
	def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
		r=sorted(zip(quality,wage),key=lambda p:p[1]/p[0])
		ans=inf
		tq=0
		h=[]
		for q,w in r[:k-1]:
			tq+=q
			heappush(h,-q)
		for q ,w in r[k-1:]:
			tq+=q
			heappush(h,-q)
			ans=min(ans,w/q*tq)
			tq+=heappop(h)
		return ans