class Solution:
	def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
		g=[[] for _ in range(n)]
		for u,v,w in times:
			g[u-1].append((v-1,w))
		dis=[inf]*n
		dis[k-1]=0
		h=[(0,k-1)]
		while h:
			d,now=heappop(h)
			if d> dis[now]:
				continue
			for next,w in g[now]:
				newD=d+w
				if newD<dis[next]:
					dis[next]=newD
					heappush(h,(newD,next))
		bst=max(dis)
		return bst if bst!=inf else -1

#Solution
'''
基于堆优化的Dijkstra算法实现
'''