class Solution:
	def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
		n=len(graph)
		f=[0]*n
		def dfs(u):
			if f[u]>0:
				return f[u]==2
			f[u]=1
			for v in graph[u]:
				if not dfs(v):
					return False
			f[u]=2
			return True
		return [i for i in range(n) if dfs(i)]