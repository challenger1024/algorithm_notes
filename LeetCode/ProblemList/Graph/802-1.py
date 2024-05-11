#拓扑排序
from collections import deque
class Solution:
	def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
		n=len(graph)
		ins=[0]*n
		g=[[] for _ in range(n)]
		for i in range(n):
			for j  in graph[i]:
				ins[i]+=1
				g[j].append(i)
		q=deque([])
		for i in range(n):
			if not ins[i]:
				q.append(i)
		while q:
			now=q.pop()
			for next in g[now]:
				ins[next]-=1
				if ins[next]==0:
					q.append(next)
		return [i for i in range(n) if ins[i]==0]

#solution
'''
如果一个节点没有出边，那么这个节点就是安全的。
如果一个节点相连的点都是安全的，那么这个点也是安全的。
所以，根据图graph，造一个反向图，那么上面提到的某个节点的出边就变成了入边。
所以，所有入度为0的节点都是安全的。
据此设计拓扑排序算法：
1. 初始化入度数组ins=[0]；
2. 构造反向图g的同时更新入度数组ins的值,用以统计反向图中每个节点的入度；
3. 建立队列q,用于广度优先搜索；
4. 将入度为0的节点加入到队列q中,同时将入度为0的节点指向的节点的入度-1;
开始广度优先搜索:
1. 结束条件:队列为空
2. 元素初队，设为now;
3. 便利now在图g中指向的所有节点,设为next;
4. 节点next的入度-1;
5. 判断next的入度是否=0，=0的话说明该节点是安全的，加入到队列q中;
最终便利完了所有入度能减少到0的节点，bfs就结束了。
返回入度=0的所有节点及为答案。
'''