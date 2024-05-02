class Solution:
	def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
		g=[[] for _ in range(n)]
		for u,v in edges:
			g[v].append(u)
			g[u].append(v)
		vis=[False]*n
		def dfs(v):
			if vis[v]:
				return False
			if v==destination:
				return True
			vis[v]=True
			ret=False
			for u in g[v]:
				ret|=dfs(u)
			return ret
		return dfs(source)