class Solution:
	def checkValidString(self, s: str) -> bool:
		a=[]
		l=[]
		for i,c in enumerate(s):
			if c=='(':l.append(i)
			elif c==')':
				if l: l.pop()
				elif a:a.pop()
				else:return False
			else:a.append(i)
		if not l:return True
		else:
			while l and a:
				x,y=l.pop(),a.pop()
				if x>y:return False
		return not l



so=Solution()
s="((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
#s = "()"
#s = "(*)"
#s = "(*))"
print(str(so.checkValidString(s)))