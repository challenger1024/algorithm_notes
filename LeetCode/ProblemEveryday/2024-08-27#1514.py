class Solution:
	def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
		g=[[] for _ in range(n)]
		for i, edge in enumerate(edges):
			u,v=edge
			g[u].append((v,succProb[i]))
			g[v].append((u,succProb[i]))
		dis=[0]*n
		dis[start_node]=1
		h=[(-1.0,start_node,-1)]
		while h:
			d,now,father=heappop(h)
			d=-d
			if d<dis[now]:
				continue
			for next,w in g[now]:
				newD=d*w
				if next!=father and newD > dis[next]:
					dis[next]=newD
					heappush(h,(-newD,next,now))
		return dis[end_node]

#solution
'''
一个dijkstra算法的变形题
1. 这里需要将dijkstra算法中的加法改成减法
2. 将求最小改成求最大,所以要用大顶堆而不是小顶堆，这点要尤其注意
'''