# 547 - 省份数量
#bfs
class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		n=len(isConnected)
		vis=[False]*n
		ans=0
		for i in range(n):
			if not vis[i]:
				q=deque([i])
				while q:
					j=q.popleft()
					vis[j]=True
					for k in range(n):
						if isConnected[j][k]==1 and vis[k]==False:
							q.append(k)
				ans+=1
		return ans

#solution
'''
本段代码思路与文件#547-1.py#中的思路相同，都是统计图中联通分量的数量
但本次使用了广度优先搜索(bfs)进行统计
若当前城市未被访问过，则加入到队列中
'''