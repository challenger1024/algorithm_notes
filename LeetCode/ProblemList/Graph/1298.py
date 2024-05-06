from collections import deque
class Solution:
	def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
		n=len(status)
		ans=0
		opens=[status[i]==1 for  i in range(n)]
		had=[False]*n
		used=[False]*n
		q=deque([])
		for box in initialBoxes:
			had[box]=True
			if status[box]==1:
				q.append(box)
				used[box]=True
				ans+=candies[box]
		while q:
			now =q.popleft()
			for key in keys[now]:
				opens[key]=True
				if not used[key] and had[key]:
					q.append(key)
					used[key]=True
					ans+=candies[key]
			for box in containedBoxes[now]:
				had[box]=True
				if not used[box] and opens[box]:
					used[box]=True
					q.append(box)
					ans+=candies[box]
		return ans

#solution
'''
#变量设置：
使用队列进行广度优先搜索
使用had数组标记盒子是否被拥有,初始时都为False
使用used数组标记盒子是否已被访问过,初始时都为False
使用opens数组存储盒子i是否能被打开，初始时都为False
使用ans记录答案，初始值为0
使用FIFO队列q，用于广度优先搜索，初始状态为空
#变量初始值设置
1. 循环便利initialBoxes中的盒子
2. 将initialBoxes中的盒子都标记为已拥有，就是把他们对应的had[i]标记为True
3. 便利initial的过程中，判断status[i]==1,若为真，则将opens标记为True,表示盒子i可以被打开
4.在执行[3]的同时，将盒子i(这个盒子肯定是既拥有又能被打开的状态)加入到队列q中，等待广度优先搜索
5.在执行[3]和[4]的同时，将used[i]标记为True,表示盒子i已经被访问过
开始广度优先搜索
1. 循环条件:队列q不为空,队列q中存储的都是有且能被打开且以访问过的盒子，若队列为空，则说明能打开的盒子都已经被打开了。
2. 最左边的元素出队,赋值给变量nowBox,
3. 便利nowBox中的每个钥匙key,将opens[key]标记为True,表示拥有了盒子key的钥匙
如果key对应的盒子没被访问过，且已拥有索引为key的盒子，
(1).  将key加入到队列q
(2).used[key]标记为True,表示key被访问过了
(3). ans+=candies[key]#因为盒子key能被打开且拥有，所以将其中的糖果加入到答案中
4. 便利完nowBox的钥匙后，再便利一次nowBox中的containedBoxes,记为box,将had[box]标记为True，表示拥有了盒子box
如果box没被访问过且拥有开启box的钥匙:
(1). 标记为以访问
(2). 将box加入到队列q中
(3). 将candies[box]加入到答案
5. 队列为空时，返回答案ans

'''