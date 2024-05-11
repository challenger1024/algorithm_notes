#dfs - 三色标记法
class Solution:
	def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
		n=len(graph)
		f=[0]*n
		def dfs(u):
			if f[u]>0:
				return f[u]==2
			f[u]=1
			for v in graph[u]:
				if not dfs(v):
					return False
			f[u]=2
			return True
		return [i for i in range(n) if dfs(i)]

#solution
'''
颜色标记法配合dfs.
根据提议，题目要求'不在环中且走不到环里'的节点.
设数组f,其中保存的变量有三种情况:
f[i]=0#表示第i 个节点还没有访问过
f[i]=1#表示节点正在被访问，或者位于环中。
f[i]=2#表示节点i是安全的
设计dfs函数
1. 传参 ：当前便利到的节点u.
2. 退出条件:找到了环或者便利到了安全节点
(1.)找到了环:f[u]==1,返回False
(2). 便利到了安全节点:f[u]==2,返回True.
3. 递归过程:
将u能到达的节点v传入dfs,递归调用函数
如果v能走到有环的地方，说明u也能走到有环的地方，则u不安全，直接返回False.
4. 递归调用全部结束，说明u能到达的节点都是安全的，都没有环，那么设f[u]=2,返回True.



'''