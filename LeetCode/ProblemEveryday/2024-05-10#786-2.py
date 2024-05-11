from heapq import heappush,heappop,heapify
class Frac:
	def __init__(self,idx,idy,x,y):
		self.idx=idx
		self.idy=idy
		self.x=x
		self.y=y
	def __lt__(self,other):
		return self.x*other.y < self.y*other.x


class Solution:
	def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
		n=len(arr)
		q=[Frac(0,i,arr[0],arr[i]) for i in range(1,n)]
		heapify(q)
		for _ in range(k-1):
			frac=heappop(q)
			i,j=frac.idx,frac.idy
			if i+1<j:
				heappush(q,Frac(i+1,j,arr[i+1],arr[j]))
		return [q[0].x,q[0].y]

#solution
'''
使用优先队列解决问题
由于arr是有序序列，那么arr[i]/arr[j](i属于[0,j-1])也会随着i的递增而递增。
所以建立一个优先队列，取出来一个元素arr[i]/arr[j],
如果i+1<j,则把arr[i+1]/arr[j]加入到优先队列中，
取到第k次，及为答案。
'''