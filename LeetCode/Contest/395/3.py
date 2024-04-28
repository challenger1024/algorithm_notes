class Solution:
	def minEnd(self, n: int, x: int) -> int:
		ori=list(map(int,bin(x)[2:]))
		ori.reverse()
		l=[0]*n
		r=[0]*len(ori)
		i=0
		while i<=n:
			if i!=0:
				li=0
				l[li]+=1
				while l[li]==2:
					l[li]=0
					l[li+1]=1
					li+=1
			rn=len(r)
			ri=0
			while ri<rn:

