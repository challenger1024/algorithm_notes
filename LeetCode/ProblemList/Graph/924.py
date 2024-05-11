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
			ans.add(p)
		ret=n+1
		l=0
		for v in initial:
			x=0
			p=uf.findset(v)
			if not vis[p]:
				x=uf.size[p]
			ret=v if x>l else ret
			if x==l:
				ret=min(v,ret)
			l=x if x>l else l
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
#solution
'''
并查集
一个与联通分量有关的变形题。
根据提议可知，要想使最终被感染病毒的节点最少，需要删除掉某个联通分量中的一个病毒节点，且这个联通分量中只有这一个病毒节点，也就是找到一个只有一个病毒节点的最长的联通分量。
所以用dfs/bfs/并查集都可以解决该问题。
这里使用并查集解决。
首先用并查集求初每个联通分量的编号和它的长度。
1. 建立数组vis,用于判断联通分量中是否只有一个节点被感染;
2. 建立集合set,用于保存联通分量的编号;
4. 第一次循环便利每一个重读节点，将重读节点的根节点放入set中，如果set中已经存在了当前便利到的节点的根节点，那么将vis[根节点]置为True.
5.设ret=n+1代表联通分量也就是根节点编号，l=0代表联通分量的长度。
6. 第二次便利重读节点v，如果vis[v的根节点]=False,那么尝试更新ret.
具体看代码，要考虑u的根节点r所在联通分量的长度，如果与当前l相等，则取得索引更小的根节点编号。
'''