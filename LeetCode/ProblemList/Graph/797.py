class Solution:
	def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
		n=len(graph)
		ans=[]
		stack=[]
		def dfs(u):
			if u==n-1:
				ans.append(stack[:])
			for v in graph[u]:
				stack.append(v)
				dfs(v)
				stack.pop()
		stack.append(0)
		dfs(0)
		return ans

#solution
'''
使用dfs统计路径数量再好不过了。
变量初始化:
1. 设二维数组ans作为答案，其中将要记录所有的路径
2. 设一个数组stack,记录当前路径中的节点
设计递归函数
1. 参数:当前便利到的节点u
2. 结束条件:当前便利到了节点n-1,那么将stack数组加入到答案ans中
3. 选择下一步递归的节点:便利节点u能直接访问的节点v，传入到dfs中，并将v加入到stack数组中
4. 当v被递归结束后，回溯到没有v的时刻，将节点v从stack数组中删除
调用dfs求解
1. 因为路径都是从0开始，所以将0加入到stack数组中
2. 将0 作为参数传入到dfs函数中
返回ans及为答案
'''