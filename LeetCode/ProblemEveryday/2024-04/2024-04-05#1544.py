class Solution:
	def makeGood(self, s: str) -> str:
		i=0
		stack=[]
		for i in range(len(s)):
			if not stack:
				stack.append(s[i])
				continue
			if abs(ord(s[i])-ord(stack[-1]))==32:
				stack.pop()
				continue
			stack.append(s[i])
		return ''.join(stack)


#test entry
so=Solution()
#s='mC'
s='Pp'
#s='leEeetcode'
#s="abBAcC"
print(so.makeGood(s))