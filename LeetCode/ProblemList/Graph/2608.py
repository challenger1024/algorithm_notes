class Solution:
	def findShortestCycle(self, n: int, edges) -> int:
		g=[[] for _ in range(n)]
		for u,v in edges:
			g[u].append(v)
			g[v].append(u)
		def bfs(start):
			ans=inf
			dis=[-1]*n
			q=deque([(start,-1)])
			dis[start]=0
			while q:
				now,father=q.popleft()
				for next in g[now]:
					if dis[next]<0:
						dis[next]=dis[now]+1
						q.append((next,now))
					elif father!=next:
						ans=min(ans,dis[now]+dis[next]+1)
			return ans
		ret=min(bfs(i) for i in range(n))
		return ret if ret!=inf else -1

#solution
'''
使用bfs解决双向图中最小环问题
n个顶点，每个顶点作为开始点被访问，结果都可能不同，所以要全都便利一遍
bfs函数中初始化变量：
1. ans=inf#设为最大值，因为最后要返回最小值
2. 设一个数组dis,存储从start出发访问每个其他节点的距离,初始时为-1,表示没访问到或者访问不到
3. 设一个队列q,其中存储的每个项目包含两个信息，当前便利到的节点和这个节点的父节点，因为这是一个双向图，存储父节点方便后面判断两个顶点之间两条边重复走的情况
4. 将dis[start]设为0，表示start到start的距离是0
5.将(start,-1)入队，表示start的父节点不存在


'''