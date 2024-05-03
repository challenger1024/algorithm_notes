class Solution:
	def makeConnected(self, n: int, connections: List[List[int]]) -> int:
		if len(connections)<n-1:
			return -1
		g=[[] for _ in range(n)]
		for x,y in connections:
			g[x].append(y)
			g[y].append(x)
		vis=[False]*n
		cables=0
		def dfs(u):
			if vis[u]==True:
				return 1
			vis[u]=True
			ret=0
			for v in g[u]:
				ret+=dfs(v)
			return ret
		ans=0
		for i in range(n):
			if not vis[i]:
				cables+=dfs(i)
				ans+=1
		return ans-1 if cables>=ans-1 else -1