from collections import deque
class Solution:
	def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
		if n==1:
			return [0]
		g=[[] for _ in range(n)]
		for x,y in edges:
			g[x].append(y)
			g[y].append(x)
		parent=[0]*n#用来记录走过的路线
		def bfs(start):
			q=deque([start])
			vis=[False]*n
			vis[start]=True
			while q:
				now=q.popleft()
				for next in g[now]:
					if not vis[next]:
						vis[next]=True
						parent[next]=now#记录目前节点的父节点
						q.append(next)
			return now
		x=bfs(0)
		y=bfs(x)
		parent[x]=-1
		path=[]
		while y!=-1:
			path.append(y)
			y=parent[y]#找到当前节点的父节点
		n=len(path)
		return [path[n//2]] if n%2 else [path[n//2-1],path[n//2]]
