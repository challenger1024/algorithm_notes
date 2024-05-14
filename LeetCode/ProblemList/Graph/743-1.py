class Solution:
	def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
		g=[[inf]*n for _ in range(n)]
		for u,v,w in times:
			g[u-1][v-1]=w
		dis=[inf]*n
		ans=dis[k-1]=0
		vis=[False]*n
		while True:
			now=-1
			for i,ok in enumerate(vis):
				if not ok and (now<0 or dis[i]<dis[now]):
					now=i
			if now<0:
				return ans
			if dis[now]==inf:
				return -1
			ans=dis[now]
			vis[now]=True
			for next,w in enumerate(g[now]):
				dis[next]=min(dis[next],dis[now]+w)

#solution
'''
朴素Dijkstra
'''