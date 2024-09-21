
class Solution:
	def diffWaysToCompute(self, expression: str):# -> List[int]:
		ans=[]
		if expression.isdigit():
			return [int(expression)]
		for i,c in enumerate(expression):
			if c in '*+-':
				left=self.diffWaysToCompute(expression[:i])
				right=self.diffWaysToCompute(expression[i+1:])
				for l in left:
					for r in right:
						if c=='+':
							ans.append(l+r)
						elif c=='-':
							ans.append(l-r)
						else:
							ans.append(l*r)
		return ans