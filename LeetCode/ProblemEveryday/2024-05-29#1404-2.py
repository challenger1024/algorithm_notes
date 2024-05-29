class Solution:
	def numSteps(self, s: str) -> int:
		ans=0
		n=len(s)
		flag=False
		for i in range(n-1,-1,-1):
			if s[i]=='0':
				ans+=2 if flag else 1
			else:
				if flag:
					ans+=1
				else:
					if i!=0:
						ans+=2
						flag=True
		return ans