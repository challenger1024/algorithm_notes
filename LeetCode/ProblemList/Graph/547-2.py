#bfs
class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		n=len(isConnected)
		vis=[False]*n
		ans=0
		for i in range(n):
			if not vis[i]:
				q=deque([i])
				while q:
					j=q.popleft()
					vis[j]=True
					for k in range(n):
						if isConnected[j][k]==1 and vis[k]==False:
							q.append(k)
				ans+=1
		return ans