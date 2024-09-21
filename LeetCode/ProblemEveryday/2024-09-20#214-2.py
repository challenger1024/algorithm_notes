#字符串哈希,寻找最长前缀回文串
BASE=131
MOD=10**9+7
class Solution:
	def shortestPalindrome(self, s: str) -> str:
		n = len(s)
		left=right=0
		mul,best=1,-1
		for i,c in enumerate(s):
			left=(left*BASE+ord(c))%MOD
			right=(right+mul*ord(c))%MOD
			mul=mul*BASE%MOD
			if left==right:
				best=i
		add='' if best==n-1 else s[best+1:]
		return add[::-1]+s