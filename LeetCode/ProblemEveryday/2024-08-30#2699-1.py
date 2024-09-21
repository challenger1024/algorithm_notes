#有题目，因为只需要找到任意一个满足题意的解，所以利用二分找到目标边权，然后构造。
class Solution:
	def modifiedGraphEdges(self, n: int, edges, source: int, destination: int, target: int):# -> List[List[int]]:
		def dijkstra(adj_matrix):
#adj_matrix是一个邻接矩阵
			dist=[float("inf")]*n
			used=set()#确定顶点有没有被便利到过
			dist[source]=0
			for round in range(n-1):
				u=-1#当前顶点
				for i in range(n):#找到距离resource最近的u
					if i not in used and (u==-1 or dist[i]<dist[u]):
						u=i
				used.add(u)
				for v in range(n):
					if adj_matrix[u][v]!=-1:
						dist[v]=min(dist[v],dist[u]+adj_matrix[u][v])
			return dist[destination]
		def construct(idx):
			adj_matrix=[[-1]*n for _ in range(n)]
			for u,v,w in edges:
				if w!=-1:
					adj_matrix[u][v]=adj_matrix[v][u]=w
				else:
					if idx>=target-1:
						adj_matrix[u][v]=adj_matrix[v][u]=target
						idx-=(target-1)
					else:
						adj_matrix[u][v]=adj_matrix[v][u]=idx+1
						idx=0
			return adj_matrix
		k=sum(1 for e in edges if e[2]==-1)
		if dijkstra(construct(0))>target:
			return []
		if dijkstra(construct(k*(target-1)))<target:
			return []
		l,r,ans=0,k*(target-1),0
		while l<=r:
			mid=(l+r)//2
			if dijkstra(construct(mid)) >=target:
				ans=mid
				r=mid-1
			else:
				l=mid+1
		for e in edges:
			if e[2]==-1:
				if ans>=target-1:
					e[2]=target
					ans-=(target-1)
				else:
					e[2]=1+ans
					ans=0
		return edges