class Solution:
	def minimumEffortPath(self, heights: List[List[int]]) -> int:
		m,n=len(heights) ,len(heights[0])
		dirs=[-1,0,1,0,-1]
		dis=[0]+[inf]*(m*n-1)
		h=[(0,0,0)]
		seen=set()
		while h:
			d,i,j=heappop(h)
			iden=i*n+j
			if iden in seen:
				continue
			if i==m-1 and j==n-1:
				break
			seen.add(iden)
			for k in range(4):
				ni,nj=i+dirs[k],j+dirs[k+1]
				if 0<=ni<m and 0<=nj<n:
					w=max(d,abs(heights[i][j]-heights[ni][nj]))
					if w<=dis[n*ni+nj]:
						dis[n*ni+nj]=w
						heappush(h,(w,ni,nj))
		return dis[-1]