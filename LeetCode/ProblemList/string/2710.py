class Solution:
	def removeTrailingZeros(self, num: str) -> str:
		n=len(num)
		i=n-1
		while i>=0:
			if num[i]!='0':
				break
			i-=1
		return num[:i+1]
