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