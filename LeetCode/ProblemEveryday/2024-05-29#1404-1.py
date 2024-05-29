class Solution:
	def calc(self,s):
		n=len(s)
		for i,c in enumerate(s):
			if c=='2':
				c='0'
				if i<n-1:
					s[i+1]='2' if s[i+1]=='1' else '1'
				else:
					s.append('1')
		return s
	def numSteps(self, s: str) -> int:
		s=list(s[::-1])
		ans=0
		while len(s)>1:
			if s[0]=='1':
				s[0]='2'
				s=self.calc(s)
			else:
				s=s[1:]
			ans+=1
		return ans