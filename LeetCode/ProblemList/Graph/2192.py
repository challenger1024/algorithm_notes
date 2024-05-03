from collections import deque
class Solution:
	def getAncestors(self, n: int, edges):# -> List[List[int]]:
		ans=[set() for _ in range(n)]
		ins=[0]*n
		outs=[0]*n
		g=[[] for i in range(n)]
		for u,v in edges:
			g[u].append(v)
			ins[v]+=1
		q=deque([])
		for i in range(n):
			if ins[i]==0:
				q.append(i)
		while q:
			now=q.popleft()
#			print(now)
			for next in g[now]:
				ans[next]|=ans[now]
				ans[next].add(now)
				ins[next]-=1
				if ins[next]==0:
					q.append(next)
		ret=[]
		for s in ans:
			l=list(s)
			l.sort()
			ret.append(l)
		return ret

#test entry
s=Solution()
n=10
edges=[[5,2],[8,7],[7,2],[8,3],[1,6],[9,0]]
print(s.getAncestors(n,edges))