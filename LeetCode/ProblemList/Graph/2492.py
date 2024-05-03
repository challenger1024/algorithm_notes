class Solution:
	def minScore(self, n: int, roads) -> int:
		uf=UnionFind(n+1)
		for x,y,w in roads:
			uf.union(x,y,w)
		return uf.costs[uf.find(n)]

class UnionFind:
	def __init__(self,n):
		self.parents=[i for i in range(n)]
		self.costs=[float('inf')]*n
		self.sizes=[1]*n
	def find(self,x):
		ret=self.parents[x]
		while ret!=self.parents[ret]:
			ret=self.parents[ret]
		return ret
	def union(self,x,y,w):
		x,y=self.find(x),self.find(y)
		if x==y:
			self.costs[y]=min(self.costs[y],w)
			return
		if self.sizes[x]>self.sizes[y]:
			x,y=y,x
		self.parents[x]=y
		self.sizes[y]+=self.sizes[x]
		self.costs[y]=min(w,self.costs[y],self.costs[x])

#test entry
s=Solution()
n=6
road=[[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],[2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]]
#n=4
#road=[[1,2,2],[1,3,4],[3,4,7]]
print(s.minScore(n,road))