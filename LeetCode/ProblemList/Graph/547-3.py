#547 - 省份数量
#ufs(unite find set)
class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		n=len(isConnected)
		parents=[0]*n
		for i in range(n):
			parents[i]=i
		def find(x):
			ret=x
			while ret!=parents[ret]:
				ret=parents[ret]
			return ret
		def union(x,y):
			parents[find(x)]=find(y)
		for i in range(n):
			for j in range(i+1,n):
				if isConnected[i][j]==1:
					union(i,j)
		ans=sum(parents[i]==i for i in range(n))#如果i的父节点不是它本身，说明它被连接到了别的节点上，所以要统计联通分量，只需要统计父节点是它本身的节点数量，也就是联通分量的根节点的数量
		return ans

#solution
'''
并查集用来统计联通分量数量还是非常好用的
这里父节点是其本身的节点及为联通分量的根节点，有几个这样的节点就意味着有几个联通分量
另外还可以统计每个联通分量中节点的数量
'''