from collections import deque
class Solution:
	def minimumTime(self, n: int, edges, disappear):# -> List[int]:
		graph=[[] for _ in range(n)]
		for edge in edges:
			graph[edge[0]].append([edge[1],edge[2]])
#			graph[edge[1]].append([edge[0],edge[2]])
		mem=[10**5+1]*n
		def bfs():
			q=deque()
			q.append([0,0])
			mem[0]=0
			while q:
				next,time=q.popleft()
				for edge in graph[next]:
					q.append([edge[0],time+edge[1]])
					if time+edge[1]<mem[edge[0]] and disappear[next]>time:
						mem[edge[0]]=time+edge[1]
		bfs()
		for i in range(n):
			if mem[i]==10**5+1:mem[i]=-1
			if mem[i]>=disappear[i]:mem[i]=-1
		return mem

#test entry
s=Solution()
n = 3
edges = [[0,1,2],[1,2,1],[0,2,4]]
disappear = [1,1,5]
#n = 3
#edges = [[0,1,2],[1,2,1],[0,2,4]]
#disappear = [1,3,5]
#n = 2
#edges = [[0,1,1]]
#disappear = [1,1]
print(s.minimumTime(n,edges,disappear))


'''


'''