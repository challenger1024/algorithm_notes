class Solution:


	def removeKdigits(self, num: str, k: int) -> str:
		stack=[]
		for n in num:
			while stack and k and stack[-1]>n:
				stack.pop()
				k-=1
			stack.append(n)
		ans=stack[:-k] if k>0 else stack
		return ''.join(ans).lstrip('0') or '0'