from collections import deque
class Solution:
	def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
		n=len(rooms)
		vis=[False]*n
		q=deque([0])
		vis[0]=True
		while q:
			u=q.popleft()
			for v in rooms[u]:
				if not vis[v]:
					q.append(v)
					vis[v]=True
		return reduce(lambda x,y: (x&y),vis)

#solution()
'''
本题需要判断整个图是不是只有一个联通分量。
每一个room都是一个节点，就构造初了一个图的结构。
这里用bfs进行搜索，用dfs和并查集也都是可以的。
变量初始化:
1. 数组vis,存储bool值，初始时都为False,表示节点还都没被访问过;
2. 队列q，用于广度优先搜索，可以将节点0放进去进行初始化，同时要把vis[0]置为True;
开始bfs:
1. 循环结束条件:队列q为空；
2. 节点now初队；
3. 便利now能到达的所有节点 next,如果next没被访问过，将next入队，并标记为已访问；
最后返回vis数组是否全为True,全为True说明所有节点都在同一个联通分量中，所以可以到达所有房间。
这里使用了reduce()函数队vis中的所有元素通过与运算两两合并后返回。
'''