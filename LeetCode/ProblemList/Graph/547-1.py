#547 - 省份数量
#dfs
class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		n=len(isConnected)
		vis=[False]*n
		def dfs(city):
			if vis[city]:
				return
			vis[city]=True
			for i in range(n):
				if isConnected[city][i]:
					 dfs(i)
		ans=0
		for i in range(n):
			if not vis[i]:
				dfs(i)
				ans+=1
		return ans

#solution
'''
本质是求图中联通分量的数量问题。
本次使用深度优先搜索(dfs)解决
1. 设一个递归函数dfs，传入参数为当前便利到的城市city.
2. 设一个bool类型数组vis,表示当前城市i是否已经被访问过。
3. dfs的递归结束条件为，当前city已经被访问过，则return
4. 若当前city没被访问，则将其标记为已访问，并便利与当前city直接相连的每座城市,将他们传入dfs函数中递归调用
5.dfs函数外，循环便利n个城市，如果当前城市未被访问过，则调用dfs函数，将与当前城市直接相连和间接相连的城市都标记为已访问，这些城市实际上就是一个联通分量，也就是题目中提到的一个省份
所以调用dfs的同时将答案+1,最终ans即为答案
'''