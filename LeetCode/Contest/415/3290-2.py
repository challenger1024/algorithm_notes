#动态规划的内存和时间优化
class Solution:
	def maxScore(self, a: List[int], b: List[int]) -> int:
		a0, a1, a2, a3 = a  # 去掉访问 list 的开销
		f0 = f1 = f2 = f3 = -inf
		for y in b:
			t = a3 * y + f2
			if t > f3: f3 = t  
			t = a2 * y + f1
			if t > f2: f2 = t
			t = a1 * y + f0
			if t > f1: f1 = t
			t = a0 * y
			if t > f0: f0 = t
		return f3