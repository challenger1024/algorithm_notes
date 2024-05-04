#拓扑排序
from collections import deque
class Solution:
	def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
		n=len(graph)
		ins=[0]*n
		g=[[] for _ in range(n)]
		for i in range(n):
			for j  in graph[i]:
				ins[i]+=1
				g[j].append(i)
		def bfs(z):
			q=deque([])
			vis=[False]*n
			for i in range(n):
				if ins[i]==0:
					q.append(i)
					vis[i]=True
			while q:
				now=q.popleft()
				for next in g[now]:
					ins[next]-=1
					if ins[next]==0:
						q.append(next)
			ans=[]
			for i in range(n):
				if ins[i]==0:
					ans.append(i)
			return ans
		return bfs(0)