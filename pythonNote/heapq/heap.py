#大顶堆和小顶堆的使用
from heapq import heappush
from heapq import heappop
heap=[]#小顶堆
heappush(heap,5)#添加元素
heappush(heap,4)
heappush(heap,3)
#print(heap)
heappop(heap)#淡出元素
#print(heap)
heappop(heap)
#print(heap)

big_heap=[]#大顶堆，加上负号后，最大值变最小值
heappush(big_heap,-(5))
print(big_heap)
heappush(big_heap,-(4))
print(big_heap)
heappop(big_heap)
print(big_heap)