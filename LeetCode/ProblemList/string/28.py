class Solution:
	def strStr(self, text: str, p: str) -> int:
		n,m=len(text),len(p)
		next=[0]*m
		x,now=1,0
		while x<m:
			if p[x]==p[now]:
				now+=1
				next[x]=now
				x+=1
			elif now!=0:
				now=next[now-1]
			else:
				x+=1
		i,j=0,0
		while i<n :
			if text[i]==p[j]:
				i+=1
				j+=1
			elif j!=0:
				j=next[j-1]
			else:
				i+=1
			if j==m:
				return i-m
		return -1

