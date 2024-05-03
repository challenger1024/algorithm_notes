#并查集
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
		ans=sum(parents[i]==i for i in range(n))
		return ans