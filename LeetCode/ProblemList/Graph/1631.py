class Solution:
	def minimumEffortPath(self, heights: List[List[int]]) -> int:
		m,n=len(heights) ,len(heights[0])
		dir=[-1,0,1,0,-1]
		dis=[[-inf]*n for _ in range(m)]
		dis[0][0]=0
		h=[(0,0,0)]
		while h:
			d,i,j=heappop(h)
			d=-d
			if d<=dis[i][j]:
				continue
			for k in range(4):
				ni,nj=i+dir[k],j+dir[k+1]
				if not 0<=ni<m or not 0<=nj<n:
					continue
				w=abs(heights[i][j]-heights[ni][nj])
				newD=max(d,w)
#				if newD > dis[ni][nj]:
				dis[ni][nj]=newD
				heappush(h,(newD,ni,nj))
		return dis[-1][-1] 
