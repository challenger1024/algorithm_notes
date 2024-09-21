class Solution:
	def findMaximizedCapital(self, k: int, w: int, pf: List[int], cpt: List[int]) -> int:
		if w>=max(cpt):
			return w+sum(nlargest(k,pf))
		items=[[cpt[i],pf[i]] for i in range(len(pf))]
		items.sort()
		i=j=0
		h=[]
		while i<k:
			while j<len(items):
				if w>=items[j][0]:
					heappush(h,-items[j][1])
					j+=1
				else:
					break
			if h:
				w+=-heappop(h)
				i+=1
			else:
				break
		return w