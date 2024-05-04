from collections import deque
class Solution:
	def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
		m=len(meetings)
		e=[False]*n
		e[0]=e[firstPerson]=True
		meetings.sort(key=lambda x: x[2])
		i=0
		while i<m:
			j=i
			while j+1<m and meetings[j+1][2]==meetings[i][2]:
				j+=1
			g=defaultdict(list)
			vis=set()
			for x,y,t in meetings[i:j+1]:
				vis.update([x,y])
				g[x].append(y)
				g[y].append(x)
			q=deque([i for i in vis if  e[i]])
			while q:
				now=q.popleft()
				for next in g[now]:
					if e[next]:continue
					e[next]=True
					q.append(next)
			i=j+1
		ans=[i for i in range(n) if e[i]]
		return ans