class Solution:
	def robotSim(self, commands, obstacles) -> int:
		ans=0
		mp=set([tuple(obs) for obs in obstacles])
		px,py,d=0,0,1
		dirs=[[-1,0],[0,1],[1,0],[0,-1]]
		for c in commands:
			if c<0:
				d+=1 if c==-1 else -1
				d%=4
			else:
				for i in range(c):
					if tuple([px+dirs[d][0],py+dirs[d][1]]) in mp:
						break
					px+=dirs[d][0]
					py+=dirs[d][1]
					ans=max(ans,px*px+py*py)
		return ans