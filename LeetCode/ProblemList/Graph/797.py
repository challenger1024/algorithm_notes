class Solution:
	def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
		n=len(graph)
		ans=[]
		stack=[]
		def dfs(u):
			if u==n-1:
				ans.append(stack[:])
			for v in graph[u]:
				stack.append(v)
				dfs(v)
				stack.pop()
		stack.append(0)
		dfs(0)
		return ans