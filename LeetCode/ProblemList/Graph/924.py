class Solution:
	def minMalwareSpread(self, graph, initial) -> int:
		n=len(graph)
		uf=UnionFind(n)
		for i in range(n):
			for j in range(i+1,n):
				if graph[i][j]==1:
					uf.unite(i,j)
		ans=set()
		vis=[False]*n
		for virus in initial:
			p=uf.findset(virus)
			if p in ans:
				vis[p]=True
#			print(p)
			ans.add(p)
		ret=n+1
		y=0
		for v in initial:
			x=0
			p=uf.findset(v)
			if not vis[p]:
#				print(f'{v}不在vis里')
				x=uf.size[p]
#			print(x)
			ret=v if x>y else ret
			if x==y:
				ret=min(v,ret)
			y=x if x>y else y
		return ret
class UnionFind:
	def __init__(self, n: int):
		self.parent = list(range(n))
		self.size = [1] * n
		self.n = n
		self.setCount = n#当前联通量数目

	def findset(self, x: int) -> int:
		if self.parent[x] == x:
			return x
		self.parent[x] = self.findset(self.parent[x])
		return self.parent[x]

	def unite(self, x: int, y: int) -> bool:
		x, y = self.findset(x), self.findset(y)
		if x == y:
			return False
		if self.size[x] < self.size[y]:
			x, y = y, x
		self.parent[y] = x
		self.size[x] += self.size[y]
		self.setCount -= 1
		return True

	def connected(self, x: int, y: int) -> bool:
		x, y = self.findset(x), self.findset(y)
		return x == y

#test entry
s=Solution()
#graph=[[1,1,0],[1,1,0],[0,0,1]]
#initial=[0,1]
graph = [[1,0,0],[0,1,0],[0,0,1]]
initial = [0,2]
#graph = [[1,1,1],[1,1,1],[1,1,1]]
#initial = [1,2]
#graph=[[1,1,0],[1,1,0],[0,0,1]]
#initial=[0,1,2]
print(s.minMalwareSpread(graph,initial))