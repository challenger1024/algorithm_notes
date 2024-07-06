class Solution:
	def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
		n=len(grid)
		q=[]
		dis=[[-1]*n for _ in range(n)]
		for i,row in enumerate(grid):
			for j ,x in enumerate(row):
				if x:
					q.append((i,j))
					dis[i][j]=0
		groups=[q]
		while q:
			tmp=q
			q=[]
			for i,j in tmp:
				for x,y in (i,j+1),(i,j-1),(i-1,j),(i+1,j):
					if 0<=x<n and 0<=y<n and dis[x][y]<0:
						q.append((x,y))
						dis[x][y]=len(groups)
			groups.append(q)
		f=list(range(n*n))
		def find(x):
			if x!=f[x]:
				f[x]=find(f[x])
			return f[x]
		for d in range(len(groups) - 2,0,-1):
			for i ,j in groups[d]:
				for x,y in (i,j+1),(i,j-1),(i-1,j),(i+1,j):
					if 0<=x<n and 0<=y<n and dis[x][y]>=dis[i][j]:
						f[find(x*n+y)]=find(i*n+j)
			if find(0)==find(n*n-1):
				return d
		return 0

#solution
'''
bfs预处理+并查集
'''