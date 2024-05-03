class Solution:
	def countCompleteComponents(self, n: int, edges) -> int:
		uf=UnionFind(n)
		for x,y in edges:
			uf.union(x,y)
		ans=0
		for i in range(n):
			j=uf.find(i)
			if i!=j:
				continue
#			print(j)
			ans+=uf.edges[j]==(uf.sizes[j]*(uf.sizes[j]-1)//2)
#			print(f'{uf.edges[j]},{uf.sizes[j]}')
		return ans


class UnionFind:
	def __init__(self,n):
		self.parents=[i for i in range(n)]
		self.edges=[0]*n
		self.sizes=[1]*n
	def find(self,x):
		ret=self.parents[x]
		while ret!=self.parents[ret]:
			ret=self.parents[ret]
		return ret
	def union(self,x,y):
		x,y=self.find(x),self.find(y)
		if x==y:
			self.edges[y]+=1
			return
		if self.sizes[x]>self.sizes[y]:
			x,y=y,x
		self.parents[x]=y
		self.edges[y]=self.edges[x]+self.edges[y]+1
		self.sizes[y]+=self.sizes[x]


#test entry
s=Solution()
#n = 6
#edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]
print(s.countCompleteComponents(n,edges))

#solution
'''
完全联通分量，及顶点数n和边数e有以下关系：
e=n*(n-1)/2
所以求初联通分量的顶点数量和边数即可。
在使用并查集时，合病x,y,如果x和y已经在同一个联通分量里，则y对应边数+1
如果x和y不在同一个联通分量里，则
edges[y]=edges[x]+edges[y]+1
加上的那个新边就是链接x和y的这个边。
'''