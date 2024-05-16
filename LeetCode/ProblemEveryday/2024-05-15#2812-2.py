class Solution:
	def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
		n=len(grid)
		if grid[0][0]==1 or grid[n-1][n-1]==1:
			return 0
		dirs=[-1,0,1,0,-1]
		q=deque([])
		for i in range(n):
			for j in range(n):
				if grid[i][j]==1:
					q.append((i,j))
					grid[i][j]=-1
		d=1
		while q:
			times=len(q)
			for _ in range(times):
				i,j=q.popleft()
				for k in range(4):
					x,y=i+dirs[k],j+dirs[k+1]
					if 0<=x<n and 0<=y<n and grid[x][y]==0:
						grid[x][y]=d
						q.append((x,y))
			d+=1
		for i in range(n):
			for j in range(n):
				if grid[i][j]==-1:
					grid[i][j]=0
		ans=[[0]*n for _ in range(n)]
		ans[0][0]=grid[0][0]
		h=[(-ans[0][0],0,0)]
		seen=set()
		while h:
			dis,i,j=heappop(h)
			if (i,j) in seen:
				continue
			seen.add((i,j))
			for k in range(4):
				x,y=i+dirs[k],j+dirs[k+1]
				if 0<=x<n and 0<=y<n:
					nd=min(-dis,grid[x][y])
					if nd> ans[x][y]:
						ans[x][y]=nd
						heappush(h,(-ans[x][y],x,y))
		return ans[n-1][n-1]