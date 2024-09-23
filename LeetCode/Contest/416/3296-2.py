#最小堆+模拟
from heapq import heappop,heappush,heapify,heapreplace


class Solution:
	def minNumberOfSeconds(self, mountainHeight: int, workerTimes) -> int:
		h=[(t,t,t) for t in workerTimes]
		heapify(h)
		for _ in range(mountainHeight):
			ret,delta,base=h[0]
			heapreplace(h,(ret+delta+base,delta+base,base))
		return ret