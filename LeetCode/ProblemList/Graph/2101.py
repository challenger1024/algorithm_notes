#2101
from collections import deque
class Solution:
	def maximumDetonation(self, bombs) -> int:
		n=len(bombs)
		g=[[] for i in range(n)]
		for i in range(n):
			x1,y1,r1=bombs[i]
			for j in range(n):
				x2,y2,r2=bombs[j]
				l=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
				if l <=r1*r1 :
#					uf.unite(i,j)
					g[i].append(j)
				if l<=r2*r2:
#					uf.unite(j,i)
					g[j].append(i)

		cnt=[1]*n
		for i in range(n):
			vis=[False]*n
			q=deque([i])
			vis[i]=True
			while q:
				now=q.popleft()
				for next in g[now]:
					if vis[next]:
#						cnt[i]+=cnt[next]
						continue
					else:
						vis[next]=True
						cnt[i]+=1
						q.append(next)
		ans=0
		for i in range(n):
			ans=max(ans,cnt[i])
		return ans

#test entry
s=Solution()
bombs=[[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]]
#bombs = [[1,1,5],[10,10,5]]
#bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
#bombs=[[2,1,3],[6,1,4]]
print(s.maximumDetonation(bombs))