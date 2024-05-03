#并查集
class Solution:
	def countPairs(self, n: int, edges: List[List[int]]) -> int:
		uf=UnionFind(n)
		for x,y in edges:
			uf.union(x,y)
		res=0
		for i in range(n):
			res+=n-uf.get(uf.find(i))
		return res//2
class UnionFind:
	def __init__(self,n):
		self.parents=[i for i in range(n)]
		self.sizes=[1]*n
	def find(self,x):
		ret=x
		while self.parents[ret]!=ret:
			ret=self.parents[ret]
		return ret
	def union(self,x,y):
		rx=self.find(x)
		ry=self.find(y)
		if rx!=ry:
			if self.sizes[rx]>self.sizes[ry]:
				self.parents[ry]=rx
				self.sizes[rx]+=self.sizes[ry]
			else:
				self.parents[rx]=ry
				self.sizes[ry]+=self.sizes[rx]
	def get(self,x):
		return self.sizes[x]
