class Solution:
	def minRemoveToMakeValid(self, s: str) -> str:
		stack=[]
		for i,c in enumerate(s):
#			print(c+','+str(stack))
			if c!='(' and c!=')':
				continue
			if stack and s[stack[-1]]=='(' and c==')':
				stack.pop()
			else:
				stack.append(i)
		removes=set(stack)
		ans=[]
		for  i in range(len(s)):
			if not i in removes:
				ans.append(s[i])
		return ''.join(ans)

#test entry
so=Solution()
s="a)b(c)d"
#s = "lee(t(c)o)de)"
print(so.minRemoveToMakeValid(s))