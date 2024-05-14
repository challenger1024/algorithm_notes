class Graph:
	def __init__(self, n: int, edges: List[List[int]]):
		self.n=n
		self.g=[[] for _ in range(n)]
		for edge in edges:
			self.addEdge(edge)
	def addEdge(self, edge: List[int]) -> None:
		self.g[edge[0]].append((edge[1],edge[2]))
	def shortestPath(self, node1: int, node2: int) -> int:
		dis=[inf]*self.n
		dis[node1]=0
		h=[(0,node1)]
		while h:
			d,now=heappop(h)
			if d>dis[now]:
				continue
			for next,w in self.g[now]:
				newD=d+w
				if newD < dis[next]:
					dis[next]=newD
					heappush(h,(newD,next))
		return dis[node2] if dis[node2]!=inf else -1


#solution
'''
简单的dijkstra实现
'''