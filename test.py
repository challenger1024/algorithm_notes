from collections import deque

class Solution:
	def calc(self,x,courses):
		g=[[] for _ in range(x)]#见图
		ins=[0]*x#记录入度数量
		for a,b in courses:
			g[b].append(a)
			ins[a]+=1
		q=deque([])
		for i in range(x):
			if ins[i]==0:
				q.append(i)
		while q:
			now=q.pop()
			for next in g[now]:
				ins[next]-=1
				if ins[next]<=0:
					q.append(next)#入度为0 的节点添加到队列中
		ret=True
		for i in ins:
			if i!=0:
				ret=False
		return ret

s=Solution()
x=3
pre = [[2,1],[0,1],[2,0]]
print(s.calc(x,pre))