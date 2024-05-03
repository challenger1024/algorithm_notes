#dfs
class Solution:
	def countPairs(self, n: int, edges: List[List[int]]) -> int:
		g=[[] for _ in range(n)]
		for x,y in edges:
			g[x].append(y)
			g[y].append(x)
		vis=[False]*n
		def dfs(u):
			if vis[u]:
				return 1
			vis[u]=True
			ret=1
			for v in g[u]:
				if not vis[v]:
					ret+=dfs(v)
			return ret
		ans=0
		for i in range(n):
			if not vis[i]:
				cnt=dfs(i)
				ans+=cnt*(n-cnt)
		return ans//2