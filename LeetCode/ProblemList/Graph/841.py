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