class Solution:
	def getLucky(self, s: str, k: int) -> int:
		pre=s
		now=''
		for c in s:
			now+=str(ord(c)-ord('a')+1)
		k-=1
		while k>-1:
			k-=1
			pre=now
			temp=0
#			print(pre)
			for c in pre:
				temp+=int(c)
			now=str(temp)
		return int(now)

s=Solution()
st='zabx'
k=2
print(s.getLucky(st,k))