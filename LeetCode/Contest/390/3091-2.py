#便利求最小值
import math
class Solution:
	def minOperations(self, k: int) -> int:
		return min(n-1+(k-1)//n for n in range(1,k+1))