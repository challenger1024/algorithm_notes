from collections import deque,defaultdict
class Solution:
	def shortestAlternatingPaths(self, n: int, redEdges, blueEdges):
		rg=defaultdict(list)
		bg=defaultdict(list)
		for x,y in redEdges:
			rg[x].append(y)
		for u,v in blueEdges:
			bg[u].append(v)
		g=[rg,bg]
		ret=[[-1]*n for _ in range(2)]
		ret[0][0],ret[1][0]=0,0
		vis=[[False]*n for _ in range(2)]
		q=deque([[0,0],[1,0]])
		vis[0][0],vis[1][0]=True,True
		while q:
			nowColour,nowNode =q.popleft()
			nextColour=1-nowColour
			for nextNode in g[nextColour][nowNode]:
				if not vis[nextColour][nextNode]:
					vis[nextColour][nextNode]=True
					ret[nextColour][nextNode]=ret[nowColour][nowNode]+1
					q.append([nextColour,nextNode])
		ans=[-1]*n
		for i in range(n):
			if ret[0][i]!=-1 and ret[1][i]!=-1:
				ans[i]=min(ret[0][i],ret[1][i])
			else:
				ans[i]=max(ret[0][i],ret[1][i])
		return ans

#test entry
s=Solution()
n = 3
red_edges = [[0,1],[1,2]]
blue_edges = []
print(s.shortestAlternatingPaths(n, red_edges, blue_edges))

#solution
'''
求最短路的变形，这里使用bfs解决
1. 红色边和蓝色边分别见图
2. 放进一个更大的数组中，第0维表示红色边，第1维表示蓝色边；
3. 建立vis数组第0维表示红色边的访问状态，第1维表示蓝色边的访问状态;
4. 建立队列q,将初始值传入队列进行初始化.初始值为[[1,0],[0,0]],表示蓝色当前长度维0,，红色当前长度维0；
5. 建立ret数组，存储红蓝交叉走的路径长度，第0维表示红色边结尾，第1维表示蓝色边结尾；


'''