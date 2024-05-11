from collections import deque
class Solution:
	def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
		n=len(patience)
		g=[[] for _ in range(n)]
		for u,v in edges:
			g[u].append(v)
			g[v].append(u)
		ans,dist=0,1
		q=deque([0])
		vis=[True]+[False]*(n-1)
		while q:
			l=len(q)
			for _ in range(l):
				now=q.popleft()
				for next in g[now]:
					if not vis[next]:
						q.append(next)
						vis[next]=True
						ans=max((2*dist-1)//patience[next]*patience[next]+2*dist+1,ans)
			dist+=1
		return ans
