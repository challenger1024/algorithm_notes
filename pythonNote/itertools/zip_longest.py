#原题见leetcode#165#比较版本号
#zip_longest中的第三个参数fillvalue介绍
#当传入zip_longest的两个序列或多个序列长度不同时，用fillvalue填充短的序列，使他们的长度变成相等的。
#本样例中fillvalue=0
from itertools import zip_longest
class Solution:
	def compareVersion(self, version1: str, version2: str) -> int:
		u=list(map(int,version1.split('.')))
		v=list(map(int,version2.split('.')))
		for i,j in zip_longest(u,v,fillvalue=0):
			if i>j:
				return 1
			elif i<j:
				return -1
		return 0
#test entry
s=Solution()
version1='1.0.1.0'
version2='1'
#version1 = "0.1"version2 = "1.1"
#version1 = "1.0"version2 = "1.0.0"
print(s.compareVersion(version1,version2))