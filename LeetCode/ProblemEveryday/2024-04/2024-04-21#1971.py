from collections import deque
class Solution:
	def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
		map=[[] for _ in range(n)]
		for edge in edges:
			map[edge[0]].append(edge[1])
			map[edge[1]].append(edge[0])
		q=deque()
		vis=[False]*n
		q.append(source)
		vis[source]=True
		while q:
			now=q.popleft()
			for next in map[now]:
				if next==destination:
					return True
				if not vis[next]:
					vis[next]=True
					q.append(next)
		return vis[destination]