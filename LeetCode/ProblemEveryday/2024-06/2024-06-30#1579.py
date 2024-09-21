class Solution:
	def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
		ans=0
		m=len(edges)
		ufa,ufb=UniteFindSet(n),UniteFindSet(n)
		for edge in edges:
			edge[1]-=1
			edge[2]-=1
			if edge[0]==3:
				if not ufa.unite(edge[1],edge[2]):
					ans+=1
				else:
					ufb.unite(edge[1],edge[2])

		for (t,u,v) in edges:
			if t==1:
				if not ufa.unite(u,v):
					ans+=1
			elif t==2:
				if not ufb.unite(u,v):
					ans+=1

		if ufa.cnt!=1 or ufb.cnt!=1:
			return -1
		return ans






class UniteFindSet:
	def __init__(self,n):
		self.n=n
		self.sets=list(range(n))
		self.sizes=[1]*n
		self.cnt=n
	def find(self,x):
		if x==self.sets[x]:
			return x
		self.sets[x]=self.find(self.sets[x])
		return self.sets[x]
	def unite(self,x,y):
		x,y=self.find(x),self.find(y)
		if x==y:
			return False
		if self.sizes[x]<self.sizes[y]:
			x,y=y,x
		self.sets[y]=x
		self.sizes[x]+=self.sizes[y]
		self.cnt-=1
		return True
