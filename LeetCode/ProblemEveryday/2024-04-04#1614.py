class Solution:
	def maxDepth(self, s: str) -> int:
		ans=0
		pnum=0
		for i ,c in enumerate(s):
			if c=='(':
				pnum+=1
			if c==')':
				ans=max(ans,pnum)
				pnum-=1
		return ans

#test entry
so=Solution()
s = "(1)+((2))+(((3)))"
#s = "(1+(2*3)+((8)/4))+1"
print(so.maxDepth(s))