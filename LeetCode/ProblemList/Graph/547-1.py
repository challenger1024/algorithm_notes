#dfs
class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		n=len(isConnected)
		vis=[False]*n
		def dfs(city):
			if vis[city]:
				return
			vis[city]=True
			for i in range(n):
				if isConnected[city][i]:
					 dfs(i)
		ans=0
		for i in range(n):
			if not vis[i]:
				dfs(i)
				ans+=1
		return ans