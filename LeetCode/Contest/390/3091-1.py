#用基本不等式，o(1)时间复杂度
import math
class Solution:
	def minOperations(self, k: int) -> int:
		return math.ceil(2*math.sqrt(k)) -2

#test entry
#k=11
#k=1
print(s.minOperations(k))
#solution
''' 用基本不等式:x+k/x>=2*sqrt(k)
但题目的解还需要向上取整，还要减去2.推理是这样的：
1.假设最终数组是有元素n组成的，则数组中共有(k//n)个元素,那么复制操作的次数就是(k//n)-1
2.因为数组最后只有n,所以要将开始的1进行(n-1)次+1操作
3.得到函数：(n-1)+(k//n)-1
化简：n+k//n-2

这就很明显了，一个基本不等式剪掉一个常数
sqrt(k)-2
要向上取整，也不好说为啥。
'''